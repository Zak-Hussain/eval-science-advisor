# Human Label Variation as Signal, Not Noise (Plank, 2022)

**What kind of evidence:** Position paper synthesizing fragmented literature across NLP, CV, and HCI, with a curated dataset repository.

**Key claims:**
- Human label variation (HLV)—plausible disagreement due to ambiguity, subjectivity, or multiple valid answers—is abundant, not just noise; at least 20% of NLI data shows plausible variation (Pavlick & Kwiatkowski, 2019).
- Aggregation (majority vote) obfuscates genuine annotator diversity and discards information relevant to all pipeline stages: data, modeling, and evaluation.
- Methods that embrace HLV (soft labels, multi-task learning with annotator-specific tasks, cost-sensitive loss) can regularize learning, but evidence is stronger in CV than NLP and remains fragmented across subfields.
- Evaluating only against hard gold labels is "severely flawed" for many tasks; models optimized to single ground truth may be "climbing the wrong hill."
- Calibration to human majority is theoretically and empirically problematic when inherent disagreement exists; instance-level measures capturing the full human distribution are proposed as alternatives.
- Distinguishing annotation errors from genuine HLV remains an open, largely overlooked challenge.

**What the advisor should take from it:**

*scoring:*
- Prefer soft-label evaluation metrics (cross-entropy, KL/Jensen-Shannon divergence, entropy correlation) over accuracy alone when annotator disagreement is plausible; these capture whether models represent the full human judgement distribution, not just the argmax.
- Consider evaluating against individual annotators or data splits by agreement level, annotator clustering, or item difficulty rather than a single aggregated gold standard.
- Hard-label accuracy can be misleadingly high and gives no indication of model reasonableness, confidence, or trustworthiness.

*reliability:*
- Low inter-annotator agreement does not necessarily indicate poor data quality; it may signal genuine ambiguity or subjectivity. Treat HLV as a reliability finding to investigate, not noise to eliminate.
- Release un-aggregated, annotator-level labels (even for a subset) plus metadata (annotator IDs, demographics, annotation time, uncertainty flags) to enable downstream reliability analysis.
- Filtering low-agreement instances can worsen performance and waste data; aggregation by definition allows only one belief, discarding cases where multiple answers are valid.

**Caveats:**
- The paper is a position/synthesis piece; it does not provide new empirical results, and many claims are hypotheses or calls to action rather than tested findings.
- Evidence that embracing HLV improves NLP model performance is described as scarce compared to CV; transferability of methods across tasks is an open question.
- The paper acknowledges it is necessarily incomplete given the breadth of the topic.

**Other categories:**

*validity:* Argues that single-ground-truth evaluation undermines validity claims for subjective or ambiguous tasks; "acceptability" may be a more appropriate standard than "right/wrong."

*generalization:* HLV-aware training on ambiguous instances may improve out-of-distribution generalization (per Swayamdipta et al., 2020); this connection is hypothesized, not established.