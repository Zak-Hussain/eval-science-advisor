# Evaluating GenAI as Social Science Measurement (Wallach et al., 2025)

**What kind of evidence:** Position paper proposing a measurement-theory framework for GenAI evaluation.

**Key claims:**
- GenAI evaluation concepts (capabilities, behaviors, impacts) are abstract and contested, making them more like social science constructs than traditional ML metrics.
- A four-level framework—background concept → systematized concept → measurement instruments → measurements—should standardize the measurement process.
- Separating systematization (defining what is measured) from operationalization (how it is measured) is essential; conflating them, as ML practice typically does, causes conceptual confusion.
- Seven validity lenses (face, content, convergent, discriminant, predictive, hypothesis, consequential) should be used to interrogate validity throughout, not just post hoc.
- Without a systematized concept, there is no "ground truth," and validity lenses are not well defined; human annotators are not automatically validated instruments.
- Validity is context-dependent: instruments valid in one context may not be valid in another, so validity must be re-interrogated for new uses.

**What the advisor should take from it:**

*constructs:*
- Before building instruments, narrow the background concept into an explicit systematized concept that specifies how the construct connects to observable phenomena, including defining constituent concepts.
- Involve stakeholders with diverse perspectives in systematization so that decisions about which meanings are reflected are made transparently, not buried in instrument design.
- Specify relationships among observable phenomena (e.g., definitional vs. causal; whether multiple indicators are individually sufficient or jointly necessary).

*validity:*
- Use all seven lenses throughout systematization and operationalization, not just face validity; content, convergent, and consequential lenses are especially useful for conceptual debates.
- Do not treat human annotations as ground truth; first assess whether they align with the systematized concept before using them to interrogate convergent validity.
- Share the systematized concept alongside instruments and measurements so others can identify apples-to-oranges comparisons and interrogate validity themselves.
- Re-interrogate validity whenever instruments are reused in a new measurement context; "sufficiently valid" has no universal threshold and should be higher for high-stakes uses.

*Caveats:*
- The paper proposes a framework and illustrates it with hypothetical examples, not empirical validation of the framework itself.
- Full adoption is resource-intensive; the authors acknowledge partial adoption (at minimum separating systematization/operationalization and interrogating validity) is still valuable.
- The framework is adapted from Adcock & Collier (2001) and Messick (1987); its applicability to GenAI is argued by analogy, not demonstrated experimentally.

**Other categories:** *scoring*—discusses LLM-as-a-judge as a measurement instrument, emphasizing that annotation guidelines, aggregation functions, and model configuration are all instrument components requiring validity interrogation. *reliability*—notes that low inter-annotator agreement may reflect systematization problems rather than annotator error. *generalization*—predictive validity and context-dependence of validity directly address extrapolating from test scores to deployment claims.