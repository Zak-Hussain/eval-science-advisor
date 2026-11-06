# Revealing the structure of LLM capabilities (Burnell et al., 2023)

**What kind of evidence:** Empirical study applying frequentist and Bayesian factor analysis to HELM benchmark data from 29 LLMs across 27 cognitive tasks.

**Key claims:**
- LLM capabilities are not monolithic; three well-delineated factors—reasoning, comprehension, and core language modeling—explain 82% of variance in model performance (Table 2).
- The three factors are moderately inter-correlated (r = 0.22–0.51) but dissociable, mirroring the structure found in human cognitive abilities.
- Model size correlates positively with all three factors but most strongly with comprehension (r = 0.70); instruction tuning correlates positively with reasoning (r = 0.44) and negatively with language modeling (r = −0.50).
- Frequentist EFA (with Hull method for factor selection) and Bayesian factor analysis both converge on a three-factor solution.
- Benchmarks could be streamlined by selecting tasks that tap each broad ability rather than testing dozens of surface-format variants.

**What the advisor should take from it:**

*constructs:*
- Three broad, inter-correlated but separable abilities—reasoning, comprehension, and language modeling—best describe what current benchmarks measure.
- Tasks with different surface formats (QA, summarization, sentiment analysis) can share a single underlying ability; similarly, math and inductive reasoning tasks may share one reasoning factor.
- The reasoning factor appears to primarily capture inductive/fluid reasoning; deductive tasks (bAbI, Dyck) loaded weakly on it, and commonsense reasoning (HellaSwag) loaded on comprehension. The authors flag this as needing further investigation.

*measurement-models:*
- Factor analysis across a population of LLMs can extract latent capability factors from task-level performance data, providing a data-driven basis for understanding capability structure.
- The Hull method balances fit against complexity for factor-number selection; Bayesian EFA (Conti et al.) offers robustness to small samples and assigns each task to one factor.
- Per-model factor scores enable direct comparison of models on each latent ability.

*generalization:*
- If a small set of broad abilities explains most variance, one can predict performance on untested tasks given knowledge of their required abilities and streamline benchmarks accordingly.
- The factor structure is contingent on included tasks; abilities not represented in HELM (e.g., creative writing) would not appear.

*validity:*
- Factor interpretation relied on expert task annotation and is inherently subjective; some tasks did not load as expected, indicating a need for tasks designed around cognitive demands rather than surface format.

**Caveats:**
- Only 29 models; frequentist fit statistics were poor (CFI = 0.70, RMSEA = 0.26), though Bayesian analysis corroborated the structure.
- Task annotations were done by a single expert; many HELM tasks were designed by format, not cognitive demand.
- The factor structure depends on the included tasks and may omit important abilities.

**Other categories:** generalization (streamlining benchmarks; predicting untested task performance from latent ability profiles).