# Judging LLM-as-a-Judge (Zheng et al., 2023)

**What kind of evidence:** Empirical study with controlled and crowdsourced human evaluation data.

**Key claims:**
- GPT-4 as a judge matches human preferences at 85% agreement (non-tie), exceeding human-human agreement (81%).
- All tested LLM judges exhibit position bias, verbosity bias, and limited math/reasoning grading ability; GPT-4 is most robust.
- Swapping answer positions and requiring consistency mitigates position bias; reference-guided grading reduces math grading failure from 70% to 15%.
- Traditional benchmarks like MMLU fail to distinguish aligned chat models from base models; preference-based benchmarks do.
- Fine-tuning an open model (Vicuna-13B) on arena votes yields 85.5% non-tie agreement with humans, showing promise as a cheaper judge.

**What the advisor should take from it:**

*scoring:*
- Three judge modes—pairwise comparison, single-answer grading, reference-guided grading—have trade-offs: pairwise is more sensitive but scales quadratically; single-answer is scalable but less discriminative; reference-guided is essential for math/reasoning.
- For multi-turn evaluation, display full conversations in a single judge prompt; splitting turns causes the judge to misreference prior answers.
- Few-shot judge examples raise GPT-4 consistency from 65% to 77.5% but cost 4× more and may introduce new biases.

*reliability:*
- Always run pairwise comparison twice with swapped positions; declare a tie on inconsistency. This directly addresses the strong first-position bias seen across all judges.
- Verbosity bias is real: a "repetitive list" attack fools GPT-3.5 and Claude 91.3% of the time but GPT-4 only 8.7%.
- Even when an LLM can solve a problem independently, providing candidate answers can mislead its grading; chain-of-thought alone does not fully fix this.

*validity:*
- Agreement with human gold standard is the core validity argument; GPT-4's 85% non-tie agreement on MT-bench and 87% on Chatbot Arena support its use as a proxy.
- GPT-4 single-answer grading agrees ~95% with GPT-4 pairwise, indicating a stable internal rubric that generalizes across scoring modes.

*constructs:*
- "Human preference" in open-ended, multi-turn dialogue is a distinct construct from core knowledge; aligned models improve on preference benchmarks without MMLU gains.
- MT-bench's 8 categories (writing, roleplay, extraction, reasoning, math, coding, STEM, humanities) operationalize this construct across two turns.

*generalization:*
- No single benchmark determines model quality; combine capability-based and preference-based benchmarks for comprehensive evaluation.

**Caveats:**
- Study emphasizes helpfulness, largely neglecting safety/harmlessness. Multiple quality dimensions are collapsed into one metric.
- Position-bias tests use near-identical answers—a hard case—so real-world bias may be less severe than reported consistency rates suggest.
- Fine-tuned Vicuna judge results are preliminary, tested on a limited model set.

**Category changes:** Added reliability, validity, constructs, generalization beyond the initial "scoring" suggestion; judge prompt design fits under scoring rather than elicitation.