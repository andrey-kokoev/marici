# Common-tree shellability: proof status after reduction

## Proved

1. Common-tree amplitudes have arbitrary-n cut/glue factorization.
2. Every proper nonempty facet subset of an associahedral sphere has a free ridge.
3. Iterative free-ridge deletion can continue to one facet.
4. Reverse deletion is a shelling exactly when every deletion is coadmissible.
5. Coadmissibility follows from connectivity of every retained face-star.
6. Deleting a facet preserves all star connectivities exactly when it is non-cut in every star containing it.
7. Every face-star factors as a Cartesian product of smaller common flip graphs.
8. A vertex can cut such a product only when exactly one factor is nontrivial and its regional coordinate is a cut vertex in that smaller factor.

## Falsified

1. Arbitrary free-ridge peeling need not reverse to a shelling; an exact six-point counterexample is recorded.
2. Maximal free-ridge count plus connected face-stars does not imply simultaneous non-cut behavior for arbitrary associahedral subcomplexes; an exact six-point counterexample is recorded.
3. A fixed lexicographic facet order is not a universal shelling order; it fails beginning at five points.

## Exhaustively certified

For all cyclic-order pairs through nine points, the selected deterministic peeling sequence is coadmissible and reverses to a shelling. At ten points it survives 5,000 deterministic stress-test orbits. The exact simultaneous non-cut condition has been checked directly through seven points.

## Unproved statement

The remaining assertion is:

> For every retained suffix arising from the deterministic common-tree peeling algorithm, the selected facet restricts in every one-factor face-star to a non-cut vertex of that smaller common flip graph.

No proof of this assertion has been obtained. The preceding reductions do not imply it, and the corresponding implication is false for general associahedral subcomplexes. Claiming the shellable-ball theorem at arbitrary n would therefore be unsupported.

## Next executable attacks

1. Exhaust the simultaneous non-cut condition at eight and nine points using bitset star graphs.
2. Search all 181,440 ten-point order orbits for the first deterministic-step obstruction.
3. Replace the degree-based selector by a recursively defined selector that explicitly chooses a non-cut regional coordinate.
4. Prove termination of that recursive selector by induction on cut-region size.

The fourth route is the most likely route to an actual arbitrary-n proof; it changes the algorithm rather than trying to prove a false general principle about maximal free-ridge degree.
