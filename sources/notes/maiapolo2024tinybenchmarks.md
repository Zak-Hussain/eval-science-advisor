# tinyBenchmarks: evaluating LLMs with fewer examples (Polo et al., 2024)

**What kind of evidence:** Methods paper with extensive empirical validation across four major benchmarks.

**Key claims:**
- 100 curated examples per scenario reliably estimate full-benchmark performance within ~2% average error across MMLU (14K examples), Open LLM Leaderboard (29K), HELM (10K), and AlpacaEval 2.0 (805).
- IRT-based anchor selection combined with the gp-IRT estimator ("IRT++") consistently matches or beats stratified random sampling and correctness-based clustering, especially under distribution shift.
- Methods remain effective when test models are the most recent releases (temporal shift), with average error staying under 2%.
- Correctness-based clustering degrades sharply on specialized domain LLMs (e.g., code, biology); IRT-based anchors are only slightly affected.
- The approach extends to prompt-template evaluation on ANLI, handling distribution shifts across model sizes and instruction templates.

**What the advisor should take from it:**

*measurement-models:*
- IRT models each example by a difficulty parameter β and a discrimination vector α capturing which latent abilities are needed; example embeddings E_i = (α̂_i, β̂_i) are clustered via K-Means to select representative anchor points.
- The gp-IRT estimator convexly combines the raw weighted subset average with IRT-predicted correctness on unobserved items; the mixing weight λ increases with sample size and decreases with estimated IRT bias, giving a principled bias-variance tradeoff.
- For non-binary scores Y_il ∈ [0,1], binarize via a scenario-specific threshold c chosen so that the mean of binarized scores matches the mean of raw scores on the training set.

*reliability:*
- Estimation error stays within 4% for nearly all individual models on MMLU with 100 examples, with slightly lower error for more capable models.
- Results are averaged over 5 restarts; IRT++ consistently improves or matches its vanilla counterpart across all benchmarks and splits.
- Effective sample size of anchor weights indicates IRT anchors yield more uniform weighting than correctness-based anchors, contributing to robustness.

*generalization:*
- Testing on the most recent 25% of models by release date simulates realistic use; methods remain effective, supporting their use for evaluating future models and monitoring checkpoints during pre-training.
- IRT-based methods generalize to specialized LLMs whose correctness patterns differ from the training set, whereas correctness-based methods do not.
- With a longer time horizon (75% test split, ~3 months future data), IRT++ remains robust, though the authors recommend periodically updating anchor examples and IRT parameters.

*validity:*
- Key threats include severe distribution shifts from architecture or pre-training data changes, model misspecification of the IRT model, and extrapolation errors from rapid capability increases—any of which can break the assumption that anchor correctness patterns transfer to new models.

**Caveats:**
- Requires existing correctness data from many LLMs on the full benchmark to fit IRT and identify anchors; benchmarks without such data cannot use the method.
- Dimensionality of the IRT model is selected from {2, 5, 10, 15} via internal validation; higher dimensions may be needed for benchmarks with more diverse latent abilities.
- Adaptive testing variant improves estimation but takes over 5 minutes per model, limiting practical appeal.

**Category changes:** Added generalization and validity to the suggested measurement-models and reliability; the paper's treatment of temporal/specialized-model transfer and threats from distribution shift substantively informs both.