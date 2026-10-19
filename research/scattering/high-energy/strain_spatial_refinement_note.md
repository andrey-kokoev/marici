# Spatial refinement of the reported strain-current sign reversals

Date: 2026-10-12  
Status: **New numerical convergence tests of the unchanged supplied finite-basis model. Not physical electron–positron scattering or certified continuum thresholds.**

## 1. Result

The three peak-time strain-current reversals from the preceding calculation are **not stable under the combined spatial refinement tested here**. Refining the strain grid alone or the radial grid alone preserves the three-reversal pattern but narrows its early expansion window. Refining both removes that early peak-time window at the retained 144-mode cutoff. One peak-time reversal remains in the tested range, near K=3.407 epsilon.

This is evidence against treating the earlier three peak-time reversals as a converged result. It does not prove that the continuous model has exactly one reversal. The early-window maximum on the combined grid is only slightly negative, and increasing the closed-mode cutoff again could change it.

The whole-packet signed-current observable continues to have three reversals. Peak-time and time-integrated transport remain different readouts.

## 2. Requested basis and unchanged dynamics

The supplied `strain_sign_transition_note.md` requested refinement of strain and radial grids after its 112/144-mode cutoff test. Its source note and diagnostic kernels provide the baseline. The supplied `pentachoron_time_resolved_strain_bundle.zip` provides the unchanged stationary solver, read-only diagnostic hooks, and coherent packet construction. Archive and solver hashes are in `provenance.json`.

No elastic law, interaction coefficient, contact geometry, endpoint gate, outgoing channel, material connection, or phase preparation is changed. The packet has the same equal incoming ground-mode mixture and RMS radial-energy width 0.035 epsilon. All energies are radial energies above the corresponding discretized joint ground; refining an eigensystem is not replacement by a different physical preparation. The material-tilt grid remains N=17, the hinge remains at 24 intervals, the internal cutoff is 144 one-body modes, and source quadratures remain 64 and 24.

The ground reference is 3.547210800136 epsilon on the 13-node strain grid and 3.553013254102 epsilon on the 17-node grid. This numerical shift is retained consistently in every energy ledger, not silently treated as an additional incoming kinetic energy.

## 3. Controlled grid design

| Fixture | Positive strain nodes | Radial cells | Strain spacing | Radial cell width |
|---|---:|---:|---:|---:|
| Supplied baseline | 13 | 12 | 2.4/14 | 0.8 ell |
| Strain-only refinement | 17 | 12 | 2.4/18 | 0.8 ell |
| Radial-only refinement | 13 | 16 | 2.4/14 | 0.6 ell |
| Combined refinement | 17 | 16 | 2.4/18 | 0.6 ell |

The strain boundary stays at 2.4 and the radial basis spans the same 9.6 ell computational support. Exterior motion still uses the source's infinite-half-line nonlocal resolvent; the radial endpoint is not a reflecting box.

There are **213 saved new stationary solutions**: 71 common energies from 2.79 through 3.71 epsilon on each of the three new grids. The baseline comparison uses the supplied 71-node subsample of its 141-node calculation, so the spatial comparison has a common spectral quadrature. The source's corresponding 141-to-71 root shifts were below approximately 1.4e-6 epsilon.

The first omitted full internal energy is 10.143482167593 epsilon at 13 strain nodes and 10.151775104826 epsilon at 17 nodes. The highest total energies solved are below 7.264 epsilon. Thus all propagating original channels are retained on every grid. The physically relevant truncation of higher closed modes is not eliminated by this check.

Each grid uses one fixed eigensystem across its energy band. No energy-dependent arbitrary phase choices are spliced into packet synthesis. The interrupted radial collection was completed by restoring its saved eigensystem and contact/output frames before recomputing the missing saved rows; source equations and preparation were unchanged. The residual checks and recovered-row indices are retained in that collection's receipt.

## 4. Same two signed-current readouts

With P(t) the occupation of the hinge and both switching graphs and J_(j+1/2) the current toward increasing strain, define

    B(t) = Delta_lambda sum_j J_(j+1/2)(t),
    R_peak(K) = B(t_peak)/P(t_peak),
    t_peak = argmax_t P(t).

Negative means compressive internal transport and positive means expansive internal transport. This omits the separate entry/release selection term. It is not the full derivative of the conditional mean length and not a classical event history.

The second observable is

    R_packet(K) = integral B(t) dt / integral P(t) dt.

Its two integrals use the source's stationary-field Parseval calculation. It is not inferred from an arbitrary stopping time.

All packet centers from 3.0 to 3.5 epsilon are sampled at steps of 0.005, followed by bracketed root refinement. The original time search is -200 to 400, with a 0.5 time spacing and a locally refined occupation maximum. These are numerical diagnostics, not measured thresholds.

## 5. Peak-time sign changes

| Grid (strain, radial) | Earlier compression → expansion | Expansion → compression | Later compression → expansion |
|---|---:|---:|---:|
| Baseline (13,12) | 3.262916 | 3.316525 | 3.396263 |
| Strain-only (17,12) | 3.282804 | 3.319614 | 3.398950 |
| Radial-only (13,16) | 3.271066 | 3.303999 | 3.406914 |
| Combined (17,16) | Not resolved | Not resolved | 3.407341 |

Units are K/epsilon. Decimal digits identify the saved numerical roots and must not be read as continuum precision.

The early positive window narrows from approximately 0.05361 epsilon on the baseline to 0.03681 under strain-only refinement and 0.03293 under radial-only refinement. On the combined grid, a finer center scan with step 0.001 over 3.24–3.34 and a local maximization find the largest peak-time rate near K=3.29962, approximately **-5.57e-5/t0**. It is slightly compressive, not a missed large positive window. The 71-to-36 energy-subsampling difference over that early interval is below 1.67e-6/t0; the sign stays negative in that control.

No theorem excludes arbitrarily narrow features outside the checked intervals or a reappearance under further spatial or internal-mode refinement.

## 6. Whole-packet sign changes

| Grid (strain, radial) | Negative → positive | Positive → negative | Negative → positive |
|---|---:|---:|---:|
| Baseline (13,12) | 3.247809 | 3.327174 | 3.381606 |
| Strain-only (17,12) | 3.263703 | 3.335539 | 3.391829 |
| Radial-only (13,16) | 3.251903 | 3.317397 | 3.391160 |
| Combined (17,16) | 3.268117 | 3.326626 | 3.400154 |

The integrated observable therefore still resolves an early expansion window on the combined grid even though peak-time transport does not. This is not contradictory: each weights different portions of the same coherent packet.

## 7. Verification actually performed

The three new datasets contain complete propagating-channel S matrices at each of their 71 energies. Their largest numerical unitarity residual is **1.9231e-12**; the largest saved common-energy residual is **1.3856e-13 epsilon**.

A separate raw-field audit reconstructs the stationary downstream equations at nine energies per grid, prepared-column fluxes, time-dependent fields at specified times, strain-slice continuity, the interior Schrodinger equation, conditional moments, and Parseval current/residence integrals. All 583 entries pass. The largest reported audit residual is approximately **8.54e-14**. This is an algebra/current check, not a second independent discretization of the full entrance PDE or that many independent physical results.

The delivered compact kernels permit a separate replay of packet normalization, peak occupations, signed rates and product fractions. This replay checks saved diagnostic reconstruction; it does not replace the independently performed raw-field audit. Raw fields can be regenerated with the supplied collector and the unchanged earlier source archive.

Energy subsampling to 36 nodes preserves the qualitative sign conclusions. Corresponding root displacements are at most approximately 0.000353 epsilon across the new grids. Coarse spectral quadrature repeats in time with period 2pi/Delta_K. Its control peak search is restricted to -100<t/t0<100 to avoid choosing a periodic Fourier replica of the same encounter. An initial unrestricted subsampling log is retained as an implementation diagnostic, not a distinct late collision. The primary 71-node calculation retains the original time window.

Across the whole 3.0–3.5 interval, some 36-to-71 rate and output differences are larger than those close to the early sign window. `quadrature_comparison.json` reports them rather than asserting uniform spectral convergence from the small root shifts.

## 8. Interpretation and next test

Agreement between 112 and 144 internal modes on one spatial grid was insufficient to establish the three peak-time reversals. Independent strain and radial refinements both narrow the first expansion window; together they remove it in this finite model. The later peak-time reversal survives all four compared grids, but its location is not certified.

The result concerns the source phase-record toy. It supplies no physical electron/positron threshold, independently occupied product species, velocity–compression law, Lorentz-covariant deformation, or experimental branching fraction.

The next focused check is a larger closed-mode basis on the combined refined grid. Its small negative early-window maximum makes that test more informative than treating either one or three peak-time reversals as final. Further strain/radial, tilt and hinge refinement also remains necessary for a continuum claim.

## 9. Reproduction

For the compact saved-kernel audit:

    OPENBLAS_NUM_THREADS=1 python replay_spatial.py

For full regeneration, restore the unchanged earlier source archive:

    python prepare_sources.py --packet /path/to/pentachoron_time_resolved_strain_bundle.zip

Then run the collector for each named fixture, for example:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python collect_spatial.py \
      --case joint17x16 --cutoffs 144 --nlam 17 --nD 16 --N 17 --nu 24 \
      --points 71 --lower 2.79 --upper 3.71 --workers 1
    OPENBLAS_NUM_THREADS=1 python analyze_spatial.py --case joint17x16 --cutoff 144 --step .005
    OPENBLAS_NUM_THREADS=1 python verify_spatial.py --case joint17x16 --cutoffs 144

Use (nlam,nD)=(17,12) for `strain17` and (13,16) for `radial16`. A single worker lowers peak memory without changing the equations. Dependencies are Python, NumPy, SciPy and the inherited source's SymPy. No network request, repository mutation or newly fitted physical parameter is used.
