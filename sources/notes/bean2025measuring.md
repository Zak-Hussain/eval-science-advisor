# Measuring what Matters (Bean et al., 2025)

**What kind of evidence:** Systematic review of 445 LLM benchmarks from leading ML and NLP conferences.

**Key claims:**
- Construct validity is frequently insufficient; 47.8% of provided phenomenon definitions are contested, and 21.7% lack a definition entirely.
- Data reuse (38.2%) and convenience sampling (12.3% exclusively) are common, risking contamination and non-representative task spaces.
- Only 16.0% of benchmarks use statistical tests or uncertainty estimates to compare model performance.
- Just over half (53.4%) of benchmarks present evidence or justify their construct validity.

**What the advisor should take from it:**
*constructs:*
- Define the target phenomenon precisely and operationally before task design. If definitions are contested, use negative (apophatic) definitions to set boundaries.
- Identify if the phenomenon has sub-components and ensure they are measured separately to improve interpretability.

*validity:*
- Design tasks to measure *only* the target phenomenon; control for confounders like strict output formats or unrelated world knowledge.
- Prepare for contamination by maintaining held-out items, adding canary strings, and testing for pre-exposure in training corpora.
- Justify the chain of decisions from phenomenon to metric and explicitly discuss design trade-offs, such as multiple-choice versus free-text.

*scoring:*
- Validate automated output parsing or LLM-as-a-judge techniques for accuracy, consistency, and bias.
- Avoid over-reliance on exact matching (used at least partially by 81.3%); use metrics that capture the inherent variability of subjective human ratings.

*reliability:*
- Report uncertainty estimates and use robust statistical methods for model comparisons.
- When using human raters, document rater demographics and mitigate potential biases in recruitment and instructions.

*generalization:*
- Ensure task items represent the overall task space via robust sampling (e.g., random or stratified) rather than convenience sampling.
- Explicitly include task items that test known LLM sensitivities, such as input permutations or minor prompt variations.

**Caveats:**
- The review is limited to peer-reviewed conference proceedings, potentially missing impactful industry or domain-specific benchmarks.
- Using GPT-4o mini for initial article screening may have introduced undetected false negatives.
- The large scale of the review limited the number of reviewers per paper, potentially reducing annotation robustness.

**Category changes:** Added reliability and generalization; dropped measurement-models as it is only briefly mentioned.