# Exact shedding criterion for a common channel

Let `K=K(alpha,beta)` be a pure common-tree complex with facets of cardinality `d+1`, and let `v` be a common channel.

## Proposition

The following are equivalent:

1. the simplicial deletion `del(v,K)` is pure of dimension `d`;
2. no facet of `link(v,K)` is also a facet of `del(v,K)`;
3. for every common tree `T` containing `v`, there is a common tree `T'` not containing `v` with
   \[
   T\setminus\{v\}\subset T';
   \]
4. in every common tree containing `v`, the channel `v` can be flipped to another channel while remaining common-planar.

When these conditions hold, `v` is a shedding vertex in the Provan--Billera recursion.

## Proof

The deletion consists of all faces avoiding `v`. Its possible maximal faces are of two forms:

- full facets of `K` that avoid `v`, of cardinality `d+1`;
- faces `T\setminus{v}` obtained from facets containing `v`, of cardinality `d`.

Thus deletion is pure of dimension `d` exactly when every face of the second kind is contained in a facet of the first kind. This is the equivalence of (1)--(3).

Because all facets have cardinality `d+1`, a facet `T'` containing `T\setminus{v}` and avoiding `v` has the form

\[
T'=(T\setminus\{v\})\cup\{v'\}.
\]

The two trees share a ridge and differ by the unique polygonal flip across that ridge. This proves equivalence with (4).

## Revised arbitrary-n target

The local existence statement needed for vertex-decomposability is therefore concrete:

> Every nonsimplex common-tree complex, and every deletion/link state generated recursively from it, contains a channel that is common-flippable in every surviving tree containing that channel.

The corrected exhaustive checker verifies this statement recursively through `n=8`. It tests the actual deletion purity condition by requiring every link facet to extend to a same-dimensional facet avoiding the selected channel.

## Potential induction

For an original common-tree complex, the link of `v` factors over the two polygons cut out by `v`. Failure of shedding means that at least one linked regional tuple has no alternative completion after removing `v`; geometrically, the two regions cannot be rejoined through the opposite diagonal of the quadrilateral adjacent to `v` while preserving `beta`-planarity.

A proof should choose an extremal common channel for which this obstruction is impossible, likely using an endpoint of an inclusion-minimal `alpha`-interval that is also a `beta`-interval. This translates the topological problem into an interval-overlap lemma for two cyclic orders.
