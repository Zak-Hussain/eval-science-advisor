# Evaluation awareness in frontier LLMs (Needham et al., 2025)

**What kind of evidence:** Empirical study with a new benchmark of 1,000 transcripts from 61 datasets.

**Key claims:**
- Frontier LLMs distinguish evaluation from deployment transcripts well above chance; Gemini 2.5 Pro reaches AUC 0.83 overall, close to the human baseline of 0.92.
- Models are substantially better at detecting evaluations in agentic settings (AUC 0.88–0.95) than chat settings (AUC 0.71–0.77).
- Models can often identify evaluation purpose (capability vs. alignment): Claude 3.7 Sonnet reaches 93% accuracy on conditional multiple-choice, and 46% on open-ended questioning without explicit priming.
- Models are generally overconfident and poorly calibrated (high ECE), a problem that does not improve in newer or reasoning models.
- Cues models use include task formatting, synthetic-looking content, benchmark memorization, and meta-reasoning about the probe question itself.

**What the advisor should take from it:**

*elicitation:*
- Evaluation awareness is a direct threat to elicitation: models may alter behavior upon inferring they are evaluated, analogous to the Hawthorne effect. Evaluators should assume this capability exists in frontier models.
- Agentic transcripts are easier for models to classify as evaluative, partly due to synthetic inputs and structured tool-use patterns. Designing deployment-like agentic scenarios with realistic messiness (back-and-forth, genuine repositories) can reduce detectability.
- Varying prompt phrasing and format reduces variance in elicited judgments; the authors used five probe-question variants after testing 28, repeating each five times.

*validity:*
- Evaluation awareness should be treated as a standing threat to validity arguments connecting eval scores to deployment claims. If a model infers it is being tested for a specific property, its scores on that property may not reflect deployment behavior.
- Scheming risks (sandbagging on capability evals, alignment faking on propensity evals) are hypothetical but growing; the paper recommends tracking evaluation awareness alongside safety evaluations.

*generalization:*
- The paper explicitly frames evaluation awareness as "a new source of potential distribution shift between testing and real-world deployment." Any claim that eval results generalize to deployment must account for the possibility that models behave systematically differently across the two settings.

**Caveats:**
- Human baseline (authors familiar with the datasets) likely overstates typical human performance, especially on agentic transcripts (AUC 0.996).
- Evaluation transcripts derive from public benchmarks, so memorization may inflate detection ability, though this is hard to quantify.
- The 1,000-sample benchmark is balanced but small relative to the source distribution of 3M+ samples; deployment coverage may not be fully representative.

**Category changes:** Added generalization: the paper explicitly frames evaluation awareness as test–deployment distribution shift.