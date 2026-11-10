# General Scales for AI Evaluation (Zhou et al., 2025)

**What kind of evidence:** Methods paper with empirical validation across 15 LLMs and 16,108 instances from 20 benchmarks.

**Key claims:**
- 18 demand rubrics (DeLeAn) on ratio scales (0, ∞) can annotate any text task instance; GPT-4o annotations agree with human Delphi consensus (average rWG = 0.86, Spearman 0.86).
- Many benchmarks lack specificity (measuring unintended dimensions) or sensitivity (insufficient level range in claimed dimensions).
- Ability profiles from characteristic curves are non-populational—independent of other models—and invariant to task-distribution difficulty changes.
- Demand-based Random Forest assessors (19 features) achieve weighted AUROC 0.84 in-distribution, 0.81 task-OOD, 0.75 benchmark-OOD, outperforming embedding and fine-tuned-LLaMA baselines OOD.
- CoT models gain in reasoning, identifying relevant information, and mind modelling; knowledge abilities track model size with diminishing returns at largest scales.

**What the advisor should take from it:**

*constructs:*
- Define demands on ratio scales with absolute zero so levels are commensurate across dimensions; abilities can then exceed current rubric ceilings.
- Include extraneous dimensions—atypicality, volume, unguessability—to separate genuine cognitive demands from contamination, amalgamation, and funnelling confounders.

*measurement-models:*
- Use "dominant slice" binning: for a dimension at level l, keep only instances where no other dimension exceeds l, enabling unidimensional curves without requiring pure items.
- Estimate ability as the area under the logistic curve fitted to per-level success rates; this equals the demand level at 0.5 success probability and is non-populational.

*validity:*
- Inspect per-benchmark demand histograms to verify each covers the full level range for target dimensions (sensitivity) and avoids loading on irrelevant ones (specificity).
- Use atypicality annotations to flag contamination where high performance coincides with low cognitive demand.

*generalization:*
- Train per-model assessors on the demand vector to predict instance-level success; these generalize better OOD than embedding or fine-tuning because demand features are interpretable and less prone to spurious overfitting.
- Compare a model's ability vector to a new task's demand vector for counterfactual failure analysis without running the model.

*reliability:*
- Validate LLM annotations against human Delphi consensus using rWG (threshold 0.7); GPT-4o achieved ≥0.75 across all 18 dimensions.

**Caveats:**
- Only text modality and LLMs evaluated; navigation and multimodal dimensions are underrepresented in the battery.
- Few level-5+ instances limit discrimination for the strongest models; scales need backward-compatible extension.
- Benchmark-OOD assessor performance drops for reasoning models (AUROC decrease 0.05–0.11), partly due to only 20 benchmarks limiting demand-space coverage.

**Category changes:** Added validity and reliability to the suggested set; the paper substantively addresses benchmark specificity/sensitivity and inter-rater agreement. Dropped elicitation and scoring: elicitation is only mentioned via CoT prompting; scoring uses standard LLM graders without methodological contribution.