# The parameter-free prime-cell gate collapses from four identities to two covariances and one diagonal

## Fixed linear comparison

The completed theta wall and odd Wronskian columns determine

\[
Q=
\begin{pmatrix}
1/2&1/4\\
1/2&-1/4
\end{pmatrix}.
\]

Its determinant is

\[
-1/4,
\]

so the local comparison is invertible and has no adjustable coefficient.

The induced source quarter turn and reflection are

\[
F=
\begin{pmatrix}
0&-1/2\\
2&0
\end{pmatrix},
\qquad
P=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

They satisfy

\[
F^2=-I,
\qquad
P^2=I,
\qquad
PF=-FP.
\]

## Metric defect

Let

\[
\Delta
=
G_{\rm St}-Q^*G_\theta Q
\]

be the difference between the independently constructed Stieltjes and theta-history forms on the local even/odd plane.

Write the general Hermitian defect as

\[
\Delta=
\begin{pmatrix}
a&x+iy\\x-iy&d
\end{pmatrix}.
\]

If both forms carry the same quarter-turn covariance, then

\[
F^*\Delta F=\Delta.
\]

Exact symbolic solution gives

\[
a=4d,
\qquad
x=0.
\]

If both forms also carry the same reflection covariance, then

\[
P^*\Delta P=\Delta,
\]

which additionally gives

\[
y=0.
\]

Therefore

\[
\Delta
=
a
\begin{pmatrix}
1&0\\
0&1/4
\end{pmatrix}.
\]

One independently verified even-wall diagonal equality forces \(a=0\), and hence all four polarized matrix-unit identities follow.

## Durable verification

Checker:

`research/voevodsky/checkers/check_prime_cell_c4_reflection_rigidity.py`

Result:

`research/voevodsky/results/prime-cell-c4-reflection-rigidity.json`

The checker uses exact symbolic arithmetic and verifies every matrix relation.

## What remains source-dependent

The four-entry comparison no longer needs four independent integrations. It reduces to three source statements:

1. the Stieltjes and theta-history forms are both invariant under the same \(F\) on a common form domain;
2. both are covariant under the same reflection \(P\);
3. their independently normalized even-wall diagonal values agree.

The finite algebra is closed. The unresolved content is whether the causal graph form or the resolved joint form is the authoritative theta-history form and whether that form has the required quarter-turn covariance.

The two known branches differ by

\[
M_\Phi(B+B^*).
\]

That cross operator cannot be deleted using Fourier invariance alone. A source comparison must either select the resolved branch before codiagonalization or prove that the cross operator vanishes on the represented incidence range.

## Next exact test

For the source-selected candidate form \(G_\theta\), compute only

\[
F^*G_\theta F-G_\theta
\]

and

\[
P^*G_\theta P-G_\theta
\]

on the two local generators. If both vanish and the even-wall norm agrees, the complete prime-cell theorem follows from the rigidity calculation.

If the causal graph branch is used, the same test isolates the obstruction contributed by \(M_\Phi(B+B^*)\). A nonzero covariance defect rejects that branch for the parameter-free prime-cell comparison without fitting any metric.

## Disposition

The local gate is now smaller than the frozen four-entry statement. It is enough to establish common dihedral covariance and one diagonal normalization from independent source constructions.
