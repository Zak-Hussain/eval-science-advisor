<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# reliability

## Measuring what Matters (Bean et al., 2025)

- Report uncertainty estimates and use robust statistical methods for model comparisons.
- When using human raters, document rater demographics and mitigate potential biases in recruitment and instructions.

## Benchmark Data Contamination of Large Language Models: A Survey (Xu et al., 2024)

- Contamination effects are inconsistent across datasets and model sizes; a model may memorize without exploiting, or exploit without verbatim memorization, making detection results non-transferable across contexts.
- Dynamic benchmarks reduce contamination risk but introduce temporal inconsistency across evaluation cycles, complicating longitudinal comparisons.

## Judging LLM-as-a-Judge (Zheng et al., 2023)

- Always run pairwise comparison twice with swapped positions; declare a tie on inconsistency. This directly addresses the strong first-position bias seen across all judges.
- Verbosity bias is real: a "repetitive list" attack fools GPT-3.5 and Claude 91.3% of the time but GPT-4 only 8.7%.
- Even when an LLM can solve a problem independently, providing candidate answers can mislead its grading; chain-of-thought alone does not fully fix this.

## Validating LLM Judges Under Rating Indeterminacy (Guerdan et al., 2025)

- Rater error affects absolute prevalence estimates but has limited impact on judge system rankings relative to forced-choice selection effects; MSE on response sets remains rank-stable under simulated rater error (Fig. 38).

## Human Label Variation as Signal, Not Noise (Plank et al., 2022)

- Release annotator-level un-aggregated labels, even for a small data subset, and include annotator metadata (IDs, background, demographics, completion time) where responsible.
- Separating genuine HLV from annotation errors remains an open challenge; both error-detection methods and theoretical work on what constitutes an error are underdeveloped.

## Prompt Format Sensitivity (Sclar et al., 2024)

- Treat prompt formatting as a major source of measurement error; a single format yields a point estimate, not the full distribution.
- Use FORMATSPREAD (or similar bandit-based sampling) to estimate the performance interval across plausible formats under a fixed computational budget.
- Report performance spread (min-max across formats) rather than relying on a single format's score.

## Signal and Noise: A Framework for Reducing Uncertainty in LM Evaluation (Heineman et al., 2025)

- Estimate noise cheaply: use the relative std. dev. of the final 5–30 checkpoints of a single training run. This captures most of the variability from seeds and data order without retraining.
- Averaging scores across the final k checkpoints (exponential moving average) consistently reduces noise and improves rank-stability during training and at final evaluation.
- Low intrinsic dataset noise does not guarantee low modeling noise: e.g., BoolQ has low statistical variability but high checkpoint-to-checkpoint noise.

## Label Errors in ML Benchmark Test Sets (Northcutt et al., 2021)

- Assume test labels contain errors, especially for crowd-sourced or automatically labeled data. Even gold-standard benchmarks are not immune.
- Use confident learning to algorithmically pre-filter likely errors before human review, reducing review burden by up to ~90%; CL-flagged examples were 2.6x more likely to be mislabeled than non-flagged ones.
- CL misses a substantial fraction of errors: ~14% of ImageNet errors were in non-CL-flagged data. Algorithmic flagging is a prioritization tool, not a complete solution.

## LLM Psychological Profiles are Measurement Artifacts (Meyer et al., 2026)

- Apparent reliability in LLM evals can be entirely artifactual. If an instrument lacks reverse-keyed items, high inter-item correlation may reflect a directional response tendency rather than coherence.
- Test whether reliability survives under full response orthogonality (balanced forward and reverse keying). If reliability collapses to near zero, the original consistency was bias-driven.

## tinyBenchmarks: evaluating LLMs with fewer examples (Polo et al., 2024)

- Estimation error stays within 4% for nearly all individual models on MMLU with 100 examples, with slightly lower error for more capable models.
- Results are averaged over 5 restarts; IRT++ consistently improves or matches its vanilla counterpart across all benchmarks and splits.
- Effective sample size of anchor weights indicates IRT anchors yield more uniform weighting than correctness-based anchors, contributing to robustness.

## General Scales for AI Evaluation (Zhou et al., 2025)

- Validate LLM annotations against human Delphi consensus using rWG (threshold 0.7); GPT-4o achieved ≥0.75 across all 18 dimensions.

## Adding Error Bars to Evals (Miller, 2024)

- Compute standard errors using the Central Limit Theorem. For fractional scores (e.g., F1), use the general CLT formula rather than the Bernoulli formula, which can be overly conservative.
- Use clustered standard errors when questions are drawn in related groups (e.g., DROP, RACE, MGSM) to account for intra-cluster correlation, as failure to do so makes results appear much more precise than they are.
- Reduce variance by resampling answers per question (until conditional variance is much smaller than question-level variance) or by analyzing next-token probabilities. Do not adjust sampling temperature solely to reduce variance, as this can shift or increase the variance of conditional means.

## Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

- Bootstrap intervals are not a safe fallback for small N; they also under-cover.
- Coverage—the proportion of intervals containing the true parameter—is the key diagnostic for whether error bars are reliable.
