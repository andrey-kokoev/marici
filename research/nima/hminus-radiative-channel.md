# A nonzero radiative-attachment trial and a zero threshold dipole amplitude

## Question

Test H + electron -> H-minus + photon beyond energy accounting. Supply an incoming state and the standard electric-dipole interaction, then evaluate the matrix element and retain photon/ion recoil data. Active obligation: conditional interaction realization, exchange compatibility and joint energy/momentum readout. No WG electromagnetic coupling is derived.

## Declared states and coupling

Keep the compact/diffuse bound trial from `hminus-nested-orbitals.md`. Its unnormalized spatial state is

\[
\Psi_f=e^{-ar_1-br_2}+e^{-br_1-ar_2}.
\]

Choose a hydrogen 1s orbital plus a free incident plane wave along z, in the spin-singlet sector:

\[
\Psi_i=e^{-r_1}e^{ikz_2}+e^{-r_2}e^{ikz_1}.
\]

This is a continuum trial, not a solution of the interacting electron-hydrogen scattering problem. Both spatial states are exchange symmetric and combine with the antisymmetric spin singlet. Supply the length-gauge electric-dipole coupling, whose matter operator is proportional to D=r1+r2 in the fixed-core approximation. Charge, continuum normalization and photon-mode factors are omitted from the displayed coefficient, so no absolute rate is reported.

## Analytic matrix element

The Fourier transform and its derivative give

\[
\int e^{-qr}e^{ikz}\,d^3r=\frac{8\pi q}{(q^2+k^2)^2},
\qquad
\int z e^{-qr}e^{ikz}\,d^3r=\frac{32i\pi qk}{(q^2+k^2)^3}.
\]

With S(q)=8/(q+1)^3, summing the four exchange-compatible overlaps yields

\[
\frac{\langle\Psi_f|D_z|\Psi_i\rangle}{i\pi^2}
=64k\left[\frac{S(a)b}{(b^2+k^2)^3}
+\frac{S(b)a}{(a^2+k^2)^3}\right].
\]

For positive a,b this is nonzero for k>0 and vanishes linearly as k approaches zero. The checker verifies exact rational coefficients at k=0, 1/100, 1/10 and 1/2, invariance under orbital-role exchange, and the sign change under k reversal. The integral identities are derived analytically; the checker verifies their consequences rather than performing an independent scattering computation.

## Selection rules and the earlier threshold packet

The final state is an even-parity spatial S state with singlet spin. At electric-dipole order, a pure incident S wave cannot connect to it: the operator is odd. The allowed component is a singlet P wave. The chosen finite-k plane wave contains this component; its k=0 limit does not. A spin-independent E1 operator also cannot connect a triplet entrance to the singlet exit.

For incident momentum along z, the trial dipole vector lies along z. A photon along x with transverse z polarization has a nonzero coupling. For a photon along z, both transverse polarizations give zero in this trial geometry. This prevents using an unphysical longitudinal photon to infer emission.

The previous zero-incident-energy recoil packet remains a valid conditional kinematic balance, but it did not establish a nonzero E1 transition amplitude. Here that amplitude is zero at the exact threshold trial. This is not a prohibition of every higher-order channel or an exact cross-section theorem.

## Joint recoil packet

For each sampled incident momentum retain the matter amplitude coefficient, approximate incoming relative kinetic energy, photon energy and final-ion recoil. Incoming kinetics uses the hydrogen/electron reduced mass with the prior rounded mass inputs. The spatial plane-wave matrix element is still fixed-core; this is not a finite-mass scattering solution.

Let I be the initial center-of-momentum energy and F the final ion rest energy, using the existing approximate affinity. Then

\[
E_\gamma=\frac{I^2-F^2}{2I},\qquad
E_{\rm ion}=I-E_\gamma.
\]

The checker verifies E_ion^2-E_gamma^2=F^2, with equal and opposite outgoing momenta in c=1 units. At k=1/10 the model yields a nonzero dipole coefficient, photon energy approximately 0.4978508432 eV and ion recoil approximately 1.31937e-10 eV. These conditional energies are not measured line predictions.

## Disposition and verification

The declared finite-momentum trial supplies a nonzero joint radiative channel, while the previous threshold configuration fails the E1 amplitude test. Conservation is necessary but not sufficient for an allowed process. A quantitative rate requires the actual scattering state, continuum normalization, consistent radiation matrix element and bound-state accuracy. Gauge-independent length/velocity agreement is not established with these approximate states.

`python research/nima/checkers/check_hminus_radiative_channel.py` passed via `structured_command_execution:e_32876_1791227084621431800_43`; results: `results/hminus-radiative-channel.json`. Exact arithmetic checks the supplied analytic matrix-element formula, selection controls and conditional final-channel kinematics. No commit or publication is claimed.
