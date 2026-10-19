# Strain-only refinement at fixed radial and angular resolution

Date: 2026-10-12  
Status: **Completed numerical refinement of the supplied finite phase-record model. Not a continuum certificate or a physical electron–positron result.**

## Result

Increasing positive strain nodes from 41 to 49, while holding the other grids and the energy-cutoff rule fixed, lowers the peak internal transport rate by 4.6749%. The new rate is still expansion-directed. Whole-packet transport decreases by 2.7816% and stays positive. The product-record fraction changes by -0.003785 percentage points.

These are observed differences between two finite grids, not error estimates relative to a known exact solution or a proof of a positive continuum limit.

## Fixed model and the sole numerical change

The immediate supplied source is `pentachoron_spatial_after_angular_bundle.zip`, preserved unchanged under `inputs/`. Its 166-entry manifest and the inherited required source manifest are checked. The source note specifically requests a strain-only refinement after its combined strain/radial test.

No geometric interface, force, elastic coefficient, material connection, kinetic law, phase convention, outgoing channel definition, or incoming lowest-mode preparation rule changes. The Gaussian packet has radial K=3.30 epsilon and RMS width 0.035 epsilon. Both grids use 33 energy samples on [3.09,3.51], 28 radial cells, 25 tilt nodes, 32 hinge intervals, and source quadratures 64 and 24. The strain upper boundary stays at 2.4 and radial support at 9.6 ell, with the same infinite-exterior resolvent.

| Fixture | Positive strain nodes | Strain spacing | Radial cells | Tilt nodes | Hinge intervals |
|---|---:|---:|---:|---:|---:|
| Supplied baseline | 41 | 2.4/42 | 28 | 25 | 32 |
| New strain-only refinement | 49 | 2.4/50 | 28 | 25 | 32 |

Radial K is measured above each grid's own discretized joint ground. The shift from 3.560159199436 to 3.560628202170 epsilon is retained consistently; it is not added as incoming kinetic energy. Each grid uses a fixed eigenbasis and fixed comparison/output frames throughout its packet band.

## Matched energy-cutoff rule

Complete multiplets below 14.307336567826175 epsilon, including the common pose shift, are retained. This selects 312 one-body modes on each grid; equal counts are an outcome, not a substituted selection rule.

| Fixture | Retained modes | Last retained internal energy / epsilon | First omitted internal energy / epsilon |
|---|---:|---:|---:|
| Supplied 41-node grid | 312 | 14.295462492181 | 14.313607591825 |
| New 49-node grid | 312 | 14.306257809620 | 14.316474854345 |

The first omitted levels differ by about 0.0200%. No multiplet is split to force exact agreement. Every propagating original channel remains below the retained cutoff throughout the packet band. Higher closed modes remain truncated.

## Readouts and results

The source observables are unchanged:

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t)
    R_peak = B(t_peak)/P(t_peak),  t_peak = argmax P(t)
    R_packet = integral B(t)dt / integral P(t)dt.

P includes the hinge and both localized switching graphs. Positive current is toward larger axial factor lambda. These rates exclude selective entry and release; they are not the full mean-length derivative, individual histories, or probabilities of compressed events. The integrated ratio uses Parseval identities. Product-record flux is a different observable.

Rates below are in 10^-3/t0, where t0=hbar/epsilon. Product flux is a percentage of the full incoming preparation.

| Strain × radial grid | Peak transport | Whole-packet transport | Product-record flux | Peak time/t0 |
|---|---:|---:|---:|---:|
| 41 × 28, supplied baseline | +1.592032 | +2.534280 | 0.572719% | 8.817302 |
| 49 × 28, newly calculated | +1.517606 | +2.463787 | 0.568933% | 8.782413 |

The baseline's saved coherent kernels and all 33 four-column scattering arrays were replayed. That replay is not counted as a fresh stationary solution. The new row comes from fresh solutions and coherent energy-amplitude summation.

The new conditional mean axial factor at peak occupation is 1.075157941, with standard deviation 0.401930178. Selective entry/release contributes -0.002087062/t0; the complete mean-rate is -0.000569456/t0. Thus positive internal transport does not mean the whole conditional mean is growing at that instant.

## Checks actually performed

There are **33 completed new stationary energy solutions**, each for four prepared incoming columns, plus two central-energy solution controls using different preconditioners for the same discretized equations. No full scattering matrix is newly computed.

| Diagnostic | Largest residual |
|---|---:|
| Prepared-column flux orthogonality, all 33 energies | 1.9067e-12 |
| Full iterative equation, relative residual | 1.9929e-12 |
| Common-energy bookkeeping, epsilon units | 9.8517e-12 |
| Downstream stationary solve | 5.5621e-13 |
| Independent raw-field audit | 1.8082e-12 |
| Independent preconditioners: largest amplitude/state difference | 7.3485e-13 |
| Retained incoming eigenpairs, Frobenius residual | 8.881e-12 |

All 53 raw-field audit entries pass. They reconstruct every saved downstream stationary equation, incoming-column normalization, coherent time-dependent fields, per-strain continuity, the interior Schrodinger equation, the conditional-mean decomposition, and Parseval current/residence sums. These are implementation identities, not that many independent physical theorems or a second continuum discretization.

A separate direct energy-space Gram calculation from raw fields, without spectral-field SVD factors, reproduces the peak rate within 2.54e-11/t0 and peak time within 1.27e-07 t0. Whole-packet transport and product flux agree as well.

One resource-controlled restart releases parent-held control arrays. Completed rows, the saved eigenbasis, and comparison/output frames are preserved; incomplete work is not counted as an additional completed solution. Equations and tolerances are unchanged. Attempt logs and the checkpoint record are included.

## Energy-sampling check

Subsampling the same band from 33 to 17 energies keeps the requested packet moments. The control peak search excludes periodic Fourier replicas.

| Observable | Absolute 33-to-17 change |
|---|---:|
| New peak internal rate, 1/t0 | 2.23949678e-06 |
| New whole-packet rate, 1/t0 | 3.0909066e-06 |
| New product flux, percentage points | 0.000356656862 |

The new peak-rate change is about 0.1476%. Subsampling both baseline and new data changes their peak-rate contrast by 4.44301318e-06/t0. The positive signs and decrease under strain refinement persist. These are observed quadrature sensitivities, not rigorous bounds on uncomputed spectral structure.

## Interpretation and next test

The unchanged model's expansive sign survives this strain-only step, while the magnitude still decreases under refinement. No new crossover energy is searched. The radial, tilt and hinge grids, domains, finite internal-energy cutoff, and all physical-model assumptions remain fixed; their errors are not removed by this test.

The source remains a direct sum of phase records with uncalibrated scales and admitted material/strain connections. This supplies no physical electron–positron threshold, independently occupied product species, Lorentz-contraction law, photon identification, or measured branching fraction.

A radial-only refinement at the new 49-node strain resolution would isolate the remaining radial-grid contribution.

## Reproduction

See `README.md`. `replay.py` audits the bundled compact kernels and actual prepared columns without solving the PDE. `reproduce.py` regenerates the eigenbasis, stationary fields, packet and current audits from the unchanged source archive. Large raw fields and basis/model caches are omitted from this delivery and generated locally. No network access or repository modification is used.
