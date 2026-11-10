# LLM Psychological Profiles are Measurement Artifacts (Meyer et al., 2026)

**What kind of evidence:** Empirical study using a formal psychometric framework.

**Key claims:**
- Between-model differences on human psychological instruments (e.g., Big Five, risk preference) are driven primarily by a directional response bias rather than the targeted traits, accounting for 81–90% of between-model variance versus 9–16% in humans.
- Apparent reliability in LLMs is almost entirely predicted by an instrument’s response orthogonality (proportion of reverse-keyed items), with cross-instrument correlation r = -0.95. Fully orthogonal instruments yield near-zero or negative reliability.
- The bias attenuates with model capability (size/proprietary status) but is not eliminated; even the most capable models fall outside the human range.
- Because bias drives responding, the apparent psychological profile of a model shifts depending on item keying and can be manufactured through item selection.

**What the advisor should take from it:**

*constructs:*
- Be cautious when attributing human-like psychological traits to LLMs using borrowed psychometric instruments; LLMs may lack stable dispositions for these constructs, or the instruments may lack validity for LLMs.

*validity:*
- High internal consistency (e.g., Cronbach’s alpha) does not establish that a construct is being measured; response bias can inflate apparent consistency just as a shared construct would.
- Profiles derived from non-orthogonal instruments are confounded and cannot be interpreted as evidence of genuine traits. Existing LLM psychological profiles need re-evaluation against response orthogonality.

*reliability:*
- Apparent reliability in LLM evals can be entirely artifactual. If an instrument lacks reverse-keyed items, high inter-item correlation may reflect a directional response tendency rather than coherence.
- Test whether reliability survives under full response orthogonality (balanced forward and reverse keying). If reliability collapses to near zero, the original consistency was bias-driven.

*measurement-models:*
- Use formal measurement models to separate trait from response bias. The paper models responses by partitioning variance into a trait component (half-difference of forward/reverse means) and a bias component (half-sum).
- Design or evaluate instruments with "response orthogonality": include items where the trait-favored option occupies different positions so trait and bias act in opposite directions.

**Caveats:**
- Treats each LLM as a single respondent in its default state; within-model variation from steering or persona prompting is not assessed.
- The instruments were designed for humans and may inherently lack validity for LLMs, which lack embodiment or volition for some items.
- Only post-trained instruction-tuned models were tested; base models and other architectures might behave differently.

**Category changes:** Added measurement-models for the formal psychometric framework; retained all suggested categories.