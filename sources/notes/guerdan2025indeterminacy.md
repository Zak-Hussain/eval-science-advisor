# Validating LLM Judges Under Rating Indeterminacy (Guerdan et al., 2025)

**What kind of evidence:** Theory plus empirical study (11 rating tasks, 9 commercial LLMs, synthetic experiments).

**Key claims:**
- Response set distributions (all plausible ratings per item) are not identifiable from forced-choice distributions unless a rating task is "fully specified" — i.e., instructions tell raters how to resolve multi-valid interpretations (Theorem 3.1).
- Forced-choice agreement metrics and response set metrics yield inconsistent judge rankings unless a strong monotonicity condition holds, which seldom does in practice (Theorem C.7).
- Judge systems vary substantially in how they resolve indeterminacy under forced-choice elicitation; estimated sensitivity parameters span 0.12–0.54 across systems for a single task (SummEval Relevance).
- Standard forced-choice validation can select judges up to 31% worse than the true optimum on downstream tasks (content filtering, prevalence estimation).
- Continuous multi-label MSE on response set ratings selects more performant judges than all forced-choice alternatives once indeterminacy is moderate (β ≥ 0.2); among forced-choice distributional metrics, KL-D(h‖j) performs best while KL-D(j‖h) performs poorly.

**What the advisor should take from it:**

*validity:*
- Forced-choice elicitation introduces a threat to meta-evaluation validity: it conflates genuine disagreement about what is "correct" with arbitrary resolution of indeterminacy, biasing judge selection.
- When validating an LLM judge, prefer response set elicitation (raters select all plausible options) and multi-label agreement metrics; if only forced-choice data exist, collect a small auxiliary corpus of paired forced-choice/response set ratings (≈100 items) to estimate the translation matrix and recover an approximate multi-label metric.

*elicitation:*
- Design "fully specified" rating tasks whenever possible — add an explicit option (e.g., "Maybe" or "Tie") with instructions for when to use it, so raters need not arbitrarily collapse multiple valid interpretations into one.
- Response set elicitation ("select ALL options that could reasonably apply") directly captures intra-rater indeterminacy that forced-choice cannot, at similar computational cost.

*scoring:*
- Choose agreement metrics based on elicitation format: hard-aggregated categorical metrics (Hit Rate, Cohen's κ) are unreliable under indeterminacy; soft-aggregated distributional metrics partially help; continuous multi-label MSE on response set vectors is most robust.
- When only forced-choice data are available, use distributional KL-D(h‖j) rather than categorical or reverse-direction metrics as a fallback.

*reliability:*
- Rater error affects absolute prevalence estimates but has limited impact on judge system rankings relative to forced-choice selection effects; MSE on response sets remains rank-stable under simulated rater error (Fig. 38).

**Caveats:**
- Framework covers only discrete-option rating tasks; continuous scales (e.g., 1–100 factuality scores) are out of scope.
- The forced-choice translation model assumes a homogeneous mapping from response sets to forced-choice options across raters (Assumption C.2), which may be violated in practice.
- Human response set distributions were not directly collected; they were reverse-engineered from forced-choice data via a sensitivity parameter β, so downstream-task "ground truth" is partly simulated.

**Category changes:** Added elicitation: the paper's core distinction between forced-choice and response set elicitation is a central contribution, not incidental. Added reliability: the paper empirically examines ranking robustness under rater error. Kept scoring and validity from the suggested set; all four are substantially informed.