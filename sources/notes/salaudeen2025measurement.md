# Measurement to Meaning: A Validity-Centered Framework for AI Evaluation (Salaudeen et al., 2025)

**What kind of evidence:** Position paper with conceptual framework, drawing on psychometrics, illustrated via case studies of GPQA and ImageNet.

**Key claims:**
- Validity in AI evaluation depends on the *claim* being made, not just the measurement or evaluation; the same evidence can support narrow claims but fail to support broad ones.
- Five forms of validity—content, criterion, construct, external, consequential—are each necessary, but which ones require active investigation depends on whether the claim targets a criterion (directly measurable) or a construct (abstract).
- When the measured object differs from the claim's object, criterion validity (predictive or concurrent) is essential for criterion-targeted claims; construct validity (structural, convergent, discriminant) is essential for construct-targeted claims.
- A nomological network—mapping relationships among constructs and their observable indicators—is critical for construct validity but is largely missing in current AI evaluation.
- Validity is iterative and never fully resolved; imperfect measurements can still support valid but narrower-scoped claims.

**What the advisor should take from it:**

*constructs:*
- Distinguish explicitly whether the claim targets a criterion (e.g., "accuracy on textbook linear algebra questions") or a construct (e.g., "mathematical reasoning"); this determines the evidence standard.
- Constructs gain meaning only through their relationships with other constructs and observables (a nomological network); claims about a construct cannot be validated in isolation.
- For construct-targeted claims, assess structural validity (does the test's internal structure match the construct's subskills?), convergent validity (does it correlate with other measures of the same construct?), and discriminant validity (does it fail to correlate with measures of unrelated constructs?).

*validity:*
- Before validating, articulate three components: the object of the claim, the claim itself, and the evidence; then assess the conceptual gap between evidence and claim.
- Use the decision tree (Figure 2): if measurement equals the criterion, content and external validity suffice; if measurement differs from the criterion, add criterion validity; if the claim is about a construct, add construct validity.
- Content and external validity must always be established; consequential validity should be assessed when evaluation results inform high-stakes decisions (e.g., EU AI Act risk classification).
- Table 4 provides concrete risks, investigation tools (expert review, red-teaming, factor modeling, stress testing, stakeholder audits), and evidence exemplars for each validity form.

**Caveats:**
- The framework is conceptual and illustrated with only two case studies; it is not empirically validated as a whole.
- Nomological networks for AI constructs are described as necessary but largely absent, making construct validity assessment currently very difficult in practice.
- Validity scoring in the case studies is subjective and explicitly described as iterative, not binary.

**Other categories:**
- **generalization:** External validity is treated as one of five core forms, covering whether results generalize across populations, settings, and time; risks include sample bias, temporal variability, and unrealistic testing conditions.
- **measurement-models:** Factor analysis and IRT are mentioned as tools for establishing structural and convergent validity, but not developed in depth.
- **reliability:** Noted only briefly—high measurement error undermines convergent validity.