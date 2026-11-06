# General Scales for AI Evaluation (Zhou et al., 2025)

**What kind of evidence:** Methods paper with large-scale empirical validation across 15 LLMs, 16,108 instances, and human inter-rater analysis.

**Key claims:**
- 18 demand-level rubrics (DeLeAn) applied automatically by GPT-4o achieve strong human agreement (rWG averaging 0.86 against Delphi consensus).
- Ability profiles derived from characteristic curves are non-populational—estimated from a single model's results alone, invariant to task-distribution shifts, and not affected by adding or removing other models.
- Demand-based assessors (Random Forest on 19 features) predict instance-level success at AUROC ~0.84 in-distribution and ~0.75 benchmark-OOD, outperforming embeddings-based (0.80→0.48) and fine-tuned-LLaMA (0.84→0.69) assessors OOD.
- Many benchmarks lack sensitivity (insufficient range in claimed dimensions) or specificity (unintended extraneous demands), confounding aggregate accuracy comparisons.
- Extraneous dimensions—Atypicality, Volume, Unguessability—account for substantial predictive power, exposing contamination, amalgamation, and funnelling artefacts.

**What the advisor should take from it:**

*constructs:*
- Dimensions span 11 primordial cognitive capabilities, 5 knowledge domains calibrated to educational levels, and 3 extraneous factors; all use ratio scales (0–5+) with absolute zero, designed not to saturate.
- Extraneous dimensions should be included alongside cognitive demands to separate genuine capability from artefacts of item design.

*measurement-models:*
- Ability is defined as the demand level yielding 50% success probability (area under the logistic curve), estimated per-dimension via "dominant slicing" (including only instances where no other dimension exceeds the target level).
- ADeLe-Light (6,179 instances after redundancy reduction) yields nearly identical ability profiles to the full 16,108-instance battery, enabling cheaper evaluation.

*generalization:*
- Interpretable 19-dimensional demand vectors predict unseen-instance performance better than black-box baselines, especially OOD; predictive power is limited mainly by demand-space coverage, not model capacity.
- Algebraic assessors combining ability–demand differences via a generalised mean (r=0.25) provide a parameter-free prediction alternative.

**Caveats:**
- Limited to text modality; navigation, multimodal, and robotics dimensions not covered.
- Few level-5+ instances constrain discrimination for frontier models; scales will need backward-compatible extension.
- OOD performance depends on battery diversity; only 63 tasks from 20 benchmarks, with some dimensions (e.g., MS, ~300 instances) underrepresented.

**Other categories:** validity—benchmark demand profiles directly expose construct-validity failures (sensitivity/specificity); scoring—dual-LLM grading with disagreement filtering removes ~12% of noisy instances; reliability—Delphi consensus mitigates human-annotator inconsistency; elicitation—CoT and distillation effects on specific dimensions are characterised but not controlled experimentally.