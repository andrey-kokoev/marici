# Holomorphic Mass Protection Does Not Protect the Physical Threshold

## Question

Can supersymmetric nonrenormalization supply the identity missing in WP844
while retaining the asymmetric charges?

## Common holomorphic mass

Introduce three vectorlike chiral pairs
((\Phi_i,\widetilde\Phi_i)) with charges ((q_i,-q_i)) for
(q_i=1,2,3), and the gauge-invariant superpotential

\[
W=m\sum_{i=1}^3\Phi_i\widetilde\Phi_i.
\]

Holomorphy can protect the common superpotential parameter (m). This is
stronger than the unconstrained tree mass of WP844 and is therefore the
natural first nonrenormalization candidate.

## Canonical physical masses

The physical thresholds depend also on the Kähler metrics. With diagonal
wavefunction factors,

\[
m_i^{\rm phys}
=\frac{m}{\sqrt{Z_i\widetilde Z_i}}.
\]

The gauge-covariant hostile

\[
Z_i=\widetilde Z_i=e^{\kappa q_i^2t},
\qquad \kappa,t>0,
\]

leaves the holomorphic mass untouched but gives

\[
m_i^{\rm phys}=m e^{-\kappa q_i^2t}.
\]

Consequently

\[
\frac{m_2^{\rm phys}}{m_1^{\rm phys}}=e^{-3\kappa t},
\qquad
\frac{m_3^{\rm phys}}{m_2^{\rm phys}}=e^{-5\kappa t}.
\]

The thresholds are distinct for every positive (\kappa t). This is an
allowed charge-dependent wavefunction hostile, not a claim that the displayed
exponential is a complete loop calculation.

## Required Kähler cancellation

To keep all physical masses equal, the total anomalous dimensions must be
common across the three pairs. Removing the scalar average from the gauge
contribution gives

\[
\Gamma_{\rm tl}
=\kappa\left(Q^2-\frac{14}{3}I\right).
\]

Thus an additional interaction sector must contribute exactly

\[
\Gamma_Y^{\rm tl}
=-\kappa\left(Q^2-\frac{14}{3}I\right),
\]

the same traceless cancellation isolated in WP844. Holomorphic
nonrenormalization does not derive this Kähler identity. It transfers the
problem from the mass parameter to wavefunction normalization.

## Compatibility with the portal flow

Yukawa interactions can contribute with the needed signs to anomalous
dimensions, but their tensor and fixed-point values must be derived from the
same source. Choosing them to cancel the three charge-dependent entries is
exactly the WP842 interaction-tensor tuning unless a unique Ward identity or
extended multiplet construction forces the cancellation.

Because (Q) has simple unequal eigenvalues, an ordinary flavor symmetry
commuting with the charge source cannot enforce a common Kähler metric. A
larger symmetry would have to act on (Q) as a spurion and remain strong
enough after the asymmetric background is selected to protect the physical
thresholds.

## Disposition

Negative for ordinary holomorphic mass protection. The superpotential mass
can remain common while the physical pole thresholds split. A successful
supersymmetric source principle requires an additional all-order Kähler or
physical-pole nonrenormalization theorem that cancels the complete traceless
charge anomalous dimension without erasing the portal orientation. Finite
matching and calibrated `physical16` readout remain open.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp845_holomorphic_mass_wavefunction_threshold_splitting.py
```
