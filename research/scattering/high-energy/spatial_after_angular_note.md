# Strain/radial refinement with finer angular grids retained

Date: 2026-10-12  
Status: Completed numerical refinement of the unchanged supplied finite phase-record model. **Not a continuum certificate or a physical electron–positron result.**

## Result

Expansion-directed internal transport persists on the new grid. Peak transport changes from +1.784504 to +1.592032 in units 10^-3/t0, a -10.7857% change. Whole-packet transport remains positive and changes by -6.5986%. Product-record flux decreases by -0.011819 percentage points.

These are observed differences between finite grids. They are not estimates of error against a known exact limit, a proof of an asymptotic sign, or a new physical threshold.

## Fixed problem and numerical change

The Hamiltonian, geometry, elastic energy, material connections, comparison coefficients, kinetic laws, incoming lowest-mode mixture rule and outgoing record definitions are unchanged. The Gaussian packet has K=3.30 epsilon and RMS width 0.035 epsilon. The 33 spectral energies span 3.09–3.51 epsilon. Complex amplitudes are combined coherently before taking currents; no stage probabilities are multiplied.

Both calculations keep 25 material-tilt nodes, 32 hinge intervals, strain upper boundary 2.4, radial support 9.6 ell, and quadratures 64 and 24. The infinite exterior resolvent is unchanged; the radial support is not a newly imposed reflecting wall.

| Fixture | Strain nodes | Radial cells | Strain spacing | Radial cell width |
|---|---:|---:|---:|---:|
| Supplied finer-angular baseline | 33 | 24 | 2.4/34 | 9.6/24 |
| New combined refinement | 41 | 28 | 2.4/42 | 9.6/28 |

Radial K is measured above each grid's discretized joint ground. The new full incoming ground reference is 3.560159199436 epsilon. A single stored eigenbasis and consistently restored comparison/output frames are used across all energy samples.

## Common energy-cutoff rule

Complete multiplets below 14.307336567826175 epsilon, including the common pose shift, are retained. Both grids retain 312 one-body modes under that rule; equal counts are an outcome, not the selection criterion.

| Fixture | First omitted internal energy / epsilon |
|---|---:|
| Supplied baseline | 14.308917881450 |
| New refinement | 14.313607591825 |

The new last retained energy is 14.295462492181 epsilon. No boundary multiplet is split to force exact energy equality. All propagating original channels are retained throughout the packet band. Higher closed modes remain truncated.

## Same two transport readouts

Let P(t) be occupation of the hinge and both localized switching graphs, and let positive J_lambda carry amplitude toward larger axial factor lambda. The definitions are

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t)
    R_peak = B(t_peak)/P(t_peak),   t_peak = argmax P(t)
    R_packet = integral B(t) dt / integral P(t) dt.

The integrated quantities use Parseval's identity, not a chosen finite stopping time. Positive means internal expansion-directed transport. These rates exclude the separate entry/release-selection contribution and are not the full derivative of mean length, angular velocities, event histories, or percentages of compressed collisions. Product flux is a separate probability.

## Packet results

Rates are in 10^-3/t0, with t0=hbar/epsilon. Product flux is a percentage of the full incoming preparation.

| Strain × radial grid | Peak internal transport | Whole-packet transport | Product-record flux | Peak time/t0 |
|---|---:|---:|---:|---:|
| 33 × 24, inherited | +1.784504 | +2.713321 | 0.584537% | 8.891384 |
| 41 × 28, new | +1.592032 | +2.534280 | 0.572719% | 8.817302 |

The old row comes from the supplied tilt/hinge refinement archive, case combined25x32. Its saved coherent kernels and all 33 prepared-column Grams were replayed in this turn; it is not counted as a fresh PDE solution. The new row comes from fresh stationary solutions and a new coherent packet reconstruction.

The new conditional mean axial factor at peak occupation is 1.074710178, with standard deviation 0.401294461. Internal transport at that instant is positive, but entry/release selection contributes -0.002174258/t0; the full mean-rate is -0.000582226/t0. This illustrates why the signed internal rate must not be equated with total mean-length growth.

## Checks actually performed

There are 33 unique production energy solutions, each for four prepared incoming columns. Two additional central-energy control solves compare channel-diagonal/Woodbury and block-Jacobi preconditioning of the **same full finite equations**. They are not different physical models or independent continuum discretizations.

**No new full scattering matrix is computed.** The stored scattering arrays have four prepared columns; mutual flux orthogonality is checked, rather than claimed full-S unitarity.

| Diagnostic | Largest recorded residual |
|---|---:|
| Prepared-column flux orthogonality, all 33 energies | 2.16316e-12 |
| Full iterative-equation relative residual | 1.96036e-12 |
| Common-energy bookkeeping, epsilon units | 1.10045e-11 |
| Downstream stationary solver | 2.39681e-13 |
| Independent raw-field audit | 2.11586e-12 |
| Independent preconditioners, largest compared amplitude/state error | 7.40657e-13 |
| Incoming retained eigenpair check | 5.85363e-12 |

The raw-field verifier has 53 passing entries. It reconstructs downstream equations at **every saved energy**, prepared-input normalization, time-dependent fields, each strain-slice continuity balance, the interior Schrodinger equation, the conditional-mean decomposition, and raw-field Parseval current/residence integrals. Counts are implementation checks, not independent physical theorems.

A second packet calculation directly forms energy-space occupation/current Gram matrices from raw fields, without the saved spectral SVD factors. It reproduces the peak rate within 5.93e-11/t0 and the peak time within 3.02e-07 t0 under an independent peak optimization. Its integrated transport and product fraction also agree. These are algebraic/readout controls, not a second discretization of the entrance PDE.

The unchanged 167-entry latest-source manifest and 42-entry required upstream payload manifest were verified. Solver restarts preserve the exact saved eigenbasis and comparison/output frames. An initial two-worker attempt was stopped to respect the runtime memory allocation; its two completed rows were retained, and the remaining rows continued with one worker. Attempt logs and the resource control are retained; equations and tolerances were not altered.

## Energy-sampling control

Subsampling the same band from 33 to 17 energies, while matching the requested packet mean and RMS and excluding periodic Fourier replicas from the peak search, gives:

| Observable | Absolute 33-to-17 difference |
|---|---:|
| Peak internal rate, 1/t0 | 2.2035164e-06 |
| Product flux, percentage points | 0.000506589377 |
| Whole-packet rate, 1/t0 | 8.11460573e-06 |

The peak-rate difference is 0.1384% of the new peak rate. Subsampling baseline and new spectra together changes their peak-rate **contrast** by 6.84369486e-06/t0. Both controls preserve the expansive sign and the reduction under spatial refinement. These are observed quadrature differences, not rigorous spectral error bounds.

## Interpretation and limits

The new spatial step lowers the rate by 10.8% while preserving its positive sign. The magnitude remains spatial-resolution sensitive. Neither a positive continuum limit nor a crossover energy is established. Tilt/hinge resolution and the finite closed-mode energy cutoff remain fixed; further errors from those truncations are not removed by this test.

The inherited direct-sum phase-record interpretation, uncalibrated energy/length scales, chosen strain boundary and material connections remain unchanged. This result supplies no electron–positron threshold, independently occupied product species, photon identification, Lorentz-contraction law or 372:1 prediction.

A strain-only refinement on the same finer angular grid would isolate its contribution to the remaining spatial sensitivity.

## Files and reproduction

See README.md. The archive includes the required unchanged source payload, source hashes, numerical scripts, scalar receipts, prepared scattering columns, compact coherent kernels, independent-audit reports and this note. Large regenerated raw fields and basis/model caches are omitted; full regeneration creates them locally. The saved-kernel replay is distinct from regenerating the scattering solution and raw-field audit. No network access or repository mutation is needed.
