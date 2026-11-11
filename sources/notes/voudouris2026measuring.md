# Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

**What kind of evidence:** Position paper building on philosophy of science, measurement theory, and cognitive science.

**Key claims:**
- Capabilities and propensities are dispositional properties: stable intrinsic features defined by counterfactual relationships between contextual conditions and behavioural outputs.
- Capabilities co-vary with task-demand components of context; propensities co-vary with incentive-relevant components. Both are formally captured as p(v|π,θ).
- Benchmarking conflates sampled performance with underlying disposition because it does not identify which contextual properties causally drive behaviour.
- Data-driven IRT infers difficulty and ability solely from performance covariance, making latent variables circular (difficulty is whatever systems fail) and population-dependent.
- A systematic review of 445 LLM benchmarks found ~50% target contested or undefined constructs, >25% use convenience sampling, and <1 in 6 employ statistical testing.
- Disposition-respecting measurement requires four steps: define the subject, hypothesise causal contextual variables, operationalise them independently of performance, and empirically map how p(v|π,θ) changes as context varies.

**What the advisor should take from it:**

*constructs:*
- Distinguish capabilities (co-vary with demands/difficulty) from propensities (co-vary with incentives). Both are dispositions, not performances.
- Performance on a dataset is a manifestation of a disposition in a narrow context, not the disposition itself.

*validity:*
- A score has construct validity only if the tasks operationalise contextually relevant variables that are hypothesised to causally structure the disposition—convenience-sampled items do not meet this bar.
- Define the subject of measurement explicitly (base model vs. deployed system with filters and tools); different system boundaries yield different dispositions.

*measurement-models:*
- IRT and latent-variable models are only defensible when item difficulty is tied to independently characterised, externally measurable task features, not inferred from pass rates alone.
- Difficulty parameters that shift when the population of evaluated systems changes cannot represent system-intrinsic dispositions.

*generalization:*
- Because dispositions are counterfactual, measurement must support extrapolation beyond tested ranges—both beyond human-level performance and into unsafe domains where direct testing is prohibited.
- Extrapolation is feasible by varying contextual properties across benign tasks that share structural features with dangerous ones, then inferring the response function in unobserved regions.

*elicitation:*
- Red-teaming samples a small, adversarially selected region of contextual space and yields anecdotes of failure, not measurements of inclination; it cannot distinguish contrived provocation from robust counterfactual tendencies.

**Caveats:**
- The paper offers a conceptual scaffold, not a validated methodology; the four-step framework is illustrated with toy examples only.
- Identifying which contextual properties matter for specific dispositions remains an open empirical challenge the authors flag as the central task ahead.

**Category changes:** Added validity and elicitation; the suggested list omitted validity and only mentioned elicitation as a starting category.