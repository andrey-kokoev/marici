# Broader packet-energy sweep: strain transport reverses direction

Date: 2026-10-12  
Status: **New finite-basis wavepacket calculations in the unchanged supplied model. Not physical electron–positron scattering or a calibrated compression-versus-speed law.**

## 1. Result and actual scope

The earlier decreasing trend on packet centers 2.25–2.35 epsilon does not extend monotonically over 1–4 epsilon. Internal compression is stronger at 2 than at 1.5 epsilon, and weaker again at 2.3 and 2.5. At the sampled centers 3.5 and 4 epsilon, the internal strain-transport contribution at peak interaction occupation is positive: amplitude moves toward larger axial factors. Product-record output has risen again by 2.5 epsilon and is much larger near 4 than in the earlier narrow band.

This is a sample-based statement, not a located extremum or an exact energy threshold. It does not say that every time slice in a high-energy packet is expansive, or that final product flux is caused exclusively by one strain direction. No individual classical compression histories are extracted.

Seven primary packet bands outside the original central preparation were freshly solved, with centers 1, 1.5, 2, 2.5, 3, 3.5 and 4 epsilon. Three additional spatially refined bands at 1, 3.5 and 4 were freshly solved. There are 1226 new stationary solves in total. The primary and refined center-2.3 spectra are the existing source data; their packet diagnostics and independent field audits are recomputed. This is not an extrapolation of the old 2.09–2.51 spectrum.

## 2. Source, preparation and conventions

Immediate inputs are the previously supplied time-resolved packet archive and local-energy-sweep extension. Exact SHA256 hashes are in `source_provenance.json`. The collector and full quantum-strain solver are reused unchanged. The new analyzer adapts the local extension's quadratic-form contractions to separately collected bands. The interaction Hamiltonian, elastic coefficient, collapse boundary, material connections, pose convention, switching graph and outgoing record channels are unchanged.

Each center uses the same equal mixture of the four lowest incoming modes in one conserved pose-energy block. Within each numerical fixture its internal strain/tilt/phase preparation is fixed. The incoming state already contains strain uncertainty. Refined fixtures approximate that same declared preparation; they are not deliberately different incident shapes.

At every center, the numerical Gaussian packet is normalized and moment-matched to exactly the requested mean radial K and actual RMS width 0.035 epsilon. Each fresh spectral interval is K_center +/- 0.21 epsilon (six widths). No energy-dependent phase reset is applied: all states in each band use the same incoming material frames and source amplitude convention. The eigensolver's arbitrary constant basis within a degenerate ground subspace cancels in the equal mixture.

K is radial energy above each fixture's joint internal ground, not speed divided by c. The common time reference is the source free inward temporal maximum at D=0. Time units are t0=hbar/epsilon. The diagnostic window is -200 to 400 t0 with time spacing 0.5 t0, as in the source. There is no independently prepared connected state or compression kick.

## 3. Currents, not a classical length history

Use the previous finite-volume identity without changing dynamics:

    dP_j/dt = J_entry,j - J_exit,j - J_lambda,j+1/2 + J_lambda,j-1/2,
    R_transport = Delta_lambda sum_j J_lambda,j+1/2 / P,
    R_selection = sum_j (lambda_j-mean_lambda)(J_entry,j-J_exit,j) / P,
    d mean_lambda/dt = R_transport + R_selection.

The rates are evaluated at each packet's maximum connected-plus-switching occupation, using the same selection rule for every center. Negative transport means internal redistribution toward smaller axial factor. Positive transport means redistribution toward larger axial factor. Neither rate is an individual object's deformation speed, a first-passage probability, or a fraction of newly compressed collisions.

## 4. Broad primary sweep

All rows below use the same primary spatial fixture (strain, tilt, retained one-body modes, radial cells, hinge intervals)=(9,17,72,10,20), with unchanged model parameters. New bands have 129 energy points; the center-2.3 primary source has 257. Each is separately subsampled by two for an energy-grid comparison. The full packet width remains moment-matched under subsampling.

Rates are in 10^-3/t0. Output is the spectral packet probability into both 2+8 record leads, as a percentage of the original incoming preparation.

| Mean radial K/epsilon | Internal transport | Entry/release selection | Net mean rate | Product-record output |
|---:|---:|---:|---:|---:|
| 1 | -3.28742 | +3.01932 | -0.26810 | 0.044156% |
| 1.5 | -0.93023 | +0.82619 | -0.10404 | 0.151677% |
| 2 | -5.90906 | +4.92293 | -0.98613 | 0.196822% |
| 2.3 | -4.71837 | +4.57365 | -0.14472 | 0.167933% |
| 2.5 | -2.00137 | +0.92883 | -1.07254 | 0.218114% |
| 3 | -4.71858 | +3.96362 | -0.75496 | 0.778162% |
| 3.5 | +3.24742 | -3.19061 | +0.05682 | 1.043092% |
| 4 | +5.80640 | -6.56933 | -0.76293 | 2.127616% |

At K=4, internal transport is +5.80640 while selection is -6.56933, leaving net mean change -0.76293, all in 10^-3/t0. Thus the mean can decrease while the subsystem's own strain transport is expansive. This is the reverse cancellation pattern of the earlier central packet.

The center-2.3 primary row differs slightly from the earlier final answer's moderately refined row; both are retained below. No different preparation is substituted to manufacture a trend.

## 5. Finite-window integrated transport

With B(t)=Delta_lambda sum J_lambda, report

    C_minus = integral_window max(-B,0) dt,
    C_plus  = integral_window max(B,0) dt,
    signed rate per residence = integral_window B dt / integral_window P dt.

The first two quantities are weighted moment-transport integrals, **not probabilities or exclusive events**. They include coherent returns. The last diagnostic gives the same negative/positive direction at the higher sampled centers as the peak test.

| K/epsilon | C_minus | C_plus | Signed rate/residence (10^-3/t0) | Mean lambda at peak |
|---:|---:|---:|---:|---:|
| 1 | 3.69678703e-05 | 7.91405062e-15 | -3.29645 | 1.042484 |
| 1.5 | 9.92904925e-05 | 2.65193362e-15 | -1.12778 | 1.035898 |
| 2 | 0.000178348857 | 4.48064143e-11 | -5.13248 | 1.055049 |
| 2.3 | 0.000154371335 | 4.35848515e-08 | -4.55176 | 1.092269 |
| 2.5 | 0.000126926914 | 1.63767574e-05 | -0.98570 | 1.048090 |
| 3 | 0.000987377033 | 8.17665899e-05 | -2.97164 | 1.078254 |
| 3.5 | 4.73863918e-06 | 0.000788615004 | +3.70815 | 1.084774 |
| 4 | 0.000117921474 | 0.00262923688 | +6.77191 | 1.066853 |

Some low-amplitude tails remain at the finite time boundary, especially for the 1.5-epsilon packet. These integrals are explicitly finite-window diagnostics. The quoted product probabilities are obtained from the normalized spectral integral, not by assuming all flux has left at t=400. The spectral-versus-window differences and endpoint occupations are retained in every row; they are not relabeled as zero or absorbed into an error bar. In particular, the primary 1.5 packet has a window-versus-spectral product discrepancy of about 9.8e-7 in absolute probability.

## 6. Refinement: sign checks versus numerical fractions

The moderately refined spatial fixture is (13,17,88,12,24). Its new 1- and 4-epsilon bands have 129 energies; its 3.5 band has 65. The old refined center-2.3 band has 129. These remain modest fixtures, not a certified full continuum calculation.

| K/epsilon | Primary transport | Refined transport | Primary output | Refined output |
|---:|---:|---:|---:|---:|
| 1 | -3.28742 | -3.23108 | 0.044156% | 0.044635% |
| 2.3 | -4.71837 | -4.56228 | 0.167933% | 0.173201% |
| 3.5 | +3.24742 | +1.17214 | 1.043092% | 1.099881% |
| 4 | +5.80640 | +3.20712 | 2.127616% | 2.639193% |

Rate units are again 10^-3/t0. The signs at the tested refinement centers are all preserved. The largest observed spatial/basis output change is 0.511578 percentage points. This is an observed difference, not a rigorous error bound. High closed-mode and continuum uncertainty inherited from the source remains.

On the common primary grid, subsampling the fresh spectra from 129 to 65 energies changes packet output by at most 0.00015342 percentage points and peak internal-transport rate by at most 3.3292172e-06/t0. These comparisons support the sampled qualitative trend but do not locate all narrow resonances or certify arbitrary energies between samples.

## 7. Verification actually performed

Every new stationary solution computes the complete propagating-channel scattering matrix of its finite retained model. The largest stored S-unitarity residual over the source and new audited bands is 1.41e-12. All open incoming modes remain below each retained cutoff throughout each packet band. Evanescent modes below the finite truncation remain in the solution.

The separate `verify_broad.py` audit performs 480 explicit reconstruction tests across twelve packet/grid cases. It reconstructs stationary downstream equations at seven energies per case from raw fields, sources, native sparse matrices and exact outgoing lead kernels; recomputes every saved prepared-channel norm; reconstructs density and strain currents by explicit energy summation at five times; checks local continuity and the time-domain interior Schrodinger equation; and checks packet moments. These tests do not treat source pass flags as a substitute for current reconstruction.

Largest audited stationary-field residual: 3.45e-13. Largest interior time-domain equation residual: 1.21e-14. Small conservation residuals verify implementation identities, not experimental accuracy or continuum convergence. This is not a second independent solver for the entire continuous entrance PDE.

## 8. Interpretation and next useful test

In this admitted model and preparation, increasing radial energy does not produce monotonically increasing compression, or even one fixed direction of strain transport at peak encounter. Output can rise while internal transport is expansive. This limits the current toy's monotonic energy-to-compression interpretation; it does not refute geometric flattening as a general conjecture or measure the behavior of real electrons.

Remaining boundaries are unchanged: phase records rather than independently occupied particles, uncalibrated length/energy scales, admitted material connections and collapse rule, finite internal truncation, no Lorentz-covariant deformation law, no photon or species identification, no new three-output channel and no 372:1 prediction.

The next localized test is to resolve the change of transport sign between the sampled 3 and 3.5 epsilon centers while independently increasing the closed-mode cutoff. The present data do not give an exact crossover energy.

## 9. Reproduction and delivered data

The extension archive contains scripts, all packet time/current arrays, spectral probabilities and moment checks, the fresh stationary scalar receipts, independent audit records, the summary CSV/JSON and source hashes. It does not duplicate the 118 MB upstream source archive, raw regenerated fields, or disposable nested caches. Raw spectra are regenerated by the unmodified collector. No web access, repository mutation, new physical parameter or fitted experimental number is required.

Place the earlier `pentachoron_time_resolved_strain_bundle.zip` locally and run:

```sh
python prepare_broad.py --source /path/to/pentachoron_time_resolved_strain_bundle.zip
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_broad.py --fixture primary
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_broad.py --fixture refined
```

Dependencies are Python, NumPy, SciPy and the source's SymPy. The stationary collector validates inherited source hashes. `verify_broad.py CASE...` reruns the independent field audit after collection and analysis. The supplied receipts record what was actually run in this turn.
