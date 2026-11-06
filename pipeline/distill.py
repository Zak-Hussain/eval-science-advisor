from pathlib import Path
import anthropic 
import yaml
import base64

ROOT = Path(__file__).resolve().parent.parent

MODEL = "claude-opus-5-5"
MAX_TOKENS = 8000
CLIENT = anthropic.Anthropic()  # Reads Anthropic's API key from environment

STEP = "notes"  # In order of processing: "notes", "reference", or "skill"
ONLY = None # For testing purposes 

# ------------------------------------------------------------------------------


def load_prompt(name: str, **fields) -> str:
    """Read pipeline/prompts/<name>.md and fill in its {placeholders}."""
    template = (ROOT / "pipeline" / f"{name}.md").read_text()
    return template.format(**fields)


def pdf_block(pdf_path: Path) -> dict:
    """Wrap a PDF so Claude reads the paper itself, figures and tables included."""
    data = base64.standard_b64encode(pdf_path.read_bytes()).decode() 
    return {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": data}}


def ask_claude(content: list[dict]) -> str:
    """Send one request to Claude and return the text of the reply."""
    response = CLIENT.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": content}]
    )

    if response.stop_reason == "max_tokens":
        raise RuntimeError(f"Reply hit MAX_TOKENS ({MAX_TOKENS}) and was cut off")
    
    # The reply is a list of content blocks; join the text ones.
    return "".join(block.text for block in response.content if block.type == "text")


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
    text = ask_claude([pdf_block(pdf_path), {"type": "text", "text": prompt}])

    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(text)
    print(f"Wrote {note_path.relative_to(ROOT)}")


# --- Run ----------------------------------------------------------------------

entries = yaml.safe_load((ROOT / "sources" / "registry.yaml").read_text())
manifest = yaml.safe_load((ROOT / "sources" / "manifest.yaml").read_text())   # written by fetch_papers.py

if STEP == "notes":
    for entry in entries:
        if ONLY and entry["id"] != ONLY:
            continue
        if entry["id"] not in manifest:
            print(f"Skipping {entry['id']}: no PDF in the manifest yet")
            continue
        make_note(entry, ROOT / manifest[entry["id"]]["pdf_path"])
    