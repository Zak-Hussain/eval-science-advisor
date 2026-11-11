<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# constructs

## GenAI Evaluation as Social Science Measurement (Wallach et al., 2025)

- Before building any eval, systematize the concept: narrow the background concept into an explicit definition specifying what will be measured and why, drawing on relevant discipline literature.
- Define constituent concepts and specify whether the relationship between observable phenomena and the concept is definitional or causal.
- Involve stakeholders with different perspectives in systematization to surface contested meanings.

## Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

- Distinguish capabilities (co-vary with demands/difficulty) from propensities (co-vary with incentives). Both are dispositions, not performances.
- Performance on a dataset is a manifestation of a disposition in a narrow context, not the disposition itself.

## Defining Model Capabilities (Harding et al., 2024)

- CAMA defines capability as requiring reliable success under conditions where the model is genuinely trying, operationalised via a behavioural test: sensitivity to φ-relevant input perturbations and insensitivity to φ-irrelevant ones (Definition 11).
- Distinguish generic capabilities (not time-indexed) from deployment-specific capabilities (what the model can do given the specific conditions it will face in practice).

## The “Everything in the Whole Wide World” Benchmark (Raji et al., 2021)

- Define constructs narrowly before benchmarking; “general-purpose” capability labels are too vague to operationalize in a single dataset.
- Avoid merging distinct constructs (e.g., linguistic form vs. world knowledge) under one benchmark without justifying why they should be measured together.
- Ground task selection in a theory of the target construct, not convenience or availability of data.

## Measurement to Meaning: A Validity-Centered Framework for AI Evaluation (Salaudeen et al., 2025)

- Distinguish criteria (directly measurable, e.g., "accuracy on physics MCQs") from constructs (abstract, e.g., "reasoning") before selecting evidence types.
- When validating a construct claim, require structural validity (does the test's internal structure match the construct's subskills?), convergent validity (correlation with other measures of the same construct), and discriminant validity (no correlation with unrelated constructs).
- Push for explicit nomological networks linking AI constructs to observables; without them, construct claims risk being unfounded.

## Measuring what Matters (Bean et al., 2025)

- Define the target phenomenon precisely and operationally before task design. If definitions are contested, use negative (apophatic) definitions to set boundaries.
- Identify if the phenomenon has sub-components and ensure they are measured separately to improve interpretability.

## Judging LLM-as-a-Judge (Zheng et al., 2023)

- "Human preference" in open-ended, multi-turn dialogue is a distinct construct from core knowledge; aligned models improve on preference benchmarks without MMLU gains.
- MT-bench's 8 categories (writing, roleplay, extraction, reasoning, math, coding, STEM, humanities) operationalize this construct across two turns.

## Emergent Abilities as Metric Artifacts (Schaeffer et al., 2023)

- "Emergent ability" as currently operationalised (sharpness + unpredictability under a chosen metric) may not correspond to a real capability discontinuity; the construct risks being an artifact of measurement choice rather than a property of the model family.

## Human Label Variation as Signal, Not Noise (Plank et al., 2022)

- Before designing an eval, distinguish genuine disagreement, subjectivity, multiple-plausible-answer cases, and annotation errors—these call for different measurement approaches.
- For many language tasks, "acceptability" may be a more appropriate construct than "correctness" when no ground truth exists.

## LLM Psychological Profiles are Measurement Artifacts (Meyer et al., 2026)

- Be cautious when attributing human-like psychological traits to LLMs using borrowed psychometric instruments; LLMs may lack stable dispositions for these constructs, or the instruments may lack validity for LLMs.

## Revealing the structure of language model capabilities (Burnell et al., 2023)

- Evaluate LLMs against three core latent constructs—reasoning, comprehension, and language modeling—rather than treating capability as a single monolithic trait.
- Recognize that task format does not dictate construct: question answering, summarization, and sentiment analysis all loaded onto the same "comprehension" factor.

## General Scales for AI Evaluation (Zhou et al., 2025)

- Define demands on ratio scales with absolute zero so levels are commensurate across dimensions; abilities can then exceed current rubric ceilings.
- Include extraneous dimensions—atypicality, volume, unguessability—to separate genuine cognitive demands from contamination, amalgamation, and funnelling confounders.

## Observational Scaling Laws (Ruan et al., 2024)

- A small set of latent capability dimensions (general, reasoning, code) underlies most standard benchmarks, suggesting benchmark batteries are not measuring independent constructs.
- PC-1 serves as a broad "general capability" factor with high dynamic range across 5 orders of magnitude, unlike single benchmarks that saturate or stay at chance.
