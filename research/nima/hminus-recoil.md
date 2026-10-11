# Finite-proton recoil and an explicit attachment complement

## Question

Add the recoil omitted by the fixed-center H-minus benchmark. Separate internal nuclear motion from momentum and energy carried by the surroundings during attachment. The supplied complement is one photon plus the recoiling final ion; this is not a model of the whole universe. Active obligation: center-of-mass separation and final-channel energy/momentum accounting.

## Internal nuclear recoil

Use the prior rounded mass ratio M=1836.152673 in electron-mass units. For electron coordinates relative to the proton, separating total center-of-mass motion gives

\[
H_{\rm int}=\frac{p_1^2+p_2^2}{2\mu}+\frac{p_1\cdot p_2}{M}
-\frac1{r_1}-\frac1{r_2}+\frac1{r_{12}},
\qquad \mu=\frac{M}{M+1}.
\]

The cross-momentum term is the mass-polarization contribution. It must not be discarded merely because the proton is heavy.

In the previous symmetrized compact/diffuse s-orbital trial, the wavefunction has no explicit inter-electron angular dependence. Every cross-gradient expectation contains a factor cos(theta), whose angular integral is zero. Thus the mass-polarization expectation vanishes within that restricted family. Common orbital scaling by mu gives E_M=mu*E_infinity and hydrogen threshold -mu/2. The optimal exponent ratio is unchanged.

An exact correlated control with scaled pair factor 1+r12/5 instead gives expectation p1 dot p2=29/423 at unit exponent. This confirms that the omitted angular structure can contribute: zero in the restricted trial is not a zero-operator theorem or a universal recoil cancellation.

### Calibration must move consistently

Keeping the old numerical energy unit fixed would lower the calculated affinity by about 0.0001969313 eV. But that unit was defined by calibrating hydrogen to 13.5984 eV, not supplied independently. Repeating that same calibration with finite-mass hydrogen changes the unit from 2*B_H to 2*B_H/mu. Common reduced-mass scaling then cancels from the calibrated affinity in this trial family, retaining Q approximately 0.3617928244 eV.

This cancellation depends on the restricted radial ansatz and calibration convention. It is not a claim that physical isotope shifts or finite-mass corrections vanish.

## Recoil of an explicit complement

Consider threshold H plus a free electron in their initial center-of-momentum frame. Declare the final channel to contain H-minus and one photon. This is a kinematic candidate, not a proof that its transition amplitude is nonzero at threshold.

Write initial total rest energy I=(M+2)m_e*c^2-B_H and final ion rest energy F=I-Q. Two-body relativistic kinematics gives

\[
E_\gamma=\frac{I^2-F^2}{2I}=Q-\frac{Q^2}{2I},
\qquad T_{\rm recoil}=\frac{Q^2}{2I}.
\]

The momenta are equal and opposite, of magnitude E_gamma/c. Using the same rounded electron rest-energy input as the prior benchmark:

| Energy readout | eV |
|---|---:|
| Model attachment release Q | 0.36179282442336 |
| Photon | 0.36179282435368 |
| Ion center-of-mass recoil | 0.00000000006967682 |

Exact rational checks verify energy conservation, momentum conservation and the final ion mass shell. A control that assigns all Q to the photon but leaves the ion at rest fails its mass shell by -Q^2. The photon and ion entries are both retained in the output; no energy is silently discarded into an unspecified reservoir.

## Disposition and verification

The model now includes finite-proton internal kinetics and a minimal specified radiative complement. The recoil is small for this toy affinity, but its conservation role is exact. Photon polarization, emission direction distribution, transition selection rules and capture rate require a radiation coupling and prepared initial state. No such dynamics, WG recoil law or universal environment has been derived. Nonrelativistic approximate bound energies are inputs to exact final-channel kinematics, not a complete relativistic atomic calculation.

`python research/nima/checkers/check_hminus_recoil.py` passed via `structured_command_execution:e_32876_1791226740000580900_40`. Results: `results/hminus-recoil.json`. The prior rounded inputs were reused, not independently precision-audited. No commit or publication is claimed.
