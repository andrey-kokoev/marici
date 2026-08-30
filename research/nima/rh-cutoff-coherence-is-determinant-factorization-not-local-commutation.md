# RH cutoff coherence is determinant factorization, not local commutation

## Decisive refinement

The relative feedback increment from adding a source layer is generally path-dependent. Requiring prime additions to contribute identical local Schur increments in both orders is too strong and would reject ordinary coupled block systems.

What is path-independent is the total elimination of a fixed complete block.

For nested internal state sets, write

\[
q_X=B_X^*A_X^{-1}B_X.
\]

Along either path from (X) to (Z), the increments telescope to (q_Z-q_X). Individual edge increments can differ because the first added state changes the effective environment in which the second is eliminated.

The exact three-state checker exhibits

\[
(q_{01}-q_0,\ q_{012}-q_{01})
\ne
(q_{02}-q_0,\ q_{012}-q_{02}),
\]

while both pairs have the same sum.

## The categorical cell

The square does not commute edge by edge. Its two composite eliminations are compared by the associativity of Schur complementation, equivalently by determinant factorization:

\[
\det
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix}
=
\det(A)\det(C-B^*A^{-1}B).
\]

Eliminating two internal layers in either legal order gives two factorizations of the same full determinant. Their comparison is canonical only when both paths arise from the same complete source block and use the same determinant-line normalization.

This changes the RH target. Primewise scalar increments need not commute. Instead:

1. each prime or prime-power addition must extend one common labelled colligation;
2. every intermediate Schur complement must be defined on its declared domain;
3. the two elimination orders must factor the same full determinant section;
4. the comparison cell must preserve endpoint, seam, primitive, square, and archimedean typing;
5. the completed determinant section must agree with the endpoint Evans section up to an independently derived nowhere-zero unit.

## DPC verdict

Strict local-increment commutation is rejected.

Bare telescoping is insufficient because any endpoint difference telescopes algebraically.

The surviving claim is stronger and more structural: a source-derived full colligation generates both paths, and the determinant functor generates their coherence cell. The unresolved RH-bearing bridge is no longer the coherence of elimination itself. It is whether the endpoint Evans readout is the determinant section of that same colligation without being installed as its scalar block by hand.

## Finite falsifier

For two labelled additions, construct the complete joint block before either elimination. Compare:

- sequential Schur elimination in both orders;
- direct elimination of the joint block;
- the independently derived scalar endpoint increment.

Failure of either sequential path to equal direct elimination disproves block coherence. Agreement of all eliminations but disagreement with the endpoint Evans increment disproves the zero-to-dagger promotion.
