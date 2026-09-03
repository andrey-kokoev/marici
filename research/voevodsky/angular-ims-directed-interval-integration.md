# Directed interval integration for the angular IMS window

## Question

Can the remaining gap between the analytic bound and the numerical localization scout be closed without solving transcendental critical-point equations?

## Claim boundary

This packet certifies an upper bound by directed interval arithmetic on a uniform rational subdivision. It does not assert the exact value of the integral.

## Method

For \(c=\pi/2\), \(\rho(t)=\sin(c s(t))\), and the septic smoothstep \(s\), evaluate

\[
\rho'''=
-c^3\cos(cs)(s')^3
-3c^2\sin(cs)s's''
+c\cos(cs)s'''
\]

on every rational cell of a uniform partition of \([0,1]\). Interval evaluation encloses the full range on each cell. Multiplying the upper endpoint of \(|\rho'''|\) by the cell width and summing gives a directed upper Darboux bound for \(\lVert\rho'''\rVert_1\).

This is not point-sampling quadrature: every cell image encloses all values on that cell, so no separate discretization-error term is omitted. The reported binary64 bound is rounded once more toward positive infinity and recorded in hexadecimal form, which denotes the exact dyadic rational supplied to downstream tooling.

The checker evaluates two nested subdivisions and requires the finer bound to improve strictly. For normalized angular overlap \(h_\theta=\pi\), it reports

\[
C_{\rm loc}^{\rm iv}
\le \frac{2}{3\pi}
\lVert\rho'''\rVert_{1,\rm upper}.
\]

## Disposition

This is the directed certificate to compare with the weighted-tail reserve. The earlier analytic value \(19.97714994\) remains a proof independent of interval arithmetic; the interval result is a sharper enclosure.

## Verification

- `research/voevodsky/checkers/check_angular_ims_interval_integration.py`
- `research/voevodsky/results/angular_ims_interval_integration.json`
