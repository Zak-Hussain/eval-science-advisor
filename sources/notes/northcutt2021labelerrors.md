# Label Errors in ML Benchmark Test Sets (Northcutt et al., 2021)

**What kind of evidence:** Empirical study across 10 benchmark datasets, with algorithmic error detection, human validation, and benchmarking experiments.

**Key claims:**
- At least 3.3% average label error rate across 10 common ML benchmark test sets; ImageNet validation set has ~6% errors, later estimated closer to 20% when accounting for non-CL-flagged errors.
- 51% of algorithmically-flagged candidates were confirmed as genuine label errors by human reviewers.
- Higher-capacity models (e.g., NASNet) perform better on original noisy test labels but worse on corrected labels for mislabeled examples, compared to lower-capacity models (e.g., ResNet-18).
- On ImageNet, ResNet-18 outperforms ResNet-50 on corrected labels if mislabeled test prevalence increases by just 6%.
- Benchmark rankings are largely unchanged by removing errors but change drastically when evaluated on corrected labels for the correctable subset.

**What the advisor should take from it:**

*reliability:*
- Assume test labels contain errors, especially for crowd-sourced or automatically labeled data. Even gold-standard benchmarks are not immune.
- Use confident learning to algorithmically pre-filter likely errors before human review, reducing review burden by up to ~90%; CL-flagged examples were 2.6x more likely to be mislabeled than non-flagged ones.
- CL misses a substantial fraction of errors: ~14% of ImageNet errors were in non-CL-flagged data. Algorithmic flagging is a prioritization tool, not a complete solution.

*validity:*
- Standard test accuracy on noisy labels can be a misleading basis for model selection: models scoring higher on original labels may perform worse on corrected labels.
- The distinction between "original accuracy" and "corrected accuracy" is central—practitioners measure the former but care about the latter.
- Validity of benchmark conclusions depends on test-label quality, not merely train/test distribution match.

*generalization:*
- In noisier real-world datasets, lower-capacity models may deploy better than higher-capacity models that overfit systematic label-error patterns.
- The gap between original and corrected accuracy grows proportionally with noise prevalence, so noisier datasets face greater risk of selecting the wrong model.
- Correcting at least test-set labels is recommended to better predict real-world deployment performance.

**Caveats:**
- Corrected labels are imperfect; failure modes exist where both original and CL-predicted labels are wrong.
- Only subsets of the two largest datasets were human-validated due to cost.
- Benchmark instability analysis uses simulated noise prevalence via interpolation rather than naturally noisier test sets.

**Category changes:** Added generalization: the paper directly addresses how benchmark scores predict real-world deployment under label noise; kept reliability and validity from suggestions.