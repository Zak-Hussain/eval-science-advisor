# Judging LLM-as-a-Judge (Zheng et al., 2023)

**What kind of evidence:** Empirical study and methods paper.

**Key claims:**
- GPT-4 used as a judge matches human preferences with over 80% agreement, on par with human-human agreement.
- LLM judges exhibit position bias (favoring the first answer), verbosity bias (favoring longer, repetitive answers), and self-enhancement bias (favoring their own outputs).
- LLM judges struggle to grade math and reasoning questions, often being misled by provided incorrect answers despite knowing the correct solution when asked separately.
- Swapping answer positions and only declaring a win if consistent improves evaluation reliability.
- Reference-guided grading (providing the judge's independently generated answer as a reference) significantly reduces math grading failures (from 70% to 15%).

**What the advisor should take from it:**
*scoring:*
- Pairwise comparison is best for discerning subtle differences between models, while single-answer grading (e.g., 1-10 scale) is more scalable and also matches human preferences well.
- To mitigate position bias, call the judge twice with swapped answer positions and only declare a winner if consistent; otherwise, default to a tie.
- For math/reasoning tasks, use reference-guided grading: ask the judge to solve the problem independently first, then provide that solution as a reference when grading the models.
- Display full multi-turn conversations in a single prompt, as splitting turns across prompts causes the judge to mislocate prior context.
- Fine-tuning an open-source model as a 3-way classifier on human vote data offers a cheaper, consistent alternative to proprietary API judges.

**Caveats:**
- The study focuses on helpfulness and largely neglects safety, honesty, and harmlessness.
- MT-bench human labels come from 58 expert labelers (mostly graduate students), which may not represent broader crowdsourced preferences.
- Self-enhancement bias is difficult to isolate in a controlled study; the authors cannot definitively conclude it exists based on their observational data.
- GPT-4 judge agreement with humans is notably higher (~100%) when model performance gaps are large, but drops to ~70% for closely performing models.

**Other categories:**
- *validity:* Demonstrates that LLM-as-judge scores serve as a valid proxy for human preferences, achieving high agreement with controlled expert and crowdsourced votes.
- *reliability:* Identifies specific response biases (position, verbosity) threatening consistency and provides empirical mitigation strategies.
- *generalization:* Introduces MT-bench and Chatbot Arena, arguing they complement traditional benchmarks like MMLU by evaluating open-ended, multi-turn alignment.
- *elicitation:* Highlights that multi-turn context must be presented as a full conversation to elicit accurate grading behavior from the judge.