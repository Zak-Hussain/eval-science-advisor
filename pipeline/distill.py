from pathlib import Path
import anthropic 
import yaml

ROOT = Path(__file__).resolve().parent.parent

MODEL = "claude-opus-5-5"
MAX_TOKENS = 8000

STEP = "notes"  # In order of processing: "notes", "reference", or "skill"
ONLY = None # For testing purposes 

# ------------------------------------------------------------------------------


def load_prompt(name: str):
    pass
