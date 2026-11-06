# tinyBenchmarks (Maia Polo et al., 2024)

**What kind of evidence:** Methods paper with empirical validation across four major LLM benchmarks.

**Key claims:**
- 100 curated examples per benchmark scenario estimate full-benchmark performance within ~2% average error across MMLU, Open LLM Leaderboard, HELM, and AlpacaEval 2.0.
- IRT-based anchor selection (clustering on IRT item representations) is more robust to temporal and specialized-model distribution shift than clustering on raw correctness patterns.
- gp-IRT, a convex combination of raw weighted anchor scores and IRT-predicted scores, consistently matches or improves its vanilla counterpart with only seconds of added compute.
- Stratified random sampling needs 200–400 examples per scenario to match IRT++ at 100.
- The approach extends to non-binary scores (e.g., AlpacaEval win rates) via a binarization threshold.

**What the advisor should take from it:**

*measurement-models:*
- Model LLMs as examinees and items as test questions via two-parameter multidimensional IRT: item parameters capture difficulty/discrimination and latent model-ability vectors capture capabilities.
- Use IRT item representations as low-dimensional embeddings for clustering to select representative anchor points, avoiding the curse of dimensionality from raw correctness vectors.
- p-IRT predicts unobserved item correctness via fitted IRT probabilities; gp-IRT blends this with observed anchor scores, with the blending weight governed by estimated IRT bias and sampling variance.
- Fit IRT via variational inference and select latent dimension (2–15) by validation prediction power.

*reliability:*
- Estimation reliability holds under temporal splits (train on older models, test on newer ones) and specialized-model splits, whereas correctness-pattern clustering degrades under such shifts.
- IRT++ keeps per-model estimation error ≤4% for almost all tested models, with slightly lower error for more capable models.
- Periodically update anchor sets and IRT parameters with newer model data to maintain reliability as capabilities evolve.

**Caveats:**
- Requires a pool of pre-evaluated LLMs to fit IRT and identify anchors; this may not exist for new bespoke benchmarks.
- Severe distribution shifts—models failing easy items while passing hard ones—can break IRT assumptions.
- The adaptive-testing variant improves estimates but takes over five minutes, limiting practical appeal.

**Other categories:**
- *generalization:* Demonstrates robust extrapolation to future and specialized models; estimates remain consistent over 3–6 month horizons.
- *constructs:* Sub-scenario weighting via balance weights ensures each domain contributes equally, preventing over-representation of high-volume sub-domains.