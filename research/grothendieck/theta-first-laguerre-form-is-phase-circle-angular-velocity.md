# The first Laguerre form is phase-circle angular velocity

## Bounded question

What does the sewn rank-two polarization `B^2+AC` mean geometrically?

## Value--flux phase curve

Using packet 119, define

\[
 \gamma(x)=(C(x),B(x))=(C(x),-C'(x)).
\]

Since `B'=A`, its derivative is

\[
 \gamma'(x)=(-B(x),A(x)).
\]

The oriented area velocity is

\[
 \det\begin{pmatrix}
 C&B\\
 -B&A
 \end{pmatrix}
 =AC+B^2.
\]

Therefore

\[
 \boxed{
 \mathcal L_1[X](x)=4\det(\gamma(x),\gamma'(x)).}
\]

This is a genuine geometric-algebra bivector: the first Laguerre form is four
times the oriented area swept by the value--flux vector per unit spectral
parameter.

## The circle behind the oval

Whenever `gamma(x)` is nonzero, normalize radially:

\[
 \widehat\gamma(x)=\frac{\gamma(x)}{\|\gamma(x)\|}\in S^1.
\]

If `theta(x)=arg(C(x)+iB(x))`, then

\[
 \boxed{
 \theta'(x)
 =\frac{AC+B^2}{C^2+B^2}
 =\frac{\mathcal L_1[X](x)}{4(C^2+B^2)}.}
\]

Thus an oval phase portrait becomes a literal circle after forgetting its
radial amplitude.  The first Laguerre inequality is exactly one-way angular
transport around that circle.

## Meaning of scalar zeros

A real zero of `X=2C` is a crossing of the vertical axis in the value--flux
plane.  At a simple zero,

\[
 \mathcal L_1[X]=4B^2>0,
\]

so the phase vector crosses transversely and retains its orientation.  The
observable scalar zero is not the disappearance of the full state; it is the
loss of the `C` coordinate while the conjugate flux `B` remains.

The full vector vanishes only at a multiple real zero.  This sharply realizes
the operator's earlier proposal that a plotted zero may be where one projected
meaning disappears rather than where the source object ceases to exist.

## Reciprocal sectors and destructive interference

Packet 119 shows that the two reciprocal quadrant pairs supply the two terms
in the bivector:

\[
 \text{opposite-sign sector}\to B^2,
 \qquad
 \text{same-sign sector}\to AC.
\]

Their interference determines the direction of phase rotation.  The critical
line is the reciprocal seam on which this real phase portrait is read; the
half-density shift centers the two source sectors before the projection.

## RH boundary

Positivity of the first angular velocity is only the first generalized
Laguerre condition.  RH requires the complete higher-order osculating flag to
have coherent orientation, not merely the tangent two-plane.  In geometric-
algebra language, higher Laguerre forms are the successive Pluecker
coordinates of the jet frame

\[
 \gamma,\gamma',\gamma'',\ldots.
\]

That identification is a programme target, not yet a theorem here.

The next gate is to determine whether the source seam-jet total positivity of
packet 114 maps to these osculating Pluecker coordinates under modular
Fourier transport. The smallest falsifier is the first jet order at which the
transported orientation differs from the source Vandermonde orientation.
