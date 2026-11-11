<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# measurement-models

## Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

- IRT and latent-variable models are only defensible when item difficulty is tied to independently characterised, externally measurable task features, not inferred from pass rates alone.
- Difficulty parameters that shift when the population of evaluated systems changes cannot represent system-intrinsic dispositions.

## LLM Psychological Profiles are Measurement Artifacts (Meyer et al., 2026)

- Use formal measurement models to separate trait from response bias. The paper models responses by partitioning variance into a trait component (half-difference of forward/reverse means) and a bias component (half-sum).
- Design or evaluate instruments with "response orthogonality": include items where the trait-favored option occupies different positions so trait and bias act in opposite directions.

## tinyBenchmarks: evaluating LLMs with fewer examples (Polo et al., 2024)

- IRT models each example by a difficulty parameter β and a discrimination vector α capturing which latent abilities are needed; example embeddings E_i = (α̂_i, β̂_i) are clustered via K-Means to select representative anchor points.
- The gp-IRT estimator convexly combines the raw weighted subset average with IRT-predicted correctness on unobserved items; the mixing weight λ increases with sample size and decreases with estimated IRT bias, giving a principled bias-variance tradeoff.
- For non-binary scores Y_il ∈ [0,1], binarize via a scenario-specific threshold c chosen so that the mean of binarized scores matches the mean of raw scores on the training set.

## Revealing the structure of language model capabilities (Burnell et al., 2023)

- Use Bayesian or frequentist exploratory factor analysis (EFA) to extract latent capability constructs from diverse benchmark item responses, mapping specific tasks to broader abilities.
- Use the Hull method or Bayesian posterior distributions to determine the optimal number of factors for a benchmark dataset, balancing fit and simplicity.

## General Scales for AI Evaluation (Zhou et al., 2025)

- Use "dominant slice" binning: for a dimension at level l, keep only instances where no other dimension exceeds l, enabling unidimensional curves without requiring pure items.
- Estimate ability as the area under the logistic curve fitted to per-level success rates; this equals the demand level at 0.5 success probability and is non-populational.

## Observational Scaling Laws (Ruan et al., 2024)

- PCA on a benchmark-by-model matrix extracts latent capability measures that are more robust predictors than raw compute or model size, because they are comparable across heterogeneous model families.
- A logistic link maps the linear PC combination to normalized downstream accuracy, with an optional floor parameter h.
