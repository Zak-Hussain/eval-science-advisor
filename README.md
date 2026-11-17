# Eval Science Advisor

**An open-source AI advisor that brings measurement science to AI evaluation.**

Eval Science Advisor is an agent skill. It helps you design, audit and interpret AI evaluations, using the research on measurement in AI evaluation. Its advice covers seven areas: constructs, validity, elicitation, scoring, reliability, measurement models and generalisation. Each piece of advice cites the papers it draws on.

It was built and tested with **Claude**, but it follows the open Agent Skills standard. It works with any compatible agent, whichever model provider you use.

**Status:** early development. 

---

## What it helps with

Ask your assistant questions like these, and the skill will apply measurement-science reasoning:

- "I'm building a benchmark for agentic coding. What exactly should it measure?"
- "Is my LLM judge good enough to replace human raters?"
- "Model A scores 2 points higher than model B. Is that a real difference?"
- "How many items do I need, and how should I report error bars?"
- "Could contamination or prompt sensitivity explain these results?"
- "Review this eval paper. Do the scores support its claims?"

It does not help with general statistics, eval harnesses and infrastructure, or the subject-matter content of domain benchmarks.

## Install

The skill is the [`science-of-evals/`](science-of-evals/) folder.

- **Claude Code:** copy it to `~/.claude/skills/` (for all your projects) or `.claude/skills/` (for one project).
- **Claude.ai / Claude Desktop:** zip the folder and upload it under *Settings → Capabilities → Skills*.
- **Other agents:** put the folder wherever your agent loads Agent Skills from.

## How it's built

The skill is distilled from a curated set of papers:

1. [`sources/registry.yaml`](sources/registry.yaml) lists the papers and tags each one with categories.
2. [`pipeline/fetch_papers.py`](pipeline/fetch_papers.py) downloads the PDFs from arXiv and records the versions it used in [`sources/manifest.yaml`](sources/manifest.yaml).
3. [`pipeline/distill.py`](pipeline/distill.py) uses an LLM to write one note per paper ([`sources/notes/`](sources/notes/)). The notes are then grouped into their respective reference files (one file per category) and distilled by an LLM into `SKILL.md`. The prompts for these steps are in [`pipeline/prompts/`](pipeline/prompts/).


## Next steps: 

1. Reconsider reference categories.
2. Expand [`sources/registry.yaml`](sources/registry.yaml), make the search more systematic. 
3. Use a more capable model for the pdf -> notes distillation. 
4. Evaluate! 


## License

[Apache 2.0](LICENSE)
