# Revealing the structure of language model capabilities (Burnell et al., 2023)

**What kind of evidence:** Empirical study using frequentist and Bayesian factor analysis on 29 LLMs across 27 HELM benchmark tasks.

**Key claims:**
- LLM capabilities are not monolithic; they are better explained by three distinct latent factors: reasoning, comprehension, and core language modeling.
- These three factors explain 82% of the variance in model performance across the benchmark (33%, 31%, and 17% respectively).
- Model size correlates more strongly with comprehension (r=0.70) than with reasoning (r=0.51) or language modeling (r=0.49).
- Instruction tuning improves reasoning (r=0.44) but actively impairs language modeling (r=-0.50), indicating that changes improving one ability may impair others.
- Benchmarks can be streamlined by selecting tasks that tap into each broad ability, allowing prediction of performance on untested tasks.

**What the advisor should take from it:**
*constructs:*
- Evaluate LLMs against three core latent constructs—reasoning, comprehension, and language modeling—rather than treating capability as a single monolithic trait.
- Recognize that task format does not dictate construct: question answering, summarization, and sentiment analysis all loaded onto the same "comprehension" factor.

*measurement-models:*
- Use Bayesian or frequentist exploratory factor analysis (EFA) to extract latent capability constructs from diverse benchmark item responses, mapping specific tasks to broader abilities.
- Use the Hull method or Bayesian posterior distributions to determine the optimal number of factors for a benchmark dataset, balancing fit and simplicity.

*generalization:*
- Use estimates of broad cognitive abilities to predict model performance on untested tasks, provided the cognitive demands of those untested tasks are known.
- Account for how model properties (like scale or instruction tuning) have divergent, non-uniform effects on different capabilities when predicting deployment behavior or scaling laws.

**Caveats:**
- The sample size is small (29 models), resulting in poor frequentist fit statistics (CFI=0.70, RMSEA=0.26); Bayesian methods were used to confirm robustness.
- Factor interpretations are subjective and constrained by the included tasks; HELM tasks were largely designed by format rather than specific cognitive demands.
- The extracted structure may miss other important abilities (e.g., creative writing) not represented in the benchmark.

**Category changes:** Added generalization: the paper explicitly discusses predicting untested task performance and deployment behavior; kept constructs and measurement-models from the suggestion.