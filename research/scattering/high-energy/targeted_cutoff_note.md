# Targeted closed-mode refinement at K = 3.30 epsilon

Date: 2026-10-12  
Status: **Completed finite-model cutoff test. Not a continuum certification or physical electron–positron prediction.**

## Result

The three newly tested peak-occupation internal-transport rates are all positive (expansion directed). The signed change from 272 to 320 retained modes is +3.0441%. The entire 240–320 tested range spans 3.7168% of its smallest rate. These are observed changes, not bounds on uncomputed modes.

The supplied previous calculation gave +2.035797 and +2.929980 in units 10^-3/t0 at 176 and 208 modes, respectively. Those baseline values are read from the supplied archive, not rerun here. Their approximately 44% difference motivated this targeted test.

## Fixed model and numerical design

No Hamiltonian term, force, geometric interface, material connection, kinetic law, elastic coefficient, incoming mixture, or outgoing channel definition changes. The spatial fixture remains 17 positive strain nodes, 17 material-tilt nodes, 16 radial cells and 24 hinge intervals; source quadratures remain 64 and 24. The strain boundary is 2.4 and radial support is 9.6 ell. All source constants and common pose energy are unchanged.

The target packet has mean radial energy K=3.30 epsilon and RMS width 0.035 epsilon. It uses the same equal ground-mode mixture and source phase convention. Radial energy is measured above the fixed-grid joint ground 3.55301325410161 epsilon. Rates use t0=hbar/epsilon. No conversion to a physical beam speed is made.

A single 320-column incoming eigensystem is constructed. The 240- and 272-column spaces are nested prefixes with complete boundary multiplets; their prepared ground columns and all downstream operators are identical. Independent source construction recovers the projected entrance potential and sample matrices with zero saved entry difference. The high-eigenpair residual is recorded, not interpreted as physical error.

First omitted full internal energies are approximately 12.224154, 12.879083 and 14.307337 epsilon. They exceed every total energy in the packet band. Thus newly retained modes are closed modes affecting virtual propagation; no previously omitted open incoming channel is introduced.

## Packet calculation and meaning of the readout

Each cutoff has 33 freshly solved stationary energies on 3.09 <= K/epsilon <= 3.51. There are 99 distinct new cutoff/energy solutions. The band extends six target standard deviations either side of the center. The Gaussian is normalized with the inherited moment-matching convention; all energies share fixed complex phase frames. The finite-band numerical preparation is a truncation of the same target Gaussian, not an independent state selected at each energy.

Let P(t) denote occupation of the hinge and both localized switching graphs. With positive strain current directed toward larger lambda, define

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t),
    R_peak = B(t_peak)/P(t_peak),
    t_peak = argmax_t P(t),
    R_packet = integral B(t)dt / integral P(t)dt.

The second ratio uses Parseval integrals of the coherent stationary fields. Conditionalization occurs only in readout. The peak rate excludes selective entry and release and is not the full derivative of mean length, an individual trajectory, or a percentage of compressed events.

Complex amplitudes are summed before taking currents. The time search uses the inherited interval -200 to 400 t0 and local refinement of the highest sampled occupation maximum. No sign-change energies are searched or recalculated.

| One-body modes | Peak internal transport, 10^-3/t0 | Whole-packet transport, 10^-3/t0 | Product-record flux | Peak time, t0 |
|---:|---:|---:|---:|---:|
| 240 | +3.108938 | +3.742787 | 0.664840% | 9.504067 |
| 272 | +3.129233 | +3.761619 | 0.662564% | 9.494459 |
| 320 | +3.224491 | +3.843627 | 0.660529% | 9.498319 |

The product flux is a separate probability, not the strain-current rate. It is provided as a consistency diagnostic of the unchanged scattering calculation.

## Energy-quadrature and band controls

Each complete new spectrum is subsampled to 17 nodes over the same band. The shorter time-search window -100 to 100 t0 avoids a periodic Fourier replica of the same packet. The table gives absolute 33-versus-17 differences, not formal error bounds.

| Modes | Peak-rate difference, 1/t0 | Whole-packet-rate difference, 1/t0 | Product difference, percentage points |
|---:|---:|---:|---:|
| 240 | 3.2391964e-06 | 7.5209215e-06 | 0.00051934102 |
| 272 | 3.1912164e-06 | 7.4193208e-06 | 0.000509857 |
| 320 | 3.186481e-06 | 7.4381836e-06 | 0.00050420561 |

A separate control narrows the *supplied* 208-mode coherent kernel to the target neighborhood without solving new PDE fields. It changes the previous peak rate by 2.5227315e-07/t0 and product probability by 2.4323776e-11. This tests band truncation/readout, not the new larger-basis equations. The requested Gaussian mean and RMS remain matched. A finite-band check is not a theorem bounding every uncomputed spectral tail.

## Independent verification actually performed

Every one of the 99 stationary solves constructs the full propagating-channel S matrix of its finite model. The maximum S-unitarity residual is 3.8823335e-13; the maximum common-energy ledger residual is 6.9277917e-14 epsilon.

An independent audit reconstructs the downstream equations from actual saved wavefunctions, sparse native matrices, entrance sources and exact outgoing logarithmic derivatives at nine energies per cutoff. It recalculates stationary strain currents and residence from all raw fields, reconstructs the time-domain field at zero, peak occupation and 40 t0 by explicit energy summation, and checks every strain-slice continuity equation and the interior time-domain equation. It independently recovers the peak transport, entry/release selection, conditional mean and integrated currents.

All 87 recorded audit entries pass; the largest reported absolute audit residual is 3.0309089e-14. This number counts implementation checks, not independent physical results. The conservative source equations are unchanged. Numerical matrix assembly is the source's verified memory-only block assembly, not a new scattering approximation.

The archive's compact replay reconstructs the readouts from saved coherent kernels. It is not a fresh PDE solve or a substitute for the raw-field audit. Full raw fields can be regenerated from the documented collector and unchanged source archive.

## Scope

This tests one packet center on one fixed spatial grid. It does not establish a globally stable compression/expansion pattern, a new crossover energy, complete closed-mode convergence, spatial convergence, a physical electron–positron threshold, or a Lorentz-contraction law. The inherited phase-record interpretation is unchanged.

A next convergence test should refine spatial coordinates while keeping a comparable omitted internal-energy threshold, so spatial and mode-cutoff errors are not silently exchanged.
