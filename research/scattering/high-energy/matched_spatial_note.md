# Spatial refinement with a matched omitted-mode energy threshold

Date: 2026-10-12  
Status: **New completed finite-model convergence tests at one packet center. Not a continuum certificate, physical electron–positron result, or calibrated speed law.**

## 1. Result

The three new spatial fixtures retain internal eigenmodes to essentially the same energy threshold as the supplied 320-mode baseline. The reported signed strain current is reconstructed from one coherent packet in each fixture; it is not inferred from a monochromatic probability or a fixed-strain table.

All three newly refined fixtures have positive peak-time and whole-packet internal transport. The combined refinement lowers the peak rate by 27.482% relative to the supplied baseline. The expansion-directed sign survives these tests, but the magnitude remains spatially sensitive. No sign-change energy is recomputed.

## 2. Unchanged model and packet

The immediate reference is `pentachoron_targeted_cutoff_bundle.zip`, especially `targeted_cutoff_note.md`, which requests spatial refinement at comparable omitted internal energy. Its full packet baseline is retained as supplied, not advertised as freshly regenerated. The unchanged stationary equations, geometry, material connections, elastic law, source coefficients, output channels and preparation rule are restored from the earlier supplied `pentachoron_time_resolved_strain_bundle.zip` and its hash-verified nested sources.

The target has mean radial energy K=3.30 epsilon and RMS width 0.035 epsilon. As in the source, K is measured above each discretized joint ground. Refining that ground is not changing the physical preparation rule. All energies share a fixed eigenframe within a fixture. The prepared equal ground-mode mixture, phase convention and Gaussian moment-matching rule remain unchanged.

The tilt grid stays at 17 Fourier nodes, the hinge at 24 intervals, and source quadratures at 64 and 24. The strain upper boundary stays 2.4 and the radial Galerkin support remains 9.6 ell. Outside it the source infinite-half-line nonlocal resolvent is retained; no new reflecting radial wall is inserted.

## 3. Match energies, not mode counts

The common cutoff is 14.307336567826175 epsilon, including the same pose-energy shift. Complete multiplets below that threshold are retained. The first omitted multiplet is not split or relabeled to force an exact numerical energy match.

| Fixture | Strain nodes | Radial cells | One-body modes | Last retained internal energy / epsilon | First omitted internal energy / epsilon |
|---|---:|---:|---:|---:|---:|
| supplied_baseline | 17 | 16 | 320 | 14.304995021 | 14.307336568 |
| strain25 | 25 | 16 | 310 | 14.302646872 | 14.311808943 |
| radial20 | 17 | 20 | 320 | 14.304995021 | 14.307336568 |
| combined25x20 | 25 | 20 | 310 | 14.302646872 | 14.311808943 |

Thus the two omitted-energy thresholds differ by approximately 0.0313%, while the number of retained modes differs. All propagating channels remain below each cutoff throughout the packet band. Higher closed modes remain truncated, so a matched finite cutoff does not remove all truncation error.

## 4. Same two current readouts

Let P(t) be total occupation of the hinge and both localized switching graphs. If J_(j+1/2) is signed current toward increasing axial factor lambda, use

    B(t) = Delta_lambda sum_j J_(j+1/2)(t),
    R_peak = B(t_peak)/P(t_peak),  t_peak = argmax P(t),
    R_packet = integral B(t)dt / integral P(t)dt.

Positive values mean internal transport toward expansion; negative values mean transport toward compression. This is not the full derivative of conditional mean length: selective entry and release provide the separate term retained by the source continuity identity. These are not individual trajectories or percentages of compressed events. The integrated ratio uses Parseval identities rather than an arbitrary finite stop time.

## 5. Computed packet results

Both rates below are in 10^-3/t0, with t0=hbar/epsilon. Product flux is a different observable, quoted as a percentage of the initial unit preparation.

| Fixture | Peak internal transport | Whole-packet transport | Product-record flux | Peak time / t0 |
|---|---:|---:|---:|---:|
| supplied_baseline | +3.224491 | +3.843627 | 0.660529% | 9.498319 |
| strain25 | +2.515602 | +3.370165 | 0.616471% | 9.073165 |
| radial20 | +3.023178 | +3.651162 | 0.643268% | 9.473270 |
| combined25x20 | +2.338335 | +3.199296 | 0.600574% | 9.043116 |

Relative to the supplied baseline, the combined-grid peak rate changes by -27.482%. The combined-grid product fraction changes by -0.059955 percentage points. These are observed finite-grid differences, not error bounds or an extrapolated limit.

## 6. Numerical methods and independent checks

There are 99 distinct newly calculated grid/energy rows: 33 per fixture on 3.09 <= K/epsilon <= 3.51. Each central energy has a full direct source scattering solve. An independent matrix-free GMRES solve of precisely the same full linear equations is compared with its complex prepared amplitudes and complete downstream fields. The other energies solve the four prepared incoming columns, not every possible incoming column.

The primary preconditioner inverts the channel-diagonal radial problem and includes the low-rank connected response by an exact Woodbury step. It only accelerates the solution of the same equations. True residuals use the complete source matrix. An initial pilot used block-Jacobi preconditioning; its source-equation solution and audit are retained. No Hamiltonian, basis, interaction or quadrature was changed by preconditioning.

It would be incorrect to call the prepared-column orthogonality checks full S-matrix unitarity tests. The source-format row key `unitarity_residual` is accompanied by `full_S_computed=false` on iterative prepared-only rows. The actual full-S checks are the three direct central-energy tests.

| Check | Largest recorded residual |
|---|---:|
| Full-S unitarity at the three reference energies | 2.084e-13 |
| Prepared-column flux orthogonality across other energies | 2.271e-12 |
| Full iterative-equation relative residual | 1.991e-12 |
| Common-energy ledger / epsilon | 9.183e-12 |
| Direct versus iterative complex amplitude/field discrepancy | 7.466e-13 |
| Independent raw-field/current audit residual | 2.217e-12 |

The independent raw-field audit freshly reconstructs downstream equations, every prepared flux column, coherent time-domain states, each strain-slice continuity balance, the interior time-domain equation, and Parseval current/residence integrals. All three fixtures pass. The source diagnostic Gram matrices are not treated as a substitute for these raw-field checks. The compact delivered kernel replay is a separate, narrower reconstruction audit.

## 7. Energy sampling control

The complete 33-node spectra are subsampled to 17 nodes with the same requested packet moments. The shorter control time window avoids periodic Fourier replicas. The table gives observed absolute changes, not quadrature error bounds.

| Fixture | Peak-rate change / t0 | Integrated-rate change / t0 | Product change, percentage points |
|---|---:|---:|---:|
| strain25 | 8.6089e-06 | 1.4376e-05 | 0.0002793 |
| radial20 | 3.1857e-06 | 7.4567e-06 | 0.0004897 |
| combined25x20 | 8.5873e-06 | 1.4367e-05 | 0.0002673 |

## 8. Limits and next check

The measured finite-grid transport is not a physical strain trajectory, electron–positron threshold, species-identification result, speed-to-compression law, or Lorentz-contraction calculation. No new force, geometric arrow, packet state or fitted experimental parameter is introduced.

This comparison controls the spectral cutoff more closely than simply holding its mode count fixed. It does not establish a continuum limit: tilt and hinge remain unrefined, higher closed modes remain omitted, and only one packet center is tested. Small conservation residuals must not be confused with spatial accuracy.

A second combined strain/radial refinement at the same spectral threshold would test the direction and size of the remaining spatial change before any crossover energy is treated as settled.

## 9. Reproduction and delivered artifacts

`README.md` documents restoration of the unchanged earlier source archive, mode reconstruction, checkpointed stationary calculations, packet reconstruction and independent audit. The compact bundle contains all numerical rows, complex diagnostic kernels, saved S columns with their scope flags, scripts, source hashes and verification reports. Large raw fields and disposable nested caches can be regenerated; their audits were completed before packaging. No repository files were modified.
