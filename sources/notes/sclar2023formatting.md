# Prompt Format Sensitivity (Sclar et al., 2024)

**What kind of evidence:** Empirical study and methods paper.

**Key claims:**
- LLMs are highly sensitive to meaning-preserving prompt formatting changes, with performance spreads up to 76 accuracy points (LLaMA-2-13B) and a median spread of 7.5 points across 50+ tasks.
- Sensitivity persists despite increasing model size, few-shot examples, or instruction tuning; e.g., 1-shot LLaMA-2-70B shows a median spread of 17.1 accuracy points.
- Format performance only weakly correlates between models: comparisons between models can reverse based on format choice, with both directions sometimes statistically significant.
- The prompt format accuracy space is highly non-monotonic, making local search ineffective; Thompson sampling (used in FORMATSPREAD) is proposed as an efficient search method.
- Prompt formats are identifiable from internal prompt embeddings (≥98% accuracy with 100 principal components), and embedding separability correlates with performance spread.

**What the advisor should take from it:**

*reliability:*
- Treat prompt formatting as a major source of measurement error; a single format yields a point estimate, not the full distribution.
- Use FORMATSPREAD (or similar bandit-based sampling) to estimate the performance interval across plausible formats under a fixed computational budget.
- Report performance spread (min-max across formats) rather than relying on a single format's score.

*validity:*
- A fixed, arbitrary prompt format is a confounding factor when comparing models; differences attributed to architecture or training data may actually be format sensitivity.
- When comparing Model A vs Model B, ensure the comparison holds across multiple plausible formats, not just the one where A happened to perform best.

*elicitation:*
- Define a grammar of plausible, semantically equivalent formats (varying separators, spacing, casing, enumerations) to systematically explore elicitation variations.
- Do not assume minor formatting tweaks are neutral; single atomic changes can yield >10 accuracy point differences.

*generalization:*
- Claims about a model's general capability on a task are suspect if based on a single format, since a non-adversarial user might encounter a much lower performance format.
- Format robustness does not transfer: a format that is good for one model may be bad for another.

*scoring:*
- The choice of metric affects the observed spread; exact prefix matching tends to show higher spreads than probability ranking and is linked to degeneration (failing to produce any valid option).

**Caveats:**
- The grammar is manually constructed and primarily evaluated on classification and multiple-choice tasks; longer or more open-ended generation may behave differently.
- Semantic equivalence is defined by grammar rules; some generated formats may be less natural than human-written ones.
- Evaluation is on a subset of Super-NaturalInstructions; broader task coverage may reveal different patterns.

**Category changes:** Added validity, generalization, and scoring; retained reliability and elicitation.