# A Fourth Determinant-Dual Channel Closes the Relative Clifford Pairing

## Operator stimulus

The operator recalled that the programme repeatedly requires a four-rung
relational tower and asked whether the three-channel Gamma-wall lift was
missing a fourth wall.

The exact answer is unexpectedly sharp. One additional reciprocal channel
repairs the spectral obstruction to a relative Clifford metric. It does not
yet produce a fixed metric for the complete degree dynamics.

## Three-channel defect

The relative map between the first two degree transfers is

\[
R=M_1M_0^{-1},
\]

with spectrum

\[
\{1,1,9/5\}.
\]

The eigenvalue \(9/5\) has no reciprocal partner. This is the obstruction to
a nondegenerate invariant quadratic form on the three-channel carrier.

## Minimal reciprocal completion

Let

\[
d_j=\det M_j
\]

and adjoin a one-dimensional channel transported by \(d_j^{-1}\):

\[
\widehat M_j=
\begin{pmatrix}
M_j&0\\
0&d_j^{-1}
\end{pmatrix}.
\]

This is the determinant-dual line. The completed transfer has determinant
one. Its relative map is

\[
\widehat R=widehat M_1\widehat M_0^{-1}
=
\begin{pmatrix}
9/5&-14/5&-4/(5c)&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&5/9
\end{pmatrix}.
\]

The spectrum is now

\[
\{1,1,9/5,5/9\}.
\]

The missing reciprocal partner has appeared exactly.

## Relative invariant forms

Solving

\[
\widehat R^TQ\widehat R=Q
\]

gives the symmetric family

\[
Q=
\begin{pmatrix}
0&0&0&-cu\\
0&a&b&7cu/2\\
0&b&d&u\\
-cu&7cu/2&u&0
\end{pmatrix}.
\]

Its determinant is

\[
\det Q=-c^2u^2(ad-b^2).
\]

Hence the form is nondegenerate whenever \(u\ne0\) and \(ad-b^2\ne0\).
The four-channel relative comparison therefore has a genuine Clifford
interpretation.

## Scope correction

The determinant-dual coordinate repairs the relative map, not the entire
transfer family. Solving

\[
\widehat M_j^TQ\widehat M_j=Q
\]

simultaneously for \(j=0,1\) still yields only the zero form. Thus no single
quadratic metric is preserved by the individual four-channel steps.

The result supports, but does not complete, the proposed four-rung picture:

1. the tail pair carries the regular state;
2. the wall channel carries the polar boundary state;
3. the determinant-dual channel carries reciprocal normalization;
4. their relative comparison admits a nondegenerate Clifford pairing.

The numbering here describes four carrier coordinates, not yet the full
categorical four-rung tower. The new coordinate should not be called a
physical wall until it is derived from the Mellin residue or determinant-line
source construction.

## Meaning

The three-channel failure was not random. It measured a missing dual line.
Adding precisely that line converts special-linear normalization into an
orthogonalizable relative comparison. This is the first post-audit geometric
algebra structure that is neither imported nor fitted to a zero set.

The next source gate is exact: derive the inverse-determinant line as an
authorized boundary or normalization channel and determine whether its
relative metric is compatible with exponent transport and completion.

## Verification

The checker
`research/grothendieck/checkers/fourth_determinant_dual_clifford_pairing.py`
verifies the completed relative matrix, reciprocal spectrum, invariant form,
nondegeneracy condition, and failure of a common stepwise invariant form.
