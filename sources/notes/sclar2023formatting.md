# Prompt Formatting Sensitivity (Sclar et al., 2024)

**What kind of evidence:** Empirical study with a proposed method (FORMAT SPREAD) for measuring performance variance across semantically equivalent prompt formats.

**Key claims:**
- LLMs show extreme sensitivity to meaning-preserving format changes: up to 76 accuracy points for LLaMA-2-13B, median ~7.5 points across 53 tasks and multiple models.
- Sensitivity is not reduced by increasing model size (tested up to 70B), adding few-shot examples (1- vs 5-shot), or instruction tuning (Falcon-7B vs Falcon-7B-Instruct).
- Format performance only weakly correlates across models; a format that is good for one model may be poor for another, undermining single-format model comparisons.
- Individual format features (separators, casing, enumeration style) rarely predict performance independently; the format space is highly non-monotonic, making local search ineffective.
- Format identity is recoverable from prompt embeddings (≥0.98 classification accuracy with 100 PCA components), and embedding separability correlates with performance spread.
- FORMAT SPREAD (Thompson sampling bandit) estimates spread within ~1 accuracy point at 51,200 evaluations vs naive sampling's ~4 points.

**What the advisor should take from it:**

*reliability:*
- Report a performance range across multiple plausible formats, not a single-format point estimate, especially when benchmarking or comparing models.
- FORMAT SPREAD provides an efficient, weight-agnostic tool to estimate this spread under a computational budget; Thompson sampling outperforms UCB and naive sampling.
- Sensitivity persists across models and settings, so single-format results risk overstating or understating true capability.

*elcitation:*
- Prompt formatting is a first-class design choice on par with example selection and wording; it should be treated as a source of spurious variance.
- Avoid assuming a format that works for one model transfers to another; re-run format exploration when switching models.
- When using few-shot prompting, fix example selection and ordering to isolate formatting effects (as the authors did).

*validity:*
- Claims about model superiority based on a single arbitrary format can be confounded; trend reversals between models occur with substantial probability (e.g., 14% for LLaMA-2-13B vs 70B).
- For socially impactful tasks (e.g., stereotype classification), report the worst-case performance a non-adversarial user might encounter, not just the best format.

**Caveats:**
- Grammar covers only a subset of plausible formats; some generated formats are unusual (e.g., `<sep>`), though contextual restrictions mitigate this.
- Evaluation restricted to classification and short-generation tasks with ≤20 valid outputs; longer inputs and more open-ended tasks may behave differently.
- Results use Super-NaturalInstructions tasks; spread patterns may not generalize to all domains or instruction styles.

**Other categories:**
- *generalization:* Findings caution that single-format results poorly support claims about model capability beyond the tested prompt; the spread itself is a robustness signal for deployment readiness.