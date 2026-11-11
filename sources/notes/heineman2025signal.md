# Signal and Noise: A Framework for Reducing Uncertainty in LM Evaluation (Heineman et al., 2025)

**What kind of evidence:** Empirical study with 465 models (60M–32B) across 30 benchmarks, plus 20 newly trained seed/data-order variants.

**Key claims:**
- Signal-to-noise ratio (SNR), defined as relative dispersion across models divided by relative std. dev. across final checkpoints, correlates strongly with decision accuracy (R=0.791, R²=0.626).
- Checkpoint-to-checkpoint noise correlates highly with seed-initialization noise (R=0.90) and data-order noise (R=0.93), making it a cheap proxy for expensive multi-run noise estimates.
- Noise around the scaling-law target correlates with prediction error (R=0.653), suggesting it acts as a floor on achievable prediction accuracy.
- Filtering subtasks by SNR can improve both decision accuracy (+2.6% for MMLU subset) and scaling-law noise, even with fewer than half the instances.
- Switching from discontinuous metrics (accuracy, exact match, pass@1) to bits-per-byte improves SNR for 90% of benchmarks, reduces scaling-law error for 73%, and improves decision accuracy across most tasks—especially generative math/code at small scales.

**What the advisor should take from it:**

*reliability:*
- Estimate noise cheaply: use the relative std. dev. of the final 5–30 checkpoints of a single training run. This captures most of the variability from seeds and data order without retraining.
- Averaging scores across the final k checkpoints (exponential moving average) consistently reduces noise and improves rank-stability during training and at final evaluation.
- Low intrinsic dataset noise does not guarantee low modeling noise: e.g., BoolQ has low statistical variability but high checkpoint-to-checkpoint noise.

*generalization:*
- Before using small-scale experiments to predict large-scale behavior, compute SNR at the small scale; benchmarks with low SNR are poor predictors of both model rankings and scaling-law targets.
- Multi-task averages are not always better than individual tasks for scaling-law prediction; some individual tasks (e.g., TriviaQA) have lower noise and prediction error than their group averages.
- SNR can diagnose benchmark saturation: tasks like ARC Easy show high SNR at 1.5B but drop at 32B.

*scoring:*
- For generative tasks (math, code) where small models are near random chance, prefer bits-per-byte over exact-match metrics—it yields dramatically higher SNR and better predictability.
- Metric choice is an intervention: BPB's continuity preserves the relationship between LM loss and downstream performance that discontinuous metrics erode.

**Caveats:**
- SNR–decision-accuracy correlation is established only for pretraining-data decisions (DataDecide models); applicability to architecture or post-training decisions is untested.
- Noise is defined only over training-checkpoint variability; other sources (prompt format, evaluation harness) are acknowledged but not measured.
- The scaling-law error analysis uses a single 13B target model per task, limiting statistical strength.

**Category changes:** Added scoring: the bits-per-byte metric intervention is substantial. Kept reliability and generalization from suggestions; dropped measurement-models (only tangentially mentioned).