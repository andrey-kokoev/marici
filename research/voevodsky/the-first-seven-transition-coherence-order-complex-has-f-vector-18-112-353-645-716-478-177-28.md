# The first seven-transition coherence order complex has f-vector `(18,112,353,645,716,478,177,28)`

## Dependency poset

The seven transition labels are

\[
A,J,P,C,T,E,F
\]

with generating relations

\[
A<J,
\quad A<C,
\quad J<T,
\quad C<T,
\quad P<T,
\quad P<E,
\quad T<F,
\quad E<F.
\]

Their transitive closure contains 13 strict relations.

## Order-ideal lattice

Let

\[
\mathcal I=J(\mathsf P)
\]

be the distributive lattice of downward-closed subsets of the transition poset. A vertex of the canonical coherence triangulation is an order ideal: it records a set of operations that can already have been performed without violating typing.

There are

\[
\boxed{|\mathcal I|=18}
\]

such vertices.

Their rank distribution by number of completed operations is

\[
\boxed{
(1,2,4,4,3,2,1,1)
}
\]

for ranks `0,...,7`.

## Simplices as chains

A `k`-simplex is a strict chain of `k+1` order ideals

\[
I_0\subsetneqI_1
\subsetneq
\cdots
\subsetneqI_k.
\]

This identifies shared faces automatically: a chain is counted once regardless of how many maximal ordering chambers contain it.

Exhaustive exact enumeration gives

\[
\boxed{
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=
(18,112,353,645,716,478,177,28).
}
\]

Thus one full coherence complex contains

\[
\boxed{
18+112+353+645+716+478+177+28
=2527
}
\]

nonempty simplices.

## Maximal chambers

A maximal chain starts at the empty ideal, adds one admissible transition at a time, and ends at the full ideal. It contains eight vertices and defines a `7`-simplex.

The number of maximal chains is

\[
\boxed{f_7=28,}
\]

agreeing with the independently enumerated 28 linear extensions.

## Euler characteristic

The alternating sum is

\[
\boxed{
18-112+353-645+716-478+177-28
=1.
}
\]

This is expected: including the empty and full operation states makes the order complex a cone/ball-like coherence resolution rather than a sphere.

## Proper-part complex

Removing the empty and full ideals gives the proper-part order complex. Its nonzero f-vector is

\[
\boxed{
(16,79,179,208,121,28).
}
\]

Its maximal simplices have dimension five because the two endpoint vertices have been deleted from each full chain. Its Euler characteristic is also `1` for this poset; the proper part still has a cone point arising from the unique rank-six ideal immediately below the final filler.

Therefore this proper-part complex is not the boundary sphere of a generic seven-dimensional polytope. The final filler relation makes it contractible.

## Interpretation of dimensions

The dimensions have the following coherence meaning:

- vertices: admissible intermediate operation states;
- edges: admissible comparisons;
- triangles: homotopies between two-step presentations;
- tetrahedra: homotopies between triangular homotopies;
- higher simplices: higher associativity/interchange coherence;
- 7-simplices: complete admissible orderings of all seven transitions.

The tetrahedral inner fillers are the `645` three-simplices, not the 28 maximal chambers. Thus “inner filler count” depends on whether one means tetrahedral 3-cells or complete 7-dimensional ordering chambers.

## Consequence for the earlier counts

The provisional number

\[
2(8+2\cdot28)+28=156
\]

counts conductor states and maximal chambers only. It is not the total number of simplices.

A single coherence plane, modeled by the full order complex, has 2527 simplices after shared-face deduplication. But the total two-polarity construction cannot yet be obtained by multiplying 2527, because the planes and inner filler share:

1. the conductor axis;
2. endpoint and source vertices;
3. lower-dimensional commuting faces;
4. possibly the entire polarity-fixed subcomplex.

The correct total must use simplicial pushouts and inclusion--exclusion.

## Required gluing data

Let

\[
K_1^+,
K_2^+,
K_1^-,
K_2^-,
H
\]

be the four polarized coherence planes and shared inner filler. The total complex is schematically

\[
\mathcal K=
K_1^+
\cup
K_2^+
\cup
K_1^-
\cup
K_2^-
\cup H.
\]

For every dimension `d`, its f-vector requires

\[
f_d(\mathcal K)
=
\sum_i f_d(K_i)
-
\sum_{i<j}f_d(K_i\cap K_j)
+
\cdots.
\]

Until the intersection subcomplexes are specified, neither 156 nor `5 times 2527` is the total cell count.

## Reproducibility

The exact enumeration is implemented in

- `temp/count_coherence_f_vector.py`

which prints:

- the transitive relation count;
- number of order ideals;
- full f-vector;
- proper-part f-vector;
- maximal-chain count;
- Euler characteristics;
- rank distribution.

## Disposition

For the current seven-transition dependency model, one coherence order complex is completely counted:

\[
\boxed{
(18,112,353,645,716,478,177,28).
}
\]

The next combinatorial step is to define the intersection diagrams of the two coherence planes and the polarity-fixed inner filler. Their simplicial pushout will determine the actual total f-vector and settle whether the inner structure is shared once or doubled.
