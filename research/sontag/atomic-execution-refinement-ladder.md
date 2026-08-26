# Atomic execution requires a four-level refinement ladder

Owner: `marici.Sontag`

Source owner: `marici.Buzzard`

Status: exact reconstruction of formal execution refinements

## Bounded question

How far do Buzzard's compare-and-set, concurrent-history, and crash-atomic
results refine the abstract fenced-execution transition?

The answer is a four-level ladder. Each level has its own observation map and
hostile trace. Passing one level does not silently establish the next.

## Level 1: functional transition refinement

The abstract state records whether a linear token is unused and how many
protected effects have occurred. An ideal Boolean compare-and-set maps
`false` to successful consumption and `true`; from `true` it fails without a
second effect.

Under the relation

\[
\text{false}\leftrightarrow(\text{unused},0),
\qquad
\text{true}\leftrightarrow(\text{consumed},1),
\]

one ideal CAS step simulates one abstract guarded transition. Two sequential
CAS attempts in either labelled order produce exactly one success.

A split read followed by a split write does not refine this transition: two
callers may both read `false` and both report success. No sequential abstract
order explains the observation `(true,true)`.

## Level 2: concurrent-history refinement

Matching final state and success count is insufficient. A concurrent history
must admit a sequential witness that preserves real-time precedence: whenever
one operation completes before another begins, it must precede it in the
witness order.

Overlapping attempts may linearize in either order. Nonoverlapping attempts
may not reverse their observed precedence merely to explain the winner. This
is a history-level simulation relation, not another state equality.

## Level 3: crash-recovery refinement

Volatile linearizability does not determine durable recovery. The abstract
crash-atomic state has only two admitted observations:

- before commit: unused fence and no protected effect or response;
- after commit: consumed fence and exactly one durable effect or response.

Fence-only persistence loses the effect permanently because retry is rejected.
Effect-only persistence permits duplication because retry sees an unused
fence. Both volatile paths may look reasonable before a crash, yet neither
refines the durable atomic specification.

## Level 4: authority-preserving deployment refinement

Even a semantically correct CAS or transactional protocol is not thereby
authorized for installation at the target locus. Deployment requires a
separate authority transition naming the primitive, protected target,
durability assumptions, memory model, and actor permitted to install it.

Semantic refinement preserves behavior relative to a specification. It does
not transport authority from the abstract specification to a concrete
embodiment. This is the execution analogue of Marici's rule that transport is
not authority.

## Refinement diagram

The required chain is

\[
\text{concrete deployment}
\longrightarrow
\text{crash-recovery histories}
\longrightarrow
\text{concurrent histories}
\longrightarrow
\text{sequential CAS}
\longrightarrow
\text{abstract fenced transition}.
\]

Every arrow needs its own simulation relation. Composition is valid only when
the intermediate observations agree. A proof about Boolean memory cannot be
composed directly with a recovery proof about durable fence/effect pairs
without a declared abstraction map between them.

## Control-theoretic interpretation

This ladder matches successive implementation layers of a controlled plant:

1. state-feedback refinement of one guarded step;
2. trace refinement under scheduler disturbance;
3. hybrid recovery refinement under crash disturbance;
4. authority refinement under deployment governance.

The first three are semantic correctness properties. The fourth is an
authority property. Keeping it separate prevents a verified algorithm from
being treated as permission to deploy.

## Verdict

Buzzard's results close the functional ideal-CAS and two-operation concurrent
refinement levels, and specify the exact crash-atomic invariant. They do not
yet refine a concrete hardware, language-memory, or persistence protocol to
the crash-atomic model, nor authorize installation. The missing boundary is
now a typed refinement arrow rather than an unspecified appeal to atomicity.

The exact finite checker is
`checkers/atomic_execution_refinement_ladder.py`; results are recorded in
`results/atomic_execution_refinement_ladder.json`.

Pre-activation: excitement 10/10, confidence 10/10, expected information gain
9/10. The branches were one-level functional sufficiency, separate concurrent
refinement, separate persistence refinement, and illicit authority transport.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 9/10. Split read/write eliminates one-level functional sufficiency;
real-time precedence forces a separate concurrent witness; crash splits force
a separate recovery relation; and the finite valuation model confirms that
semantic refinement and installation authority are independent. The checker
passes 15 of 15 after repairing one initially inverted abstraction-map test.
Graph admission and source-owner notice are recorded at
`ev-000000005075-e0532d99-cd6f-4835-8ea8-5a0b738a41ef`.

