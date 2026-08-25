# Theta Clark derivative is the sharp endpoint-trace repair criterion

## Connection between two previously separate channels

The full tail--seam `L2` Gram does not control the endpoint

\[
 L(c)=C'\int y(\xi)\,d\xi,
 \qquad
 y=\widehat c\,\overline{\widehat\Phi}.
\]

But the native two-sheet Clark bulk contains the additional source-derived
square

\[
 a^2|\partial_zG|^2.
\]

Under spectral translation, differentiating the source multiplier contributes
`Phihat'`.  On the locus where `Phihat` is nonzero, the resulting model energy
is

\[
 \mathcal E_a(y)
 =\int_{\mathbb R}|y(\xi)|^2
 \left(1+a^2
 \left|\frac{\widehat\Phi'(\xi)}{\widehat\Phi(\xi)}\right|^2
 \right)d\xi.
\]

The exact transform convention and any additional derivative terms must be
audited in the labelled system.  The statement below is the sharp criterion
once this multiplier form is obtained.

## Sharp weighted trace theorem

Put

\[
 w_a(\xi)=1+a^2
 \left|\frac{\widehat\Phi'(\xi)}{\widehat\Phi(\xi)}\right|^2.
\]

Then the endpoint functional `y -> integral y` is continuous in the weighted
energy `integral w_a |y|^2` if and only if

\[
 \boxed{
 \int_{\mathbb R}\frac{d\xi}{w_a(\xi)}<\infty.}
\]

Sufficiency is Cauchy--Schwarz:

\[
 \left|\int y\right|^2
 \le
 \left(\int w_a|y|^2\right)
 \left(\int w_a^{-1}\right).
\]

Necessity follows by testing truncated Riesz representatives

\[
 y_R=\mathbf1_{[-R,R]}w_a^{-1}.
\]

If the reciprocal integral diverges, the ratio of squared endpoint value to
energy diverges with `R`.

## Consequence

If the completed theta source satisfies, for example,

\[
 \left|\frac{\widehat\Phi'}{\widehat\Phi}(\xi)\right|
 \ge c|\xi|-C
\]

outside a compact set, then every nonzero Clark parameter `a` makes the
endpoint continuous.  The derivative square would therefore serve two roles:

1. cancel the sheet-odd spin-two bulk and produce positivity;
2. prevent the scalar zero boundary condition from disappearing at
   completion.

At `a=0` the repair disappears, agreeing with the explicit `L2` endpoint
no-go.

## New falsifier

The route fails if either:

1. the labelled Fourier calculation does not produce the logarithmic-
   derivative weight without uncontrolled cross terms; or
2. the theta logarithmic derivative grows too slowly on a set large enough
   that
   `integral 1/w_a` diverges.

Zeros of `Phihat`, if present, must be treated through the original two-channel
form rather than by division.

## Honest frontier

The immediate calculation is now source-specific and one-dimensional:

\[
 \boxed{
 \text{derive the exact Clark spectral weight and decide }
 \int w_a^{-1}<\infty.}
\]

If it passes, the endpoint need not be appended as an unrelated port: its
continuity is already enforced by the native Clark relationship energy.
