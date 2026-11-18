# Eval Science Advisor

**An open-source agent skill for applying measurement science to AI evaluation.**

Eval Science Advisor is an agent skill. It is meant to help you design, audit and interpret AI evaluations, using the research on measurement in AI evaluation. Its advice is intended to cover seven areas: constructs, validity, elicitation, scoring, reliability, measurement models and generalisation. The skill instructs the agent to cite the papers each piece of advice draws on.

It follows the open [Agent Skills](https://agentskills.io/home) standard, so it should work with any compatible agent, whichever model provider you use.

**Status:** early development (yet to be evaluated!). 

> **AI use statement:** Most of the code in this repo was written with Claude Code (Claude Opus 5.5). A human domain expert led and directed the work. LLMs also produce parts of the skill's content: they expanded the source list, wrote the per-paper notes and drafted `SKILL.md`. See [How it's built](#how-its-built) for which model did each step.

---

## What it is meant to help with

The skill is designed to apply measurement-science reasoning to questions like these:

- "I'm building a benchmark for agentic coding. What exactly should it measure?"
- "I'm measuring refusal rate on self-harm prompts. Is that the right metric?"
- "I changed the system prompt and the safety score went up. Can I say the change caused it?"
- "How do I check my LLM judge against human raters before I trust its scores?"
- "Model A scores 2 points higher than model B, but they were run with different system prompts. Is that a real difference?"
- "How many items do I need, and how should I report error bars?"
- "Could contamination, saturation or prompt sensitivity explain these results?"
- "My model is 97% safe on single-turn prompts. Does that tell me how it behaves in long conversations or in production?"
- "Review this eval paper. Do the scores support its claims?"

It is not meant to help with general statistics, eval harnesses and infrastructure, or the subject-matter content of domain benchmarks.

## Install

The skill is the [`science-of-evals/`](science-of-evals/) folder.

- **Claude Code:** copy it to `~/.claude/skills/` (for all your projects) or `.claude/skills/` (for one project).
- **Claude.ai / Claude Desktop:** zip the folder and upload it under *Settings → Capabilities → Skills*.
- **Other agents:** put the folder wherever your agent loads Agent Skills from.

## How it's built

The skill is distilled from a curated set of papers:

1. **Registry.** [`sources/registry.yaml`](sources/registry.yaml) lists the sources and tags each one with categories. It started as about 10 papers chosen by a domain expert. Claude Opus 5.5 then expanded it to 31 sources, using the `/deep-research` skill.
2. **Fetching.** [`pipeline/fetch_papers.py`](pipeline/fetch_papers.py) downloads the PDFs from arXiv and records the versions it used in [`sources/manifest.yaml`](sources/manifest.yaml). Only the 23 sources on arXiv are fetched and distilled so far.
3. **Notes.** [`pipeline/distill.py`](pipeline/distill.py) uses an LLM to write one note per paper ([`sources/notes/`](sources/notes/)). For now the notes are written by `zai-org/GLM-5.2` (served by DeepInfra). Frontier-model credits would allow better notes; we are looking for funding for them.
4. **References.** The notes are grouped into one reference file per category ([`science-of-evals/references/`](science-of-evals/references/)). The grouping is currently hard-coded. An LLM could do this step instead and add more context.
5. **Skill.** Claude Fable 5.2 wrote [`SKILL.md`](science-of-evals/SKILL.md) from the reference files, using the `/skill-creator` skill.

The prompts for the LLM steps are in [`pipeline/prompts/`](pipeline/prompts/).

## Next steps

1. Reconsider reference categories.
2. Fix [`pipeline/prompts/paper_note.md`](pipeline/prompts/paper_note.md) to make sure paper titles are not abreviated/paraphrased. 
3. Expand [`pipeline/fetch_papers.py`](pipeline/fetch_papers.py) to non-arXiv, licence-permitting papers. Update `evaluation/plagarism_check.py` to include additional sources in check.
4. Expand [`sources/registry.yaml`](sources/registry.yaml), make the search more systematic.
5. Use a more capable model for the pdf -> notes distillation.
6. Evaluate!

## License

[Apache 2.0](LICENSE)
