# Defining Model Capabilities (Harding et al., 2024)

**What kind of evidence:** Theory paper drawing on philosophy of ability modals, illustrated with ML examples.

**Key claims:**
- A model has a capability to φ iff there exist background conditions where, when its output is best explained by being directed at φing (it "tries"), it reliably succeeds (CAMA, Definition 10).
- Successful performance need not evidence capability: memorisation, surface heuristics, or luck yield correct outputs coincidentally (non-coincidence).
- Capability (competence) is invariant across background conditions; performance is not—changing prompting or sampling changes performance without changing capability.
- For fair inter-model comparison, background conditions should be optimised per model, but only conditions where the model genuinely "tries" count; gerrymandered conditions exploiting non-φ mechanisms are excluded.
- RLHF typically changes propensity to try harmful capabilities, not the underlying capability; the conditional "if it tries, it succeeds" is largely unchanged.

**What the advisor should take from it:**

*constructs:*
- CAMA defines capability as requiring reliable success under conditions where the model is genuinely trying, operationalised via a behavioural test: sensitivity to φ-relevant input perturbations and insensitivity to φ-irrelevant ones (Definition 11).
- Distinguish generic capabilities (not time-indexed) from deployment-specific capabilities (what the model can do given the specific conditions it will face in practice).

*validity:*
- Operationalisation gaps between benchmarks and deployment are unavoidable; benchmarks concretise one construct but cannot define the capability.
- Ecological validity requires similarity between evaluation and deployment environments; a construct valid for one evaluation may be invalid for another.
- Non-coincidence is a core validity threat: high scores may reflect memorisation or heuristics rather than the target capability. The perturbation test provides a concrete check.

*elicitation:*
- Background conditions (prompting, sampling, tokenisation, content filters) are evaluation variables, not part of the model; they profoundly affect whether capabilities are manifested.
- Few-shot prompting can be understood as getting the model to "try" the right task; chain-of-thought affects success probability given trying—distinct mechanisms.
- Content filters can "mask" a capability: the model retains the generic ability but lacks the deployment-specific ability.

*generalization:*
- Capability claims are often deployment-specific; a model succeeding via memorisation lacks a generic capability but may have a specific one where it never sees novel queries.
- For inter-model comparison, use model-specific background conditions optimised to elicit the capability, but exclude gerrymandered conditions via the "trying" test.

**Caveats:**
- The behavioural test for "trying" cannot distinguish intensionally different but extensionally identical capabilities (e.g., genuine understanding vs statistical sensitivity).
- Illustrated with LLMs only; extension to RL agents or multi-module systems is left to future work.
- Teleological explanation of opaque models is underdetermined by behavioural evidence; interpretability may be needed but specifics are unspecified.

**Category changes:** Added validity and generalization; the first pass only suggested constructs and elicitation.