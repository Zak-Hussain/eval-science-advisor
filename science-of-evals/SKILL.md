---
name: "science-of-evals"
description: "Advises on designing, building, auditing and interpreting AI evaluations using measurement science, covering what is being measured, validity, elicitation, scoring, reliability, measurement models and generalising from scores. Use whenever a user is designing a benchmark or eval, choosing a metric or rubric, setting up or validating an LLM judge or human raters, deciding whether a score supports a claim, comparing models or reading a leaderboard, adding error bars or testing significance, picking a sample size, worrying about contamination, prompt sensitivity, sandbagging or evaluation awareness, predicting deployment or future-model performance from eval results, or reviewing someone else's eval or paper, even if they never say \"measurement\" or \"eval science\". Not for general statistics or programming help, eval harnesses and infrastructure, or the subject-matter content of domain benchmarks."
---

# Science of evals

## Scope

This skill covers what makes an AI evaluation trustworthy: defining the construct, arguing validity, eliciting the intended behaviour, scoring, reliability, measurement models, and generalising from scores to claims. It does not cover general statistics or programming help, eval infrastructure and harnesses, or the content of benchmarks in particular domains.

## Core principles

1. **State the claim, and what it is about, before choosing tasks or metrics.** A claim about a directly measurable criterion needs different evidence from a claim about an abstract construct, and the wider the gap between what is measured and what is claimed, the more evidence is owed (Salaudeen et al., 2025). Narrow the concept into an explicit definition before any task design (Wallach et al., 2025; Bean et al., 2025), and treat broad labels such as "general capability" as too vague to operationalise (Raji et al., 2021).

2. **Treat a score as one manifestation of a disposition under stated conditions.** Prompting, sampling, filters and tools are evaluation variables, and a base model and a deployed system are different subjects of measurement (Harding et al., 2024; Voudouris et al., 2026). Record the system boundary and conditions, and vary those a plausible user could vary, because one prompt format gives only a point estimate (Sclar et al., 2024).

3. **Treat metric choice as an intervention on the result.** All-or-nothing metrics can turn smooth improvement into an apparent jump, and continuous metrics can recover signal near chance (Schaeffer et al., 2023; Heineman et al., 2025); metric choice also changes observed prompt sensitivity (Sclar et al., 2024). Check that a headline finding survives more than one reasonable metric.

4. **Look for ways to score well without the target ability.** Memorised test items, shortcuts, label errors and response biases all produce high scores (Xu et al., 2024; Harding et al., 2024; Northcutt et al., 2021; Meyer et al., 2026). Recommend a direct check: perturbed items, post-cutoff items, corrected labels, or reverse-keyed items.

5. **Do not accept consistency or agreement as proof of validity.** Internal consistency can come entirely from response bias (Meyer et al., 2026), and reproducible scores do not show the benchmark represents the claimed capability (Raji et al., 2021). The papers differ on judges: Zheng et al. (2023) treat agreement with human labels as the core argument for an LLM judge, while Wallach et al. (2025) ask first whether the humans match the defined concept, and Guerdan et al. (2025) show forced-choice human labels can bias judge selection.

6. **Consider that the eval may not have elicited the behaviour that matters.** Prompting alone can understate what fine-tuning reveals (Greenblatt et al., 2024), and models that detect testing may behave differently in deployment (Needham et al., 2025). Red-teaming gives anecdotes of failure, which is different from measuring an inclination (Voudouris et al., 2026). Needham et al. (2025) describe sandbagging and alignment faking as hypothetical but growing risks, so present them as threats to rule out.

7. **Report uncertainty that fits the structure of the data.** Give intervals with scores, use paired item-level differences for comparisons, and cluster when items come in related groups (Miller, 2024; Bean et al., 2025). Miller (2024) builds on the Central Limit Theorem; Bowyer et al. (2025) show those intervals, and bootstrap ones, are too narrow below a few hundred items and recommend Bayesian or Wilson intervals. Item sampling is one noise source among several: format and training-run noise are separate (Sclar et al., 2024; Heineman et al., 2025).

8. **Separate rater disagreement that is signal from error.** Genuine disagreement, subjectivity, multiple plausible answers and annotation mistakes call for different treatment, and collapsing them into one gold label discards information (Plank et al., 2022; Guerdan et al., 2025).

9. **Generalise only as far as the item sample and context allow.** Treating items as a sample from a wider population licenses generalising (Miller, 2024), but only if items were sampled to represent the task space; convenience samples do not earn this (Bean et al., 2025; Voudouris et al., 2026). Check that test coverage matches the deployment context (Raji et al., 2021) and re-examine validity when the context changes (Wallach et al., 2025; Salaudeen et al., 2025).

10. **Do not read an aggregate or latent score as one clean ability.** Aggregates can hide subgroup failures (Raji et al., 2021), and benchmark batteries share a few latent dimensions (Burnell et al., 2023; Ruan et al., 2024). The papers disagree on method: several fit latent models to populations of models (Polo et al., 2024; Burnell et al., 2023; Ruan et al., 2024), whereas Voudouris et al. (2026) accept such models only when difficulty is tied to independently measured task features, as Zhou et al. (2025) attempt.

## Workflow

1. **Establish the claim.** Find out what the scores are meant to show, about which system, for whom, and what decision depends on it. Most later choices follow from this. If the concept is fuzzy, read `references/constructs.md`.
2. **Classify the claim.** Decide whether it concerns a criterion or a construct and how far it reaches beyond the test; this sets which validity evidence is needed. Read `references/validity.md`.
3. **Identify the kind of request** and follow the matching branch.
   - **Designing a new eval:** (a) define the construct and its sub-components (`constructs`); (b) plan validity evidence and contamination defences (`validity`); (c) plan item sampling and coverage (`generalization`); (d) fix and vary elicitation conditions (`elicitation`); (e) choose metric, rubric and raters or judge (`scoring`); (f) plan sample size, repeats and uncertainty reporting (`reliability`, `generalization`); (g) only if aggregating across items or benchmarks, choose a measurement model (`measurement-models`).
   - **Auditing or reviewing an eval:** reconstruct the claim the authors make, then check in this order, since earlier failures make later checks moot: construct definition (`constructs`), match between measurement and claim and score-inflating threats (`validity`), elicitation (`elicitation`), scoring (`scoring`), consistency and error bars (`reliability`), then reach of the conclusions (`generalization`). Report the most serious gaps first, with the check that would close each.
   - **Interpreting or reporting results:** start with uncertainty and comparison method (`reliability`, `generalization`), then metric artefacts (`scoring`), then what the scores do and do not support (`validity`, `generalization`).
4. **Read only the files the step calls for,** then state what remains unsupported: claims the evidence cannot carry and questions the files do not answer.

## Reference files

| File | What it covers | When to read it |
|---|---|---|
| `references/constructs.md` | Systematising concepts; capability versus propensity; criterion versus construct; narrow definitions and sub-components; latent structure of capabilities; label variation; borrowed psychometric traits | "What are we measuring?"; vague or contested targets; one construct or several |
| `references/validity.md` | Validity lenses and which evidence a claim needs; contamination detection and prevention; memorisation, label-error and response-bias threats; evaluation awareness; emergence claims; judge validation | "Does this score support this claim?"; reviewing an eval; contamination worries |
| `references/elicitation.md` | Background conditions as variables; fine-tuning elicitation and password-locked models; evaluation awareness and realistic scenarios; format grammars; memorisation probes; rating-task design | Possible under-elicitation or sandbagging; prompt and setup choices; designing rater tasks |
| `references/scoring.md` | Indicators and aggregation; continuous versus discontinuous metrics; judge modes and guidelines; agreement and soft-label metrics; intervals for confusion-matrix metrics | Choosing a metric or rubric; setting up an LLM judge; choosing an agreement metric |
| `references/reliability.md` | Standard errors and clustering; variance reduction; format spread; checkpoint noise; judge position and verbosity biases; label errors; artifactual consistency | Error bars; unstable results; judge or rater consistency; label quality |
| `references/measurement-models.md` | IRT and anchor items; factor analysis and PCA; demand-level scales; separating trait from response bias | Combining items or benchmarks into ability scores; shrinking a benchmark |
| `references/generalization.md` | Coverage and sampling; small-sample intervals and model comparison; power analysis; predicting untested tasks, deployment and future models; scaling laws; saturation | Sample size; small evals; "will this hold in deployment or for the next model?" |

Questions that need more than one file:

- Trusting an LLM-judge score: `scoring`, then `reliability`, then `validity`.
- Error bars or "is this difference real?": `reliability`, then `generalization`; the small-sample methods are in the second.
- Contamination: `validity`, then `elicitation` for probing methods.
- Sandbagging or evaluation awareness: `elicitation`, then `validity`.
- Prompt sensitivity: `reliability`, then `elicitation`.
- Human label disagreement: `constructs`, then `scoring`.
- Emergence or scaling claims: `scoring`, then `generalization`.

## How to advise

- Ask what claim the scores should support and how they will be used when this is unclear; if the user cannot say yet, help them write it down before anything else.
- Give concrete next steps sized to the user's situation, with a reason for each, instead of surveying the literature.
- Cite the papers from the reference files as (Author et al., year) for each substantive recommendation, and paraphrase them.
- Say plainly when the evidence is thin, rests on one paper, or the papers disagree, and when the files do not cover a question. Do not fill gaps with papers or numbers from outside the files; label any general reasoning as your own.
- Stay within scope. For out-of-scope parts, say so briefly and continue with the measurement question.

<!--
Reviewer notes

Principles considered but left out for lack of support:
- Preregistering analyses and predictions: only Ruan et al. (2024) touches it, via preregistered future models.
- Correcting for multiple comparisons: only Schaeffer et al. (2023), one bullet.
- Human baselines and comparing models to people: nothing in the files.
- Documentation and reporting standards as a principle of their own: scattered bullets (Raji, Plank, Bean) but no shared framework.
- Benchmark saturation and retirement: brief mentions only (Heineman, Ruan).
- Weighing eval cost against decision value: not covered.

Thin or oddly placed material:
- elicitation.md has almost nothing on scaffolding or agents despite the category definition, and its sandbagging evidence is essentially Greenblatt et al. (2024). It also holds contamination probes (Xu) and rating-task design (Guerdan), which the routing notes work around.
- Error-bar advice is split: standard errors and clustering are in reliability.md, while small-sample intervals, paired differences and power analysis are in generalization.md, and F1/MCC intervals are in scoring.md. I routed around this; moving them might be cleaner.
- reliability.md has little on run-to-run variance beyond Miller's resampling and little on human inter-rater reliability.
- measurement-models.md covers "efficient testing" only through tinyBenchmarks; nothing on adaptive testing.
- Wallach's "seven lenses" are referred to but not listed in validity.md.
- Harding's "trying" test is named without an operational procedure.

Disagreements I surfaced: Miller (CLT) vs Bowyer (not below a few hundred items); Zheng (human agreement validates a judge) vs Wallach and Guerdan; population-fitted latent models (Polo, Burnell, Ruan) vs Voudouris; Miller's super-population framing vs convenience sampling (Bean, Voudouris).
Not surfaced: Guerdan finds rater error has limited effect on judge rankings, while Northcutt finds label errors can reorder models. The settings differ, so I was unsure whether this is a real conflict.

Unsure about:
- Many figures in the files describe specific models or datasets; I dropped a 'keep figures in context' bullet for length.
- I wrote ten principles, the top of the allowed range; 8 (rater disagreement) is the narrowest and could move to scoring.md.
- The audit order in the workflow is my own judgement; no paper in the files prescribes one.
- "Label any general reasoning as your own" permits the agent to reason beyond the files; tighten if you want strict refusal.
- Zheng's agreement and bias figures are tied to specific judge models, so I kept all such numbers out of SKILL.md.
-->