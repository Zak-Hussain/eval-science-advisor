# Human Label Variation as Signal, Not Noise (Plank et al., 2022)

**What kind of evidence:** Position paper synthesizing fragmented literature across NLP, CV, and HCI.

**Key claims:**
- Human label variation (HLV)—plausible annotation differences due to ambiguity, subjectivity, or multiple valid answers—is abundant and should not be treated as noise.
- Relying on a single aggregated gold label is problematic across the entire ML pipeline: data collection, modeling, and evaluation.
- Evidence that learning from un-aggregated labels helps is stronger in CV than in NLP, where it remains scarce; enriching gold labels with HLV (e.g., soft-label auxiliary tasks, cost-sensitive losses) is more studied in NLP.
- Current evaluation against hard gold labels "obfuscates the truth about the state of ML models" and creates a gap between in-vitro and in-vivo performance.
- Even small amounts of un-aggregated annotation data can improve learning in sequential fine-tuning setups (Lalor et al., 2017; Plank et al., 2014a).
- The paper provides a repository of publicly-available datasets with un-aggregated labels.

**What the advisor should take from it:**

*constructs:*
- Before designing an eval, distinguish genuine disagreement, subjectivity, multiple-plausible-answer cases, and annotation errors—these call for different measurement approaches.
- For many language tasks, "acceptability" may be a more appropriate construct than "correctness" when no ground truth exists.

*validity:*
- Evaluating against a single gold label threatens validity when HLV is present; accuracy can be high while masking how unreasonable or untrustworthy a model's predictions actually are.
- HCI audits show that standard metrics are misaligned with real-world performance, indicating a systematic in-vitro/in-vivo validity gap.

*scoring:*
- Consider soft-label evaluation metrics: cross entropy, entropy correlation, and KL or Jensen-Shannon divergence to compare model outputs against human label distributions.
- Evaluate against individual annotators, or via data splits by agreement level, annotator clustering, or item difficulty rather than only against a single gold label.
- Aggregation (majority vote, probabilistic methods) discards information by construction; document the choice and its implications.

*reliability:*
- Release annotator-level un-aggregated labels, even for a small data subset, and include annotator metadata (IDs, background, demographics, completion time) where responsible.
- Separating genuine HLV from annotation errors remains an open challenge; both error-detection methods and theoretical work on what constitutes an error are underdeveloped.

**Caveats:**
- This is a position paper; claims are synthesized from fragmented literature rather than a single controlled study.
- The authors acknowledge the dataset repository and literature review are necessarily incomplete.
- Comprehensive cross-method evaluation is lacking; whether methods transfer across tasks is an open question.

**Category changes:** Added constructs and validity: the paper centrally argues that ground truth is often ill-defined and that single-label evaluation is invalid. Kept scoring and reliability from the suggestion.