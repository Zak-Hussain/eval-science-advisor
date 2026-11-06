from pathlib import Path
import re
import urllib.request
import yaml
from datetime import date
import time

ROOT = Path(__file__).resolve().parent.parent

_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v(\d+))?")

# ------------------------------------------------------------------------------

def parse_arxiv_url(url: str) -> tuple[str, int | None]:

    """'https://arxiv.org/abs/2405.10938v2' -> ('2405.10938', 2)
    'https://arxiv.org/pdf/2405.10938'   -> ('2405.10938', None)"""

    match = _ARXIV_ID_RE.search(url)
    if match is None:
        raise ValueError(f"Could not find an arxiv ID in URL: {url!r}")
    arxiv_id, version = match.groups()
    return arxiv_id, int(version) if version else None


def resolve_latest_version(arxiv_id: str) -> int:
    """Asks the arXiv API for the paper's current version number."""
    url = f"https://arxiv.org/api/query?id_list={arxiv_id}"
    xml = urllib.request.urlopen(url).read().decode()    # The response contains links like 'http://arxiv.org/abs/2405.10938v2'
    match = re.search(rf"{re.escape(arxiv_id)}v(\d+)", xml)
    if match is None:
        raise ValueError(f"Could not find a version for arXiv ID {arxiv_id!r} in the API response")
    return int(match.group(1))


def download_pdf(arxiv_id: str, version: int, out_dir: Path) -> Path:
    """Download https://arxiv.org/pdf/{id}v{version} to out_dir/{id}v{version}.pdf"""
    url = f"https://arxiv.org/pdf/{arxiv_id}v{version}"
    out_path = out_dir / f"{arxiv_id}v{version}.pdf"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(urllib.request.urlopen(url).read())
    return out_path



def fetch_arxiv_paper(url: str, out_dir: Path) -> dict: 
    """
    Download an arXiv paper as a PDF and return the version for documentation purposes.
    
    Returns e.g.: {"arxiv_id": "2405.10938", "version": 2, "pdf_path": Path("sources/pdfs/2405.10938v2.pdf")}
    """
    arxiv_id, version = parse_arxiv_url(url)  
    if version is None:
        version = resolve_latest_version(arxiv_id)
    pdf_path = download_pdf(arxiv_id, version, out_dir)
    return {"arxiv_id": arxiv_id, "version": version, "pdf_path": pdf_path}


# Load the registry 
entries = yaml.safe_load((ROOT / "sources" / "registry.yaml").read_text())

# Loop through entries, identify arxiv articles, fetch and save
manifest = {}
for entry in entries:

    if "arxiv.org" in entry['url']:
        result = fetch_arxiv_paper(entry['url'], ROOT / "sources" / "pdfs")
        manifest[entry['id']] = {
            "arxiv_id": result["arxiv_id"],
            "version": result["version"],
            "pdf_path": str(result["pdf_path"].relative_to(ROOT)),
            "fetched": date.today(),
        }
    
    # arXiv asks scripts to pause between requests 
    time.sleep(3)

# Save manifest 
(ROOT / "sources" / "manifest.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False))




    