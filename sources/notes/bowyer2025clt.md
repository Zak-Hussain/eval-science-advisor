# Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

**What kind of evidence:** Position paper with extensive empirical simulations using known ground-truth parameters.

**Key claims:**
- CLT-based confidence intervals systematically under-cover for evals with fewer than a few hundred examples; at N=100, 95% CLT intervals achieved only ~92.5% coverage.
- CLT intervals can collapse to zero width (all questions right/wrong) or extend beyond [0,1], producing nonsensical error bars.
- Bootstrap intervals also under-cover in small-data settings.
- Bayesian Beta-Bernoulli credible intervals and Wilson score intervals achieve good coverage even for small N in the IID single-model setting.
- For clustered data (e.g., multiple questions per passage), only Bayesian methods modelling the clustering achieve correct coverage; no simple frequentist alternative exists.
- For non-linear metrics (F1, odds ratio), the CLT/delta method performs poorly; Bayesian methods via Dirichlet-Categorical or Beta posteriors work well.
- Bayesian methods enable direct probabilistic model comparison (P(θA > θB | data)), which frequentist methods cannot provide.

**What the advisor should take from it:**

*generalization:*
- For evals with fewer than a few hundred items, do not report CLT-based error bars; they typically overstate confidence by producing intervals that are too narrow.
- For single-model IID accuracy, use Bayesian Beta-Bernoulli credible intervals or Wilson score intervals (both trivial to implement via SciPy).
- For model comparison, sample from Beta posteriors to get credible intervals on the difference or odds ratio, and to compute P(model A > model B).
- For clustered evals, use a hierarchical Bayesian model (Beta-Binomial with dispersion parameter) fitted via importance sampling; code is provided in the paper's library.

*reliability:*
- Bootstrap intervals are not a safe fallback for small N; they also under-cover.
- Coverage—the proportion of intervals containing the true parameter—is the key diagnostic for whether error bars are reliable.

*validity:*
- Significance claims built on under-covering intervals are invalid; using methods that achieve nominal coverage is necessary for trustworthy model comparisons.
- Large benchmarks broken into sub-tasks cannot invoke total N for CLT justification, since sub-task data is not IID.

*scoring:*
- For confusion-matrix metrics like F1 or MCC, use Bayesian intervals from a Dirichlet-Categorical posterior rather than the delta method.

**Caveats:**
- Coverage experiments use simulated data with known ground truth, not real LLM outputs (real examples are illustrative only).
- Uniform/non-informative priors are used throughout; informative priors could tighten intervals but risk bias if misspecified.
- The "few hundred" threshold is deliberately not a hard cutoff—context-dependent and difficult to determine a priori.

**Category changes:** Added validity and scoring to the suggested generalization and reliability; all four are substantially informed.