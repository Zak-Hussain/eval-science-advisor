# Observational Scaling Laws (Ruan et al., 2024)

**What kind of evidence:** Empirical methods paper proposing and validating a scaling-law framework across ~100 publicly available LMs.

**Key claims:**
- Standard LM benchmark performance across 21 model families is low-dimensional: top 3 principal components (PCs) explain ~97% of variance, with PC-1 alone explaining ~80%.
- These PCs correlate log-linearly with training FLOPs within each model family (R² > 0.9), enabling a shared capability scale across heterogeneous families.
- Capabilities labelled "emergent" (e.g., 3-digit subtraction, word unscramble) follow smooth sigmoidal curves and are predictable from small models using PCs, far better than using raw FLOPs or model size.
- Agentic performance (AgentBench, AgentBoard) of GPT-4/Claude-2 is accurately predicted from weaker models' PC measures; programming capability (HumanEval) is a key driver.
- Post-training interventions (CoT, Self-Consistency) show predictable, differential scaling trends; CoT scales more aggressively than SC.
- A V-optimality criterion selects 10–20 representative models that reproduce full-set prediction accuracy.

**What the advisor should take from it:**

*measurement-models:*
- PCA on a benchmark–model matrix extracts interpretable latent capability dimensions (PC-1: general; PC-2: reasoning; PC-3: programming), analogous to factor scores in psychometrics.
- The framework formalises a two-stage model: benchmarks → PC capability scores → downstream performance via sigmoidal regression, enabling cross-family comparison without compute access.
- f-equivalent FLOPs transform maps any model onto a reference family's compute scale, making heterogeneous models comparable on one axis.

*generalization:*
- Observational scaling laws let evaluators extrapolate held-out strong models' performance from weaker ones with low MSE, including preregistered forecasts validated on post-release models (Llama-3.1-405B).
- Using 77+ models provides resolution sufficient to reveal that "discontinuous emergence" is often a sigmoid viewed at low resolution.
- Recommended model subsets (Table 1) give practitioners a concrete starting kit for cost-efficient scaling analyses.

**Caveats:**
- Does not directly address pretraining optimisation; suited to post-training and downstream capability forecasting.
- Assumes no benchmark contamination and uniform efficiency within a family; both can bias PC extraction and predictions.
- Validated mainly on few-shot/CoT-style evaluation; extension to fine-tuning or heavy inference-time compute is untested.

**Other categories:** *constructs:* PCs operationalise general, reasoning, and programming as latent capability constructs. *scoring:* accuracy metrics normalised to [0,1] feed sigmoidal regression; floor-performance parameter h accounts for metric ceilings.