# The Cayley-real projective matrix monoid provides the rank-one extension of reciprocal unitarity

## Compactified metric law

In the real projective frame define the Hermitian form

\[
J_0=i
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

For every real `2 by 2` matrix `M`, including singular matrices,

\[
M^*J_0M
=M^T J_0M
=(\det M)J_0.
\]

Thus the full real projective matrix monoid satisfies a conformal reciprocal
metric law. On the rank-two stratum this is projective unitarity. On the
rank-one stratum it becomes

\[
M^*J_0M=0.
\]

Equivalently, the image line of every real rank-one correspondence is
`J_0`-isotropic. The equation remains polynomial and meaningful when inversion
and determinant normalization fail.

## Cayley frame

Choose a fixed Cayley matrix `C` with

\[
C^*J_0C=J,
\qquad
J=\operatorname{diag}(1,-1),
\]

up to a nonzero real scalar. Then

\[
\mathbb P(\operatorname{Mat}_2(\mathbb R))
\]

is the Cayley-frame compactification of the reciprocal projective unitary
carrier. Rank-one amplituhedron boundary correspondences are therefore
compatible with reciprocal unitarity after all; the correct law is conformal
and polynomial rather than group-valued.

## Prime spectral transport

The determinant-one prime transport in the reciprocal frame is

\[
\widehat T_{p,z}
=\operatorname{diag}(p^{z/2},p^{-z/2}).
\]

Move it to the real frame:

\[
R_{p,z}=C\widehat T_{p,z}C^{-1}.
\]

Then

\[
R_{p,z}\in PSL(2,\mathbb R)
\quad\Longleftrightarrow\quad
\widehat T_{p,z}\in PSU(1,1)
\quad\Longleftrightarrow\quad
\operatorname{Re}z=0.
\]

Hence a comparison placing `R_(p,z)` in the same real projective matrix monoid
as the positive-geometric boundary transport would force critical-line
confinement while remaining compatible with rank-one boundary cells.

## Exact remaining cell

The required rung-four filler can now be stated without global inversion:
construct a source-derived projective correspondence

\[
\mathscr M_{p,z}
\in\mathbb P(\operatorname{Mat}_2(\mathbb R))
\]

from the two-phase four-presentation packet and prove that its rank-two prime
restriction is

\[
[\mathscr M_{p,z}]=[R_{p,z}].
\]

The real-monoid condition is independently supplied by positive source data;
the identification with prime transport is the only remaining comparison.

## Noncircularity condition

The Cayley matrix must be fixed before specialization to a Xi zero by the
source reciprocal involution. Allowing `C` to depend on `z` would realify every
individual semisimple matrix in a fitted frame and destroy the argument.