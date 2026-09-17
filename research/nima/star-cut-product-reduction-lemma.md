# Reduction of face-star cut vertices to smaller common flip graphs

## Lemma

Let `Q` be a face of a common-tree complex and cut along `Q` into regions `P_1,...,P_r`. The facet graph of the star of `Q` is the Cartesian product

\[
G_Q\cong G_1\square\cdots\square G_r,
\]

where `G_i` is the common flip graph for the induced order pair on `P_i`.

For a facet `F=(F_1,...,F_r)`, `F` is a cut vertex of `G_Q` only if exactly one factor `G_j` has more than one vertex and `F_j` is a cut vertex of `G_j`.

## Proof

The product decomposition follows from restriction and gluing: a flip preserving `Q` occurs in exactly one cut region.

If all factors are singletons, the product is a singleton and has no relevant deletion obstruction. Suppose at least two factors, say `G_a,G_b`, each contain an edge. Remove one product vertex `F`. Given any two remaining product vertices `X,Y`, change coordinates one at a time along factor paths. If the resulting coordinate path would pass through `F`, detour in the other nontrivial factor by one edge, pass the dangerous coordinate value while the auxiliary coordinate differs from `F_b`, and then return. Hence the deleted product remains connected. Additional factors do not affect the argument.

If exactly one factor `G_j` is nontrivial, all other coordinates are fixed and the Cartesian product is canonically `G_j`. Deleting `F` disconnects the product exactly when deleting `F_j` disconnects `G_j`.

## Consequence

Every simultaneous non-cut obstruction in a face-star is inherited from a cut vertex in a strictly smaller common-tree flip graph on one polygonal region.

Thus the arbitrary-n preservation theorem reduces to a lower-dimensional graph statement:

> The regional component chosen by the global deletion rule must never be a cut vertex of the corresponding smaller common flip graph.

This removes arbitrary face-stars from the induction. Only whole common flip graphs on smaller polygons need to be controlled.

## Degree decomposition

For a facet containing `Q`, flips preserving `Q` are exactly regional flips, so its star degree is the sum of its regional degrees. Equivalently, the number of unavailable regional flips is additive over regions. This is the quantity compared by the maximal-free-ridge rule, apart from channels of `Q`, whose preservation status is common to every facet of the star.

A complete proof now needs a tie-safe minimum-degree theorem for common flip graphs: the deterministic minimum-degree component selected by the channel order must be non-cut. General graphs do not satisfy this, but the obstruction has now been reduced from all links and suffixes to this specific class of smaller common flip graphs.
