<references>
{references}
</references>

You are helping build an AI advisor that helps researchers and engineers design, build and validate AI evaluations using measurement science. It is packaged as an Agent Skill: a folder with a SKILL.md file and a `references/` folder holding one file per category. Above are all seven reference files. Each one was assembled by copying the advice for that category from short notes on a curated set of papers, so each file is a list of papers rather than a synthesis.

Your job is to write the SKILL.md. An agent loads it every time the skill is used. It loads a reference file only when SKILL.md tells it to. So SKILL.md must do what the reference files can't: give the agent the ideas that cut across categories, a way to work through a request, and a clear guide to which reference file to read when. It should not repeat the reference files' detail. If a point is specific to one category, leave it in that file and point to it.

The categories are:
- constructs: what exactly is being measured (capabilities, propensities, dispositions, defining concepts)
- validity: whether scores support the intended claims (validity arguments, evidence types, threats such as contamination)
- elicitation: getting the behaviour you mean to measure (prompting, scaffolding, fine-tuning, controls, sandbagging, evaluation awareness)
- scoring: turning outputs into scores (metrics, rubrics, LLM judges, human raters)
- reliability: whether scores are consistent (across runs, prompts, formats and items; response biases; label errors)
- measurement-models: from item responses to construct scores (IRT, factor analysis, general scales, efficient testing)
- generalization: from scores to claims beyond the test (eval-specific uncertainty, coverage, predicting deployment and future models)

The skill's scope is what makes AI evals trustworthy. General statistics or programming help, eval infrastructure and harnesses, and the content of benchmarks in particular domains are out of scope.

Write SKILL.md using exactly this structure. Aim for about 1,000–1,500 words in total, not counting the frontmatter.

```
---
name: science-of-evals
description: <see below>
---

# Science of evals

## Scope
## Core principles
## Workflow
## Reference files
## How to advise
```

**description** (frontmatter): one paragraph of at most 1,000 characters, in the third person. The agent reads only this text when deciding whether to use the skill, so say what the skill does and list the situations it should be used in. Include situations where the user does not say "eval science" or "measurement", for example: designing a benchmark, deciding whether a score supports a claim, comparing models on a leaderboard, setting up an LLM judge, adding error bars, worrying about contamination or sandbagging, or reviewing someone else's eval. Lean towards using the skill too often rather than too rarely, but don't claim the out-of-scope topics.

**Scope:** two or three sentences on what the advisor covers and what it does not.

**Core principles:** 6–10 principles that hold across categories and that several papers support. Make each one a bold one-line statement, followed by one to three sentences on why it matters and what it implies in practice, citing the papers it rests on as (Author et al., year). Prefer principles that change what someone does, such as "state the claim before choosing the metric", over general statements such as "validity is important". Where papers disagree or emphasise different things, say so in a sentence rather than smoothing it over.

**Workflow:** the order in which the agent should work through a request, as numbered steps. Start by establishing what claim the user wants their scores to support, because most later choices depend on it. Then cover the main kinds of request: designing a new eval, auditing or reviewing an existing one, and interpreting or reporting results. These can be short sub-lists or notes on which steps matter most for each kind. At each step, name the reference file or files to read.

**Reference files:** a table with three columns: file (as `references/<category>.md`), what it covers (from the papers it actually contains, not only the category definition), and when to read it (the questions or situations that call for it). After the table, add a few lines on common questions that need more than one file, e.g. "judging whether an LLM-judge score can be trusted: scoring, then reliability".

**How to advise:** 4–6 bullets on how the agent should answer. Cover asking about the intended claim and use when it is unclear, giving concrete next steps rather than a survey of the literature, citing papers from the reference files, saying plainly when the evidence is thin or the papers don't cover a question, and staying within scope.

Rules:
- Base everything on the reference files above. Do not add papers, findings or numbers that are not in them. If a principle you think is important has no support in the files, leave it out, and note it in the closing comment described below.
- Cite every substantive claim as (Author et al., year), spelled as in the reference files' headings.
- Paraphrase in your own words. Quote only if the exact wording matters, and then use fewer than 15 words.
- Write instructions to the agent in the imperative ("Ask...", "Read..."), and explain why where it isn't obvious. Avoid all-caps MUST or NEVER.
- Use tool-neutral wording such as "read references/validity.md". Do not name the tools of a particular product.
- Output only the SKILL.md content, starting with the `---` line of the frontmatter. After it, add one HTML comment (`<!-- ... -->`) for the human reviewer listing: principles you considered but left out for lack of support, places where the reference files seemed thin or contradictory, and anything you were unsure about.
