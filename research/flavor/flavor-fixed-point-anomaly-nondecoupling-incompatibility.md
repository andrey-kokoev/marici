# Fixed-point anomaly/nondecoupling incompatibility: WP748

## Question

Can pure anomaly mediation derive the soft mass required by WP747 while an
interacting fixed point simultaneously fixes the WP746 gauge magnitude and RG
basin?

## Source maps

Pure anomaly mediation expresses the gaugino and scalar soft terms through RG
data:

\[
M_\lambda=\frac{\beta_g}{g}m_{3/2},
\qquad
m_i^2=\frac{|m_{3/2}|^2}{2}
\beta^I\partial_I\gamma_i.
\]

These relations are RG-covariant: no independent visible-sector soft
coefficient is inserted. Modern derivations recover the familiar two-loop
scalar masses and their RG invariance. See
[D'Eramo, Thaler, and Thomas](https://arxiv.org/abs/1307.3251).

## Exact fixed-point obstruction

At an interacting fixed point,

\[
\beta^I(g_*)=0.
\]

Therefore

\[
M_\lambda(g_*)=0,
\qquad
m_i^2(g_*)=0.
\]

Feeding the gauge-breaking soft mass into WP747 gives

\[
\epsilon_*
=\frac{m_{\mathrm{soft}}^2(g_*)}
{g_*^2M^2+m_{\mathrm{soft}}^2(g_*)}
=0.
\]

The additional (D)-term portal decouples exactly. Thus the same fixed point
that could normalize the gauge coupling removes the pure anomaly-mediated
nondecoupling source.

## Off-fixed-point fiber

For one linearized eigendirection,

\[
\beta=\lambda\delta,
\qquad
\delta(t)=C e^{\lambda t},
\]

and a local anomalous-dimension slope (c), the soft mass is

\[
m_{\mathrm{soft}}^2(t)
=\frac{|m_{3/2}|^2}{2}c\lambda C e^{\lambda t}.
\]

Moving off the fixed point restores the threshold only by restoring the
trajectory amplitude (C), RG time (t), and supersymmetry-breaking scale
(m_{3/2}). Its sign is the sign of (c\lambda C), so positivity is not
automatic. Two amplitudes on the same critical eigendirection give different
finite-energy portal magnitudes while sharing the same fixed point and critical
exponent.

## Disposition

Pure anomaly mediation does not complete the simple-group moment-map source.
At the exact magnitude-selecting fixed point it forces the portal to decouple;
away from the fixed point it reintroduces the relevant amplitude and clock
fibers already isolated by WP721–WP722.

The result does not exclude deflected anomaly mediation, gauge mediation,
gravity mediation, or explicit relevant deformations. Those mechanisms add a
messenger scale, compensator coupling, or boundary condition and must prove
that the new datum is source-selected rather than another fitted clock.

The remaining source needs a positive soft/vector ratio that survives at the
interacting normalization without an independent trajectory amplitude. Full
threshold spectra and calibrated physical16 channels remain required.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp748_fixed_point_anomaly_nondecoupling_incompatibility.py`.

Generated result:
`results/wp748_fixed_point_anomaly_nondecoupling_incompatibility.json`.
