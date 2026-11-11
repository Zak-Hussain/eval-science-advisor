# Benchmark Data Contamination of Large Language Models: A Survey (Xu et al., 2024)

**What kind of evidence:** Systematic survey reviewing detection techniques and mitigation strategies for benchmark data contamination (BDC) in LLMs.

**Key claims:**
- BDC distorts evaluation results by exposing models to benchmark data during training, inflating performance metrics and undermining reliability across accuracy, calibration, fairness, and robustness.
- Contamination severity increases across four levels—semantic, information, data, and label—while detection difficulty inversely correlates with severity.
- Matching-based detection (n-gram overlap, membership inference) and comparison-based detection (perplexity, chronological analysis, distribution comparison) each have distinct scope limitations.
- Mitigation strategies fall into data curation (private/dynamic benchmarks), data refactoring (regeneration, content filtering), and benchmark-free evaluation (LLM-as-judge, human participation).
- Complete BDC elimination is impracticable: large-scale pretraining inevitably captures benchmark-related information, and AIGC recursion compounds semantic-level contamination.
- Larger models may benefit more from contaminated test sets than smaller ones, with accuracy boosts observed on certain benchmarks.

**What the advisor should take from it:**

*validity:*
- BDC is a core threat to validity arguments: scores may reflect memorization rather than capability, affecting all four automatic-evaluation metric families (accuracy, calibration, fairness, robustness).
- N-gram overlap detection (13-gram for GPT-3, 50-character for GPT-4) has high false-negative rates; paraphrased or semantically equivalent content easily bypasses string-matching filters.
- Chronological analysis—testing on data released after training cutoffs—provides evidence of contamination when performance drops sharply on post-cutoff items.

*elicitation:*
- TS-Guessing and Data Contamination Quiz probe for memorization by masking or perturbing benchmark items and asking the model to reconstruct them; high reconstruction accuracy signals exposure.
- Membership inference via name-cloze or cloze-style queries can detect label-level contamination without accessing training data.

*reliability:*
- Contamination effects are inconsistent across datasets and model sizes; a model may memorize without exploiting, or exploit without verbatim memorization, making detection results non-transferable across contexts.
- Dynamic benchmarks reduce contamination risk but introduce temporal inconsistency across evaluation cycles, complicating longitudinal comparisons.

*generalization:*
- Semantic and information-level contamination cannot be fully filtered from pretraining corpora, so claims extrapolated from benchmark scores to real-world deployment remain vulnerable even after decontamination efforts.
- Secondary contamination can occur when regenerated or newly curated data is itself absorbed into future pretraining corpora.

**Caveats:**
- Survey compiles methods with varying empirical rigor; many detection techniques were validated on limited benchmark sets and specific model families.
- Most matching-based methods require access to training data, which is unavailable for proprietary models like GPT-4 and Claude-3.
- The authors acknowledge that no mitigation strategy is immune to secondary contamination or semantic-level exposure.

**Category changes:** Added elicitation and generalization; the paper substantively discusses probing techniques for detecting contamination and limits on extrapolating from decontaminated benchmarks. Dropped scoring and measurement-models; not substantively addressed.