"""Check that the distilled markdown (notes, references, SKILL.md) does not copy the source papers.

Every passage (a paragraph or a bullet) in the markdown is compared against the text of every
PDF in sources/pdfs/, using overlapping runs of N words ("shingles"). Two things get flagged:

  VERBATIM  the passage shares a long run of consecutive words with one paper
  CLOSE     a large share of the passage's N-word runs appear in one paper, even if broken up
            by small edits (a sign of close paraphrase: same sentences, a few words swapped)

Comparison ignores case, punctuation, markdown formatting, and line-break hyphenation in the PDFs.
Headings (mostly paper titles) and short "quoted" spans (attributed quotations) are not checked.
Every passage is checked against every paper, not only the paper its note is about, because the
reference files and SKILL.md draw on many papers.

Run it from anywhere: python evaluation/plagarism_check.py 
"""

from collections import defaultdict
from pathlib import Path
import re
import unicodedata

import pymupdf
import yaml

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "sources" / "pdfs"
MD_FILES = (
    sorted((ROOT / "sources" / "notes").glob("*.md"))
    + sorted((ROOT / "science-of-evals" / "references").glob("*.md"))
    + [ROOT / "science-of-evals" / "SKILL.md"]
)

# --- Thresholds: edit these, then press play -----------------------------------
N = 5                 # words per shingle
VERBATIM_RUN = 12     # flag a passage sharing at least this many consecutive words with one paper
CLOSE_OVERLAP = 0.5   # flag a passage when at least this share of its shingles appear in one paper...
MIN_WORDS = 20        # ...but only for passages at least this long (short bullets are mostly technical terms)
MAX_QUOTE_WORDS = 25  # text in quote marks up to this long is an attributed quotation and is not checked
# ------------------------------------------------------------------------------


def tokenize(text: str) -> list[str]:
    """Lowercase words with punctuation dropped. Hyphens inside words are removed, so
    'multi-turn', 'multiturn' and a PDF's 'multi-\\nturn' all become 'multiturn'."""
    text = unicodedata.normalize("NFKC", text).lower()   # NFKC turns ligatures such as 'ﬁ' into 'fi'
    text = re.sub(r"-\s*\n\s*", "", text)                 # rejoin words hyphenated across a line break
    return [word.replace("-", "") for word in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text)]


def strip_markdown(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)        # HTML comments
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)            # [link text](url) -> link text
    text = re.sub(r"https?://\S+", " ", text)                       # bare URLs
    return text


def passages(markdown: str) -> list[str]:
    """Split markdown into paragraphs, with each list item as its own passage.
    Headings are left out: they are mostly paper titles, which other papers cite verbatim."""
    markdown = strip_markdown(markdown)
    markdown = re.sub(r"^#+ .*$", "", markdown, flags=re.MULTILINE)
    result = []
    for block in re.split(r"\n\s*\n", markdown):
        # Start a new passage at every list item ("- ", "* ", "1. ").
        items = re.split(r"\n(?=\s*(?:[-*+]|\d+\.)\s)", block)
        result.extend(item.strip() for item in items if item.strip())
    return result


def drop_short_quotes(text: str) -> str:
    """Remove "quoted" spans of up to MAX_QUOTE_WORDS words. Longer quotes are kept and checked."""
    def replace(match: re.Match) -> str:
        return " quoteremoved " if len(match.group(1).split()) <= MAX_QUOTE_WORDS else match.group(0)
    # The placeholder word matches no paper, so the words either side of a removed quote can't join into one run.
    return re.sub(r"[\"“]([^\"”\n]+)[\"”]", replace, text)


def shingles(words: list[str]) -> list[tuple[str, ...]]:
    return [tuple(words[i:i + N]) for i in range(len(words) - N + 1)]


def load_papers() -> dict[str, list[str]]:
    """{registry id (or PDF file name if not in the manifest): words of the paper}"""
    manifest = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text()) or {}
    id_by_pdf = {Path(info["pdf_path"]).name: paper_id for paper_id, info in manifest.items()}

    papers = {}
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        with pymupdf.open(pdf_path) as doc:
            text = "\n".join(page.get_text() for page in doc)
        papers[id_by_pdf.get(pdf_path.name, pdf_path.name)] = tokenize(text)
    return papers


def check_passage(words: list[str], index: dict) -> dict | None:
    """Compare one passage against the index. Returns the worst match if it crosses a threshold."""
    grams = shingles(words)
    if not grams:
        return None

    # For each paper, the positions in the passage whose shingle also appears in that paper.
    hits = defaultdict(list)
    for position, gram in enumerate(grams):
        for paper_id in index.get(gram, ()):
            hits[paper_id].append(position)

    worst = None
    for paper_id, positions in hits.items():
        # Consecutive matching shingles chain into a run of shared words.
        longest_start, longest_len, run_start = positions[0], 1, positions[0]
        for previous, current in zip(positions, positions[1:]):
            if current != previous + 1:
                run_start = current
            if current - run_start + 1 > longest_len:
                longest_start, longest_len = run_start, current - run_start + 1
        run_words = longest_len + N - 1
        overlap = len(positions) / len(grams)

        verbatim = run_words >= VERBATIM_RUN
        close = len(words) >= MIN_WORDS and overlap >= CLOSE_OVERLAP
        if not (verbatim or close):
            continue

        match = {
            "paper": paper_id,
            "run_words": run_words,
            "overlap": overlap,
            "kinds": [kind for kind, flagged in (("VERBATIM", verbatim), ("CLOSE", close)) if flagged],
            "run_text": " ".join(words[longest_start:longest_start + run_words]),
        }
        if worst is None or (run_words, overlap) > (worst["run_words"], worst["overlap"]):
            worst = match
    return worst


# --- Run ----------------------------------------------------------------------

papers = load_papers()
if not papers:
    raise FileNotFoundError(f"No PDFs in {PDF_DIR.relative_to(ROOT)}; run pipeline/fetch_papers.py first.")

index = defaultdict(set)   # shingle -> ids of the papers containing it
for paper_id, words in papers.items():
    for gram in shingles(words):
        index[gram].add(paper_id)

print(f"Checking {len(MD_FILES)} markdown files against {len(papers)} papers "
      f"(verbatim run >= {VERBATIM_RUN} words, or >= {CLOSE_OVERLAP:.0%} of {N}-word shingles "
      f"for passages of {MIN_WORDS}+ words)\n")

n_passages = 0
flagged = []
for md_path in MD_FILES:
    for passage in passages(md_path.read_text()):
        n_passages += 1
        match = check_passage(tokenize(drop_short_quotes(passage)), index)
        if match:
            flagged.append((md_path, passage, match))

for md_path, passage, match in flagged:
    excerpt = " ".join(passage.split())
    excerpt = excerpt if len(excerpt) <= 160 else excerpt[:157] + "..."
    print(f"[{'+'.join(match['kinds'])}] {md_path.relative_to(ROOT)}  vs  {match['paper']}")
    print(f"  longest shared run: {match['run_words']} words; shingle overlap: {match['overlap']:.0%}")
    print(f"  passage: {excerpt}")
    print(f"  shared:  \"{match['run_text']}\"\n")

print(f"{len(flagged)} of {n_passages} passages flagged across {len(MD_FILES)} files.")
