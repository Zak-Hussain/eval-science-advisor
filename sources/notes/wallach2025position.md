# GenAI Evaluation as Social Science Measurement (Wallach et al., 2025)

**What kind of evidence:** Position paper grounded in social science measurement theory.

**Key claims:**
- Evaluating GenAI systems is a social science measurement challenge because the concepts to be measured are abstract and contested, resembling concepts social scientists have measured for decades.
- A four-level framework—background concept, systematized concept, measurement instruments, measurements—separates conceptual debates (what and why) from operational debates (how); the ML community typically conflates these.
- Validity is a single, overarching concept concerning evidence for particular interpretations and uses of measurements, and must be re-interrogated whenever instruments are used in new contexts.
- Seven lenses of validity—face, content, convergent, discriminant, predictive, hypothesis, consequential—each provide different evidence; without a systematized concept, they are not well defined.
- Human annotators cannot be assumed to be validated measurement instruments or "ground truth" without evidence their annotations align with the systematized concept.

**What the advisor should take from it:**

*constructs:*
- Before building any eval, systematize the concept: narrow the background concept into an explicit definition specifying what will be measured and why, drawing on relevant discipline literature.
- Define constituent concepts and specify whether the relationship between observable phenomena and the concept is definitional or causal.
- Involve stakeholders with different perspectives in systematization to surface contested meanings.

*validity:*
- Use all seven lenses throughout the measurement process—face, content, and consequential validity especially inform conceptual debates; all seven inform operational ones.
- Content validity has two facets: substantive (alignment with specified observable phenomena) and structural (alignment with specified relationships among them).
- Validity is context-dependent; re-interrogate before deploying instruments in new contexts.
- When comparing judge LLM annotations to human annotations, first verify humans align with the systematized concept before treating agreement as evidence of convergent validity.

*scoring:*
- Define indicators (variables reflecting observable phenomena) and aggregation functions that mirror the relationships specified during systematization before writing annotation guidelines or judge prompts.
- LLM-as-a-judge systems need annotation guidelines derived from the systematized concept, not just high-level instructions with few-shot examples; validity must be interrogated, not assumed.

**Caveats:**
- No empirical validation of the framework itself; it is adapted from political science measurement theory (Adcock & Collier, 2001; Messick, 1987).
- Full adoption requires significant time, resources, and organizational support; authors acknowledge partial adoption is still valuable.
- Determining what "sufficiently valid" means has no universal answer; higher-stakes uses demand higher standards of evidence.

**Category changes:** Added scoring: the paper gives concrete guidance on indicator design, aggregation functions, and LLM-as-a-judge guidelines. Dropped elicitation: not discussed.