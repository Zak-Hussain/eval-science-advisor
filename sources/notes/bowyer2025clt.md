# Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints (Bowyer et al., 2025)

**What kind of evidence:** Position paper with extensive simulation experiments comparing interval methods across small-N eval scenarios.

**Key claims:**
- CLT-based confidence intervals systematically under-cover in small-data LLM evals (e.g., at N=100, 95% CLT intervals achieve only ~92.5% coverage), producing error bars that are too narrow.
- CLT intervals can collapse to zero width (when a model gets all items right or wrong) or extend beyond [0,1], both invalid for proportions.
- Bootstrap intervals also under-cover in small-N settings.
- Bayesian credible intervals (Beta-Bernoulli conjugate, or importance sampling for clustered/paired settings) and the frequentist Wilson score interval achieve near-nominal coverage even at N=3.
- No simple frequentist alternative exists for clustered or paired data structures; Bayesian methods via importance sampling fill this gap.
- For non-linear metrics like F1-scores or odds ratios, the CLT is not directly applicable; Bayesian methods using Dirichlet-Multinomial posteriors handle these naturally.

**What the advisor should take from it:**

*generalization:*
- When extrapolating from a small benchmark to claims about model capability, use Bayesian or Wilson intervals—not CLT intervals—to avoid overstating precision.
- For clustered benchmarks (e.g., multiple questions per passage), only a Bayesian clustered model (Beta-Binomial likelihood) gives valid coverage; neither plain nor clustered-CLT adjustments suffice at small N.
- Bayesian posteriors allow direct probabilistic statements (e.g., P(model A > model B)), which frequentist intervals cannot provide.

*reliability:*
- Error bars on LLM evals are a reliability requirement; CLT-based bars are unreliable below a few hundred datapoints and should be replaced.
- For paired comparisons (same questions across models), paired Bayesian inference via importance sampling accounts for inter-model correlation and yields narrower, better-calibrated intervals than unpaired approaches.
- Computational cost of Bayesian methods is negligible (under ~200ms) relative to eval-running cost.

*Caveats:*
- Simulations use uniform Beta(1,1) priors; under prior mismatch (e.g., true θ near 0.95), Bayesian intervals can over-cover for very small N but recover quickly as N grows.
- The threshold "fewer than a few hundred" is deliberately vague; no hard N* exists, and adequacy depends on data structure and true parameters.
- Experiments are simulations, not real eval data; real-world coverage may differ, though real-data examples (LangChain, AIME) show the same qualitative failure modes.

**Other categories:** *scoring* — the paper provides concrete guidance for non-linear metrics (F1, odds ratios) where CLT fails entirely, recommending Dirichlet-Multinomial Bayesian posteriors.