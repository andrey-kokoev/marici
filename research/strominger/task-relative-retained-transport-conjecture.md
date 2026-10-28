# Task-relative retained transport: conjecture and test

## Conjecture tested

A full retained state together with an independently specified transport task determines a unique admissible next operation. The task states what changes or remains fixed, without naming an operation sequence or stage count.

Stronger extension: one fixed global task generates seven-stage presentations and quarter-chart handoffs without an imposed schedule.

Falsifier: the same retained state and the same task admit two distinct next operations satisfying every declared constraint.

## Tasks defined before matching operations

The [task contract](contracts/retained-transport-task-selection.v1.json) defines a common requirement:

> Advance the realization origin by one, preserve species, retain all five coefficients through invertible transport, and preserve the required next-occurrence overlap.

It then specifies three geometric variants:

1. **Advance realization:** no further geometric condition.
2. **Reread fixed carrier:** keep the same geometric primitive.
3. **Propagate across a face:** move to a distinct primitive across a complete shared face.

The matcher uses origin, species, occurrence identities, coefficients and cell incidence. It does not select by operation name. Native operation names are reported only after matching.

## Concrete result

Test all24 ordered seed markings, both at the initial P state and after a retained PN transition:48 source states total.

| Source family | Number of sources | Advance realization | Fixed carrier | Across a face |
|---|---:|---:|---:|---:|
| P |24|1|1|0|
| N, phase-compatible marking |8|2|1|1|
| N, other marking in fixed subdivision |16|0|0|0|

Each number in the last three columns is the number of admitted next operations per source.

For the eight ambiguous N states, both reader advance and NN phase advance satisfy the **same** broad task. Their sources include identical full coefficient vectors, nonempty PN histories, retained P and N packets, external contexts, frames and assembly witnesses.

Both outputs have the same species, origin increment and even the same full coefficient vector. They differ in geometric carrier and contextual vertex identities. Both can be extended by NE to a certified E exit, with all retained packets able to reach an exit and no unwitnessed contact.

Thus the broad task has eight explicit counterexamples. The checker also verifies24 viable P continuations, for40 certified continuations overall.

## Availability is not uniqueness

In this native fixed subdivision, the eight N markings supporting either phase operation are exactly those whose C1/C2 reference pair has squared barycentric distance4: it is the selected octahedral diagonal. The remaining16 have no matching phase advance. This is a checked classification of these source fixtures, not a claim of frame covariance under an independently transported subdivision.

A task can therefore be unavailable, uniquely realizable, or multiply realizable. Specifying a task does not automatically select a next operation.

## Surviving restricted result

For every tested source where the task is available, explicitly distinguishing **rereading the same carrier** from **propagation across a face** selects a unique next operation.

This supplies a precise missing geometric requirement for these cases. It is not yet a theorem for arbitrary retained assemblies, nor an intrinsic choice between the two tasks. A separate selection policy could choose between admissible operations; its existence is not refuted, but it is not implied by the stated broad task.

Do not infer the stronger global extension: all three tested tasks preserve species, so none alone generates P/E exchange or a seven-stage clock.

## Reproduction

```sh
node research/strominger/checkers/check_retained_transport_task_selection.mjs
```

**58 named checks passed.** [Receipt](results/retained-transport-task-selection.json) contains48 complete sources, task matches, eight same-source/same-task counterexamples,40 certified continuations and source hashes. Native source rules are unchanged.

Previous results: [intrinsic-selector falsifier](intrinsic-retained-selector-conjecture.md), [native FCC end-to-end binding](native-fcc-end-to-end-binding.md), [global28-stage conjecture](global-28-stage-pe-fibration-conjecture.md).
