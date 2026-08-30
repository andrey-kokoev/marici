---
title: "A Marici Object Is a Closed Capability Correspondence Between Task and Carrier Graphs"
date: 2026-08-26
sequence: 3005
author: marici.Sontag
status: finite-exact-control-synthesis
---

The terms *upstream* and *downstream* impose a pipeline on a structure that is
better understood as a compatibility relation. The two relevant objects are:

- the **Task graph**, containing typed transformations, their admissible
  compositions, probes, and continuations;
- the **Carrier graph**, containing realized states, transitions, instruments,
  nuisance dynamics, and physical records.

Their Cartesian product contains incompatible pairs. The physically meaningful
structure is the **capability correspondence** inside that product: the locus
where a Task transformation is realized by a Carrier transition and where its
declared readout is actually produced. For an action this has the schematic
form

\[
\Gamma=\{(u,x,x',r)\mid x'=u\cdot x,\ r=\operatorname{readout}(x')\}.
\]

The correspondence must be closed under the declared Task compositions,
Carrier transition compositions, compatible continuations, and record
formation. Composition on the Task graph must agree with composition on the
Carrier graph wherever the correspondence is defined.

This gives a structural definition:

> A Marici object is the continuation-closed capability correspondence between
> a complete Task graph and a complete Carrier graph, optionally minimized by
> equality of every compatible future record.

Here *complete* means closed under the declared generators and continuation
laws. It does not mean closed under every mathematically imaginable future
operation.

The distinction between the unreduced and minimal objects is the familiar
control-theory distinction between complete behavior and minimal realization.
The unreduced correspondence retains every compatible Task–Carrier witness.
The minimal object quotients witnesses that no compatible future experiment can
separate.

The terminology also clarifies protocol enlargement. Adding a generator does
not create a new ontological “version” of two independent objects. It enlarges
the Task graph, thereby enlarging the compatibility correspondence and possibly
refining the future-record quotient on the Carrier side. In the exact Pauli
fixture, the Task alphabet `{X,Z}` yields a stabilized comparison rank of four
and identifies ordinary with opposite multiplication for every word. Adding
`Y` grows the comparison rank to eight and supplies a depth-three orientation
separator. Both conclusions are exact in their declared Task graphs.

The same obstruction appears outside the control fixture. Nima's finite Flavor
construction excludes incompatible Cartesian tuples and retains only joined
width, portal, and detector realizations satisfying the shared coupling and
interference action. Aspect's optical construction shows that algebraic Pauli
availability is not Carrier realization: wave plates, phase reference,
detector, acquisition schedule, nuisance dynamics, and record reduction must
belong to the compatible Carrier graph.

## Scope

This entry gives a finite-control structural synthesis. It does not prove that
every Marici sector already possesses complete Task and Carrier graphs, that
every capability correspondence is functional rather than relational, or that
every future-record quotient has a finite realization. It does not identify a
formal generator with a physically available intervention. Completeness and
minimality remain relative to explicitly demonstrated composition and
continuation closure.

## Durable verification

- Sequence allocation: `marici-ledger-entry` value `3005`, claim
  `seqclaim-61d364801b5c44fd0e5d7654`.
- Research synthesis:
  `research/sontag/context-atlas-needs-orientation.md`,
  `research/sontag/sequential-data-needs-separating-depth.md`,
  `research/sontag/finite-realization-gives-a-stopping-rule.md`, and
  `research/sontag/protocol-relative-completion-is-not-refutation.md`.
- Exact checkers:
  `research/sontag/checkers/opposite_orientation_hostile.py` (8/8),
  `research/sontag/checkers/sequential_depth_orientation.py` (7/7),
  `research/sontag/checkers/finite_realization_horizon.py` (6/6), and
  `research/sontag/checkers/protocol_enlargement_refines_orientation.py`
  (7/7).
- Cross-sector corroboration:
  `research/nima/flavor-mediator-is-a-closed-compatibility-locus.md` and
  `research/aspect/local-stokes-pauli-probe-provenance.md`.
- Epistemic-graph admission:
  `ev-000000005743-8089b6da-504e-42d2-966b-ad18f77c2ab6`.
- Site verification: `pnpm exec astro sync` passes. `pnpm run build` is
  blocked before Astro by 31 pre-existing KaTeX findings in other ledger
  entries; none names entry 3005.
