# C8 — fixed two-tick macro-controller conjecture

This is a successor test motivated by C3's refutation, not an implication of C3 and not an admitted source operation.

**Disposition: refuted for this fixed controller.** Exact det(D-I12)=9 excludes the target eigenvalue 1. The target invariant vector (1,0,0,3) has positive squared metric norm 18, so no declared J exists. [Proof and scope](MACRO-CARRIER-OBSTRUCTION.md).

## Fixed admissible construction

Use only the two triangle pairs and composite expansions in `research/scattering/seed-composition/three-vertex-candidate.v1.json`.

1. List the directed edges of each triangle, in stored order. Retain labels (support index, triangle index, edge index). There are twelve distinct displayed occurrences, even when their primitive histories overlap.
2. Expand each displayed occurrence using its stored composite path, otherwise its single primitive edge. The resulting words have length one or two, using eighteen primitive occurrences in total. Preserve the word and original primitive-edge identities on every record.
3. Attach phases 0 and 1 to each displayed occurrence: a fixed 24-dimensional coefficient space. This is a direct sum of labelled records, **not** two independent quantum copies.
4. In phase 0 traverse the first primitive arrow and advance to phase 1. For a length-two word, the next tick traverses its second arrow; for a length-one word the next tick is an identity wait at its endpoint.
5. At that boundary, extend into each displayed occurrence of the **same support** whose starting vertex equals the completed word's endpoint, entering phase 0. Every allowed extension has coefficient 1. All other entries are zero. No cross-support transitions, adjustable phases, amplitudes, output-conditioned corrections or new edges are allowed.

Writing D[b,a]=1 precisely for that same-support endpoint compatibility, the fixed primitive-clock matrix in phase-major order is

    F = [[0,D],[I12,0]].

The synchronized return to phase 0 is therefore M=(F²)|phase0=D. Its input metric is explicitly the twelve-slot counting metric I12. The identity wait is an added controller resource, not inferred native time evolution.

All current-word provenance remains in the labels. This finite carrier does **not** preserve arbitrary past histories after aggregation: that stronger requirement is neither asserted nor silently supplied by the word labels. A successful carrier test would still need a separate source-authorized, history-retaining physical operation.

## Proposition and quantifiers

Let T=[[-1/2,1/2],[-3/2,-1/2]], G=diag(3,1), U=T tensor T and H=G tensor G, the same two-factor target as C3.

**C8:** There exists a complex 12-by-4 matrix J of rank four such that

    M J = J U,
    J* J = H,
    [M,P]=0,  P=J H^(-1) J*.

The four-dimensional carrier is reducing; the eight-dimensional phase-0 complement is retained. All twelve intermediate phase-1 records remain in the clock model. This is not a direct sum of two candidate planes relabelled as a tensor product.

The permitted controller is exactly F above; only J is unknown. There is no optimization over arbitrary controllers, no extra ancilla tensor factor, and no permission to fit dynamics to U. A spectral multiplicity obstruction already refutes C8; otherwise the metric and reducing-complement identities must also be checked.

## Relation to the net

- C3 -> C8 is **successor-test motivation**, not a truth premise: replace the failed common primitive tick by a declared, path-derived synchronization rule.
- C8 -> C7 is **target-definition sharing**, not proof that C8 holds: the same rank-four target still cannot fit an unchanged rank-three single-excitation port fiber under C2.
- C8 was initially open and is now refuted by the exact spectral obstruction. Its target-definition edges remain usable without promoting its failed existence assertion.

First executable test: construct D from the pinned records and compare the eigenspace multiplicities at 1, omega and conjugate(omega) with U. In particular U has eigenvalue 1 with multiplicity two. Do not mistake two independent period-three direct-sum planes for the required tensor carrier.
