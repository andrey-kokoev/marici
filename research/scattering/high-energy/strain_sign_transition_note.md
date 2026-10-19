# Targeted sign-reversal test with an independently enlarged internal-mode basis

Date: 2026-10-12  
Status: **New finite-basis packet diagnostics in the unchanged supplied model. Not physical electron–positron scattering, a certified continuum threshold, or a speed-to-compression law.**

## 1. Result

The change from compressive to expansive internal transport is not described by one crossover in the tested interval. On the common spatial grid, the 112- and 144-mode calculations resolve a small expansion window near mean radial energy 3.27–3.31 epsilon, a return to compression, and a later return to expansion near 3.40 epsilon.

The 88-mode calculation has no positive peak-current window at the earlier energies sampled; it resolves only the later reversal. Thus increasing the closed-mode cutoff changes qualitative details, not just decimal digits. The two larger cutoffs agree on the three-reversal pattern, with corresponding estimated locations differing by less than 0.004 epsilon. This is evidence of finite-basis stability over these tests, not a continuum-convergence proof.

A separate whole-packet signed-current diagnostic also resolves three reversals, but at different energies. The instantaneous sign at maximum occupation and the time-integrated sign must not be called one universal threshold.

## 2. Sources and unchanged assumptions

The immediate research direction is section 8 of `broad_energy_sweep_note.md`: resolve the 3–3.5 epsilon region while increasing the closed-mode cutoff independently. Its earlier broad scan supplies context, not interpolated data for this calculation.

The stationary Hamiltonian, contact geometry, strain/tilt kinetic law, elastic coefficient, material connections, pose convention, face-switch graph, and product-record leads are those in the supplied `pentachoron_time_resolved_strain_bundle.zip`, through its unchanged `quantum_strain_route.py`. SHA256 identifiers are in `source_provenance.json`. The inherited diagnostics expose the already-solved wavefunction through read-only hooks; they do not alter the equations.

Keep the equal mixture of the same four lowest incoming modes in one conserved pose-energy block. Every packet has requested mean radial energy K and actual RMS energy width 0.035 epsilon, enforced by normalization and moment matching. No phase is reset across energy, no compression kick is supplied, no rare component is independently renormalized during evolution, and no stage probabilities are multiplied.

K is radial energy above the fixture's joint incoming ground. Time units are t0=hbar/epsilon. The preparation already has quantum strain width. All original caveats about direct-sum phase records, uncalibrated scales, domains, and physical particle identities remain.

## 3. Controlled numerical design

Use one spatial fixture throughout the cutoff comparison:

| Quantity | Value |
|---|---:|
| Positive strain nodes | 13 |
| Material-tilt Fourier nodes | 17 |
| Entrance radial cells | 12 |
| Hinge intervals | 24 |
| Angular potential quadrature | 64 |
| Patch quadrature | 24 |
| Retained one-body internal modes | 88, 112, 144 |

The 144-mode eigensystem is built once. The smaller Galerkin matrices are nested submatrices of that same orthonormal eigenbasis. Incoming ground vectors and every downstream matrix are therefore identical across the three cutoffs. An independently source-built smaller entrance reproduces those projected matrices exactly at saved precision.

Every propagating incoming channel is retained. Increasing the cutoff adds closed internal channels, which affect coherent virtual propagation. The first omitted full internal energies are approximately 8.24818, 9.00078 and 10.14348 epsilon. The highest total energy used is approximately 7.25721 epsilon.

There are **423 new production stationary solutions**: 141 energies, from K=2.79 to 3.71 epsilon, at each cutoff. The full propagating-channel scattering matrix is calculated at every row. Parallel workers inherit one initialized eigenbasis; separately chosen energy-dependent eigensolver phases are not spliced into a packet.

The packet centers are evaluated from 3.0 through 3.5 in steps of 0.005 epsilon. At either end, the common spectral interval contains at least six packet standard deviations. Its negligible tails are normalized with the same stated moment convention. This common-band evaluation is coherent superposition of freshly computed amplitudes, not interpolation of the previous broad-sweep percentages.

## 4. Define the sign before locating its changes

Let P(t) be occupation of the hinge and both switching graphs, and let J_lambda,j+1/2 be their signed current toward increasing axial factor lambda. Define

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t),
    R_peak(K) = B(t_peak)/P(t_peak),
    t_peak = argmax_t P(t).

Negative R_peak means internal transport toward smaller lambda; positive means transport toward larger lambda. It excludes the separate selection contribution from entry and release. The conditional mean obeys the unchanged balance

    d mean(lambda)/dt = R_transport + R_selection.

A decreasing mean can coexist with expansive internal transport, and conversely. These are not individual trajectories or fractions of compressed events.

The main time scan is -200 to 400 t0 with 0.5 t0 spacing. The maximum is then locally refined in continuous time by evaluating the same coherent spectral sum. Both the sampled and refined peak readings are saved. The earlier sign changes are not jumps between two comparable occupation maxima in the checked packet records.

For a second observable use

    R_packet = [integral_all_time B(t) dt] / [integral_all_time P(t) dt].

Both integrals are calculated by Parseval's identity from the stationary fields weighted by |a(K)|^2. This avoids treating a chosen finite stop time as complete release. Finite-window integrals and residual occupations are retained separately. Negative and positive parts of B integrated separately remain moment-transport diagnostics, not event probabilities.

## 5. Peak-current results

Estimated locations below are roots in the sampled, finite numerical models. Three displayed decimals do not assert that physical or continuum thresholds have that precision.

| Direction change at peak occupation | 88 modes | 112 modes | 144 modes |
|---|---:|---:|---:|
| Compression to expansion, earlier window | Not resolved | 3.263905 | 3.262915 |
| Expansion back to compression | Not resolved | 3.313150 | 3.316527 |
| Compression to expansion, later window | 3.419730 | 3.400019 | 3.396263 |

Units are K/epsilon. The largest corresponding 112-to-144 root displacement is approximately 0.003755 epsilon. No all-cutoff or spatial limit is certified.

Representative rates, in 10^-3/t0:

| Mean K/epsilon | 88 modes | 112 modes | 144 modes |
|---|---:|---:|---:|
| 3.000 | -4.258 | -3.896 | -3.983 |
| 3.250 | -1.255 | -0.673 | -0.664 |
| 3.275 | -0.173 | +0.341 | +0.406 |
| 3.300 | -0.151 | +0.342 | +0.440 |
| 3.350 | -1.472 | -0.904 | -0.793 |
| 3.400 | -0.543 | -0.001 | +0.110 |
| 3.425 | +0.117 | +0.638 | +0.747 |
| 3.500 | +1.235 | +1.712 | +1.832 |

At 88 modes, the largest sampled peak-current value in the early window is still slightly negative, about -0.02785 in the table's rate units at K=3.29. At 144 modes the corresponding early-window maximum is about +0.55343. The additional window cannot be summarized as rounding an earlier positive signal.

## 6. Whole-packet sign changes are different

| Whole-packet signed transport change | 88 modes | 112 modes | 144 modes |
|---|---:|---:|---:|
| Negative to positive | 3.258543 | 3.248114 | 3.247811 |
| Positive to negative | 3.308685 | 3.324594 | 3.327174 |
| Negative to positive | 3.401418 | 3.384830 | 3.381606 |

The larger-cutoff differences are at most approximately 0.003223 epsilon. The packet-integrated diagnostic already has an early sign window at 88 modes even though the peak diagnostic does not. This is a distinction between observables, not contradictory conservation ledgers.

No calculation assigns a unique compression-versus-expansion history to each outgoing product. Signed transport includes returns and interference.

## 7. Verification and limits

Actual tests:

- Source hashes and exact nested Galerkin projection against the source entrance constructor.
- Full scattering matrices on all 423 production stationary solves; maximum numerical unitarity residual approximately 1.23e-12.
- Prepared-channel flux normalization, common-energy ledgers, and retention of every open channel.
- Independent reconstruction of downstream stationary equations from stored fields, sparse native operator, sources and outgoing logarithmic derivatives.
- Direct coherent energy summation at specified times; raw current reconstruction, every strain-slice continuity balance, and the internal time-domain Schrodinger equation.
- Independent raw-field Parseval calculation of packet-integrated current and residence, without relying on the diagnostic Gram matrices.
- 583 raw-field verification entries across the three cutoffs; largest reported audit residual approximately 5.47e-14 in the stated normalization. This count is not that many independent physical results.
- Spectral subsampling from 141 to 71 nodes at 88 and 144 modes. Corresponding located roots change by at most about 1.32e-6 epsilon; the largest compared peak-rate change is about 3.82e-6/t0. This is an observed quadrature check, not a rigorous error bound.
- Finer packet-center scan at step 0.005, with bracketing followed by root refinement. No theorem excludes arbitrarily narrow additional features between all samples.

The spatial grid is deliberately NOT varied in this turn. This isolates mode-cutoff sensitivity, but leaves the inherited strain, tilt, radial and hinge discretization errors. In particular the earlier broad source showed sizable changes between spatial fixtures. Conservation errors and tight energy quadrature do not imply continuum accuracy.

## 8. Interpretation

Within the fixed model and preparation, radial energy does not select one permanent direction of strain transport. The larger internal bases support an expansion window, renewed compression, and another expansion window. Adding closed modes changes the interference response without changing geometric arrow counts, forces, or the incoming state.

These are conditional model findings, not measured electron–positron behavior, physical speed thresholds, a Lorentz-contraction law, photon production, or a 372:1 result.

The next convergence test is to refine the strain and radial grids around the three identified intervals while maintaining a sufficiently large closed-mode basis. The current results identify where to test; they do not settle that spatial limit.

## 9. Reproduction and archive contents

The delivered archive contains new collector/analyzer/verifier scripts, source hashes, the unchanged source analyzer used for packet normalization, all new scalar receipts, diagnostic kernels, packet time series, CSV data, and verification records. It does not duplicate the previously supplied 118 MB source archive or the large regenerated raw stationary fields.

Quick reconstruction of reported diagnostics from saved kernels:

    OPENBLAS_NUM_THREADS=1 python replay_kernels.py

Full regeneration, using the earlier attachment locally:

    python prepare_inputs.py --source /path/to/pentachoron_time_resolved_strain_bundle.zip
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python collect_transition.py
    OPENBLAS_NUM_THREADS=1 python analyze_transition.py --cutoff 88 --step .005
    OPENBLAS_NUM_THREADS=1 python analyze_transition.py --cutoff 112 --step .005
    OPENBLAS_NUM_THREADS=1 python analyze_transition.py --cutoff 144 --step .005
    OPENBLAS_NUM_THREADS=1 python analyze_transition.py --cutoff 88 --stride 2
    OPENBLAS_NUM_THREADS=1 python analyze_transition.py --cutoff 144 --stride 2
    OPENBLAS_NUM_THREADS=1 python verify_transition.py

The raw-field audit requires regenerated fields; the kernel replay is a separate, explicitly narrower diagnostic reconstruction. Dependencies are Python, NumPy, SciPy and the inherited SymPy source. No network access, repository mutation, new physical parameter, or fitted experimental input is used.
