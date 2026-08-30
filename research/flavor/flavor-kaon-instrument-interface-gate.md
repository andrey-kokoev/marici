# Neutral-kaon instrument interface gate: WP454

## Question

Can the WP453 current-orientation coefficient be mapped directly to an experimentally calibrated neutral-kaon constraint?

## Source operator pattern

The diagonal flavor current is vectorlike. In the chiral operator coordinates (O_{LL},O_{RR},O_{LR}),

\[
(J_L+J_R)^2=O_{LL}+O_{RR}+2O_{LR}.
\]

Its coefficient ray is therefore

\[
(C_{LL},C_{RR},C_{LR})\propto(1,1,2).
\]

This correlation is fixed by the source representation and may not be discarded when applying a bound.

## Available instrument excerpt

The [2025 Particle Data Group CKM review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf), Section 12.5, illustrates high-scale flavor constraints with the isolated operator

\[
(\bar q_i\gamma_\mu P_Lq_j)^2
\]

and states that existing kaon-mixing data require (\Lambda/\sqrt{|z_{sd}|}) to exceed about (10^4) TeV for a generic coefficient.

That displayed readout is rank one on the three-dimensional chiral operator packet. Its kernel has dimension two. It is not a calibrated likelihood for the correlated source ray ((1,1,2)), whose LR component has different RG evolution and hadronic matrix elements.

## Formal diagnostic, not admitted bound

If one incorrectly retained only the LL component, WP453's hostile coefficient magnitude (1/(12\mu^2)) would give

\[
\mu>\frac{5000}{\sqrt3}\ {\rm TeV},\qquad
f>5000\sqrt2\ {\rm TeV},
\]

and, using (v=0.246) TeV,

\[
\frac f v>\frac{2{,}500{,}000\sqrt2}{123}.
\]

These values are retained only as an order-of-magnitude projected diagnostic. They are not constraints on WP447 because the projection deletes the correlated RR and LR source components. Nor would such a lower bound source-select (g_Ff/v); (g_F) remains independent.

## Missing common-frame constructor

An admitted bound needs, in one named convention:

- the correlated Wilson vector at the flavor-gauge matching scale;
- its full operator-mixing RG transport;
- lattice matrix elements and covariance;
- the experimental likelihood, including Standard Model interference;
- support and uncertainty assumptions.

Neutral-kaon mixing is a real physical instrument class. The currently extracted single-operator number is not yet the response matrix for this source.

## Smallest exact falsifier

A published common-scale likelihood or response matrix for the correlated ((1,1,2)) ray that yields a stable nonzero bound after RG and hadronic uncertainties closes the interface gate.
