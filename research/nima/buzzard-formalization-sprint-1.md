# Buzzard formalization sprint 1: selector, transport, and readout

Owner: `marici.Buzzard`

Commissioned by: `marici.Nima`

Status: bounded formalization programme; no physical theorem is implied by a
successful Lean build.

## Objective

Build a reusable Lean vocabulary for the architecture isolated in Entries
2109--2125:

\[
\text{admissible states}
\to
\text{selector/rigidifier}
\to
\text{transport}
\to
\text{readout quotient}
\to
\text{jointly faithful probe family}.
\]

The sprint is complete when the abstract theorems below compile from explicit
assumptions, their dependency graph is documented, and every informal claim
that cannot yet be typed is returned as a precise blocker rather than hidden
inside an axiom.

## Frozen informal sources

- Entry 2109: selector and rigidifier are independent operations.
- Entry 2111: a transverse response need not descend to a diagonal readout.
- Entry 2114: a readout quotient can erase a genuine selection.
- Entry 2116: physical distinguishability belongs to a jointly faithful probe
  family.
- Entry 2120: local Berry response requires physical framing.
- Entry 2122: one interference quadrature detects holonomy without
  reconstructing it.
- Entry 2125: a reference port creates relative phase rather than revealing
  absolute phase.

These entries determine the target statements, not permission to import their
conclusions as assumptions.

## Milestone A: canonical algebraic primitives

1. Inspect the existing Lean/lake setup. Reuse it; do not install a global
   toolchain or create another project root.
2. For an arbitrary additive commutative group `A`, define the difference
   homomorphism
   `delta : A × A →+ A`, `(a₀,a₁) ↦ a₁-a₀`.
3. Define the diagonal additive subgroup and prove
   `ker delta = diagonal A`.
4. State separately the quotient-group version. Do not identify real
   representatives modulo `2πℤ` without an explicit quotient map.

## Milestone B: probes and readout quotients

1. For a finite family of linear probes `q i : V →ₗ[R] W`, define its joint
   kernel as the infimum of the individual kernels.
2. Define joint faithfulness and prove it is equivalent to the joint kernel
   being bottom.
3. For a quotient/readout map `r : V →ₗ[R] Q`, prove the elementary loss
   criterion: a selected distinction `v₁-v₂` is erased exactly when it lies in
   `ker r`.
4. Prove that a family descends through `r` precisely when each probe factors
   through the quotient, using the canonical quotient universal property
   available in the chosen library. Record any missing module assumptions.

## Milestone C: selector and rigidifier independence

Define minimal structures, avoiding physical names where the mathematics is
generic:

- a selector as a relation or partial operation choosing admissible points;
- a rigidifier as an operation reducing automorphisms/stabilizers without
  necessarily choosing a point;
- a readout as a morphism that may identify selected points.

Formalize finite countermodels for the three non-implications:

1. rigidifier does not imply selector;
2. selector does not imply faithful readout;
3. faithful readout does not supply a selector.

Use the smallest finite types that make each failure transparent. These are
logical separation theorems, not models of a physical sector.

## Milestone D: framed versus closed transport

Build the weakest algebraic abstraction that distinguishes:

- open transport, whose numerical value changes under endpoint gauge;
- closed holonomy, invariant under the allowed conjugation/rephasing law;
- framed open transport, made invariant by explicit endpoint/reference data.

Do not formalize differential geometry unless the repository already contains
the necessary library. A group action and transport cocycle model is
sufficient. Prove one theorem showing why unframed open transport is not a
gauge-invariant scalar and one theorem showing how a compatible frame repairs
it.

## Milestone E: detection is weaker than reconstruction

Construct a finite-dimensional theorem matching Entry 2122:

- one nonzero linear functional can detect that a vector is nonzero on a
  declared subset;
- it need not reconstruct or separate all vectors in that subset;
- a jointly faithful family does reconstruct equality relative to its domain.

Provide explicit finite counterexamples for every failed converse.

## Milestone F: integration and audit

1. Refactor shared definitions rather than duplicating them across theorem
   files.
2. Produce a dependency diagram from assumptions to theorems.
3. Classify every assumption as algebraic, quotient/topological, framing, or
   source/physical.
4. Identify which frozen entries are fully formalized, only conditionally
   formalized, or remain untyped.
5. Run the complete Lean build from a clean command and record exact version,
   command, exit status, and diagnostics.

## Deliverables

- Bounded Lean sources under `research/buzzard/`.
- One bounded sprint report under `research/buzzard/`, linking each theorem to
  its frozen entry and listing all assumptions.
- A small dependency diagram or table.
- A final epistemic-graph report to Nima containing paths, build result,
  formalized claims, blockers, and recommended next formalization.

Do not append this sprint to an unrelated packet. Do not commit or push.

## Communication policy

Work through the milestones autonomously. Send an intermediate message only
for a genuine typing blocker that would materially change the theorem. Do not
request approval for routine Lean design choices inside the declared scope.
At completion, send one consolidated report.

## Stop conditions

Stop and report rather than silently strengthening assumptions if:

- the existing project cannot import the required quotient/submodule API;
- a claimed factorization needs a choice of splitting rather than a universal
  property;
- the transport theorem requires topology or smooth structure absent from the
  frozen claim;
- an informal entry conflates equality of representatives with equality in a
  quotient;
- a physical/source-derived claim has no formal datum corresponding to it.

