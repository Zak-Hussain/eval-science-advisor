# Signal and Noise for Reducing Evaluation Uncertainty (Heineman et al., 2025)

**What kind of evidence:** Empirical study with methods interventions, using 465 models across 30 benchmarks (60M–32B parameters).

**Key claims:**
- Signal-to-noise ratio (SNR) — dispersion of model scores divided by checkpoint-to-checkpoint score variability — correlates strongly with decision accuracy (R² = 0.626), whereas signal or noise alone do not.
- Noise (relative std. dev. of final n checkpoints) correlates with scaling-law prediction error (R² = 0.426); noisier targets set a lower bound on achievable prediction error.
- Checkpoint-to-checkpoint noise is a cheap proxy for seed and data-order noise (R² ≥ 0.82 with both), requiring no extra training runs.
- Three interventions improve reliability: filtering low-SNR subtasks (e.g., 16 of 57 MMLU subtasks match or beat full-set SNR), averaging final k checkpoints (decision accuracy +2.4% on 30-task average), and switching from accuracy/exact-match to bits-per-byte (BPB), which raises SNR and decision accuracy for ~90% of benchmarks.
- Larger benchmark size shows diminishing returns; a 1K-instance subset can outperform a 30K benchmark on SNR when the latter is noisy.

**What the advisor should take from it:**

*reliability:*
- Compute checkpoint-to-checkpoint noise as relative std. dev. over the final ~5–20 checkpoints; it captures most seed/data-order variability at negligible cost.
- Average scores over the final k checkpoints (or use EMA) before comparing models — this consistently reduces noise-driven ranking flips.
- Prefer BPB over discontinuous metrics (accuracy, pass@1) for small models or hard tasks where scores cluster near chance.

*measurement-models:*
- SNR (relative dispersion / relative std. dev.) is a single scalar that predicts whether a benchmark will support rank-preserving scaling extrapolation; use it to triage which benchmarks to include in development suites.
- Subtask-level SNR can identify low-quality items: half of MMLU Redux's high-error subtasks fall in the bottom 20 by SNR.

*generalization:*
- Benchmarks with high SNR at small scale yield higher decision accuracy and lower scaling-law error at large scale; SNR measured at 1B predicts utility for 13B+ decisions.
- When multi-task averages have low SNR, individual high-SNR tasks (e.g., TriviaQA vs. OLMES Gen average) may generalize better.
- SNR also flags benchmark saturation: tasks like ARC Easy drop from SNR 7.9 (1.5B) to 5.1 (32B).

**Caveats:**
- All experiments use base models trained ≤32B; findings may not transfer to instruction-tuned or much larger models.
- Noise is defined only as training checkpoint variability, not evaluation-config or prompt-format noise.
- Decision accuracy and scaling-law error are the sole generalization proxies tested; other extrapolation settings (e.g., emergence) are untested.

**Other categories:** none.