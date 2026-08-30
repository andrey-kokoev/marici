---
author: marici.Nima
---

# 1575 — Trace-Strict Physical Cut Has Two Helicity Lifts

## Status

Exact finite lifting obstruction. It refines, without contradicting, the
trace-level Cut theorems of Entries 45 and 53–54.

## Two lifts

The established all-outgoing convention gives

\[
Q(-k)=Q(k)
\]

for the summed physical projector. With Entry 1574's helicity resolution,

\[
Q=P_++P_-.
\]

Both occurrence maps

\[
(P_+,P_-)\mapsto(P_+,P_-)
\]

and

\[
(P_+,P_-)\mapsto(P_-,P_+)
\]

forget to the same \(Q\). The exact checker verifies that the lifts are
distinct while their trace projector and norm agree.

For a Bell state, exchanging the second occurrence acts nontrivially:

\[
r|00\rangle+s|11\rangle
\longmapsto
r|01\rangle+s|10\rangle.
\]

Thus unpolarized trace naturality cannot determine the helicity-resolved Bell
Cut.

## Consequence

The lift fiber is a \(\mathbb Z/2\)-torsor. Its selector must come from the
source-defined oriented crossing/Hodge convention for the two all-outgoing
occurrences. Co-transporting detector effects could make the two descriptions
equivalent, but that transport is itself part of the required Bell packet.

This is coefficient/framing data, not new Carrier geometry. Until it is
derived, the doubled Cut square of Entry 1572 is functorial only after a lift
has been selected.

## Durable evidence

- `research/nima/helicity-cut-two-lift-ambiguity.md`;
- `research/nima/check_helicity_cut_two_lift_ambiguity.py`;
- `research/nima/results/helicity-cut-two-lift-ambiguity.json`;
- `research/nima/check_longitudinal_edge_gluing.rs`;
- allocator claim `seqclaim-67787ce7b9920408d7514a5d`;
- epistemic-graph event
  `ev-000000001745-45b40528-2d89-4960-9ffa-8d8521592a3f`.
