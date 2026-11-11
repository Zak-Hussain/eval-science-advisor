# Adding Error Bars to Evals (Miller, 2024)

**What kind of evidence:** Methods paper (statistical theory and formulas applied to LLM evals).

**Key claims:**
- Evals should be analyzed as experiments sampling from an unseen super-population, requiring standard errors and confidence intervals rather than just point estimates.
- Naive standard errors underestimate uncertainty when questions are clustered (e.g., shared passages or translations); clustered standard errors can be over 3x larger.
- Paired analysis (computing question-level differences between two models) reduces estimator variance compared to unpaired analysis, leveraging the correlation of question difficulty across models.
- Variance can be reduced by resampling answers or using next-token probabilities instead of sampled outputs for non-chain-of-thought evals.
- Power analysis formulas allow practitioners to calculate required sample sizes or the Minimum Detectable Effect (MDE) between two models.

**What the advisor should take from it:**
*reliability:*
- Compute standard errors using the Central Limit Theorem. For fractional scores (e.g., F1), use the general CLT formula rather than the Bernoulli formula, which can be overly conservative.
- Use clustered standard errors when questions are drawn in related groups (e.g., DROP, RACE, MGSM) to account for intra-cluster correlation, as failure to do so makes results appear much more precise than they are.
- Reduce variance by resampling answers per question (until conditional variance is much smaller than question-level variance) or by analyzing next-token probabilities. Do not adjust sampling temperature solely to reduce variance, as this can shift or increase the variance of conditional means.

*generalization:*
- Conceptualize eval questions as a random sample from a hypothetical super-population to justify generalizing from specific eval items to broader model capabilities.
- Report standard errors alongside mean scores, and use paired question-level differences with confidence intervals when comparing models, as this provides a "free" variance reduction.
- Use the provided power analysis formulas to determine if an eval has enough questions to reliably detect a hypothesized difference between models (Minimum Detectable Effect), preventing wasted effort on underpowered evals.

*scoring:*
- For non-chain-of-thought evals (e.g., multiple choice), score by analyzing the next-token probability of the correct answer rather than sampling outputs, which eliminates conditional variance entirely.

**Caveats:**
- The super-population assumption—that questions are drawn randomly from an infinite pool—may not hold for highly curated or fixed eval datasets.
- Worked examples for variance reduction and power analysis rely on simplified assumptions (e.g., uniformly distributed question difficulty, binary scores) that may not reflect all real-world eval score distributions.
- Applying clustered standard errors and power analysis requires prior data to estimate variance components; without this, calculations are purely theoretical.

**Category changes:**
Added scoring: it introduces next-token probability analysis as a scoring method to reduce variance; dropped elicitation: only mentioned in passing.