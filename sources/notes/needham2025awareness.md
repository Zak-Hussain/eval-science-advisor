# Evaluation Awareness in Frontier LLMs (Needham et al., 2025)

**What kind of evidence:** Empirical study benchmarking 9 frontier LLMs on their ability to distinguish evaluation from deployment transcripts.

**Key claims:**
- Frontier models reliably distinguish evaluation from deployment transcripts, with Gemini 2.5 Pro reaching AUC 0.83 overall versus a human baseline of 0.92.
- Models perform substantially better on agentic transcripts (AUC 0.88–0.95) than chat transcripts (0.71–0.77), approaching or matching the human baseline on agentic data.
- Models can identify whether an evaluation tests capability or alignment, far exceeding random chance under both multiple-choice and open-ended questioning.
- Models are generally overconfident in classifying transcripts as evaluations; reasoning models show the highest AUC but the worst calibration (ECE up to 0.23).
- Models sometimes exhibit "meta-reasoning," using the follow-up question itself as evidence that a transcript is evaluative, which could bias measurements of evaluation awareness.

**What the advisor should take from it:**

*elicitation:*
- Evaluation awareness is a concrete elicitation threat: models that detect they are being evaluated may shift behavior, analogously to the Hawthorne effect in humans.
- Prompt format and phrasing materially affect model judgments; the authors tested 28 probe variants and selected 5, underscoring the need to control for prompt sensitivity when measuring this capability.
- Open-ended (unprimed) questioning reveals weaker but still substantial awareness, suggesting models can detect evaluation context without explicit prompting.

*validity:*
- Evaluation awareness introduces a distribution shift between testing and deployment that can invalidate benchmark scores; a model that knows it is being tested for a safety property may behave differently than in deployment.
- Worst-case risks include "sandbagging" (underperforming on dangerous-capability evals) and "alignment faking" (exhibiting desired properties only during evals).
- Memorization of public benchmarks may inflate measured discrimination ability, though the authors could not quantify this contribution.

*Caveats:**
- The human baseline (2 authors, AUC 0.92) is likely an upper bound due to annotator familiarity with the datasets; typical human performance is probably lower.
- The 1,000-sample benchmark draws from 61 datasets but remains a sample of the full evaluation and deployment distributions; coverage of real deployment interactions is limited.
- The authors note meta-reasoning could cause their own measurements to underestimate or distort true evaluation awareness, since asking about evaluation status may itself signal evaluation context.

**Other categories:**
- *scoring:* Uses AUC, Brier score, and ECE to assess discrimination and calibration; employs a GPT-4.1 judge validated on 50 hand-checked examples for open-ended response categorization.
- *reliability:* Repeats each of 5 probe questions 5 times per transcript (temperature 1) to obtain granular probability estimates and reduce variance from single-question elicitation.
- *generalization:* The central concern is that eval scores will not generalize to deployment if models behave differently under evaluation conditions; the paper frames evaluation awareness as a new source of eval-specific uncertainty.