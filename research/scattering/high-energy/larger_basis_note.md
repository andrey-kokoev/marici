# Larger closed-mode test on the combined strain/radial grid

Date: 2026-10-12  
Status: **Completed numerical test of the supplied finite phase-record model. Not a converged continuum or physical electron–positron threshold.**

## Result

The expansive peak-time response returns at the larger cutoffs, but not as the earlier narrow, isolated positive window. On this fixed grid, 176 and 208 retained one-body modes each give one compression-to-expansion crossing much earlier than the 144-mode crossing. No subsequent return to negative peak-time transport is resolved up to K=3.5 epsilon in those two larger-basis scans.

The difference between the two larger bases is still substantial. At K=3.30 epsilon the peak transport magnitude rises by approximately 44% from 176 to 208 modes. This is evidence that the cutoff dependence is not yet small, not a proof of a limiting sign pattern.

The underlying interaction, preparation rule, packet width and spatial grid remain fixed. Only the numerical Galerkin cutoff changes.

## Peak-time results

K is radial energy in epsilon units above the unchanged joint ground of this spatial grid. Rates in the last two columns use 10^-3/t0, with t0=hbar/epsilon. Negative means compressive **internal transport**, not the full mean-length derivative.

| One-body modes | Peak-time compression-to-expansion crossing K/epsilon | Rate at K=3.30 | Largest rate on 3.24–3.34 |
|---:|---:|---:|---:|
| 144 | 3.407341 | -0.055798 | -0.055681 |
| 176 | 3.257369 | +2.035797 | +2.064293 |
| 208 | 3.250574 | +2.929980 | +2.993963 |

The early maxima occur at K=3.299624, 3.305528 and 3.308229 respectively. The 144-mode negative maximum is recovered from a fresh calculation, not copied into the new comparison. The 176-to-208 peak-crossing displacement is approximately 0.006795 epsilon.

The principal center scan uses step 0.005 on 3.0–3.5; an additional early scan uses step 0.001 on 3.24–3.34 with a locally refined maximum. Numerical bracketing does not exclude every arbitrarily narrow unsampled feature. The tabulated decimals identify finite-model roots, not precision continuum thresholds.

## Whole-packet transport remains a different observable

The time-integrated current divided by integrated residence gives the following roots:

| Modes | Compression to expansion | Expansion to compression | Compression to expansion |
|---:|---:|---:|---:|
| 144 | 3.268117 | 3.326626 | 3.400154 |
| 176 | 3.101405 | 3.147180 | 3.247421 |
| 208 | 3.093347 | 3.155649 | 3.241367 |

Thus three whole-packet reversals remain resolved, but their locations also change substantially. They are not the peak-time crossings and do not imply three separate event classes.

## Numerical checks and outstanding uncertainty

There are 213 saved fresh stationary solutions: 71 common energies per cutoff. Every solve includes the full propagating-channel S matrix. Adding modes extends the closed-channel subspace; it does not add an omitted propagating channel or change a physical reaction threshold.

- Largest full-S unitarity residual: 2.058e-13.
- Largest common-energy ledger residual: 6.92779e-14 epsilon.
- Independent raw-field audit: 535 passing entries; largest reported residual 3.25224e-14.
- Packaged coherent-kernel replay: 1830 passing entries. This is a narrower readout audit, not a fresh PDE solution or that many independent theorems.
- Fresh 144-mode baseline recovery: product-flux difference at most 8.47412e-15; residence difference at most 2.35367e-13.

The 71-to-36 spectral-node control preserves the number of peak-time and whole-packet roots. For the two larger cutoffs, the peak-time crossing shifts by about 0.0000020 and 0.0000153 epsilon. Some whole-packet crossings shift by as much as 0.00202 epsilon under that control; they should not be assigned the same quadrature precision as the peak-time crossing.

The spatial grid was NOT refined again in this calculation. Strain nodes=17, tilt nodes=17, radial cells=16 and hinge intervals=24 are unchanged. The 44% rate change between the two larger cutoffs prevents a numerical convergence claim even though the flux-conservation residual is small. No extrapolated continuum root, physical collision speed, Lorentz-contraction law, photon identity or branching ratio is inferred.

## Next focused test

A further cutoff sequence at K=3.30, with this same packet and spatial grid, would test the still-large current-amplitude change before another root is treated as settled.

## Files and reproduction

`larger_basis_methods.md` gives the equations, nested-basis construction, source conventions and numerical implementation controls. `larger_basis_summary.json` and `larger_basis_rates.csv` retain the main readouts. `larger_basis_quadrature.json` records root shifts under spectral subsampling.

The archive includes compact coherent kernels, packet time/current arrays, scalar stationary receipts, raw-field audit reports, source hashes and scripts. It omits the large unchanged upstream archive and raw spectral fields. Those fields were audited before packaging and can be regenerated with the included collector. No repository file was modified and no outside particle theory or experimental value was inserted.

See README.md for complete regeneration and the smaller saved-kernel replay.
