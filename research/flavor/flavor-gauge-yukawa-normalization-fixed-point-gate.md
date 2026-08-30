# Gauge–Yukawa normalization fixed-point gate: WP719

## Question

Does identifying the WP718 auxiliary normalization with a gauge coupling fix
the asymmetric portal magnitude, or does it merely replace one free continuous
parameter by another?

## Gauge–Yukawa relation

Let representation theory fix positive Clebsch invariants \(C_n\) and \(C_m\),
and let a gauge–Yukawa identity impose

\[
g_n=g^2C_n,
\qquad
g_m=g^2C_m.
\]

This fixes

\[
\frac{g_n}{g_m}=\frac{C_n}{C_m},
\qquad
g_n-g_m=g^2(C_n-C_m).
\]

Representation ordering therefore fixes the contrast sign, and the common
gauge coupling replaces the arbitrary auxiliary normalization. This is
stronger than WP718, but it does not yet predict a numerical magnitude.

## One-loop obstruction

For an autonomous one-loop gauge flow

\[
\frac{dg}{dt}=bg^3,
\]

the exact solution is

\[
g^2(t)=\frac{g_0^2}{1-2bg_0^2t}.
\]

The projective portal ratio is preserved, but every admissible boundary value
\(g_0\) produces a different magnitude at finite scale. For \(b\ne0\), the
only one-loop fixed point is Gaussian and gives a zero portal. For \(b=0\), a
continuum of constant values remains. Neither case selects the required
nonzero magnitude.

The smallest hostile pair is two distinct values \(g_{0a}\ne g_{0b}\). They
obey the same representation and gauge–Yukawa identities yet remain distinct
under the one-loop flow.

## Interacting fixed-point gate

The minimal formal possibility appears at the next order:

\[
\beta_g=g^3(b_0+b_1g^2).
\]

An interacting zero exists at

\[
g_*^2=-\frac{b_0}{b_1},
\]

so \(b_0\) and \(b_1\) must have opposite signs. Its linearized exponent is

\[
\left.\frac{d\beta_g}{dg}\right|_{g_*}
=\frac{2b_0^2}{b_1}.
\]

The sign required for attraction depends on the declared RG orientation. The
full gauge–Yukawa–quartic stability matrix, not this scalar derivative, must
establish the basin. The fixed point is explanatory only if anomaly-free
matter fixes all beta coefficients independently and the zero survives scheme
and truncation checks.

## Threshold and readout boundary

Even a valid ultraviolet or infrared fixed point does not automatically fix a
low-energy portal. A relevant deformation can introduce a new scale, and
ordinary heavy-sector decoupling can erase the fixed relation. The source must
derive a matching map whose finite threshold terms retain the Clebsch contrast
with controlled uncertainty.

Likewise, representation labels are only potential readout channels. A
physical instrument must resolve those channels after widths, mixing,
backgrounds, and detector confusion. An unlabelled total rate may still factor
through a nonfaithful sum.

## Claim boundary and disposition

WP719 proves that gauge–Yukawa unification fixes the portal ratio and
conditional sign but not its magnitude at one loop. A nonzero interacting
fixed point of the completed source theory is a necessary magnitude-selector
candidate. It is not sufficient until the full basin, threshold transport,
and calibrated labelled readout are derived from the same matter packet.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp719_gauge_yukawa_normalization_fixed_point_gate.py`

Generated result: `results/wp719_gauge_yukawa_normalization_fixed_point_gate.json`.
