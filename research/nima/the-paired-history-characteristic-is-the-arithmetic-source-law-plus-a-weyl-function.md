# The paired history characteristic is the arithmetic source law plus a Weyl function

## Paired pencil

Let \(A\) be the skew-adjoint bilateral history generator, let

\[
B:U\to H
\]

be the retained source incidence, and let

\[
D_U(s):U\to U
\]

be the still-to-be-fixed arithmetic/source reservoir law.  The paired pencil
is

\[
\mathcal P(s)
=
\begin{pmatrix}
A-z(s)&-B\\
B^\dagger&D_U(s)
\end{pmatrix}.
\]

For \(\operatorname{Re}z(s)\ne0\), the history block is invertible.

## Source Schur characteristic

Eliminating the history coordinate gives

\[
M_U(s)
=
D_U(s)+B^\dagger(A-z(s))^{-1}B.
\]

Thus

\[
\ker\mathcal P(s)

e0
\quad\Longleftrightarrow\quad
\ker M_U(s)
e0
\]

on the history-resolvent chart.

The second term is the operator-valued Weyl function

\[
M_H(s)=B^\dagger(A-z(s))^{-1}B.
\]

Its Hermitian real part has the strict sign opposite
\(\operatorname{Re}z(s)\) on the range of \(B\).

## Rank-one forcing channel

For \(U=\mathbb C\), write

\[
D_U(s)=d_U(s)
\]

and

\[
m(s)=
\left\langle
\Phi,(A-z(s))^{-1}\Phi
\right\rangle.
\]

Then the characteristic equation is simply

\[
d_U(s)+m(s)=0.
\]

The column-only forced history corresponds to fixing the source amplitude
without imposing this source equation.  The paired spectral problem adds the
constitutive law \(d_U\).

## Passivity condition

If the source law has Hermitian real part with the same strict sign as the
Weyl real part—equivalently, the sign opposite
\(\operatorname{Re}z(s)\) in the present resolvent convention—then the two
terms cannot cancel off the seam. The total source Schur function is strictly
accretive or strictly dissipative in each open half-plane.

This supplies off-seam invertibility of \(M_U\) and hence of the paired
pencil.  The condition must be checked in the actual source metric; scalar
entrywise signs are insufficient for a multiport \(U\).

## Exact Xi comparison target

The divisor-bearing theorem is now

\[
\det_{m rel}M_U(s)
=E(s)\xi(s),
\qquad E(s)\ne0.
\]

In rank one,

\[
d_U(s)+m(s)=E(s)\xi(s).
\]

This identity exposes the only missing arithmetic datum.  The history Weyl
function \(m\) is source-derived and has the correct half-plane orientation.
The source reservoir law \(d_U\) must be independently derived from the
primitive, square, connected, endpoint, seam, and archimedean ports.

Defining

\[
d_U(s)=E(s)\xi(s)-m(s)
\]

from the desired scalar equality is forbidden: it installs the Xi divisor as
the constitutive law.

## Multiport requirement

The retained source is not genuinely rank one after preserving prime, grade,
and reciprocal labels.  The correct object is the operator-valued
characteristic \(M_U(s)\).  Terminal determinant evaluation occurs only after:

- prime and grade labels are retained;
- reciprocal covariance of \(D_U\) and \(M_H\) is proved;
- the primitive and square anomaly lines are fixed;
- connected returns are in the declared determinant ideal;
- no dark source vector lies in \(\ker B\).

A scalar \(d_U\) fitted after prime summation would erase the required
provenance.

## G4 reduction

The paired-history construction, adjoint incidence, Green cancellation, and
Weyl sign are now explicit.  G4 is reduced to construction of the arithmetic
source law \(D_U(s)\) and proof that its source Schur determinant is the Xi
section up to a unit.

This is sharper than an unspecified determinant factorization, but it remains
the unresolved RH-bearing constitutive theorem.  No RH conclusion is
authorized.
