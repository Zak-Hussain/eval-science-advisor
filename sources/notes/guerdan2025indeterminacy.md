# Validating LLM-as-a-judge under rating indeterminacy (Guerdan et al., 2025)

**What kind of evidence:** Methods paper with theoretical framework, real-data experiments (11 rating tasks, 9 LLMs), and synthetic experiments.

**Key claims:**
- Rating indeterminacy—where multiple ratings are plausibly "correct" for one item—is pervasive in toxicity, factuality, relevance, and helpfulness tasks; forced-choice elicitation discards this information irrecoverably.
- The response set distribution is identifiable from forced-choice data only when a rating task is "fully specified" (i.e., instructions tell raters how to resolve indeterminacy); otherwise infinitely many response set distributions are consistent with observed forced-choice data (Theorem 3.1).
- Judge systems differ substantially from each other and from humans in how they resolve indeterminacy under forced-choice (estimated sensitivity parameters span 0.12–0.54 across systems on SummEval Relevance).
- Standard forced-choice categorical metrics select judge systems up to 31% worse (in downstream content-filtering consistency) than systems selected via response-set metrics.
- Continuous multi-label MSE over response-set ratings selects more performant judges than all forced-choice alternatives; a small auxiliary corpus (~100 paired ratings) estimating the translation matrix recovers most of this benefit.
- Among forced-choice-only metrics, KL-Divergence(h‖j) outperforms both categorical metrics and KL-D(j‖h).

**What the advisor should take from it:**

*scoring:*
- Prefer multi-label "response set" elicitation ("select ALL options that could reasonably apply") over forced-choice; aggregate via soft response-set vectors and measure agreement with continuous multi-label MSE.
- If stuck with forced-choice data, distributional metrics (especially KL-D in the human→judge direction) are less biased than categorical ones (Hit Rate, Cohen's κ).
- Fully specifying tasks (adding unambiguous "Maybe"/"Tie" options with clear instructions) eliminates indeterminacy and makes all metrics equivalent.

*validity:*
- Human–judge agreement on forced-choice ratings is not a valid proxy for downstream task performance when indeterminacy is present and humans/judges resolve it differently.
- Validate judges against downstream metrics (decision consistency, prevalence-estimation bias) defined over response-set distributions, not against gold-label agreement.
- Rank inversions between agreement metrics and downstream metrics are common and can be severe (e.g., 28% additional prevalence-estimation error).

*reliability:*
- Judge rankings are sensitive to how indeterminacy is resolved; the same judge can rank #1 or #4 depending on the metric used.
- Rater error matters less than forced-choice selection effects for judge selection; MSE(srs/srs) rankings are robust to error in synthetic experiments.
- Very few ratings per item (1–3) capture insufficient information about indeterminacy regardless of metric; more ratings help but fully-specified tasks reduce per-item requirements.

**Caveats:**
- Framework applies only to discrete-option tasks, not continuous scales.
- Assumes a fixed forced-choice translation matrix across raters within a task (homogeneity assumption that may not hold).
- Human response-set distributions are not directly observed; experiments reverse-map from forced-choice data using a sensitivity parameter β varied systematically rather than empirically measured.

**Other categories:** *elicitation*—response-set elicitation is a concrete alternative prompting strategy; *generalization*—downstream task performance (content filtering, prevalence estimation) is the intended generalization target, analogous to selecting a classifier by likelihood but deploying at a threshold.