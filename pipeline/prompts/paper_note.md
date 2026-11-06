You are helping build an AI advisor that helps researchers and engineers design, build and validate AI evaluations using measurement science. The advisor's knowledge is distilled from a curated set of papers, and you are working on one of them.

The attached paper is "{title}". It was selected for these categories of the advisor: **{categories}**.

The advisor's categories are:
- constructs: what exactly is being measured (capabilities, propensities, dispositions, defining concepts)
- validity: whether scores support the intended claims (validity arguments, evidence types, threats such as contamination)
- elicitation: getting the behaviour you mean to measure (prompting, scaffolding, fine-tuning, controls, sandbagging, evaluation awareness)
- scoring: turning outputs into scores (metrics, rubrics, LLM judges, human raters)
- reliability: whether scores are consistent (across runs, prompts, formats and items; response biases; label errors)
- measurement-models: from item responses to construct scores (IRT, factor analysis, general scales, efficient testing)
- generalization: from scores to claims beyond the test (eval-specific uncertainty, coverage, predicting deployment and future models)

Write a short distillation note on it, at most about 400 words. The note will be read by later steps that combine several papers into one reference file per category, and by a human checking those steps' claims against the source. So capture what someone advising on evals would need from this paper, not a summary of everything in it. Give each of the paper's categories its due, rather than centring the note on one of them.

Use exactly this structure:

# <short title> (<first author surname> et al., <year>)

**What kind of evidence:** one line, e.g. empirical study, systematic review, theory, position paper, methods paper.

**Key claims:** 3–6 bullets. Each is one claim the paper supports, stated plainly, with the specific number or finding where there is one.

**What the advisor should take from it:** practical guidance for someone designing, auditing or interpreting an eval, grouped under a sub-heading for each of the paper's categories (e.g. `*validity:*`), with 1–4 bullets each. If the paper has little to say about one of its listed categories, say so in one line rather than stretching.

**Caveats:** 1–3 bullets on limits of the evidence: sample, methods, anything the authors acknowledge, or reasons to apply it cautiously.

**Other categories:** any category not listed above that the paper also informs substantially, with a few words on how. Write "none" if there are none.

Rules:
- Paraphrase in your own words. Quote only if the exact wording matters, and then fewer than 15 words.
- Only include what the paper actually says. If something is your inference, mark it as such.
- No preamble or closing remarks: output only the note.