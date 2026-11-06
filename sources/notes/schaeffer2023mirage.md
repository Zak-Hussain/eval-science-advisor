# Emergent abilities as metric artifacts (Schaeffer et al., 2023)

**What kind of evidence:** Empirical and theoretical study with reanalysis of published benchmarks.

**Key claims:**
- Emergent abilities (sharp, unpredictable performance jumps with scale) appear under nonlinear or discontinuous metrics (e.g., Exact String Match, Multiple Choice Grade) but vanish under linear or continuous metrics (e.g., Token Edit Distance, Brier Score).
- >92% of BIG-Bench emergent abilities occur under just two metrics: Multiple Choice Grade and Exact String Match.
- Insufficient test-data resolution makes smaller models appear to have zero ability when they actually perform above chance; generating more test data reveals smooth improvement even under nonlinear metrics.
- Emergent abilities can be artificially induced in vision tasks (autoencoders on CIFAR100, transformers on Omniglot, LeNet on MNIST) purely by choosing sharp metrics.
- Per-token cross-entropy loss scales smoothly and predictably as a power law with model size.

**What the advisor should take from it:**

*scoring:*
- Before claiming a capability "emerges," check whether the result persists under linear or continuous metrics; if it only appears under nonlinear/discontinuous ones, the emergence is likely a metric artifact.
- Prefer metrics whose error rate scales roughly linearly with per-token error (e.g., edit distance) over all-or-nothing metrics (e.g., exact match) when you want to track graded improvement.
- Ensure sufficient test-data volume to resolve small-model performance; underpowered evaluation can make nonzero ability look like zero.

*constructs:*
- "Emergent ability" as sharpness + unpredictability may not correspond to any underlying discontinuity in model behavior; the construct may be measuring metric properties rather than model properties.
- Continuous per-token error rate is a more stable construct for tracking scaling behaviour than task-level pass/fail.

*generalization:*
- Claims that a model family has an emergent ability on a task do not generalize across metrics; emergence is task-metric-model-specific, not task-model-specific.
- The large number of task-metric-model triplets in benchmarks like BIG-Bench (~10^6) creates a multiple-comparisons risk: some apparent emergence may arise by chance.

*Caveats:**
- The mathematical model assumes per-token errors are independent, which the authors acknowledge is empirically false.
- Direct retesting was limited to the GPT-3/InstructGPT family; other families were analyzed only through published results.
- The paper does not claim emergent abilities are impossible, only that previously claimed examples are likely artifacts.

**Other categories:** *reliability* — insufficient test-data resolution is a reliability failure that can be remedied by increasing sample size. *validity* — emergent-ability claims face a construct-validity threat from metric choice and a statistical-validity threat from multiple comparisons.