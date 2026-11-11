<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# generalization

## Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

- Because dispositions are counterfactual, measurement must support extrapolation beyond tested ranges—both beyond human-level performance and into unsafe domains where direct testing is prohibited.
- Extrapolation is feasible by varying contextual properties across benign tasks that share structural features with dangerous ones, then inferring the response function in unobserved regions.

## Defining Model Capabilities (Harding et al., 2024)

- Capability claims are often deployment-specific; a model succeeding via memorisation lacks a generic capability but may have a specific one where it never sees novel queries.
- For inter-model comparison, use model-specific background conditions optimised to elicit the capability, but exclude gerrymandered conditions via the "trying" test.

## The “Everything in the Whole Wide World” Benchmark (Raji et al., 2021)

- Do not assume benchmark coverage matches deployment scope: evaluate geographic, temporal, and demographic alignment between the test set and the intended application context.
- Resist extrapolating from benchmark scores to out-of-context applications; the paper cites cases where firms cited benchmark performance as evidence of broad technical achievement.

## Measurement to Meaning: A Validity-Centered Framework for AI Evaluation (Salaudeen et al., 2025)

- External validity must be established whenever the claim must hold in a context different from the measurement context—test across formats, populations, and settings.
- The conceptual gap between what is measured and what is claimed determines the standard of evidence required; broader gaps demand stronger justification.

## Measuring what Matters (Bean et al., 2025)

- Ensure task items represent the overall task space via robust sampling (e.g., random or stratified) rather than convenience sampling.
- Explicitly include task items that test known LLM sensitivities, such as input permutations or minor prompt variations.

## Benchmark Data Contamination of Large Language Models: A Survey (Xu et al., 2024)

- Semantic and information-level contamination cannot be fully filtered from pretraining corpora, so claims extrapolated from benchmark scores to real-world deployment remain vulnerable even after decontamination efforts.
- Secondary contamination can occur when regenerated or newly curated data is itself absorbed into future pretraining corpora.

## Password-locked models for stress-testing capability elicitation (Greenblatt et al., 2024)

- Elicitation transfers across domains: unlocking on one domain often unlocks others, so narrow demonstrations may suffice to assess broader capabilities—but MMLU shows domain-dependent variation, so don't assume it.

## Evaluation awareness in frontier LLMs (Needham et al., 2025)

- The paper explicitly frames evaluation awareness as "a new source of potential distribution shift between testing and real-world deployment." Any claim that eval results generalize to deployment must account for the possibility that models behave systematically differently across the two settings.

## Judging LLM-as-a-Judge (Zheng et al., 2023)

- No single benchmark determines model quality; combine capability-based and preference-based benchmarks for comprehensive evaluation.

## Emergent Abilities as Metric Artifacts (Schaeffer et al., 2023)

- Do not extrapolate from a single metric's sharp transition to claims about fundamental capability thresholds or future model behaviour; check whether the underlying per-token loss follows a smooth scaling law that the metric is merely reformatting.

## Prompt Format Sensitivity (Sclar et al., 2024)

- Claims about a model's general capability on a task are suspect if based on a single format, since a non-adversarial user might encounter a much lower performance format.
- Format robustness does not transfer: a format that is good for one model may be bad for another.

## Signal and Noise: A Framework for Reducing Uncertainty in LM Evaluation (Heineman et al., 2025)

- Before using small-scale experiments to predict large-scale behavior, compute SNR at the small scale; benchmarks with low SNR are poor predictors of both model rankings and scaling-law targets.
- Multi-task averages are not always better than individual tasks for scaling-law prediction; some individual tasks (e.g., TriviaQA) have lower noise and prediction error than their group averages.
- SNR can diagnose benchmark saturation: tasks like ARC Easy show high SNR at 1.5B but drop at 32B.

## Label Errors in ML Benchmark Test Sets (Northcutt et al., 2021)

- In noisier real-world datasets, lower-capacity models may deploy better than higher-capacity models that overfit systematic label-error patterns.
- The gap between original and corrected accuracy grows proportionally with noise prevalence, so noisier datasets face greater risk of selecting the wrong model.
- Correcting at least test-set labels is recommended to better predict real-world deployment performance.

## tinyBenchmarks: evaluating LLMs with fewer examples (Polo et al., 2024)

- Testing on the most recent 25% of models by release date simulates realistic use; methods remain effective, supporting their use for evaluating future models and monitoring checkpoints during pre-training.
- IRT-based methods generalize to specialized LLMs whose correctness patterns differ from the training set, whereas correctness-based methods do not.
- With a longer time horizon (75% test split, ~3 months future data), IRT++ remains robust, though the authors recommend periodically updating anchor examples and IRT parameters.

## Revealing the structure of language model capabilities (Burnell et al., 2023)

- Use estimates of broad cognitive abilities to predict model performance on untested tasks, provided the cognitive demands of those untested tasks are known.
- Account for how model properties (like scale or instruction tuning) have divergent, non-uniform effects on different capabilities when predicting deployment behavior or scaling laws.

## General Scales for AI Evaluation (Zhou et al., 2025)

- Train per-model assessors on the demand vector to predict instance-level success; these generalize better OOD than embedding or fine-tuning because demand features are interpretable and less prone to spurious overfitting.
- Compare a model's ability vector to a new task's demand vector for counterfactual failure analysis without running the model.

## Adding Error Bars to Evals (Miller, 2024)

- Conceptualize eval questions as a random sample from a hypothetical super-population to justify generalizing from specific eval items to broader model capabilities.
- Report standard errors alongside mean scores, and use paired question-level differences with confidence intervals when comparing models, as this provides a "free" variance reduction.
- Use the provided power analysis formulas to determine if an eval has enough questions to reliably detect a hypothesized difference between models (Minimum Detectable Effect), preventing wasted effort on underpowered evals.

## Observational Scaling Laws (Ruan et al., 2024)

- Fit scaling laws on weak models (FLOPs ≤ Llama-2-7B) and extrapolate to stronger ones; PC measures yield lower MSE than compute baselines on holdout and preregistered future models (Llama-3.1-405B, Qwen2-72B).
- Sigmoidal curves predict transition points for "emergent" tasks, reframing discontinuity as an artifact of low resolution.

## Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

- For evals with fewer than a few hundred items, do not report CLT-based error bars; they typically overstate confidence by producing intervals that are too narrow.
- For single-model IID accuracy, use Bayesian Beta-Bernoulli credible intervals or Wilson score intervals (both trivial to implement via SciPy).
- For model comparison, sample from Beta posteriors to get credible intervals on the difference or odds ratio, and to compute P(model A > model B).
- For clustered evals, use a hierarchical Bayesian model (Beta-Binomial with dispersion parameter) fitted via importance sampling; code is provided in the paper's library.
