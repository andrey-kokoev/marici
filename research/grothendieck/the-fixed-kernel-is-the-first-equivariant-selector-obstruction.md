# The fixed kernel is the first equivariant-selector obstruction

## Exact classification

For an equivariant surjection `B:X->Y`, any two equivariant right inverses differ by an equivariant map from `Y` into `ker B`. Therefore the space of equivariant selectors is affine over

\[
\operatorname{Hom}_G(Y,\ker B).
\]

Reciprocal averaging proves existence from any finite splitting, but it proves uniqueness only when this intertwiner space vanishes.

## Minimal hostile pair

Take `B=[1,0]` and let the output carry the even reciprocal representation.

If the hidden kernel is odd, averaging sends every selector `K_alpha=(1,alpha)^T` to `K_0`. Symmetry removes the hidden gain.

If the hidden kernel is even, every `K_alpha` is already equivariant. Two cutoff levels may choose `K_a0` and `K_a1`; with identity refinement their exact commutator is

\[
\begin{pmatrix}0\\a_0-a_1\end{pmatrix}.
\]

It is invisible to the boundary map but obstructs compatible descent.

## Consequence

The first source calculation is not an operator-norm estimate. It is the reciprocal representation decomposition of the boundary-null chain space. If

\[
\operatorname{Hom}_G(Y_N,\ker B_N)=0
\]

at every cutoff, finite selector uniqueness follows and refinement compatibility becomes much more rigid. If a fixed kernel component survives, modular sewing must supply additional contraction data on that component; equivariance alone cannot choose it.

## Disposition

When source cutoff objects are materialized, compute the plus/minus decomposition of `ker B_N` and the dimension of `Hom_G(Y_N,ker B_N)` before searching for selectors. A nonzero fixed intertwiner sector is the earliest exact obstruction and the location where Voevodsky's representative-change 2-cell is required.
