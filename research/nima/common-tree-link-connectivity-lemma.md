# Link connectivity and initial coadmissibility of common-tree complexes

## Statement

Let `K(alpha,beta)` be a nonempty common-tree complex. For every face `Q` of `K`, the facet graph of the star of `Q`—facets containing `Q`, adjacent when they differ by one channel—is connected.

Consequently, every facet `F` of a nontrivial `K(alpha,beta)` is coadmissible relative to all other facets.

## Cut decomposition

A face `Q` is a common noncrossing set of channels. Cutting the labelled disk along all channels in `Q` produces polygonal regions `P_1,...,P_r`. Both cyclic orders induce an order pair `(alpha_i,beta_i)` on each region after every cut boundary is represented by a new common cut label.

A common tree containing `Q` is uniquely equivalent to a tuple

\[
(T_1,\ldots,T_r),\qquad
T_i\in K(\alpha_i,\beta_i),
\]

because restriction gives the tuple and gluing the regional trees to `Q` gives the inverse. A single flip preserving `Q` changes exactly one component. Therefore the facet graph of the star of `Q` is the Cartesian product of the facet graphs of the nontrivial regional common-tree complexes.

## Connectivity proof by induction

Induct on the number of labels.

For polygons with at most four labels, every nonempty common-tree complex has one facet or an immediately connected facet graph.

Assume connectivity for all smaller polygons. If `Q` is nonempty, every nontrivial region cut out by `Q` has fewer labels than the original polygon. Each regional factor is nonempty because a chosen facet containing `Q` restricts to a facet in that factor. By induction every regional facet graph is connected. A Cartesian product of connected graphs is connected. Hence the star facet graph of every nonempty face `Q` is connected.

For `Q` empty this argument does not reduce the polygon size, so it does not independently prove connectivity of the whole common-tree complex. Whole-complex connectivity remains a separate input. It is exhaustively verified through nine points. The conclusion below only needs nonempty intersections `Q`.

## Coadmissibility consequence

Fix a facet `F` and another facet `G`. Put `Q=F intersection G`. Since `F` and `G` are distinct facets of equal cardinality, `Q` is a proper face; when `Q` is nonempty, star connectivity provides a flip path from `F` to `G` through facets containing `Q`. The first step changes one channel, producing a facet `H` such that

\[
Q\subseteq F\cap H,
\qquad |F\cap H|=|F|-1.
\]

Thus `F intersection G` is contained in a shared ridge of `F`.

If `Q` is empty, it is contained in every shared ridge. Provided `K` has more than one facet and its facet graph is connected, `F` has at least one neighboring facet, so the condition again holds.

Therefore, assuming whole-complex facet connectivity, every facet is coadmissible relative to the complete set of other facets.

## Exact remaining gap

This proves coadmissibility before deletions. It does not show that coadmissibility survives an arbitrary partial deletion, because the retained facets containing `Q` may cease to be connected. To complete the shelling theorem one needs an ordering whose every suffix preserves star connectivity for all faces. The deterministic peel-shelling computations show such suffix connectivity through `n=9`; proving it for arbitrary `n` is the remaining hereditary-ordering lemma.
