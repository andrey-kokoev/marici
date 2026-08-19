# 1036 — The Six Loaded Walls Are Not the Facets of One Associahedron

## Primary regularization type

The generalized Pochhammer construction regularizes one loaded associahedron
using its actual face poset.  A codimension-(k) face contributes the product
of the (k) inverse boundary factors of the facets meeting there.  Thus its
edge and corner terms require one coherent facet local system, not merely six
available factors with the right determinant.

This is the construction in Section 4.1 of Mizera,
*Combinatorics and Topology of Kawai–Lewellen–Tye Relations*,
arXiv:1706.08527.

## Two distinct six-tuples

The native chamber hexagon of Entries 979 and 1015 has half-monodromy
transports

\[
(B_{34},B_{24},X,B_{34}^{-1},B_{24}^{-1},X^{-1}).
\]

Hence its total holonomy is

\[
1,
\]

and its three opposite pairs are inverse.

The loaded boundary complex instead has occurrence monodromies

\[
(M_1,M_2,M_2,M_3,M_4,M_4),
\]

where

\[
\begin{aligned}
M_1&=(ZA_2)^2,&
M_2&=(ZA_2B_{24})^2,\\
M_3&=(A_3/Z)^2,&
M_4&=(A_3B_{34}/Z)^2.
\end{aligned}
\]

Their generic product is

\[
\boxed{
M_1M_2^2M_3M_4^2\neq1.
}
\]

Moreover, the loaded multiset contains no inverse pair.  No relabelling can
turn it into the facet monodromies of the native hexagon.

## Narrow result

\[
\boxed{
\text{the six loaded factors are not the six facets of one loaded
associahedron.}
}
\]

They are six occurrence-labelled tubular boundaries drawn from four source
walls, with two walls appearing twice.  Entry 1032's diagonal Pochhammer
cancellation is therefore valid locally at each occurrence, but it cannot be
promoted by simply declaring those six occurrences to be one hexagon's
facets.

This independently explains why Entry 1025 found that a rank-one
Koba–Nielsen local system on the hexagon cannot close all six loaded columns.

## Revised global object

The correct target is an occurrence-resolved Cousin/Čech diagram:

\[
\bigoplus_i \operatorname{Reg}_{D_i}
\Longrightarrow
\bigoplus_{i<j}\operatorname{Reg}_{D_i\cap D_j}
\Longrightarrow\cdots,
\]

where the repeated (M_2) and (M_4) occurrences remain distinct and corner
terms exist only for source-derived wall intersections.

The native chamber hexagon and this wall-occurrence diagram may later be
compared, but they must not be identified cell by cell.

## Next falsifier

Freeze the actual incidence graph among the four loaded source walls from the
source character blocks.  Construct only those codimension-two Pochhammer
terms whose wall intersections are present.  Test whether their Cousin
differential closes.  A surviving class is a genuine global comparison
extension; exactness closes the static loaded regularization without fitting
a hexagon.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_loaded_monodromy_type_gate.rs`;
- packet:
  `research/benincasa/string-six-point-loaded-monodromy-type-gate.json`;
- primary source:
  Mizera, arXiv:1706.08527, Section 4.1;
- allocator claim:
  `seqclaim-850cf35af361caed470f343f`.
- epistemic event:
  `ev-000000000655-5609554e-fc58-439b-b074-816a0e11b4d8`.
