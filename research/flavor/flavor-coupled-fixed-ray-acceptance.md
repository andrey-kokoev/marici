# Coupled gauge–Yukawa fixed-ray acceptance gate

## Why this gate is needed

WP480 closes the gauge-only fixed-point route after the messenger triplication
required by the isotropic portal. Gauge–Yukawa theories can nevertheless admit
weak interacting fixed points after asymptotic freedom is lost; this mechanism
requires a correlated Yukawa nullcline rather than a gauge root in isolation.
The general possibility is established in the source literature, for example
[Litim and Sannino](https://arxiv.org/abs/1406.2337). WP481 does not assume that
their particular model or coefficients apply to flavor.

## Reduced exact theorem

Write a generic leading reduced system as

\[
\beta_{\alpha_g}=2\alpha_g^2
(A+C\alpha_g-D\alpha_y),
\]

\[
\beta_{\alpha_y}=2\alpha_y
(E\alpha_y-F\alpha_g),
\]

with positive coefficients and `A>0` representing loss of asymptotic freedom.
The interacting Yukawa nullcline is

\[
\alpha_y={F\over E}\alpha_g.
\]

On it, the unique nonzero gauge root is

\[
\alpha_g^*={A\over DF/E-C},
\qquad
\alpha_y^*={F\over E}\alpha_g^*.
\]

A positive root exists exactly when

\[
{DF\over E}-C>0.
\]

Perturbative authority additionally requires `alpha_g*` to be much smaller
than one. WP480 supplies the one-loop loss term, but the actual `C,D,E,F` of
the triplicated flavor action have not been computed.

## Selector propagation along a fixed ray

Normalize the fixed ray by

\[
y_Q^2=16\pi^2r_Q\alpha_g,
\quad y_\Phi^2=16\pi^2r_\Phi\alpha_g,
\quad \eta=16\pi^2r_\eta\alpha_g.
\]

Substitution into the WP478 threshold and WP477 normal form gives

\[
c={3k_\Phi r_Qr_\Phi
\over16\pi^2r_\eta y_{\rm geom}^2},
\]

\[
{g_Ff\over v}
=4\pi y_{\rm geom}
\sqrt{{r_\eta\over k_\Phi r_Qr_\Phi}}.
\]

The fixed-point magnitude and common scale cancel. Therefore a complete
source-derived fixed ray would genuinely select the requested ratio. It must
derive all ray ratios; finding only `alpha_g*` is insufficient.

## Predeclared acceptance conditions

Before inspecting the target value, a concrete successor must:

1. Derive `A,C,D,E,F` from the complete triplicated action in one scheme.
2. Prove `DF/E-C>0` and a controlled positive fixed point.
3. Derive every Yukawa and quartic ray ratio entering `c`.
4. Prove scalar stability and RG preservation of the equal-port Gram.
5. Perform finite messenger-threshold matching and prove that `c` descends.
6. Keep messenger and charged-scalar channels above the vector poles before
   reusing the frozen widths.
7. Only then compare the predicted `c` with kaon, Higgs, and pole instruments.

The five-TeV benchmark is retained solely as a withheld test. It requires

\[
{y_{\rm geom}^2r_\eta\over k_\Phi r_Qr_\Phi}
={R_*^2\over16\pi^2},
\]

but this equality may not be used to choose the beta-function coefficients or
ray ratios.

## Disposition

WP481 is an exact acceptance theorem, not evidence that the concrete flavor
theory has the required fixed point. Its smallest falsifier is
`DF/E-C<=0`. No selector, rigidifier, instrument, or reference port is admitted
until the actual action passes every condition above.
