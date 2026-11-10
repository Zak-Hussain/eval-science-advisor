# The “Everything in the Whole Wide World” Benchmark (Raji et al., 2021)

**What kind of evidence:** Position paper with illustrative case studies.

**Key claims:**
- Benchmarks like ImageNet and GLUE are framed as measures of general capabilities (visual understanding, language understanding), but this framing lacks construct validity because datasets are finite, specific, and contextual.
- Tasks in “general” benchmarks are arbitrarily selected rather than systematically mapped to a construct; GLUE tasks came from an informal survey of ~30 colleagues, not a theory of linguistic competence.
- Such benchmarks conflate distinct constructs—e.g., linguistic competence with world knowledge and commonsense reasoning—making them invalid as measures of any single capability.
- Benchmark data is de-contextualized and subjective: 45% of ImageNet images are US-sourced, and GLUE targets specific varieties of English with annotation artifacts.
- Aggregate performance on “general” benchmarks can mask disparate failures on minority subgroups, enabling unsafe deployment justification.
- The Common Task Framework was built for tightly scoped practical tasks; extending it to abstract “general” performance subverts its purpose.

*constructs:*
- Define constructs narrowly before benchmarking; “general-purpose” capability labels are too vague to operationalize in a single dataset.
- Avoid merging distinct constructs (e.g., linguistic form vs. world knowledge) under one benchmark without justifying why they should be measured together.
- Ground task selection in a theory of the target construct, not convenience or availability of data.

*validity:*
- Treat construct validity as a design task: ask whether the data, metric, and methodology actually represent the claimed capability, not just whether they produce reproducible scores.
- Scrutinize the gap between benchmark scores and real-world deployment claims; SOTA on a general benchmark does not support claims about deployment readiness or AGI progress.
- Use disaggregated analysis to check whether aggregate scores hide failures on specific subgroups—especially when benchmarks justify commercial deployment.
- Document the subjective, culturally-situated limitations of the dataset rather than presenting it as neutral.

*generalization:*
- Do not assume benchmark coverage matches deployment scope: evaluate geographic, temporal, and demographic alignment between the test set and the intended application context.
- Resist extrapolating from benchmark scores to out-of-context applications; the paper cites cases where firms cited benchmark performance as evidence of broad technical achievement.

**Caveats:** Conceptual argument supported by illustrative examples, not systematic empirical measurement. Analysis centers on two case studies (ImageNet, GLUE); applicability to other benchmark types (e.g., RL environments) is acknowledged but not explored. Proposed alternatives (test suites, audits, ablation) are surveyed briefly without validation of effectiveness.

**Category changes:** Added generalization: the paper substantially discusses coverage limits and deployment mismatch; dropped elicitation, scoring, reliability, and measurement-models as they are not addressed.