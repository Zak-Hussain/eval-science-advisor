# Defining Model Capabilities (Harding & Sharadin, 2024)

**What kind of evidence:** Theory paper drawing on philosophy of action to define and operationalise what it means for an ML model to possess a capability.

**Key claims:**
- A model has a capability to φ iff, in some set of background conditions, it would reliably succeed at φing if it "tried"—where trying means its output is best explained by being directed at φing (CAMA, Definition 10).
- Capability possession (competence) is distinct from capability manifestation (performance); the same capability is invariant across different elicitation methods, even though performance varies.
- Coincidental success—via memorisation, surface heuristics, or luck—does not evidence capability. One can test for this by checking sensitivity to φ-relevant input perturbations and insensitivity to φ-irrelevant ones (Definition 11).
- Benchmarks concretise a particular operationalisation construct but inevitably have "operationalisation gaps" relative to deployment, so they cannot define what capabilities are.
- For fair inter-model comparison, background conditions (including prompting) should be varied per model to accommodate different performance constraints—but only conditions where the model genuinely "tries" to φ should count, ruling out gerrymandered setups.
- RLHF plausibly leaves the conditional "if it tries, it succeeds" intact while reducing the model's propensity to try harmful capabilities.

**What the advisor should take from it:**

*constructs:*
- Distinguish generic capabilities ("can add numbers") from deployment-specific ones ("can add numbers in this environment"); the latter depends on the deployment distribution and fixed scaffolding.
- An operationalisation construct must specify queries, success conditions, and relevant perturbations; ecological validity requires similarity to deployment conditions.
- Competence–performance separation means a model can possess a capability it fails to manifest under particular background conditions (e.g., content filters "mask" it).

*elicitation:*
- Different prompting strategies affect different things: few-shot may change whether the model "tries" to φ; chain-of-thought changes the probability of success conditional on trying. Design evaluations with this distinction in mind.
- When evaluating adversarial prompts or jailbreaks, measure "response rate" (whether the model attempts the behaviour), not just success—CAMA provides a principled basis for this via the trying test.
- For inter-model comparisons, allow model-specific prompting rather than forcing identical conditions, but verify the model is genuinely trying, not exploiting a gerrymandered shortcut.

**Caveats:**
- The behavioural test for "trying" (Definition 11) is coarse-grained: some capabilities lack clean φ-irrelevant perturbations, and behavioural evidence underdetermines the best-explanation judgement.
- The account is illustrated with LLMs only; application to other architectures (RL agents, multi-module systems) requires adapting the "trying" test.
- Operationalising CAMA depends on knowing the deployment environment for ecological validity, which may be uncertain or unspecified.

**Other categories:**
- *validity:* Directly informs construct validity (face, convergent, divergent, ecological) and identifies contamination/memorisation as threats to valid capability inference.
- *generalization:* Deployment-specific ability claims and ecological validity connect test scores to deployment claims; memorisation exemplifies a generalisation failure.
- *reliability:* Reliable performance across queries is a core desideratum of capability possession, but reliability alone is insufficient without the non-coincidence condition.