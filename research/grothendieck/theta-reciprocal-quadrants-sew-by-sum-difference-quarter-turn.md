# Reciprocal quadrants sew by a sum--difference quarter-turn

## Bounded question

What is the exact contribution of reciprocal modular sewing to the first
Laguerre two-copy form?

## Full even source

Let `Phi` be the positive even completed source and

\[
 X(x)=\int_{\mathbb R}\Phi(u)e^{ixu}\,du.
\]

The first Laguerre form is

\[
 \mathcal L_1[X](x)
 =\frac12\iint_{\mathbb R^2}
 (u-v)^2\Phi(u)\Phi(v)e^{ix(u+v)}\,du\,dv.
\]

Write `u=epsilon a`, `v=eta b` with `a,b>=0` and
`epsilon,eta in {+1,-1}`. Pairing conjugate quadrants makes the result real.
The same-sign pair contributes

\[
 (a-b)^2\cos x(a+b),
\]

while the opposite-sign pair contributes

\[
 (a+b)^2\cos x(a-b).
\]

Therefore reciprocal sewing gives the exact positive-quadrant formula

\[
 \boxed{
 \mathcal L_1[X](x)
 =\iint_{[0,\infty)^2}\Phi(a)\Phi(b)
 \left[
 (a-b)^2\cos x(a+b)
 +(a+b)^2\cos x(a-b)
 \right]da\,db.}
\]

## The quarter-turn

Set

\[
 S=a+b,
 \qquad D=a-b.
\]

The sewn bracket is

\[
 \boxed{D^2\cos(xS)+S^2\cos(xD).}
\]

The reciprocal quadrant exchanges `S` and `D`: the separation weight of one
sector becomes the phase coordinate of the other.  Modular sewing therefore
acts as a quarter-turn on the two-copy sum--difference plane, not as pointwise
cancellation of a one-chart endpoint.

This is the exact mathematical realization of the operator's proposed
two-plane interference picture.

## Rank-two scalar reduction

Using

\[
 \cos x(a+b)=\cos(xa)\cos(xb)-\sin(xa)\sin(xb),
\]

\[
 \cos x(a-b)=\cos(xa)\cos(xb)+\sin(xa)\sin(xb),
\]

the bracket becomes

\[
 2(a^2+b^2)\cos(xa)\cos(xb)
 +4ab\sin(xa)\sin(xb).
\]

Define

\[
 C(x)=\int_0^\infty\Phi(a)\cos(xa)\,da,
\]

\[
 B(x)=\int_0^\infty a\Phi(a)\sin(xa)\,da,
 \qquad
 A(x)=\int_0^\infty a^2\Phi(a)\cos(xa)\,da.
\]

Then `X=2C`, `X'=-2B`, `X''=-2A`, and the sewn form reduces exactly to

\[
 \boxed{
 \mathcal L_1[X](x)=4\bigl(B(x)^2+A(x)C(x)\bigr).}
\]

The positive square `B^2` is the cross-quadrant repair channel. The sole
possible defect is the signed polarization `AC`.

## What this explains

The moving endpoint found in packet 118 was a coordinate artifact of keeping
only the same-sign quadrant. Full reciprocal sewing replaces it by an
orthogonal cross-quadrant channel. The completed problem is neither a lone
positive bulk nor an arbitrary collection of boundary terms:

\[
 \boxed{
 \text{same-sign sector}
 +\text{opposite-sign sector}
 =\text{one rank-two polarization}.}
\]

The sewn integrand is not pointwise nonnegative. Consequently modular
reflection alone still does not prove the Laguerre inequality.

## Next gate and falsifier

The exact first-order target is now

\[
 B(x)^2\ge -A(x)C(x)
\]

whenever `A(x)C(x)<0`.  The all-order integral sign-regularity theorem must be
tested against this particular rank-two polarization rather than against an
unspecified endpoint repair.

The smallest falsifier is one real `x` for which the exact theta integrals
satisfy `B(x)^2+A(x)C(x)<0`.  A proof must derive the domination from labelled
transport; merely observing it numerically would restate the first Laguerre
inequality.
