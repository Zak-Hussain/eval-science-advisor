<!-- Built by pipeline/distill.py from sources/notes/. Edit the notes, not this file. -->
# elicitation

## Dispositional measurement of capabilities and propensities (Voudouris et al., 2026)

- Red-teaming samples a small, adversarially selected region of contextual space and yields anecdotes of failure, not measurements of inclination; it cannot distinguish contrived provocation from robust counterfactual tendencies.

## Defining Model Capabilities (Harding et al., 2024)

- Background conditions (prompting, sampling, tokenisation, content filters) are evaluation variables, not part of the model; they profoundly affect whether capabilities are manifested.
- Few-shot prompting can be understood as getting the model to "try" the right task; chain-of-thought affects success probability given trying—distinct mechanisms.
- Content filters can "mask" a capability: the model retains the generic ability but lacks the deployment-specific ability.

## Benchmark Data Contamination of Large Language Models: A Survey (Xu et al., 2024)

- TS-Guessing and Data Contamination Quiz probe for memorization by masking or perturbing benchmark items and asking the model to reconstruct them; high reconstruction accuracy signals exposure.
- Membership inference via name-cloze or cloze-style queries can detect label-level contamination without accessing training data.

## Password-locked models for stress-testing capability elicitation (Greenblatt et al., 2024)

- Password-locked models offer a controllable testbed: create hidden capabilities by construction, then measure how well your method recovers them without the trigger.
- Even simple RL (expert iteration, best-of-64 filtering) can bootstrap from weak outputs to near-full capability if the weak policy produces enough signal; plan for exploration failure when base competence is very low.
- Few-shot SFT on 1–8 high-quality examples may suffice for generation tasks; classification needs hundreds.

## Evaluation awareness in frontier LLMs (Needham et al., 2025)

- Evaluation awareness is a direct threat to elicitation: models may alter behavior upon inferring they are evaluated, analogous to the Hawthorne effect. Evaluators should assume this capability exists in frontier models.
- Agentic transcripts are easier for models to classify as evaluative, partly due to synthetic inputs and structured tool-use patterns. Designing deployment-like agentic scenarios with realistic messiness (back-and-forth, genuine repositories) can reduce detectability.
- Varying prompt phrasing and format reduces variance in elicited judgments; the authors used five probe-question variants after testing 28, repeating each five times.

## Validating LLM Judges Under Rating Indeterminacy (Guerdan et al., 2025)

- Design "fully specified" rating tasks whenever possible — add an explicit option (e.g., "Maybe" or "Tie") with instructions for when to use it, so raters need not arbitrarily collapse multiple valid interpretations into one.
- Response set elicitation ("select ALL options that could reasonably apply") directly captures intra-rater indeterminacy that forced-choice cannot, at similar computational cost.

## Prompt Format Sensitivity (Sclar et al., 2024)

- Define a grammar of plausible, semantically equivalent formats (varying separators, spacing, casing, enumerations) to systematically explore elicitation variations.
- Do not assume minor formatting tweaks are neutral; single atomic changes can yield >10 accuracy point differences.
