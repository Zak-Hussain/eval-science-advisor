# Emergent Abilities as Metric Artifacts (Schaeffer et al., 2023)

**What kind of evidence:** Empirical study with mathematical modelling and meta-analysis.

**Key claims:**
- Emergent abilities—sharp, unpredictable performance jumps with scale—arise primarily from the researcher's choice of nonlinear or discontinuous metrics, not from fundamental changes in model behaviour.
- Over 92% of claimed emergent abilities on BIG-Bench appear under just two metrics: Multiple Choice Grade (discontinuous) and Exact String Match (nonlinear).
- Switching from nonlinear Accuracy to linear Token Edit Distance on GPT-3 arithmetic tasks makes emergent abilities vanish, revealing smooth, predictable improvement.
- Increasing test dataset size (measurement resolution) shows smaller models have above-chance accuracy even under Accuracy, hidden when data is sparse.
- Never-before-seen "emergent abilities" can be induced in vision tasks (autoencoders on CIFAR100, transformers on Omniglot, LeNet on MNIST) purely by choosing discontinuous or nonlinear scoring rules.

**What the advisor should take from it:**

*scoring:*
- Prefer continuous or linear metrics (e.g., Brier Score, Token Edit Distance) over discontinuous or all-or-nothing metrics (Exact String Match, Multiple Choice Grade, subset Accuracy) when tracking capability over model scale; the latter can manufacture sharp transitions from smoothly improving per-token error rates.
- If you must use a nonlinear metric, ensure sufficient test data to estimate small but nonzero performance in weaker models; sparse data rounds low probabilities to zero, creating an illusion of absence.

*validity:*
- A claim that a capability is "emergent" is not supported unless the result persists across multiple reasonable metrics, not just the one that produces a sharp transition.
- Control for multiple comparisons: BIG-Bench alone contains ~10⁶ task-metric-model triplets, making spurious emergence likely by chance.

*generalization:*
- Do not extrapolate from a single metric's sharp transition to claims about fundamental capability thresholds or future model behaviour; check whether the underlying per-token loss follows a smooth scaling law that the metric is merely reformatting.

*constructs:*
- "Emergent ability" as currently operationalised (sharpness + unpredictability under a chosen metric) may not correspond to a real capability discontinuity; the construct risks being an artifact of measurement choice rather than a property of the model family.

**Caveats:**
- The per-token error independence assumption is acknowledged as empirically false; the mathematical model is illustrative, not exact.
- Direct experiments use only four GPT-3/InstructGPT model sizes; other model families are analysed indirectly via published results.
- The paper does not prove emergent abilities are impossible—only that existing evidence is insufficient to establish them.

**Category changes:** Added validity and constructs: the paper centrally addresses whether evidence supports emergent-ability claims and what the construct really measures.