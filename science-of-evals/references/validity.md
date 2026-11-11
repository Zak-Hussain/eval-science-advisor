<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# validity

## GenAI Evaluation as Social Science Measurement (Wallach et al., 2025)

- Use all seven lenses throughout the measurement process—face, content, and consequential validity especially inform conceptual debates; all seven inform operational ones.
- Content validity has two facets: substantive (alignment with specified observable phenomena) and structural (alignment with specified relationships among them).
- Validity is context-dependent; re-interrogate before deploying instruments in new contexts.
- When comparing judge LLM annotations to human annotations, first verify humans align with the systematized concept before treating agreement as evidence of convergent validity.

## Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

- A score has construct validity only if the tasks operationalise contextually relevant variables that are hypothesised to causally structure the disposition—convenience-sampled items do not meet this bar.
- Define the subject of measurement explicitly (base model vs. deployed system with filters and tools); different system boundaries yield different dispositions.

## Defining Model Capabilities (Harding et al., 2024)

- Operationalisation gaps between benchmarks and deployment are unavoidable; benchmarks concretise one construct but cannot define the capability.
- Ecological validity requires similarity between evaluation and deployment environments; a construct valid for one evaluation may be invalid for another.
- Non-coincidence is a core validity threat: high scores may reflect memorisation or heuristics rather than the target capability. The perturbation test provides a concrete check.

## The “Everything in the Whole Wide World” Benchmark (Raji et al., 2021)

- Treat construct validity as a design task: ask whether the data, metric, and methodology actually represent the claimed capability, not just whether they produce reproducible scores.
- Scrutinize the gap between benchmark scores and real-world deployment claims; SOTA on a general benchmark does not support claims about deployment readiness or AGI progress.
- Use disaggregated analysis to check whether aggregate scores hide failures on specific subgroups—especially when benchmarks justify commercial deployment.
- Document the subjective, culturally-situated limitations of the dataset rather than presenting it as neutral.

## Measurement to Meaning: A Validity-Centered Framework for AI Evaluation (Salaudeen et al., 2025)

- Use the three-question decision process: (1) Is the claim's object a criterion or construct? (2) Does the measurement match the claim's object? (3) Is a mediating construct required? The answers determine which forms of validity need evidence.
- Always establish content and external validity; add criterion validity when the measured object differs from the claimed criterion; add construct validity when a construct is involved.
- Frame validity as iterative, not a checklist—valid claims can become invalid as contexts or use cases change.

## Measuring what Matters (Bean et al., 2025)

- Design tasks to measure *only* the target phenomenon; control for confounders like strict output formats or unrelated world knowledge.
- Prepare for contamination by maintaining held-out items, adding canary strings, and testing for pre-exposure in training corpora.
- Justify the chain of decisions from phenomenon to metric and explicitly discuss design trade-offs, such as multiple-choice versus free-text.

## Benchmark Data Contamination of Large Language Models: A Survey (Xu et al., 2024)

- BDC is a core threat to validity arguments: scores may reflect memorization rather than capability, affecting all four automatic-evaluation metric families (accuracy, calibration, fairness, robustness).
- N-gram overlap detection (13-gram for GPT-3, 50-character for GPT-4) has high false-negative rates; paraphrased or semantically equivalent content easily bypasses string-matching filters.
- Chronological analysis—testing on data released after training cutoffs—provides evidence of contamination when performance drops sharply on post-cutoff items.

## Password-locked models for stress-testing capability elicitation (Greenblatt et al., 2024)

- Prompting-only evaluations may underestimate capabilities that fine-tuning would reveal; use fine-tuning-based elicitation as a complementary validity check.
- Weak-to-strong generalization can cause SFT on mediocre demonstrations to exceed the demonstrator's own performance, complicating inferences about minimum demonstration quality.

## Evaluation awareness in frontier LLMs (Needham et al., 2025)

- Evaluation awareness should be treated as a standing threat to validity arguments connecting eval scores to deployment claims. If a model infers it is being tested for a specific property, its scores on that property may not reflect deployment behavior.
- Scheming risks (sandbagging on capability evals, alignment faking on propensity evals) are hypothetical but growing; the paper recommends tracking evaluation awareness alongside safety evaluations.

## Judging LLM-as-a-Judge (Zheng et al., 2023)

- Agreement with human gold standard is the core validity argument; GPT-4's 85% non-tie agreement on MT-bench and 87% on Chatbot Arena support its use as a proxy.
- GPT-4 single-answer grading agrees ~95% with GPT-4 pairwise, indicating a stable internal rubric that generalizes across scoring modes.

## Emergent Abilities as Metric Artifacts (Schaeffer et al., 2023)

- A claim that a capability is "emergent" is not supported unless the result persists across multiple reasonable metrics, not just the one that produces a sharp transition.
- Control for multiple comparisons: BIG-Bench alone contains ~10⁶ task-metric-model triplets, making spurious emergence likely by chance.

## Validating LLM Judges Under Rating Indeterminacy (Guerdan et al., 2025)

- Forced-choice elicitation introduces a threat to meta-evaluation validity: it conflates genuine disagreement about what is "correct" with arbitrary resolution of indeterminacy, biasing judge selection.
- When validating an LLM judge, prefer response set elicitation (raters select all plausible options) and multi-label agreement metrics; if only forced-choice data exist, collect a small auxiliary corpus of paired forced-choice/response set ratings (≈100 items) to estimate the translation matrix and recover an approximate multi-label metric.

## Human Label Variation as Signal, Not Noise (Plank et al., 2022)

- Evaluating against a single gold label threatens validity when HLV is present; accuracy can be high while masking how unreasonable or untrustworthy a model's predictions actually are.
- HCI audits show that standard metrics are misaligned with real-world performance, indicating a systematic in-vitro/in-vivo validity gap.

## Prompt Format Sensitivity (Sclar et al., 2024)

- A fixed, arbitrary prompt format is a confounding factor when comparing models; differences attributed to architecture or training data may actually be format sensitivity.
- When comparing Model A vs Model B, ensure the comparison holds across multiple plausible formats, not just the one where A happened to perform best.

## Label Errors in ML Benchmark Test Sets (Northcutt et al., 2021)

- Standard test accuracy on noisy labels can be a misleading basis for model selection: models scoring higher on original labels may perform worse on corrected labels.
- The distinction between "original accuracy" and "corrected accuracy" is central—practitioners measure the former but care about the latter.
- Validity of benchmark conclusions depends on test-label quality, not merely train/test distribution match.

## LLM Psychological Profiles are Measurement Artifacts (Meyer et al., 2026)

- High internal consistency (e.g., Cronbach’s alpha) does not establish that a construct is being measured; response bias can inflate apparent consistency just as a shared construct would.
- Profiles derived from non-orthogonal instruments are confounded and cannot be interpreted as evidence of genuine traits. Existing LLM psychological profiles need re-evaluation against response orthogonality.

## tinyBenchmarks: evaluating LLMs with fewer examples (Polo et al., 2024)

- Key threats include severe distribution shifts from architecture or pre-training data changes, model misspecification of the IRT model, and extrapolation errors from rapid capability increases—any of which can break the assumption that anchor correctness patterns transfer to new models.

## General Scales for AI Evaluation (Zhou et al., 2025)

- Inspect per-benchmark demand histograms to verify each covers the full level range for target dimensions (sensitivity) and avoids loading on irrelevant ones (specificity).
- Use atypicality annotations to flag contamination where high performance coincides with low cognitive demand.

## Observational Scaling Laws (Ruan et al., 2024)

- Claims of emergence are sensitive to the number of data points and metric choice; high-resolution scaling analyses reveal smooth transitions.
- Single benchmarks have limited dynamic range (saturation or chance-level), threatening construct validity at the extremes.

## Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

- Significance claims built on under-covering intervals are invalid; using methods that achieve nominal coverage is necessary for trustworthy model comparisons.
- Large benchmarks broken into sub-tasks cannot invoke total N for CLT justification, since sub-task data is not IID.
