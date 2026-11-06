# Dispositional Measurement for AI Evaluation (Voudouris et al., 2026)

**What kind of evidence:** Position paper / theoretical framework drawing on philosophy of science, measurement theory, and cognitive science.

**Key claims:**
- Capabilities and propensities are dispositional properties: stable, intrinsic features characterised by counterfactual relationships between contextual conditions and behavioural outputs. Capabilities co-vary with task demands; propensities co-vary with incentives.
- Dispositions require a causal basis (system properties × context → behaviour), gradedness, and comparability across systems.
- Benchmarking and elicitation do not measure dispositions: they sample performance in narrow regions of contextual space without identifying which contextual properties causally drive behaviour.
- Data-driven IRT infers difficulty and ability solely from performance covariance, making latent variables circular and population-dependent; without independently grounded task-structure theory, IRT summarises patterns rather than measuring dispositions.
- Scientific measurement of dispositions requires: (1) defining the subject, (2) hypothesising causal contextual properties, (3) operationalising those properties independently of performance, (4) empirically mapping p(v|π,θ) across systematic variation.
- Dispositional measurement enables extrapolation beyond observed performance, including into superhuman and ethically prohibited regimes.

**What the advisor should take from it:**

*constructs:*
- Define the measurement target explicitly as a disposition: specify the target behaviour v, the contextual space π, and whether π components are demand-relevant (capability) or incentive-relevant (propensity).
- Distinguish performance (a manifestation in one context) from the underlying disposition (the full counterfactual relationship). Aggregate scores are not dispositions.
- Capabilities and propensities are conceptually independent; both can co-exist and should be measured separately rather than inferred from each other.

*validity:*
- Construct validity requires a defensible theoretical link between task items and the target disposition. A review of 445 LLM benchmarks found nearly half target contested or undefined constructs, over a quarter use convenience samples, and fewer than 1 in 6 use statistical testing.
- Benchmarks conflate base model, system prompts, safety filters, tool pipelines, and human evaluators — the subject of measurement is often unspecified, making scores uninterpretable.
- Confounds such as prompt phrasing, response format, and data contamination inflate or deflate scores without reflecting the underlying disposition.

*elicitation:*
- Red-teaming and adversarial prompting sample a tiny, human-selected region of contextual space, yielding anecdotes of failure rather than measurements of inclination.
- Elicitation cannot distinguish behaviours arising only under contrived provocation from those that would robustly manifest across relevant counterfactual contexts.
- A disposition-respecting alternative: systematically vary incentive-relevant contextual features (e.g., justificatory framing, oversight cues, perceived user vulnerability) and map how the probability of the target behaviour changes, rather than seeking single worst-case failures.

*measurement-models:*
- Data-driven IRT difficulty parameters are circular: they are whatever items systems fail, not independently characterised task features. Two items with identical difficulty may require entirely different skills.
- IRT ability and difficulty are population-dependent: adding or removing systems shifts all estimates. A disposition must be a property of the system itself, not an artefact of the comparison class.
- IRT can support disposition measurement only when paired with an externally grounded theory of task structure (e.g., working-memory theory in psychometrics). Without it, latent variables are statistical decompositions, not measurements of dispositions.

*generalization:*
- Benchmarks require known answers and human-authored items; elicitation requires human judgement. Both fail as systems exceed human competence or when tasks are too dangerous to administer.
- Dispositional measurement enables extrapolation: vary π across safe tasks sharing structural properties with dangerous ones, estimate p(v|π,θ), and infer behaviour in unobserved or prohibited regions — analogous to estimating tensile strength without catastrophic failure.
- Measurements expressed in terms of theory-grounded external variables (not performance-derived latent scores) can generalise beyond the tested range and support principled cross-system comparison.

**Caveats:**
- The paper is a conceptual framework, not an empirical validation; the toy illustrations (arithmetic capability, honesty propensity) are deliberately simplified demonstrations, not tested protocols.
- The field lacks mature theories specifying which contextual properties matter for AI dispositions; identifying these is the central scientific challenge, not a solved problem.
- The authors acknowledge that partitioning π into demand vs. incentive components may not be the only principled partition; other dimensions (modality, time pressure, tool availability) may define additional dispositional kinds.

**Other categories:** none.