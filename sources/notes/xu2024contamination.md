# Benchmark Data Contamination of LLMs: A Survey (Xu et al., 2024)

**What kind of evidence:** Systematic review covering detection and mitigation of benchmark data contamination in LLMs.

**Key claims:**
- BDC—exposure of a model to evaluation benchmark data during training—distorts evaluation results across all three evaluation methods: traditional benchmark testing, automatic evaluation, and human evaluation.
- Contamination severity ranges across four levels: semantic (same topic/source), information (metadata/label distributions), data (test content without labels), and label (full exposure). Severity increases toward label level, but detectability decreases toward semantic level.
- Detection methods divide into matching-based (n-gram overlap, membership inference, example generation) and comparison-based (content comparison, perplexity, chronological analysis). N-gram overlap is simple but has high false negatives; paraphrasing can bypass it.
- Mitigation strategies fall into three groups: curating new data (private or dynamic benchmarks), refactoring existing data (regeneration, content filtering), and benchmark-free evaluation (LLM-as-judge, human participation). None fully eliminates BDC.
- Contamination rates across 15+ LLMs and six QA benchmarks ranged from 1% to 45%, and contamination does not always correlate with improved performance—though larger models may benefit more.
- Full elimination is impracticable given the scale of pre-training data and recursive AIGC content generation.

**What the advisor should take from it:**

*validity:*
- BDC is a core threat to score-based validity arguments: inflated accuracy, skewed calibration, compromised robustness, and reinforced fairness biases are all direct consequences.
- When auditing an eval, check all four contamination levels, not just label leakage. Semantic-level contamination (same topic/source in training) is hardest to detect and mitigate.
- Chronological analysis—comparing model performance on data released before vs. after training cutoff—can provide evidence of contamination without training-data access.

*constructs:*
- Contamination can inflate apparent capabilities (e.g., code generation, QA, sentiment analysis) without reflecting true reasoning or generalization, so construct claims built on contaminated scores are unfounded.

*generalization:*
- Contaminated benchmark scores do not support claims about deployment performance. Dynamic or time-windowed benchmarks (e.g., LatestEval, LiveCodeBench) better approximate novel-data generalization.

*reliability:*
- Scores on contaminated vs. uncontaminated items within the same benchmark may differ systematically, undermining cross-item consistency.

*scoring:*
- Automatic metrics (accuracy, F1, ROUGE) are directly inflated; calibration metrics like ECE can give false confidence when based on contaminated data.

*elicitation:*
- The paper has little direct guidance on prompting or scaffolding, aside from noting that TS-Guessing and DCQ protocols can probe whether a model has seen specific test items.

**Caveats:**
- The survey synthesizes heterogeneous studies with different definitions and detection thresholds; contamination rates cited are not directly comparable across studies.
- Most detection methods are validated on specific model families and benchmarks; generalization of detection accuracy across architectures is not established.
- The authors note that no mitigation strategy is immune to secondary contamination—newly generated or refactored data may still reflect patterns from previously contaminated training corpora.

**Other categories:** none.