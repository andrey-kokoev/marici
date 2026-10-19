# Radial-only refinement with the strain and angular grids held fixed

Date: 2026-10-12  
Status: **Numerical refinement of the unchanged supplied finite phase-record model. Not a continuum certificate or a physical electron–positron prediction.**

## Result

Increasing the radial grid from 28 to 32 cells, while retaining 49 positive strain nodes, changes peak internal transport by -2.382413%. The new signed peak rate is +1.481450755 in units of 10^-3/t0. Whole-packet transport changes by -1.434368%, and product-record flux changes by -0.003098580 percentage points.

These are differences between two finite numerical models approximating the same declared operator. They are not error bounds against a known exact limit, evidence of a physical particle threshold, or proof of a limiting sign.

## Fixed model and sole numerical refinement

The unchanged input is `inputs/pentachoron_strain_only_refinement_bundle.zip`. Its source manifest is verified before the inherited solver and nested source payloads are loaded. Its note requested precisely a radial-only refinement on the new 49-node strain grid.

The Hamiltonian, geometric comparator, material-frame connections, restoring law, native phase matrices, positive interface coefficients, kinetic laws, output definitions and incoming lowest-mode mixture rule are unchanged. Both packets have radial center K=3.30 epsilon and RMS width 0.035 epsilon, using 33 coherent energy samples on [3.09,3.51] epsilon. Complex amplitudes are summed before taking norms and currents.

| Quantity | Supplied baseline | New radial refinement |
|---|---:|---:|
| Positive strain nodes | 49 | 49 |
| Radial cells | 28 | 32 |
| Material-tilt nodes | 25 | 25 |
| Hinge intervals | 32 | 32 |
| Radial support / ell | 9.6 | 9.6 |
| Radial cell width / ell | 0.342857142857 | 0.300000000000 |
| Strain upper boundary | 2.4 | 2.4 |
| Source quadratures | 64, 24 | 64, 24 |

The infinite-exterior resolvent is retained; the finite radial Galerkin support is not a new reflecting wall. Refinement changes the radial basis and numerical integration of the same contact region, not its physical definition.

## Energy cutoff and incoming preparation

Complete multiplets below 14.307336567826175 epsilon, including the common pose shift, are retained. Both grids use 312 one-body modes. The reconstructed internal spectrum has last retained energy 14.306257809620 epsilon and first omitted energy 14.316474854345 epsilon. Its full ground reference is 3.560628202170 epsilon.

The internal problem is unchanged because only the radial grid varies. Rebuilding its eigenbasis reproduces the supplied ground and cutoff energies within 9e-15 epsilon. Every energy sample uses the same saved eigenbasis and comparison/output frames. The lowest-mode mixture is invariant under a consistent change of basis within its degenerate subspace. All propagating incident modes remain retained; higher closed modes remain truncated.

## Observables

Let P(t) denote occupation of the hinge and both localized switching graphs. With positive J_lambda directed toward increasing axial factor lambda, retain

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t)
    R_peak = B(t_peak)/P(t_peak),  t_peak = argmax_t P(t)
    R_packet = integral B(t) dt / integral P(t) dt.

The packet integrals use Parseval identities. Conditionalization occurs only in reporting observables, not in the evolution. Positive internal transport is not the full derivative of mean axial length: selective entry and release give a separate contribution. Product-record flux is a different observable, not a rate of strain transport or a fraction of individually compressed trajectories.

## Packet results

Rates use 10^-3/t0, where t0=hbar/epsilon. Flux is a percentage of the full unit incoming preparation.

| Strain × radial grid | Peak internal transport | Whole-packet transport | Product-record flux | Peak time / t0 |
|---|---:|---:|---:|---:|
| 49 × 28, supplied | +1.517606414 | +2.463787229 | 0.568933250% | 8.782412658 |
| 49 × 32, newly calculated | +1.481450755 | +2.428447461 | 0.565834671% | 8.776620429 |

The baseline kernels and all 33 saved four-column scattering arrays were independently replayed; that is not counted as a new PDE solve. The second row comes from freshly solved stationary equations and coherent packet reconstruction.

The new conditional mean axial factor at maximum occupation is 1.075162843, with standard deviation 0.401920478. The entry/release selection contribution is -0.002051556874/t0, while the complete mean-rate is -0.000570106119/t0. This records the distinction between internal transport and the net mean-length change.

## Checks actually performed

There are 33 new production energy solutions, each with four prepared incoming columns. **No new full S matrix is computed.** The prepared-column Gram matrices are audited without relabeling them as full-matrix unitarity tests.

| Diagnostic | Largest recorded residual |
|---|---:|
| Prepared-column flux orthogonality | 1.94912e-12 |
| Full iterative equation, relative residual | 1.99567e-12 |
| Common-energy ledger / epsilon | 1.07088e-11 |
| Downstream stationary equations | 5.54521e-13 |
| Independent raw-field audit | 1.84419e-12 |

All 53 raw-field audit entries pass. The audit reconstructs every saved stationary downstream equation, prepared fluxes, time-dependent fields, strain-slice continuity, the interior Schrodinger equation, the conditional-mean balance, and independent Parseval current and residence integrals. These tests assess implementation identities, not that many independent physical claims or a second continuum discretization.

Two additional central-energy solutions compare channel-diagonal/Woodbury and block-Jacobi preconditioners on the same full finite equations. The maximum difference among their compared complex outgoing amplitudes, entrance state and downstream field is 1.9765e-12. This is an independent algebraic solution check, not a changed Hamiltonian or another continuum method.

A separate direct energy-space Gram calculation from the raw fields, without the spectral-field SVD, gives peak transport +0.001481450807/t0. Its difference from the main reconstruction is 5.23668e-11/t0. The whole-packet and product-probability comparisons are retained in the receipt.

## Energy-sampling control

Subsampling the same band from 33 to 17 nodes preserves the requested packet moments. The shorter control time search excludes periodic Fourier replicas.

| Observable | Absolute change |
|---|---:|
| Peak internal rate / (1/t0) | 2.23686246e-06 |
| Whole-packet rate / (1/t0) | 3.09010691e-06 |
| Product fraction / percentage points | 0.000354269919 |

The relative change in the new peak-rate magnitude is 0.150991%. Subsampling both baseline and new data changes their peak-rate contrast by 2.63432435e-09/t0. These are observed quadrature sensitivities, not rigorous bounds on unsampled spectral structure.

## Scope

This test isolates a radial-grid contribution at the fixed strain/tilt/hinge resolutions and finite closed-mode cutoff. No crossover energy is recomputed. The continuum limit, higher closed modes, other spatial discretizations and all physical-model assumptions remain unresolved by this one refinement.

The source remains a direct sum of phase records with uncalibrated energy and length scales. Nothing here supplies independently occupied physical particles, stability/species identity, Lorentz contraction, a photon assignment, a physical electron–positron threshold or a measured branching fraction.

## Reproduction

See `README.md`. `replay.py` audits the packaged coherent kernels and actual prepared scattering columns. `reproduce.py` regenerates the basis, stationary fields, packet and raw-field checks from the unchanged supplied archive. Large working caches and raw wavefunctions are regenerated locally and omitted from the delivery. No network access or repository write is used.
