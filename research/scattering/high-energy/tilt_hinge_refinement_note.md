# Independent tilt and hinge refinement at a matched internal-energy cutoff

Date: 2026-10-12
Status: Completed numerical tests of the unchanged supplied finite phase-record model. Not a physical electron–positron result or a continuum certificate.

## Result

Expansion-directed peak internal transport persists in all three new angular refinements. Tilt-only refinement changes the peak rate by +0.5757%; hinge-only refinement by -5.2746%; the combined refinement by -4.6911%, relative to the supplied 17-tilt/24-hinge baseline. These changes are smaller than the preceding 19.929% strain/radial-grid change, but do not certify any continuum limit. Whole-packet signed transport also remains positive.

The combined product fraction changes by +0.009937 percentage points. Product flux and signed strain transport are separate observables; their changes need not have the same sign.

## Fixed problem

K=3.30 epsilon; incoming Gaussian RMS width 0.035 epsilon. Strain nodes=33, radial cells=24, strain upper boundary=2.4, radial support=9.6 ell, source quadratures=64 and 24. The same Hamiltonian, prepared lowest-mode mixture rule, phase-frame conventions and asymptotic output definitions are retained. Radial K is measured above each discretized incoming ground. Every packet uses 33 energies on [3.09,3.51].

Tilt and hinge resolutions are changed separately and together. The internal selection threshold is 14.307336567826175 epsilon including the retained pose shift. Complete multiplets below it are retained, rather than forcing the same mode count or splitting a multiplet. All propagating channels remain below the cutoff. Closed-mode truncation is not thereby eliminated.

## Observables

R_peak=B(t_peak)/P(t_peak), where P is occupation of the hinge and both localized switching graphs, t_peak maximizes P, and B=Delta_lambda sum J_lambda. Positive means internal transport toward larger axial factor. This excludes entry/release selection and is not the full mean-length derivative. R_packet=integral B dt / integral P dt uses the stationary-field Parseval identity. Product-record flux is a separate probability. No individual histories or physical particle species are assigned.

## Results

Rates are in 10^-3/t0, t0=hbar/epsilon. Flux is a percentage of the full incoming unit preparation.

| Fixture | Tilt nodes | Hinge intervals | Modes | Peak transport | Whole-packet transport | Product flux |
|---|---:|---:|---:|---:|---:|---:|
| supplied baseline | 17 | 24 | 306 | +1.872338 | +2.793354 | 0.574600% |
| tilt25 | 25 | 24 | 312 | +1.883117 | +2.801871 | 0.573865% |
| hinge32 | 17 | 32 | 306 | +1.773579 | +2.704671 | 0.585288% |
| combined25x32 | 25 | 32 | 312 | +1.784504 | +2.713321 | 0.584537% |

The baseline is inherited; the other three rows are new stationary solves and coherent packet reconstructions. These are finite-grid observations, not error bounds or extrapolated limits. No new sign-change energy is searched.

## Checks actually performed

There are 99 new stationary grid/energy rows, with four prepared incoming columns per row. No full S matrix is computed on the new grids. Largest prepared-column orthogonality residual: 1.90921e-12; full linear-equation relative residual: 1.98723e-12; energy-bookkeeping residual: 9.49996e-12 epsilon. All amplitude/current reconstruction audits passed (87 entries; not that many independent theorems). Largest raw-field audit residual: 1.83686e-12.

The separate audit reconstructs downstream stationary equations, individual prepared-channel fluxes, actual time-dependent fields and their strain currents, every strain-slice continuity balance, the interior Schrodinger equation, the conditional-mean decomposition, and independent Parseval current/residence sums. It does not merely read source success flags. It is not a second independent discretization of the entire continuum entrance problem.

## Energy quadrature

The same spectra are subsampled from 33 to 17 energies, with packet moments matched and a shortened time search to exclude periodic Fourier replicas. Absolute differences:

| Fixture | Peak-rate difference (1/t0) | Product-flux difference (percentage points) |
|---|---:|---:|
| tilt25 | 9.1635837e-06 | 0.00065138783 |
| hinge32 | 9.055444e-06 | 0.00067291229 |
| combined25x32 | 9.0472113e-06 | 0.00067199593 |

These are observed quadrature checks, not rigorous bounds on all unsampled spectral structure. Paired contrasts with the baseline are also saved: all compared models are subsampled together, rather than comparing a refined packet against an unrelated quadrature.

### Paired quadrature contrast control

Subsampling the baseline and each new fixture together changes the estimated peak-rate refinement contrast by only about 6.81e-9/t0 (tilt), 1.15e-7/t0 (hinge), and 1.23e-7/t0 (combined). These smaller paired differences should not be confused with the roughly 9e-6/t0 individual packet-rate quadrature changes. They support the reported refinement contrasts within this numerical experiment, not an error bound on the continuous problem.

## Remaining uncertainty

The strain/radial grid, finite internal-energy cutoff, interaction quadratures, domain and constitutive choices remain fixed. Agreement on a sign at these grids is not a proof of its continuum limit. The model still uses direct sums of phase records rather than independently occupied physical particles; no calibrated electron speed, Lorentz contraction, photons or 372:1 branching ratio is inferred.

## Reproduction

See README.md. The supplied unchanged pentachoron_time_resolved_strain_bundle.zip is required for full regeneration. This compact archive retains scripts, provenance, prepared S columns, scalar receipts, coherent diagnostic kernels, time arrays, and raw-field audit reports. Large regenerated fields, eigensystem/model caches, and the unchanged source archive are omitted. No network access or repository mutation is needed.
