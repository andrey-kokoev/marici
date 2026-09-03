# The heat kernel fixes the Gaussian corona scale and bounds the order embedding

## Question

Does the completed heat kernel canonically choose the Gaussian Mellin state, and does the adjacent-gap order completion map boundedly into its GNS space?

## Exact scale

Normalize the Gaussian appearing in the prime cosine pairing:

\[
d\gamma_t(u)=\sqrt{\frac{t}{\pi}}e^{-tu^2}du.
\]

Its variance is `1/(2t)` and its characteristic function is

\[
\int_{\mathbb R}e^{-isu}d\gamma_t(u)
=e^{-s^2/(4t)}.
\]

Comparing with

\[
\omega_\sigma(U_s)=e^{-\sigma^2s^2/2}
\]

fixes, rather than fits,

\[
\sigma(t)^2=\frac1{2t}.
\]

Thus the exact heat factor selects the differentiable Gaussian Mellin state at every `t>0`.

## Bounded order-to-Gaussian map

For a finite zero-sum packet on ordered logarithmic labels, let

\[
(Jc)(u)=\sqrt2\sum_{\lambda_i>u}c_i.
\]

Prior research proves

\[
\|Jc\|_{L^2(du)}^2
=\langle c,[\Lambda,S]c\rangle.
\]

Since the Gaussian density is bounded by `sqrt(t/pi)`,

\[
\|Jc\|_{L^2(\gamma_t)}^2
\le
\sqrt{\frac{t}{\pi}}\,
\|Jc\|_{L^2(du)}^2.
\]

Therefore `J` extends uniquely from the finite packet core to a bounded map

\[
J_t:\mathcal H_{\mathrm{ord}}
\longrightarrow L^2(\mathbb R,\gamma_t)
\]

with

\[
\|J_t\|\le\left(\frac{t}{\pi}\right)^{1/4}.
\]

This map is source-derived from ordered logarithmic labels and the exact heat kernel. It is non-diagonal in the original coefficient basis and therefore is not covered by the coefficient-diagonal Hardy no-go.

## Range and generator boundary

The range is the Gaussian-weighted image of the closed fixed-partition step subspace determined by adjacent logarithmic gaps; it need not be dense in the full Gaussian GNS space.

Boundedness into `L2(gamma_t)` does not imply that the range lies in the generator domain. For finite packets it does, but extension of `Q_t J_t`, where `Q_t` is multiplication by `u`, requires the stronger estimate

\[
\int u^2|Jc(u)|^2d\gamma_t(u)
\le C_t\|c\|_{\mathrm{ord}}^2.
\]

This estimate also holds immediately because `u^2 sqrt(t/pi)e^{-tu^2}` is bounded. In fact

\[
\sup_u u^2\sqrt{\frac{t}{\pi}}e^{-tu^2}
=\frac{e^{-1}}{\sqrt{\pi t}},
\]

so

\[
\|Q_tJ_tc\|_{L^2(\gamma_t)}
\le
\frac{e^{-1/2}}{(\pi t)^{1/4}}
\|c\|_{\mathrm{ord}}.
\]

Hence the map lands boundedly in the graph domain of the Mellin generator for every fixed positive heat parameter.

## What this does not prove

The construction supplies two previously missing arrows: the heat-derived regularization scale and a bounded nonlocal map from the order completion into a differentiable Mellin domain. It does not identify the von Mangoldt Hankel quadratic with a form in `J_t c`, nor does it prove a lower bound for the coupled gamma–prime form. The map from a Hankel polynomial `p` to the zero-sum arithmetic packet `c_(t,h,p)` is still absent.

## Disposition

The differentiable-corona-domain blocker is resolved for each fixed `t>0`. The remaining first missing object is now the explicit source map

\[
p\longmapsto c_{t,h,p}\in\mathcal H_{\mathrm{ord}}
\]

that reproduces the completed prime cosine pairing. No positivity claim follows until that identity and the coupled form bound are proved.