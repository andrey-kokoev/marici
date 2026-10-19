# Second combined spatial refinement at the matched energy cutoff

Date: 2026-10-12
Status: Completed numerical refinement of the supplied finite phase-record model. Not a continuum certificate or a physical electron–positron result.

## Result

The new peak internal transport is +1.872338 in units 10^-3/t0. It is expansion-directed. Relative to the preceding 25-by-20 combined grid, the signed rate changes by -19.929%. Product-record flux changes by -0.025974 percentage points. These are measured finite-grid differences, not estimated errors relative to an exact limit.

## Fixed model and comparison

The Hamiltonian, geometry, elastic energy, comparison coefficients, material-frame connections, outgoing record channels, incoming lowest-mode mixture rule, and Gaussian packet are unchanged. K=3.30 epsilon is radial energy above each discretized ground, sigma_K=0.035 epsilon. The domain remains 0<lambda<2.4 and radial Galerkin support 9.6 ell, with the inherited infinite exterior resolvent. Tilt remains 17 nodes, hinge 24 intervals, source quadratures 64 and 24. The new grid has 33 strain nodes and 24 radial cells. Its spacings are 2.4/34 and 9.6/24, respectively. No radial reflecting wall or physical strain tolerance is introduced.

The shared spectral selection threshold is 14.307336567826175 epsilon including the pose shift. Complete multiplets below this threshold give 306 retained one-body modes. The last retained energy is 14.304420061452 epsilon and first omitted energy is 14.309987252634 epsilon. The prior first omitted energy was 14.311808943 epsilon. A multiplet is not split to force exactly equal omitted energies. All propagating channels remain retained throughout the packet band.

The new total joint ground reference is 3.559320673795 epsilon. One fixed incoming eigenbasis and fixed output/comparison frames are used across the whole energy band. The two incoming ground modes per body, four total prepared columns, are averaged with their inherited weights. No independent physical particle interpretation is added.

## Observables

Let P(t) be occupation of the hinge and both localized switch graphs, and let positive J_lambda transport amplitude toward larger lambda. Define B(t)=Delta_lambda sum_j J_(j+1/2)(t), R_peak=B(t_peak)/P(t_peak), with t_peak maximizing occupation. R_packet=integral B dt / integral P dt is calculated by Parseval from the stationary fields. The two are different readouts. Neither is the full derivative of mean length, which also contains selective entry and release. Product flux is a separate probability, not a strain current.

## Comparison table

| Grid (strain, radial) | Retained modes | Peak transport, 10^-3/t0 | Whole-packet transport, 10^-3/t0 | Product-record flux | Peak time/t0 |
|---|---:|---:|---:|---:|---:|
| 17, 16 | 320 | +3.224491 | +3.843627 | 0.660529% | 9.498319 |
| 25, 20 | 310 | +2.338335 | +3.199296 | 0.600574% | 9.043116 |
| 33, 24 | 306 | +1.872338 | +2.793354 | 0.574600% | 8.872923 |

The first two rows are inherited numerical receipts, not fresh PDE solutions. The third is newly calculated. No crossover energies are located in this single-packet test.

## Actual calculation and checks

There are 33 new distinct stationary grid/energy rows on 3.09<=K/epsilon<=3.51, extending six RMS widths on each side. Every row solves the four prepared columns of the unchanged source equations by matrix-free GMRES. The wave amplitudes, not their probabilities, are summed coherently to reconstruct the packet. Source Gaussian moment matching and local peak refinement are retained.

The primary preconditioner is the inherited channel-diagonal radial/Woodbury preconditioner. A separate central-energy solve uses block-Jacobi preconditioning, and is compared in complex outgoing amplitudes, the complete entrance state, and the downstream field. This is an independent algebraic solution check of the same discretized equations, not a second independent continuum discretization. Two additional central control solutions are separate from the 33 stored production rows.

**No full scattering matrix is computed on the new grid.** Stored S arrays contain four prepared columns. Their mutual flux orthogonality is audited; it must not be described as full S-matrix unitarity. The inherited older-grid full-S checks are not relabeled as new.

The independent raw-field audit contains 29 passing tests. It reconstructs downstream stationary equations, individual prepared-column fluxes, coherent time-dependent fields, per-strain continuity, the internal Schrodinger equation, mean-strain decomposition, and Parseval integrals. A separate audit recomputes all 33 saved column Gram matrices. Counts are implementation checks, not independent physical theorems.

| Diagnostic | Largest recorded residual |
|---|---:|
| prepared_orthogonality | 2.12104e-12 |
| linear_equation | 1.99916e-12 |
| energy_ledger | 8.53007e-12 |
| downstream | 2.24097e-13 |
| independent_raw_audit | 2.03959e-12 |
| independent_preconditioner | 1.53948e-12 |
| eigen_residual | 4.67325e-12 |

## Spectral sampling control

Subsampling the same complete band from 33 to 17 nodes preserves the requested packet moments. The shorter control time window avoids periodic Fourier replicas. Observed absolute changes are:

- transport_peak: 9.17039453194e-06.
- rate_per_residence: 1.56620344711e-05.
- product_probability: 6.52243803895e-06.
- peak_time: 0.00472578217912.
- mean_lambda_at_peak: 2.77118601728e-05.

These differences are quadrature controls, not rigorous bounds on an infinite spectral integral. The source phase reference and Hamiltonian are unchanged.

## Remaining uncertainty

This test refines strain and radial discretization together at one finite internal-energy threshold. It does not independently refine the tilt grid, hinge, source quadratures, strain domain, or high closed-mode cutoff. No extrapolated continuum current, sign-change energy, physical speed, Lorentz contraction, photon species, or experimental branching fraction is inferred. The model still uses direct sums of retained phase records rather than independently occupied particles.

A useful next independent control is tilt and hinge refinement at the same spectral threshold, rather than interpreting the small linear-solver residual as a spatial error bound.

## Reproduction

The supplied earlier pentachoron_time_resolved_strain_bundle.zip is required for full regeneration. Run:

```sh
python prepare_sources.py --packet /path/to/pentachoron_time_resolved_strain_bundle.zip
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python probe_second.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_second.py --case second33x24 --nlam 33 --nD 24 --points 33 --independent-control
OPENBLAS_NUM_THREADS=1 python analyze_matched.py --case second33x24 --cutoff 306
OPENBLAS_NUM_THREADS=1 python verify_second.py --case second33x24 --cutoffs 306
python finalize_second.py
```

The compact archive omits raw fields, large eigenbasis/model caches and the unchanged 118 MB source archive. Raw fields were independently audited before packaging and can be regenerated. The delivered coherent kernels support a smaller saved-readout replay. No network access or repository mutation is performed.
