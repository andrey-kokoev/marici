# Existing source-constraint kernel

## Question

Does any equality already authorized by the present source grammar remove
WP537's fixed-\(v\) coefficient direction and numerically select
\(g_Ff_{\mathrm{phys}}/v\)?

## Strongest admitted equality packet

Use logarithmic coordinates

\[
x=(\log a,\log w,\log g_F^2,\log g_P^2).
\]

The fixed electroweak norm supplies the row

\[
(1,2,0,0).
\]

WP490's exact dual-gauge ray supplies

\[
(0,0,-1,1).
\]

Granting the instrument programme its strongest contemplated independent
\(g_F\) normalization adds

\[
(0,0,1,0).
\]

The resulting three-by-four Jacobian has rank three and a one-dimensional
kernel.

## Exact surviving direction

WP537's source family has logarithmic tangent

\[
v_t=(2,-1,0,0).
\]

The checker verifies

\[
J_{\mathrm{source}}v_t=0.
\]

The logarithmic clock-ratio gradient is

\[
\nabla\log{g_Ff_{\mathrm{phys}}\over v}
=\left(-{1\over2},0,{1\over2},0\right),
\]

and therefore

\[
\nabla\log{g_Ff_{\mathrm{phys}}\over v}\,v_t=-1.
\]

Thus the unique surviving source-equality direction changes the target ratio.

## RG authority audit

The existing RG packets do not add a transverse equality:

- WP490 has a gauge-coupling ratio ray but no finite nonzero one-loop fixed
  point.
- WP491 proves that the gauge-Yukawa beta vector field is not yet typed.
- WP492 freezes tensor shapes while leaving ten scalar normalizations.
- WP493-WP495 add compulsory independent radial, alignment, and Gram
  coordinates.
- WP498 finds three further missing connector-quartic coordinates under the
  maximal admitted stabilizer.
- WP537 proves that strict threshold inequalities hold at two different
  points on the \(t\) fiber.

Support closure enlarges the running coordinate space. It is not a beta-zero
equation and cannot be counted as selection.

WP538 detects the \(t\)-direction. Adding its readout gradient to the source
Jacobian would raise the rank to four, but that would convert measured
projection authority into source authority and is therefore circular.

## Disposition

The present source grammar conditionally selects relational outputs once its
coefficients are fixed. It does not numerically select \(t\) or
\(g_Ff_{\mathrm{phys}}/v\).

This is bounded, not universal. Reopening requires the independently completed
tensor and quartic grammar, a declared renormalization scheme and threshold
map, and a derived stable beta-zero or matching equation whose gradient has
nonzero contraction with \(v_t\). No flavor readout may supply that equation.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp543_existing_source_constraint_kernel.py

The generated result is
research/flavor/results/wp543_existing_source_constraint_kernel.json.

The reviewed claim and report to marici.Nima were admitted at graph event
ev-000000004885-f9fef18e-6f10-4c8d-b069-85bbb84838a5. Admission records
reviewed provenance and does not certify truth.
