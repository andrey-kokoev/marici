# Theta log-concavity proves global tilt monotonicity of translation defect

## Bounded question

Can the locally positive conditional band-boundary current cross sign at a
finite positive Mellin tilt?

## Centered defect representation

Let

\[
g(x)=\Phi(|x|),
\qquad
f_a(x)=e^{ax}g(x),
\]

and let

\[
\mathcal C_a(D)
=
\frac12\|f_a-\tau_Df_a\|_2^2
=
W_a(0)-W_a(D).
\]

For the translated correlation, set

\[
y=x-\frac D2.
\]

Because \(g\) is even, both \(g(y)^2\) and

\[
g\!\left(y+\frac D2\right)
g\!\left(y-\frac D2\right)
\]

are even in \(y\). Therefore

\[
\mathcal C_a(D)
=
\int_{\mathbb R}
\cosh(2ay)
\left[
g(y)^2
-
g\!\left(y+\frac D2\right)
g\!\left(y-\frac D2\right)
\right]dy.
\]

## Global orientation

Strict log-concavity gives the pointwise midpoint slack

\[
\Delta_D(y)
=
g(y)^2
-
g\!\left(y+\frac D2\right)
g\!\left(y-\frac D2\right)
\ge0.
\]

For \(D>0\), it is strictly positive away from the degenerate set. Hence

\[
\partial_a\mathcal C_a(D)
=
2\int_{\mathbb R}
y\sinh(2ay)\Delta_D(y)\,dy.
\]

For \(a>0\), the factor \(y\sinh(2ay)\) is nonnegative and is positive for
\(y\ne0\). It follows that

\[
\partial_a\mathcal C_a(D)>0
\qquad
(a>0,\ D>0).
\]

By reflection, the derivative is negative for \(a<0\).

## Conditional boundary theorem

Since

\[
J_a(0)-J_a(D)=\partial_a\mathcal C_a(D),
\]

the completed theta source satisfies

\[
J_a(0)>J_a(D)
\qquad
(a>0,\ D>0).
\]

Thus the first boundary condition of the aggregate conditional adjacent-band
residual holds globally throughout the outer tilt sector. No finite-\(a\)
crossing exists.

## Source-operation interpretation

The relevant native operation is the fixed translation-incidence map

\[
B_D=I-\tau_D.
\]

The energy is

\[
\mathcal C_a(D)=\frac12\|B_Df_a\|_2^2.
\]

This does not construct a moving orthogonal compression with nonzero Berry or
Grassmann curvature. The common Mellin connection may remain flat. Source
log-concavity instead orients the response of one fixed incidence port under
the normal tilt.

Accordingly, this theorem supplies one globally transverse flag coordinate,
not the complete source-derived projection requested for the full
theta/Tate port system.

## Remaining block obstruction

The full conditional adjacent-band residual also contains

\[
D W_a(D)
-
(D+L)W_a(D+L),
\]

and its integral over a canonical band. The theorem above controls the
\(J\)-boundary term but does not orient this weighted correlation term.

The next attack must rewrite that second term as another source energy or
produce its smallest exact falsifier.

## Result

Strict theta log-concavity proves global Mellin-tilt monotonicity of the
translation-defect energy:

\[
\partial_a\mathcal C_a(D)>0
\]

for every \(a,D>0\). The feared finite-tilt sign crossing cannot occur.

This closes the first aggregate boundary gate of the conditional
continuous-band transport.

## Sharp falsifier for the remaining route

Find \(a,L>0\) and \(D\in(0,L)\) for which the weighted correlation component

\[
D W_a(D)-(D+L)W_a(D+L)
\]

has the wrong block-integrated sign after inclusion of the already positive
\(J\)-term.
