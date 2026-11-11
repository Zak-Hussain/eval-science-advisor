You are helping build an AI advisor that helps researchers and engineers design, build and validate AI evaluations using measurement science. The advisor's knowledge is distilled from a curated set of papers, and you are working on one of them.

The attached paper is "{title}". A first pass, made without reading the full text, suggested these categories of the advisor: **{categories}**. Treat them as a starting point, not a final answer: you have the full paper, so you decide which categories it really belongs to.

The advisor's categories are:
- constructs: what exactly is being measured (capabilities, propensities, dispositions, defining concepts)
- validity: whether scores support the intended claims (validity arguments, evidence types, threats such as contamination)
- elicitation: getting the behaviour you mean to measure (prompting, scaffolding, fine-tuning, controls, sandbagging, evaluation awareness)
- scoring: turning outputs into scores (metrics, rubrics, LLM judges, human raters)
- reliability: whether scores are consistent (across runs, prompts, formats and items; response biases; label errors)
- measurement-models: from item responses to construct scores (IRT, factor analysis, general scales, efficient testing)
- generalization: from scores to claims beyond the test (eval-specific uncertainty, coverage, predicting deployment and future models)

Write a short distillation note on it, at most about 400 words. The note will be read by later steps that combine several papers into one reference file per category, and by a human checking those steps' claims against the source. So capture what someone advising on evals would need from this paper, not a summary of everything in it. Give each of the categories you choose its due, rather than centring the note on one of them.

Use exactly this structure:

# <short title> (<first author surname> et al., <year>)

**What kind of evidence:** one line, e.g. empirical study, systematic review, theory, position paper, methods paper.

**Key claims:** 3–6 bullets. Each is one claim the paper supports, stated plainly, with the specific number or finding where there is one.

**What the advisor should take from it:** practical guidance for someone designing, auditing or interpreting an eval, grouped under a sub-heading for each category the paper substantially informs, with 1–4 bullets each. Choose these categories from the full list above: include a suggested category only if the paper really supports it, and add any other category it substantially informs. Leave out a category entirely rather than writing a thin or filler section for it. Each sub-heading must be on its own line and spelled exactly like this, using a name from the list: `*validity:*`

**Caveats:** 1–3 bullets on limits of the evidence: sample, methods, anything the authors acknowledge, or reasons to apply it cautiously.

**Category changes:** one line on how your categories differ from the suggested ones, e.g. "added scoring: it introduces a new metric; dropped elicitation: only mentioned in passing". Write "none" if they are the same.

Rules:
- Paraphrase in your own words. Quote only if the exact wording matters, and then fewer than 15 words.
- Only include what the paper actually says. If something is your inference, mark it as such.
- No preamble or closing remarks: output only the note.