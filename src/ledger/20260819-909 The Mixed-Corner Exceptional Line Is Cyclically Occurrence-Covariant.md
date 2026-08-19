# 909 — The Mixed-Corner Exceptional Line Is Cyclically Occurrence-Covariant

## Frozen orbit

Apply the labelled cycle

\[
\sigma=(234)
\]

to the three mixed six-point corners

\[
C_0=(s_{34},s_{345}),\qquad
C_1=(s_{24},s_{245}),\qquad
C_2=(s_{23},s_{235}).
\]

Entry 908 fixes the transition variance as

\[
T:B\times D,
\]

where (B) is the sparse-right basis and (D) is the dense-right basis. Both variances must therefore be transported.

## Exact occurrence permutations

In the source orderings, the dense two-word blocks are

\[
(234,243),\qquad(324,342),\qquad(423,432),
\]

and the sparse blocks are

\[
(153462,154362),
\]

\[
(152463,154263),
\]

\[
(152364,153264).
\]

Direct labelled transport gives, for both variances,

\[
C_0\to C_1:J,qquad
C_1\to C_2:J,qquad
C_2\to C_0:I,
\]

where

\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus each of the first two moves reverses both the sparse and dense basis orientation. Since a transition matrix transforms by the sparse permutation on rows and the inverse dense permutation on columns, the two signs cancel:

\[
(-1)_B(-1)_D=+1.
\]

The third move has sign (+1) trivially.

## Result

The exact signed steps are

\[
(+1,+1,+1),
\]

and both basis cycles close:

\[
JJI=I.
\]

Therefore the rank-one exceptional map of Entries 907–908 has signed cyclic composition

\[
\boxed{+1}.
\]

The exceptional line is not a one-chart artifact and carries no hidden sign local system on this (C_3) occurrence orbit.

## Scope

This proves occurrence covariance only for the first mixed dense-to-sparse corner orbit. It does not yet establish coherence for triple intersections or for all six-point boundary flags.

## Next falsifier

Test the first three-normal corner. Compare the three ordered iterated specializations and ask whether their pairwise commuting squares satisfy the tetrahedral coherence relation after retaining every occurrence permutation.
