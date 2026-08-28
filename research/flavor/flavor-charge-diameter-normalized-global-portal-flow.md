# Charge-Diameter Normalization Selects a Global Portal Flow

## Question

Can the normalization fiber of WP840 be closed by an invariant already
contained in the primitive charge source, without inserting a fitted number?

## Source-derived normalization candidate

Let (Q) be the self-adjoint primitive charge operator with spectrum
({1,2,3}). Its spectral diameter is

\[
\Delta_Q=\lambda_{\max}(Q)-\lambda_{\min}(Q)=2.
\]

The diameter is invariant under unitary weak-basis conjugation and under
common charge shifts (Q\mapsto Q+cI). Integer rescaling changes it, but the
primitive charge normalization removes every rescaling except sign; oriented
inflow fixes that sign while the diameter remains positive.

Thus (Delta_Q) is the first source-contained candidate for WP840's missing
normalization (eta).

## Diameter-normalized flow

Define the positive coupling coordinate (x=g^2) and the source flow

\[
\beta_x=\kappa x^2(1-\Delta_Qx),
\qquad \kappa>0.
\]

The overall positive (kappa) changes RG speed but neither the fixed point nor
its basin. On (x>0), the unique nonzero fixed point is

\[
x_*=\frac1{\Delta_Q}=\frac12.
\]

For (V=(x-x_*)^2),

\[
\dot V=-2\kappa\Delta_Qx^2(x-x_*)^2<0
\]

away from (x_*). Therefore the whole positive half-line is its forward RG
basin. The linear exponent is (-\kappa/\Delta_Q<0).

The oriented adjacent contrast is (q_3-q_2=1), so this source law predicts

\[
g_n-g_m=(q_3-q_2)\sqrt{x_*}=\frac1{\sqrt2}>0.
\]

This is coefficient-robust: no freely chosen relative coefficient remains,
and (kappa) affects only parametrization speed.

## What has and has not been derived

Mathematically, the construction closes four earlier fibers at once inside
the declared primitive packet:

- primitive inflow fixes the sign;
- spectral diameter fixes the dimensionless magnitude;
- the beta law fixes a unique nonzero fixed point;
- the Lyapunov identity proves its global positive basin.

However, the beta law itself is a conjectured source principle. No admitted
microscopic gauge--Yukawa action has yet been shown to generate its coefficient
ratio from (Delta_Q). The theorem therefore supplies a hard-to-vary target
for microscopic derivation, not authority to replace the actual loop beta
functions.

## Threshold hostile

The diameter is relative to the active spectrum. If the charge-one state
decouples while charges two and three remain active, then

\[
\Delta_{Q,\mathrm{active}}=1,
\qquad x_{*,\mathrm{active}}=1.
\]

The high-energy fixed value (1/2) is not the low-energy fixed value. Thus
threshold survival requires either:

1. a source theorem keeping both extremal charge sectors active throughout
   the relevant interval; or
2. a derived finite matching map transporting the high-energy prediction to
   the low-energy portal while preserving the labelled contrast.

Anomaly or primitive-charge data alone do not supply that map.

## Physical readout boundary

A labelled two-channel response can retain the adjacent contrast, whereas an
inclusive row annihilates it. Aspect's comb reference can type the common
calibration frame, but it does not derive this source flow or realize its
finite-width `physical16` response. A physical instrument still needs a named
production process, channel labels, widths, backgrounds, efficiency model,
and calibrated covariance.

## Disposition

First progressive dimensionless sign--magnitude--global-basin selector from
the primitive current itself. It remains a conjectured beta constructor, and
threshold survival plus physical realization are open. The smallest exact
falsifier of threshold stability is deletion of one extremal active charge,
which moves the selected coordinate from (1/2) to (1).

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp841_charge_diameter_normalized_global_portal_flow.py
```
