# Same-grade-first global Morse preflight

## Question

Does reserving same-grade positive-dimensional cancellations before vertex--edge component mergers repair the failed global greedy matching?

## Claim boundary

This is a bounded cell-level test in distinct-shell multiplicative degrees two through five at grade 20000. It does not yet prove global synchronization or allow algebraic combinations of cells.

## Revised constructor

Run two phases.

1. Process positive dimensions upward. Match each unmatched \(k\)-cell to the least unmatched incident \((k+1)\)-cell of exactly the same grade.
2. After all positive-dimensional reservations, match unmatched vertices to remaining incident edges.

The first phase protects square, cube, and higher fillers from being consumed indirectly by lower-dimensional choices. The second phase accounts for connected-component deaths.

## Bold conjecture

The revised rule pairs every positive-dimensional cell, leaves exactly one unmatched vertex per final connected component, preserves grade in every positive-dimensional pair, and has no closed gradient path.

## Rivals

1. Lexicographic same-grade choices still leave positive cells unmatched.
2. The matching census is correct but gradient cycles remain.
3. Cell-level matching is impossible even though algebraic persistence has only zero-length positive bars.

## Test

Apply the unchanged cell enumeration and face posets from the failed preflight. Record unmatched positive cells, critical vertices versus absolute \(H_0\), cross-grade positive pairs, and directed cycles after reversing matched arrows. Retain the first failure in every sector.

## Computed result

The priority reversal removes every cross-grade positive pair and every gradient cycle in all four sectors. Its same-grade pair counts reproduce the persistence counts exactly: degree two has 73 edge--square pairs; degree three has 317 edge--square and 35 square--cube pairs; degree four has 336, 52, and 2 successive pair counts.

The second phase still fails because local greedy vertex choices do not construct a rooted forest matching. It leaves 24, 247, 235, and 134 edges unmatched in multiplicative degrees two through five. In each sector the excess critical-vertex count over absolute \(H_0\) equals the number of leftover edges.

## Disposition

The full bold conjecture is rejected, but the failure is now confined to component pairing. Same-grade positive-dimensional reservation is acyclic and matches the algebraic persistence census. The next constructor should retain this first phase and replace greedy vertex matching by a rooted spanning-forest orientation of the remaining edge graph.
