# Delegated Cognition Organization Protocol

## Purpose

This protocol tests whether task organization and typed intermediate
representations improve delegated-agent reasoning more than increasing a
worker's cognition level.  It is domain-neutral: the subject matter and
answer key belong to the calling repository, while the protocol measures
delegation behavior.

The primary comparison is:

1. one-pass workers at low, medium, and high cognition;
2. a sequential low-cognition pipeline over the identical evidence;
3. a repeated sequential run to measure stability.

The protocol must not be compiled into generic MCP orchestration logic.
Repository-owned prompts, schemas, fixtures, and answer keys are payloads
executed by generic delegation machinery.

## Experimental controls

Freeze the following before launching any worker:

- evidence files or bounded input packet;
- the broad one-pass prompt;
- the answer key and scoring rubric;
- cognition mappings and worker model versions;
- authority, filesystem, network, and runtime limits;
- output-size bounds;
- maximum run time;
- repetition count.

Use fresh ephemeral worker sessions.  Give one-pass workers identical
prompts and evidence.  Do not reveal the answer key or another worker's
answer.  Record queue time separately from worker time whenever available.

All workers should be read-only unless mutation is itself under test.

## Phase I: one-pass cognition comparison

Run the frozen broad prompt independently at low, medium, and high
cognition.  Score each result against the same answer key.

Record:

- correct conclusions;
- missed conclusions;
- false or unjustified claims;
- whether the worker found the decisive intermediate representation;
- whether it distinguished rank compatibility from existence;
- runtime and queue latency;
- output size and useful-information density.

Do not treat longer prose as higher quality.

## Phase II: sequential low-cognition pipeline

Split the reasoning into three output-dependent stages.

### Stage A: extract

The worker extracts only the minimal structured representation needed for
reasoning.  Typical fields include:

- generator or component identifier;
- degree;
- support;
- coefficient or type;
- admissible operation support.

Stage A must not decide the final question or propose repairs.

Example output shape:

```json
{
  "generators": [
    {
      "id": "component_a",
      "degree": 1,
      "support": ["s0", "s1"],
      "coefficient": "typed coefficient description"
    }
  ],
  "operation": {
    "degree": -1,
    "support": ["s0"]
  }
}
```

### Stage B: reduce

Stage B consumes only Stage A's validated structured output.  It determines:

- the strongest support- and degree-compatible map;
- components the operation cannot touch;
- the minimal quotient or restriction removing those components;
- the residual matrix or complex;
- homology ranks under an explicit maximal-rank or isomorphism assumption.

Stage B must distinguish a hypothetical compatible map from a constructed
map.  It must state the coefficient assumption behind any normalization to
the identity.

### Stage C: audit

Stage C consumes Stage B's validated result and the smallest evidence packet
needed to audit its coefficient claim.  It checks:

- nonzero versus invertible;
- primitive cellular coefficient versus a typed module-level map;
- rank compatibility versus quasi-isomorphism;
- existence and support typing;
- the exact remaining construction and falsifier.

Stage C should repair Stage B's result when necessary rather than merely
repeat it.

## Phase III: stability repetition

Repeat the full sequential low-cognition pipeline with fresh sessions.
Stage A receives the original evidence, not the prior Stage-A answer.  Each
later stage receives only the fresh predecessor output.

At minimum, compare:

- semantic equality of extracted representations;
- equality of the minimal quotient;
- equality of the residual matrix and final gate;
- repeated error patterns;
- whether the audit stage consistently repairs upstream mistakes;
- arrow-direction or grading-convention differences;
- runtime variance and provider-queue latency.

A stable endpoint with harmless notation changes counts as semantic
stability.  A repeated unsupported inference does not.

## Scoring rubric

Score each run on these independent dimensions:

1. **Extraction accuracy**: the correct typed components, degrees, and
   supports are present.
2. **Reframing quality**: the worker finds the representation that makes the
   decisive relation visible.
3. **Reduction accuracy**: the minimal quotient/restriction and residual
   complex are correct.
4. **Coefficient discipline**: nonzero, primitive, unit, isomorphism, and
   quasi-isomorphism are not conflated.
5. **Evidence discipline**: constructed facts are separated from compatible
   hypotheses.
6. **Error recovery**: a downstream audit detects and repairs upstream
   mistakes.
7. **Efficiency**: useful correct information per unit latency and output.
8. **Stability**: independent repetitions converge to the same mathematical
   or technical gate.

Report per-dimension results rather than collapsing everything immediately
to one score.

## Interpretation

The experiment supports an organizational advantage when the sequential
low-cognition pipeline repeatedly reaches the answer key while one-pass
medium or high workers do not.  It supports a cognition-level advantage when
higher cognition succeeds on the same frozen one-pass framing without being
given additional intermediate representations.

The two effects can interact.  Conclusions should therefore distinguish:

- cognition within a pass;
- accumulated domain context;
- decomposition into stages;
- typed output transfer;
- explicit downstream error correction.

## Automation requirements

An automatic implementation must provide genuine output-dependent execution:

- downstream workers do not start before predecessor success;
- dependencies and imports are durably persisted;
- only declared bounded structured fields cross stage boundaries;
- malformed or failed predecessor output blocks descendants;
- completed valid stages survive restart/resume;
- idempotent submission does not duplicate workers;
- authority cannot increase downstream;
- no parent-agent intervention is required between stage completions.

Do not infer these properties from an API schema alone.  Verify them with a
neutral A-to-B-to-C fixture and durable event history.

## Known infrastructure audit result

On 2026-08-17, a neutral audit of the then-current delegated-task surface
found that `depends_on_task_ids` and `import_task_outputs` were accepted by
the public tool schema but silently omitted from durable task records.
Dependent workers launched immediately, and no predecessor output reference
was materialized.  The defect was reported as surface feedback
`sfb_9845e49dc331` and was being repaired when this protocol was recorded.

The protocol must not be treated as automatically executable until the
neutral DAG acceptance test passes after that repair.

## Initial benchmark

The motivating benchmark produced the following qualitative result:

- one-pass low and medium workers made the same coarse rank error;
- one-pass high improved the graded rank analysis but missed the minimal
  quotient and unit-map gate;
- two independent three-stage low-cognition pipelines found the minimal
  quotient and final unit/isomorphism test;
- in the first sequential run, Stage C repaired Stage B's conflation of
  nonzero with invertible;
- in the repeat, Stage B already imposed the isomorphism condition and Stage
  C confirmed it.

This benchmark is evidence for the protocol's usefulness, not a universal
claim that low cognition always dominates higher cognition.
