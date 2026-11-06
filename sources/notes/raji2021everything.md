# The "Everything in the Whole Wide World" Benchmark (Raji et al., 2021)

**What kind of evidence:** Position paper with illustrative case studies of ImageNet and GLUE/SuperGLUE.

**Key claims:**
- Benchmarks framed as measuring "general" capabilities (e.g., general language understanding, general-purpose object recognition) suffer construct validity failures because they are finite, subjective, and context-bound, yet presented as universal.
- Task selection in "general" benchmarks is arbitrary rather than theory-driven: GLUE tasks came from an informal survey of ~30 colleagues; ImageNet categories were lifted from WordNet subtrees with little consideration of suitability.
- GLUE conflates distinct constructs—linguistic competence, world knowledge, and commonsense reasoning—under one "language understanding" label, though these differ in scope and testability.
- De-contextualized reporting hides geographic and cultural bias: 45% of ImageNet images sourced from the US, only 1% from China; offensive categories found in the "person" subtree.
- Competitive SOTA-chasing distorts research agendas and enables misleading marketing claims (e.g., Microsoft calling SuperGLUE performance a milestone "toward general AI").
- Aggregate benchmark scores can mask harmful subgroup performance disparities, as later demonstrated in commercial facial recognition audits.

**What the advisor should take from it:**

*constructs:*
- Define the construct explicitly and independently of the dataset; do not let the dataset implicitly become the construct definition.
- Avoid conflating multiple distinct capabilities under a single benchmark label—separate linguistic competence from world knowledge, commonsense reasoning, etc.
- Justify task/category selection with reference to a theory of the target capability, not convenience or precedent.

*validity:*
- Benchmark scores do not automatically support claims beyond the specific tasks and data they contain; restrict claims to what was actually tested.
- The Common Task Framework was designed for tightly scoped practical tasks—extending it to abstract "general performance" claims is an invalid generalization.
- Report context, scope, and known limitations of the dataset rather than presenting it as neutral and universal.
- Check whether aggregate scores mask differential performance across socially salient subgroups.

**Caveats:**
- The paper is a position paper, not an empirical study; case studies are illustrative rather than systematic.
- Focus is limited to dataset-based benchmarks; gameplay/RL environments receive little attention.
- The alternative evaluation methods are surveyed briefly but not empirically compared against benchmarking.

**Other categories:** `scoring` (briefly: aggregate metrics like average accuracy across tasks are criticized as meaningless when task meanings differ); `generalization` (briefly: claims of general capability from benchmark performance are the central invalid inference the paper critiques).