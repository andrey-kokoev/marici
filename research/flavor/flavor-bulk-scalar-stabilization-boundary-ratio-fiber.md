# Bulk-scalar stabilization boundary-ratio fiber: WP759

## Question

Does a dynamical bulk-scalar stabilizer fix the BPS wall–boundary separation
strongly enough to select the asymmetric portal magnitude?

## Claim boundary

Use the stiff-boundary leading stabilization potential

\[
V(s)=C\left(v_\pi-v_0e^{-\epsilon s}\right)^2,
\qquad C>0,
\qquad v_0>v_\pi>0.
\]

This is the exact algebraic core of the bulk-scalar radion mechanism introduced
by [Goldberger and Wise](https://arxiv.org/abs/hep-ph/9907447). The admitted
boundary packet contains \(v_0,v_\pi\); their values are inputs to the boundary
potentials, not outputs of the bulk variational equation.

## Conditional stabilization

The minimum is

\[
s_*=\frac{1}{\epsilon}\log\frac{v_0}{v_\pi},
\]

with curvature

\[
V''(s_*)=2C\epsilon^2v_\pi^2>0.
\]

Thus this mechanism genuinely removes the translation flat direction for a
fixed boundary packet.

Grant the most favorable common-scale relation between the stabilizer and the
WP758 wall, so that

\[
a=\epsilon s_*=\log r,
\qquad
r=\frac{v_0}{v_\pi}.
\]

The predicted portal contrast becomes

\[
\Delta(r)
=\frac12\tanh^2(\log r)
=\frac{(r^2-1)^2}{2(r^2+1)^2}.
\]

The same bulk action and stabilization law with \(r=2\) and \(r=3\) give

\[
\Delta(2)=\frac{9}{50},
\qquad
\Delta(3)=\frac{8}{25}.
\]

Both stationary points are stable. The numerical difference is sourced only
by the unexplained boundary-value ratio. Every \(0<\Delta<1/2\) has a formal
preimage

\[
r=\sqrt{\frac{1+\sqrt{2\Delta}}{1-\sqrt{2\Delta}}}.
\]

## Disposition

The bulk scalar is a conditional separation selector and genuine local
stabilizer. It does not select among its boundary packets and therefore does
not select the portal magnitude. Under generic scale assignments an additional
wall-width-to-stabilizer ratio survives; the calculation deliberately grants
that ratio away.

The next source must derive \(v_0/v_\pi\) and the labelled boundary ordering
from quantized data or a unique vacuum. Those data must not be chosen after the
desired portal is known. The resulting prediction must still survive boundary
renormalization, radion and Kaluza–Klein thresholds, RG transport,
`physical16` descent, and a calibrated experimental channel.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.py

Generated result:
research/flavor/results/wp759_bulk_scalar_stabilization_boundary_ratio_fiber.json
