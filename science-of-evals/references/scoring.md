<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# scoring

## GenAI Evaluation as Social Science Measurement (Wallach et al., 2025)

- Define indicators (variables reflecting observable phenomena) and aggregation functions that mirror the relationships specified during systematization before writing annotation guidelines or judge prompts.
- LLM-as-a-judge systems need annotation guidelines derived from the systematized concept, not just high-level instructions with few-shot examples; validity must be interrogated, not assumed.

## Measuring what Matters (Bean et al., 2025)

- Validate automated output parsing or LLM-as-a-judge techniques for accuracy, consistency, and bias.
- Avoid over-reliance on exact matching (used at least partially by 81.3%); use metrics that capture the inherent variability of subjective human ratings.

## Judging LLM-as-a-Judge (Zheng et al., 2023)

- Three judge modes—pairwise comparison, single-answer grading, reference-guided grading—have trade-offs: pairwise is more sensitive but scales quadratically; single-answer is scalable but less discriminative; reference-guided is essential for math/reasoning.
- For multi-turn evaluation, display full conversations in a single judge prompt; splitting turns causes the judge to misreference prior answers.
- Few-shot judge examples raise GPT-4 consistency from 65% to 77.5% but cost 4× more and may introduce new biases.

## Emergent Abilities as Metric Artifacts (Schaeffer et al., 2023)

- Prefer continuous or linear metrics (e.g., Brier Score, Token Edit Distance) over discontinuous or all-or-nothing metrics (Exact String Match, Multiple Choice Grade, subset Accuracy) when tracking capability over model scale; the latter can manufacture sharp transitions from smoothly improving per-token error rates.
- If you must use a nonlinear metric, ensure sufficient test data to estimate small but nonzero performance in weaker models; sparse data rounds low probabilities to zero, creating an illusion of absence.

## Validating LLM Judges Under Rating Indeterminacy (Guerdan et al., 2025)

- Choose agreement metrics based on elicitation format: hard-aggregated categorical metrics (Hit Rate, Cohen's κ) are unreliable under indeterminacy; soft-aggregated distributional metrics partially help; continuous multi-label MSE on response set vectors is most robust.
- When only forced-choice data are available, use distributional KL-D(h‖j) rather than categorical or reverse-direction metrics as a fallback.

## Human Label Variation as Signal, Not Noise (Plank et al., 2022)

- Consider soft-label evaluation metrics: cross entropy, entropy correlation, and KL or Jensen-Shannon divergence to compare model outputs against human label distributions.
- Evaluate against individual annotators, or via data splits by agreement level, annotator clustering, or item difficulty rather than only against a single gold label.
- Aggregation (majority vote, probabilistic methods) discards information by construction; document the choice and its implications.

## Prompt Format Sensitivity (Sclar et al., 2024)

- The choice of metric affects the observed spread; exact prefix matching tends to show higher spreads than probability ranking and is linked to degeneration (failing to produce any valid option).

## Signal and Noise: A Framework for Reducing Uncertainty in LM Evaluation (Heineman et al., 2025)

- For generative tasks (math, code) where small models are near random chance, prefer bits-per-byte over exact-match metrics—it yields dramatically higher SNR and better predictability.
- Metric choice is an intervention: BPB's continuity preserves the relationship between LM loss and downstream performance that discontinuous metrics erode.

## Adding Error Bars to Evals (Miller, 2024)

- For non-chain-of-thought evals (e.g., multiple choice), score by analyzing the next-token probability of the correct answer rather than sampling outputs, which eliminates conditional variance entirely.

## Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

- For confusion-matrix metrics like F1 or MCC, use Bayesian intervals from a Dirichlet-Categorical posterior rather than the delta method.
