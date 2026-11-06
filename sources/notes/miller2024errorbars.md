# Adding Error Bars to Evals (Miller et al., 2024)

**What kind of evidence:** Methods paper with statistical theory and worked examples.

**Key claims:**
- Evals should be treated as experiments drawing from a hypothetical super-population of questions; standard errors are computable via the Central Limit Theorem (SE = sqrt(Var(s)/n)) without bootstrapping.
- Clustered standard errors for evals with grouped questions (e.g., shared passages, translated items) can be over 3× larger than naive standard errors; failing to cluster yields falsely precise estimates.
- Paired differences between models on the same questions reduce variance proportional to score correlation; a correlation of 0.5 cuts variance by roughly one third.
- Resampling answers K times and analyzing next-token probabilities both reduce conditional variance; resampling yields diminishing returns once E[σ²]/K ≪ Var(x).
- Adjusting sampling temperature to reduce variance is counterproductive—it can inject bias and increase variance of conditional means.
- Power analysis formulas relate sample size to minimum detectable effect; worked examples suggest new evals need ≥1,000 questions for good signaling.

**What the advisor should take from it:**

*reliability:*
- Report standard errors alongside mean scores; use CLT-based SEs, not bootstrapping, for standard cases. For fractional scores (e.g., F1), use CLT-based SE, not the Bernoulli formula, which is conservative.
- When questions share a passage or translation, compute clustered standard errors; report cluster counts alongside question counts.
- Reduce score variance by resampling answers or using next-token probabilities; do not adjust sampling temperature for this purpose.
- When comparing two models, compute paired differences on the same questions rather than comparing population-level summary statistics.

*generalization:*
- Frame eval questions as draws from a super-population to justify inference about underlying capability beyond specific items.
- Use the sample-size/power formula (Equation 9) to determine whether an eval or subsample can detect a target effect size δ, given α, β, and variance estimates from prior data.
- When fixed, compute the Minimum Detectable Effect to judge whether the eval is worth running.

**Caveats:**
- The super-population assumption is a modeling fiction; real eval questions are curated, not randomly drawn.
- Power analysis requires prior data to estimate variance components (ω², σ²_A, σ²_B); these may not be available for novel constructs.
- Worked examples use simplified assumptions (e.g., uniform difficulty distributions).

**Other categories:**
- *scoring:* Recommends next-token probabilities over sampled outputs for variance reduction; notes Bernoulli SE is inappropriate for fractional scores like F1.
- *elicitation:* Warns that changing sampling temperature alters model behavior and should not be used as a variance-reduction tool.