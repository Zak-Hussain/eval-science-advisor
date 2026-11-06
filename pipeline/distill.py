from pathlib import Path
import yaml
from huggingface_hub import InferenceClient
import pymupdf
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent

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


def make_reference(category: str, category_entries: list[dict]) -> None:
    """Pass 2: the notes of every paper tagged with this category -> skills/eval-science-advisor/references/<category>.md

    category_entries includes papers whose secondary categories include this one, not just their first.

    TODO:
      - read each entry's note from sources/notes/<id>.md and join them into one string
      - prompt = load_prompt("reference_file", category=category, notes=all_notes)
      - text = ask_model(prompt)
      - write text to the reference file
    """


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
        progress.set_postfix_str(entry['id']) 

        if ONLY and entry["id"] != ONLY:
            continue
        if entry["id"] not in manifest:
            print(f"Skipping {entry['id']}: no PDF in the manifest yet")
            continue
        make_note(entry, ROOT / manifest[entry["id"]]["pdf_path"])

elif STEP == "references":
    categories = sorted({c for entry in entries for c in entry["categories"]})
    for category in categories:
        if ONLY and category != ONLY:
            continue
        make_reference(category, [e for e in entries if category in e["categories"]])

elif STEP == "skill":
    make_skill()