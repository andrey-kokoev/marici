# Coadmissible deletion is exactly reverse shelling

## Definitions

Let `K` be a finite pure simplicial complex with facets of cardinality `d+1`. For a facet `F` and a set `R` of other facets, call `F` **coadmissible relative to `R`** when

1. `F` shares at least one ridge with a facet in `R`; and
2. for every `G in R`, the face `F intersection G` is contained in a ridge `F intersection H` for some `H in R`.

Equivalently, the maximal faces of

\[
F\cap\bigcup_{G\in R}G
\]

all have cardinality `d`.

A deletion sequence `F_1,...,F_{m-1}` with survivor `F_m` is coadmissible when `F_i` is coadmissible relative to `{F_{i+1},...,F_m}` for every `i<m`.

## Lemma

The reverse order

\[
F_m,F_{m-1},\ldots,F_1
\]

is a shelling if and only if the deletion sequence is coadmissible.

## Proof

By definition, an ordering `H_1,...,H_m` of the facets of a pure `d`-dimensional simplicial complex is a shelling when, for every `j>1`,

\[
H_j\cap\bigcup_{i<j}H_i
\]

is nonempty and pure of dimension `d-1`.

Put `H_j=F_{m-j+1}`. At the stage when `H_j=F_i` is attached, the already attached facets are exactly

\[
F_m,F_{m-1},\ldots,F_{i+1}.
\]

Thus the shelling intersection is exactly

\[
F_i\cap\bigcup_{k>i}F_k.
\]

A subcomplex of the simplex `F_i` is nonempty and pure of dimension `d-1` precisely when every one of its maximal faces is a ridge of `F_i`. This is equivalent to requiring at least one shared ridge and requiring every intersection `F_i intersection F_k` to be contained in some shared ridge `F_i intersection F_l`. Those are exactly the two coadmissibility conditions. Applying this equivalence at every index proves both directions.

## Consequences

- Coadmissibility implies that `F_i` has a shared ridge. It is not the same as having a free ridge.
- A free ridge controls the boundary side of a deleted facet; shelling controls how that facet meets the retained side.
- Therefore the free-ridge lemma cannot by itself prove shellability.
- The exact remaining statement for common-tree complexes is:

> Every proper nonempty common-tree complex has a facet that is both removable along a free ridge and coadmissible relative to the remaining facets, and the remainder again has such a facet unless only one remains.

The deterministic computations through `n=9` and sampled at `n=10` certify such sequences. Proving the quoted existence statement at arbitrary `n` is now the sole combinatorial gap in the shellable-ball argument.
