# Password-locked models for stress-testing capability elicitation (Greenblatt et al., 2024)

**What kind of evidence:** Empirical methods paper introducing password-locked models as a controlled tool to evaluate fine-tuning-based elicitation.

**Key claims:**
- Password-locked models—trained to imitate a strong policy when a password is present and a weak policy otherwise—let you test whether elicitation methods recover hidden capabilities without the password.
- SFT on very few high-quality demonstrations (1–8 for generation tasks; ~512 for MMLU) recovers most locked capabilities.
- SFT unlocking generalizes across domains: fine-tuning on one subdomain unlocks performance on others, even with one password per domain.
- With only reward signals, RL methods (expert iteration, iterated DPO) recover most capabilities, but success depends on weak-policy quality—very weak base policies fail to explore.
- Models locked from scratch require 2–4× more unlocking data than SFT-locked models but still unlock with modest data.

**What the advisor should take from it:**

*elicitation:*
- Password-locked models offer a controllable testbed: create hidden capabilities by construction, then measure how well your method recovers them without the trigger.
- Even simple RL (expert iteration, best-of-64 filtering) can bootstrap from weak outputs to near-full capability if the weak policy produces enough signal; plan for exploration failure when base competence is very low.
- Few-shot SFT on 1–8 high-quality examples may suffice for generation tasks; classification needs hundreds.

*validity:*
- Prompting-only evaluations may underestimate capabilities that fine-tuning would reveal; use fine-tuning-based elicitation as a complementary validity check.
- Weak-to-strong generalization can cause SFT on mediocre demonstrations to exceed the demonstrator's own performance, complicating inferences about minimum demonstration quality.

*generalization:*
- Elicitation transfers across domains: unlocking on one domain often unlocks others, so narrow demonstrations may suffice to assess broader capabilities—but MMLU shows domain-dependent variation, so don't assume it.

**Caveats:**
- Password-locked capabilities may be more "salient" than naturally hidden ones, potentially making unlocking easier than in real settings.
- The weak policy is trained to imitate the strong policy, providing RL exploration signal that may be absent with genuinely unknown capabilities.
- Experiments use 7B-scale models; frontier-scale applicability is untested.

**Category changes:** Added validity and generalization; kept elicitation as primary.