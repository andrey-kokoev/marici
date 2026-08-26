# The seventh theta quarter-turn rotates spectral flow into positive delay density

## Ordered-port correction

The positive delay density here belongs to the unframed full Weyl Cayley path.
It controls full-port rank crossings, not zeros of the ordered theta
source-to-endpoint transfer. The theorem remains exact but does not orient the
theta divisor unless the missing lower-minor or framed-pencil bridge is first
constructed.

Exact finite-dimensional generator theorem. Fix the Hermitian Weyl path and
its Cayley unitary from the sixth rotation. Differentiating the unitary path
produces a positive operator-valued density whenever the Weyl crossing form
has the source-derived negative orientation. This identifies the control-
theoretic time-delay object hidden inside the Lagrangian crossing picture.
It does not construct the missing theta-to-Weyl bridge.

## Fixed unitary path

Retain

\[
U(\lambda)
=
\bigl(W(\lambda)-iI\bigr)
\bigl(W(\lambda)+iI\bigr)^{-1},
\qquad
W(\lambda)=W(\lambda)^*.
\]

Write

\[
R(\lambda)=\bigl(W(\lambda)+iI\bigr)^{-1}.
\]

Then

\[
U=I-2iR,
\qquad
U'=2iRW'R.
\]

Since

\[
U^*R=R^*,
\]

we obtain the exact logarithmic derivative

\[
U^*U'=2iR^*W'R.
\]

## The seventh quarter-turn

Define the signed delay density using the orientation compatible with the
negative crossing form:

\[
\mathcal Q(\lambda)
=
iU(\lambda)^*U'(\lambda).
\]

Therefore

\[
\mathcal Q
=
-2R^*W'R.
\]

For the selfadjoint feedback realization

\[
W(\lambda)
=
A-\lambda I-B^*(D-\lambda)^{-1}B,
\]

we have

\[
-W'(\lambda)
=
I+B^*(D-\lambda)^{-2}B.
\]

Consequently

\[
\mathcal Q(\lambda)
=
2R^*
\left(I+B^*(D-\lambda)^{-2}B\right)
R
>0
\]

between poles.

The earlier crossing orientation has become an ordinary positive operator.
This positivity is not fitted to a zero set. It is forced by the derivative
of the source-independent selfadjoint resolvent realization.

## Spectral time is generated rather than assumed

The parameter \(\lambda\) labels the spectral path. The operator
\(\mathcal Q\) measures the infinitesimal rotation of its unitary scattering
frame. Thus the time-like quantity is not an extra primitive coordinate. It
is the generator of transport along the spectral parameter.

For a differentiable state \(v\),

\[
\langle v,\mathcal Q(\lambda)v\rangle
=
2\left\|
\left(I+B^*(D-\lambda)^{-2}B\right)^{1/2}
R(\lambda)v
\right\|^2.
\]

This is the precise control-theoretic form of oriented relationship energy.

## Phase winding is the integral of the density

Where a continuous determinant phase is chosen,

\[
\det U(\lambda)=e^{i\vartheta(\lambda)},
\]

and hence

\[
\vartheta'(\lambda)
=
-\operatorname{tr}\mathcal Q(\lambda).
\]

The phase therefore moves monotonically clockwise under this convention.
Its signed winding is the integral of a positive local density, with pole
contributions retained separately as residue data.

This rotates the global integer-valued spectral-flow invariant into a local
positive operator-valued measure along the spectral path.

## What this adds

The sixth rotation preserved multiplicity and orientation globally. The
seventh rotation localizes that information:

\[
\left(
U,
\operatorname{Sf},
\operatorname{Mas}
\right)
\quad\longmapsto\quad
\left(
\mathcal Q(\lambda),
\operatorname{tr}\mathcal Q(\lambda)\,d\lambda,
\mathcal R
\right).
\]

Here \(\mathcal R\) denotes the separately typed pole and residue data.

This is stronger than merely observing that the determinant winds. It gives
an operator density whose positivity witnesses the direction of every
regular crossing.

## Exact limitation

The result is conditional on having the actual theta/Tate comparison as a
Hermitian Weyl path of the stated form. Starting with the completed scalar
section and defining \(W\) backward would merely repackage the unresolved
problem.

The source gate is therefore unchanged but sharper:

1. construct the full theta/Tate exterior comparison operator;
2. prove it has a selfadjoint feedback realization before scalar projection;
3. identify its Cayley unitary with the completed local sewing phases;
4. retain primitive, square, archimedean, and pole currents in the delay
   measure;
5. prove that completion preserves the positive operator-valued density.

## Finite falsifiers

The proposed theta realization fails immediately if any finite cutoff has:

- a non-Hermitian \(W_X(\lambda)\) on the real spectral path;
- a nonunitary Cayley transform;
- an indefinite \(iU_X^*U_X'\);
- a phase derivative whose sign disagrees with
  \(-\operatorname{tr}\mathcal Q_X\);
- a pole contribution that cannot be typed into \(\mathcal R_X\);
- or a positive finite density whose lower control disappears under the
  authorized completion.

## Decisive conclusion

After seven quarter-turns, the candidate orientation law has a precise
physical form: the completed two-sector comparison must be a passive
selfadjoint colligation whose unitary sewing path carries a positive signed
delay density. The new law is independently positive once that colligation
is source-derived. The unresolved RH content is whether labelled theta/Tate
data actually constructs this colligation and whether its positivity survives
restricted-product completion.
