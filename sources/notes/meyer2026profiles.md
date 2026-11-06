# Apparent Psychological Profiles as Measurement Artifacts (Meyer et al., 2026)

**What kind of evidence:** Empirical study administering personality and risk-preference instruments to 56 instruction-tuned LLMs with large human reference samples.

**Key claims:**
- Between-model variation in LLM responses is driven by directional response bias, not target traits: 81–90% of between-model variance is bias versus 9–16% in humans.
- Apparent internal consistency is almost entirely predicted by response orthogonality (proportion of reverse-keyed items): cross-instrument r = −0.95 for LLMs versus −0.41 for humans.
- Response bias declines with model capability but is not eliminated; even proprietary models remain outside human ranges.
- Psychological profiles shift with item keying and can be manufactured through forward- or reverse-heavy item selection.
- The pattern holds across ten prompting conditions, model sizes, and is not explained by negation handling or degenerate responders.

**What the advisor should take from it:**

*constructs:*
- Apparent psychological profiles in LLMs do not reflect the traits instruments claim to measure; they largely reflect a directional response tendency toward one end of the scale.
- Whether LLMs possess human-like stable dispositions remains open; borrowed human instruments may lack construct validity for LLMs because items presuppose embodiment or volition.

*validity:*
- Without response orthogonality, trait and response bias are confounded; high reliability alone does not establish a valid construct.
- Existing LLM psychological profiles and their reliability coefficients need re-evaluation against orthogonality.
- Valid assessment requires either fully orthogonal instruments or an explicit psychometric measurement model that separates trait from bias.

*reliability:*
- High internal consistency (Cronbach's α up to 0.96) on forward-keyed instruments is a bias artifact, not evidence of a coherent latent trait; reliability collapses (α negative) under balanced keying.
- The orthogonality-consistency gradient is a diagnostic: if reliability plummets when reverse-keyed items are added, responding is bias-driven, not trait-driven.
- Behavioral tasks fare no better than self-reports; they show greater sensitivity to response bias.

**Caveats:**
- Only 56 models (10 proprietary); proprietary subset too small for standard inferential tests.
- Only post-trained instruction-tuned models assessed; base models untested.
- Two domains covered (personality and risk); generalization to other domains untested.

**Other categories:** Elicitation (bias pattern robust across ten prompting conditions including context, elicitation method, and option order); measurement-models (formal variance-decomposition framework separating trait from response bias via orthogonal contrasts).