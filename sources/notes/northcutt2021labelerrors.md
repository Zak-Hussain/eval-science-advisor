# Pervasive Label Errors in Test Sets (Northcutt et al., 2021)

**What kind of evidence:** Empirical study across 10 standard ML benchmark datasets, with algorithmic error detection, crowdsourced human validation, and expert review on a subset.

**Key claims:**
- An average of at least 3.3% label errors exist across 10 common benchmark test sets; ImageNet validation has ~6% (conservatively) and closer to ~20% when extrapolating from expert review of non-flagged examples.
- Confident learning (CL) flags are 2.6x more likely to be erroneous than random non-flagged examples, making CL a useful prioritization filter for limited human review budgets.
- Benchmark rankings are largely unchanged by removing errors from the full test set, but on the correctable subset, higher-capacity models (e.g., NASNet) perform best on original (wrong) labels and worst on corrected labels; lower-capacity models (e.g., ResNet-18) show the opposite.
- Relatively small increases in test-label noise prevalence (e.g., +6% on ImageNet, +5% on CIFAR-10) flip model selection so that a lower-capacity model is favored on corrected labels while a higher-capacity model is favored on original labels.

**What the advisor should take from it:**
*reliability:*
- Treat test-set labels as a measurable source of score inconsistency; estimate label-error rates before trusting benchmark comparisons, especially with noisy or crowdsourced labels.
- Use CL-style filtering to prioritize human verification of likely errors, reducing cost by up to ~90%.

*validity:*
- "Original accuracy" (on given labels) and "corrected accuracy" (on human-corrected labels) can diverge enough to change which model is preferred; report or bound both when feasible.
- High-capacity models can systematically fit label-error patterns, inflating original accuracy while degrading real-world utility—a threat to the validity argument that test accuracy reflects deployment performance.
- Expert review found MTurk workers sometimes mislabel when neither presented label is correct; interface design and reference examples matter for human validation quality.

**Caveats:**
- Error rates are lower bounds: only CL-flagged subsets were fully human-verified for most datasets, and expert review suggests ~14% additional errors in non-flagged ImageNet images.
- Corrected labels are not guaranteed perfect; failure modes include cropped/ambiguous images where even experts struggle.
- Model-selection instability analysis uses simulated noise prevalence by subsampling, not independently collected noisy datasets.

**Other categories:** *scoring*—informs choice of accuracy metric (top-1 vs top-5) and human-rater protocols for label correction; *generalization*—directly addresses whether benchmark rankings transfer to noisier real-world deployment conditions.