# Triangle vertex actions do not extend as pointed seed-loop transport

## Actual prior actions reused

`check_seed_edge_action_extension.py` runs and imports g and h from the existing `check_seed_cycle_response_transport.py`. On the common four-state carrier A,B,C,D, these are

    g=(A B C), h=(A D B).

They describe global cyclic vertex permutations. They are not yet holonomies of based traversals. This distinction matters before factoring them into edge actions.

## Pointed extension test

Test an S4 equivalence on each supplied directed edge, requiring it to send that edge's marked source vertex to its marked target. There are six such permutations for each edge. Let x,y,z,u,v,w denote AB,BC,CA,AD,DB,BA respectively.

Endpoint compatibility forces

    (z*y*x)(A)=A,
    (w*v*u)(A)=A.

But g(A)=B and h(A)=D. Consequently z*y*x=g and w*v*u=h are impossible under these conditions. The checker exhausts all 6^3 pointed assignments for each triangle and confirms the contradiction. In general, a composite of pointed comparisons along a closed path preserves its base mark; this argument is not specific to numerical weights.

This is an obstruction to this common-carrier, vertex-marked interpretation, not a proof that no fiber-valued or differently marked transport exists. Different fiber semantics would require an explicit source adapter. Nor does the result invalidate g,h as global permutations or their noncommuting response calculation.

## Unpointed control and genuine remaining freedom

If the condition mapping source marks to target marks is removed, extensions are easy. Choose arbitrary x,y,u,v in S4 and define

    z=g*(y*x)^-1,
    w=h*(v*u)^-1.

Every choice yields the two requested products. Hence there are 24^4 labelled extensions in this unpointed model. The checker tests two choices that produce different AB-BA loop responses with different fixed-point counts. Those loop responses cannot be related by base-frame conjugation.

Thus dropping endpoint compatibility does not merely remove a notation issue: it permits distinct additional loop data not fixed by the two triangle products. No such choice is source-selected here.

## Structural correction

The prior cut-response calculation remains a valid comparison of ordered GLOBAL VERTEX ACTIONS. It must not be promoted silently to sequential transport along the primitive seed arrows. In particular, a triangle successor permutation advances one slot/vertex around a triangle; traversing a complete endpoint-returning triangle is a different operation.

Before another arbitrary-cut construction, the source must identify the transported fiber, its marked value and the action assigned to a traversal, as distinct from the cyclic successor extracted from the triangle's record. The existing native pointed-comparison interface makes this obligation explicit; no native filler satisfying the failed assignment was constructed.

## Source-carrier follow-up: six occurrence slots

`record4-spectral-promotion.md` explicitly locates its cyclic operator on the original packet-occurrence coefficient slots, not the vertex A. The natural full-tour analogue is therefore the successor on its six retained occurrences. `check_seed_typed_execution.py` now tests that combinatorial operator for BOTH tours.

For each tour, the next slot's source equals the current slot's target. Each successor is one six-cycle, and its sixth power is identity with no earlier return. In the fixed six-edge ordering the two successors differ; the actual seed swap intertwines them. Within one execution, each primitive edge occurs once, so these edge indices identify the slots; replay must still retain fresh event IDs separately.

There is no deterministic vertex map f with source(next(slot))=f(source(slot)) across all six slots. At A the two outgoing occurrences require successor-source values B and D; at B they require A and C. This holds for both tours. The earlier unique four-vertex routing obtains determinism only by selecting one outgoing edge per vertex and omitting AB and BA.

Thus a full-support successor needs occurrence/context information that a four-vertex state alone discards. This is a concrete carrier requirement, not another missing sign convention.

Its coefficient permutation has characteristic polynomial t^6-1 and a one-dimensional fixed subspace. It must not be identified with the prior simultaneous pair of triangle short-half-phases: that operator has characteristic polynomial (t-1)^2*(t^2-t+1)^2 and a two-dimensional fixed subspace. Matching six-step return does not match representations. Nor does the six-cycle's permutation return erase an executed six-event history.

This identifies a valid combinatorial slot carrier, but not a native physical fiber or per-edge transport law. Advancing its successor as physical time remains an additional interpretation. Both tour choices are still retained rather than selected.

## Verification

    python research/nima/checkers/check_seed_edge_action_extension.py

Fresh pass includes the imported prior response/rung checks, exhaustive pointed negative controls, explicit unpointed factorizations and the nonconjugate extra-loop control. No physical law or Agda theorem was added.
