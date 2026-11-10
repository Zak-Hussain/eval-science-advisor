from pathlib import Path
import re
import yaml
from huggingface_hub import InferenceClient
import pymupdf
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "science-of-evals"   # the folder users install

# The advisor's seven categories (see SPEC.md). Notes may use any of them, not only a paper's registry tags.
CATEGORIES = ["constructs", "validity", "elicitation", "scoring", "reliability", "measurement-models", "generalization"]

# Pin both the model and the provider (the part after ":"). Different providers can serve the
# same open-weights model with different settings, so pinning the provider keeps runs comparable.
MODEL = "zai-org/GLM-5.2:deepinfra"   # TODO: choose your model and provider
MAX_TOKENS = 8000
CLIENT = InferenceClient()   # reads HF_TOKEN from your environment

# --- What to run: edit these, then press play ----------------------------------
STEP = "notes"   # "notes", "references" or "skill"
ONLY = None     # None = everything; or one registry id (notes) / one category (references)
# ------------------------------------------------------------------------------


def load_prompt(name: str, **fields) -> str:
    """Read pipeline/prompts/<name>.md and fill in its {placeholders}."""
    template = (ROOT / "pipeline" / "prompts" / f"{name}.md").read_text()
    return template.format(**fields)


def pdf_to_text(pdf_path: Path) -> str:
    """Extract the text of a PDF. Open models on the HF API take text, not PDF files,
    so figures are lost and tables may come out jumbled."""
    with pymupdf.open(pdf_path) as doc:
        return "\n".join(page.get_text() for page in doc)


def ask_model(prompt: str) -> str:
    """Send one prompt to the model and return the text of the reply."""
    response = CLIENT.chat_completion(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    choice = response.choices[0]

    # A reply that hit the token limit is cut off mid-way, so don't save it as if it were complete.
    if choice.finish_reason == "length":
        raise RuntimeError(f"Reply hit MAX_TOKENS ({MAX_TOKENS}) and was cut off")

    return choice.message.content


def advice_by_category(note: str) -> dict[str, str]:
    """Pull the "What the advisor should take from it" part out of a note and split it
    into {category: advice text}, using the *<category>:* sub-headings."""
    # Everything after the heading, up to the next bold heading such as **Caveats:** (or the end).
    match = re.search(
        r"^\*\*What the advisor should take from it:\*\*\s*$(.*?)(?=^\*\*[^*\n]+:\*\*|\Z)",
        note,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError("no 'What the advisor should take from it' section")

    # Splitting on a pattern with a (group) keeps the group, giving
    # [text before the first sub-heading, category, advice, category, advice, ...].
    parts = re.split(r"^\*([^*\n]+):\*\s*$", match.group(1), flags=re.MULTILINE)
    advice = {category: text.strip() for category, text in zip(parts[1::2], parts[2::2])}

    # A misspelled sub-heading (e.g. *Validity:* or *measurement models:*) would otherwise be silently left out.
    unknown = [category for category in advice if category not in CATEGORIES]
    if unknown:
        raise ValueError(f"unknown category sub-heading(s): {unknown}")
    return advice


def make_note(entry: dict, pdf_path: Path) -> None:
    """Pass 1: one paper -> sources/notes/<id>.md"""
    note_path = ROOT / "sources" / "notes" / f"{entry['id']}.md"
    if note_path.exists():
        print(f"Skipping {entry['id']}: note already exists")
        return

    prompt = load_prompt(
        "paper_note",
        title=entry["title"],
        categories=", ".join(entry["categories"]),
    )
    paper = pdf_to_text(pdf_path)
    text = ask_model(f"<paper>\n{paper}\n</paper>\n\n{prompt}")

    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(text)
    print(f"Wrote {note_path.relative_to(ROOT)}")


def make_reference(category: str, entries: list[dict]) -> None:
    """Pass 2 (no model): copy this category's advice from every note that has a *<category>:*
    section -> SKILL_DIR/references/<category>.md

    The notes decide which papers belong to a category, not the registry tags (those were a
    first guess made without the full text). Mismatches are printed so the registry can be fixed.
    The file is rebuilt from scratch each run, so edit the notes, not the reference file.
    """
    sections = []
    for entry in entries:   # registry order
        note_path = ROOT / "sources" / "notes" / f"{entry['id']}.md"
        if not note_path.exists():
            continue

        note = note_path.read_text()
        try:
            advice = advice_by_category(note)
        except ValueError as error:
            raise ValueError(f"{note_path.name}: {error}") from error
        tagged = category in entry["categories"]
        if category not in advice:
            if tagged:
                print(f"  Note: {entry['id']} is tagged {category} in the registry, but its note has no section for it")
            continue
        if not tagged:
            print(f"  Note: {entry['id']} has a {category} section, but isn't tagged {category} in the registry")

        heading = note.splitlines()[0].lstrip("#").strip()   # e.g. "Adding Error Bars to Evals (Miller, 2024)"
        sections.append(f"## {heading}\n\n{advice[category]}")

    text = (
        f"<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->\n"
        f"# {category}\n\n" + "\n\n".join(sections) + "\n"
    )
    reference_path = SKILL_DIR / "references" / f"{category}.md"
    reference_path.parent.mkdir(parents=True, exist_ok=True)
    reference_path.write_text(text)
    print(f"Wrote {reference_path.relative_to(ROOT)} ({len(sections)} papers)")


def make_skill() -> None:
    """Pass 3: all reference files -> SKILL.md.draft (a draft, so you review before replacing SKILL.md)

    TODO: read every file in references/, fill the "skill_md" prompt, ask the model, write the draft.
    """


# --- Run ----------------------------------------------------------------------

entries = yaml.safe_load((ROOT / "sources" / "registry.yaml").read_text())
manifest = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text())   # written by fetch_papers.py

if STEP == "notes":

    progress = tqdm(entries, desc="Taking notes", unit="paper")
    for entry in progress:
        print(f"Processing {entry["id"]}")

        if ONLY and entry["id"] != ONLY:
            continue
        if entry["id"] not in manifest:
            print(f"Skipping {entry['id']}: no PDF in the manifest yet")
            continue
        make_note(entry, ROOT / manifest[entry["id"]]["pdf_path"])

elif STEP == "references":
    for category in CATEGORIES:
        if ONLY and category != ONLY:
            continue
        make_reference(category, entries)   # all papers: the notes decide which ones belong

elif STEP == "skill":
    make_skill()