# Cayley crossing form orients full Weyl rank, not cross-transfer zeros

## Bounded question

Does differentiating the source-derived two-port Cayley sewing path orient the
theta cross-transfer divisor?

## Source-derived Weyl family

Let \(A=A^*\) be a finite source-authorized carrier compression and let

\[
B=\begin{pmatrix}b_f&b_0\end{pmatrix}.
\]

With a constant Hermitian boundary matrix \(A_\partial\), define

\[
W(z)=A_\partial-B^*(A-zI)^{-1}B.
\]

For real \(\lambda\) away from the carrier spectrum, \(W(\lambda)\) is
Hermitian. Moreover,

\[
W'(\lambda)
=
-B^*(A-\lambda I)^{-2}B
\le0.
\]

Thus the finite theta/Tate two-port comparison does supply a native Hermitian
Weyl path without defining it backward from the scalar theta transform.

## Cayley crossing form

Set

\[
U(\lambda)
=
\bigl(W(\lambda)-iI\bigr)
\bigl(W(\lambda)+iI\bigr)^{-1}.
\]

On every real resolvent interval, \(U\) is unitary. Its differentiated Cayley
form is

\[
Q(\lambda)
=
iU(\lambda)^*U'(\lambda)
=
-2
\bigl(W(\lambda)-iI\bigr)^{-1}
W'(\lambda)
\bigl(W(\lambda)+iI\bigr)^{-1}.
\]

Since

\[
\bigl(W+iI\bigr)^{-1*}
=
\bigl(W-iI\bigr)^{-1},
\]

the sign of \(W'\) gives

\[
Q(\lambda)\ge0.
\]

This positivity is exact and source-derived at every finite cutoff.

## Which divisor it orients

The Cayley path sees eigenvalue crossings of \(W\). Its determinant phase and
trace density therefore govern

\[
\det W(\lambda)=0.
\]

The theta scalar is instead the cross entry

\[
F(\lambda)=W_{f0}(\lambda)
\]

up to the fixed boundary normalization. A cross-entry zero does not imply
\(\det W=0\). At such a point one may have

\[
W(\lambda)=
\begin{pmatrix}
a&0\\
c&d
\end{pmatrix},
\qquad
ad\ne0.
\]

Then the theta transmission channel vanishes while the full Weyl comparison
remains invertible and the Cayley path has no rank crossing.

Therefore positive \(Q\) orients the wrong divisor for the present RH lane.
The seventh rotation is a valid theorem about full-port exterior rank, not a
zero-confinement theorem for the source-to-endpoint scalar.

## Current bookkeeping cannot repair the mismatch

Primitive, prime-square, archimedean, and carrier-pole currents may reproduce
the trace density of the full Cayley path and its residue measure. Even exact
agreement would explain the winding of \(\det W\), not the winding of
\(W_{f0}\).

To transfer this orientation to the theta divisor, the source must first prove
a lower-minor relation such as

\[
W_{f0}(z)=u(z)\det W(z),
\qquad
u(z)\ne0,
\]

or a rank constraint making cross cancellation equivalent to full rank loss.
Packet 241 showed that no such relation is presently derived.

## Result

The finite source-derived Hermitian Weyl family and its positive Cayley
crossing form exist. They do not solve the theta problem because they classify
full Weyl rank loss, whereas theta zeros are cross-transfer cancellations.
The route is blocked by a lower-minor mismatch before completion, residue
matching, or boundary-current closure.

## Sharp falsifier

At the smallest declared theta compression, evaluate both \(F_X=W_{f0,X}\)
and \(\det W_X\). Any point satisfying

\[
F_X=0,
\qquad
\det W_X\ne0
\]

is invisible to the Cayley rank crossing and falsifies direct promotion of its
positive crossing form to the theta divisor. Absent an exact source-derived
minor identity, matching trace and residue currents is insufficient.
