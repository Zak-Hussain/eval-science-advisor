# Construct Validity in LLM Benchmarks (Bean et al., 2025)

**What kind of evidence:** Systematic review of 445 LLM benchmarks from six leading ML/NLP conferences (2018–2024), annotated by 29 expert reviewers.

**Key claims:**
- 78.2% of benchmarks define their target phenomenon, but 47.8% of those definitions are contested, lacking consensus.
- Only 16.0% of benchmarks use any statistical tests or uncertainty estimates to compare model results.
- Exact matching is the most common metric (used at least partially by 81.3%, exclusively by 40.7%), despite known limitations.
- Only 53.4% of benchmarks justify construct validity; nearly every reviewed paper has weaknesses in at least one area.
- 12.3% of benchmarks rely exclusively on convenience sampling; 27.0% incorporate it, risking non-representative task items.

**What the advisor should take from it:**

*constructs:*
- Provide a precise, operational definition of the phenomenon before designing tasks; where definitions are contested, use negative/apophatic definitions to set boundaries.
- Identify whether the phenomenon is composite (61.2% are) and measure sub-components separately to improve interpretability.
- Specify the scope covered and explicitly acknowledge excluded aspects.

*validity:*
- Justify the full chain from phenomenon definition → task → metric → claims; compare against similar benchmarks (35.2% do) and human baselines (32.4%).
- Control for confounding subtasks such as format compliance (21.1% impose strict output formats), instruction-following, or world knowledge by baselining these independently.
- Implement contamination checks, maintain held-out items, and investigate pre-exposure in training corpora.
- Conduct error analysis to verify that failure modes correlate with the target construct rather than confounders.

*scoring:*
- Move beyond exact matching where possible; consider soft match, LLM-as-judge, or human ratings with validated rubrics.
- Report uncertainty estimates and statistical tests for all primary scores; justify sample size and statistical power.
- For subjective metrics, capture the distribution of ratings rather than single-point aggregation; consider rater demographics and cultural context.

**Caveats:**
- Review covers only peer-reviewed conference papers, excluding influential industry benchmarks and domain-specific venues.
- LLM-assisted screening (GPT-4o mini) may have introduced undetected false negatives despite 84% F1 validation.
- Inter-rater agreement was moderate (mean BPK 0.524), with interpretive fields like task ecology and sampling method showing lower consistency.

**Other categories:**
- reliability: advocates statistical testing and uncertainty reporting across runs.
- generalization: addresses contamination, ecological validity, and real-world task relevance.
- elicitation: flags format constraints and complex instructions as confounders affecting elicited behaviour.