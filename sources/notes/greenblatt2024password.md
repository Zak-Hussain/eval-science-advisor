# Password-Locked Models for Testing Elicitation (Greenblatt et al., 2024)

**What kind of evidence:** Empirical methods paper introducing a controlled testbed and stress-testing fine-tuning-based elicitation.

**Key claims:**
- Password-locked models — fine-tuned to show a capability only when a password appears in the prompt and to imitate a weaker model otherwise — provide a systematic way to evaluate elicitation methods.
- SFT on very few high-quality demonstrations (as few as 1 for generation tasks) often recovers most hidden capabilities; MMLU requires a few hundred.
- SFT-based elicitation generalizes across domains: demonstrations from one domain unlock capabilities in others, even those locked with different passwords.
- RL methods (expert iteration, iterated DPO) recover most capabilities when only rewards are available, but fail when the weak policy is too weak for exploration.
- Models locked from scratch require 2–4× more data to unlock than those locked via SFT, but are still unlockable.

**What the advisor should take from it:**

*elicitation:*
- Use password-locked models as a stress-test: lock a capability with a password, then attempt recovery without it to validate any elicitation method.
- Fine-tuning on a handful of demonstrations is often enough; prompting alone should not be assumed adequate.
- RL can work without demonstrations but needs a baseline policy that occasionally produces correct outputs; very weak base policies cause exploration failure.

*validity:*
- Password-locked models let you test whether elicitation recovers capabilities present-but-hidden, rather than introducing new ones.
- The paper distinguishes "possessing" a capability from "exhibiting" it under default prompting — useful for framing what an eval measures.

*generalization:*
- Cross-domain unlocking is strong: fine-tuning on one domain recovers performance on others, including those locked with different passwords. Narrow elicitation coverage does not imply narrow capability bounds.

*constructs:*
- Provides an informal account of possessing vs exhibiting capabilities and defines "hidden" relative to a party lacking the eliciting prompt.

*scoring:* Not a focus; uses binary correctness and embedding-similarity thresholds only.

*reliability:* Reports standard error over 3 seeds; no systematic reliability analysis.

*measurement-models:* Not addressed.

**Caveats:**
- Password-locking creates a simple conditional that may be easier to reverse than naturally hidden capabilities; real sandbagging could be harder to elicit.
- The weak policy is fine-tuned to imitate the strong policy, providing exploration signal that may be absent in realistic scenarios.
- Does not model deliberate developer deception or anti-elicitation countermeasures.

**Other categories:** none.