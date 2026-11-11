# Observational Scaling Laws (Ruan et al., 2024)

**What kind of evidence:** Empirical study with methods paper elements, analyzing ~77 pretrained and ~20 instruction-tuned public models.

**Key claims:**
- Standard LM benchmarks are low-dimensional: top 3 principal components explain ~97% of variance, with interpretable axes (general, reasoning, programming).
- These principal capability (PC) measures scale log-linearly with log-training-FLOPs within each model family (R² > 0.9), serving as a cross-family surrogate for compute.
- "Emergent" capabilities (e.g., 3-digit subtraction, word unscramble) follow smooth sigmoidal curves and are predictable from sub-7B models when using PC measures rather than raw FLOPs.
- Agentic performance (AgentBench, AgentBoard) is predictable from simple benchmark metrics; programming capability (HumanEval) carries the highest fitted weight.
- Post-training gains from CoT and Self-Consistency scale predictably; CoT shows stronger scaling than SC, with higher weights on MMLU and HumanEval.
- As few as 10-20 models selected via V-optimality suffice for accurate scaling predictions.

**What the advisor should take from it:**

*constructs:*
- A small set of latent capability dimensions (general, reasoning, code) underlies most standard benchmarks, suggesting benchmark batteries are not measuring independent constructs.
- PC-1 serves as a broad "general capability" factor with high dynamic range across 5 orders of magnitude, unlike single benchmarks that saturate or stay at chance.

*measurement-models:*
- PCA on a benchmark-by-model matrix extracts latent capability measures that are more robust predictors than raw compute or model size, because they are comparable across heterogeneous model families.
- A logistic link maps the linear PC combination to normalized downstream accuracy, with an optional floor parameter h.

*generalization:*
- Fit scaling laws on weak models (FLOPs ≤ Llama-2-7B) and extrapolate to stronger ones; PC measures yield lower MSE than compute baselines on holdout and preregistered future models (Llama-3.1-405B, Qwen2-72B).
- Sigmoidal curves predict transition points for "emergent" tasks, reframing discontinuity as an artifact of low resolution.

*validity:*
- Claims of emergence are sensitive to the number of data points and metric choice; high-resolution scaling analyses reveal smooth transitions.
- Single benchmarks have limited dynamic range (saturation or chance-level), threatening construct validity at the extremes.

**Caveats:** Observational laws are post-training analysis tools, not pretraining optimizers. Assumes no benchmark contamination and homogeneous compute efficiency within families. Prediction accuracy degrades when extrapolating from very few near-chance data points. The approach is validated only on few-shot and basic prompting setups.

**Category changes:** Added constructs and validity: the paper provides evidence about latent capability structure and threats to emergence claims; the suggested measurement-models and generalization are confirmed.