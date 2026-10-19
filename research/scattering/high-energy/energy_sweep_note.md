# Local energy sweep of time-resolved strain transport

Date: 2026-10-12  
Status: New packet diagnostics of the supplied finite-basis model. **Not physical electron–positron scattering or a converged continuum prediction.**

## 1. Result and actual scope

Across packet mean radial energies 2.25–2.35 epsilon, the compressive contribution to the connected/switching subsystem's conditional mean weakens as energy increases. Product-record flux also decreases across these five samples. The integrated compressive contribution and its residence-normalized signed rate support the same direction of change.

This completes a **local** sweep, not the initially contemplated 1-to-4 epsilon comparison. Only the source's phase-coherent spectral band 2.09–2.51 epsilon is used. No complete new stationary spectrum outside that band is claimed. Incomplete exploratory broad-range data are not used in any result or included in this report.

The model, all its coupling coefficients, and the incoming internal-mode mixture are unchanged. No compression function, new force, or altered topology rule is supplied.

## 2. Source and preparation

Immediate source: `pentachoron_time_resolved_strain_bundle.zip`, SHA256 `262642d188ac73d94b29aea80469518a371a10bb0afdd820d9daa281f868c3bb`. Its `time_resolved_strain_note.md`, sections 3–7 and 8, supplies the coherent spectral fields, the Gaussian packet convention, the strain-current balance, and the request for an energy sweep.

Use the same equal mixture of four lowest incoming modes within one retained pose-energy block. At every new center the strain/tilt/native preparation is unchanged. The reference time is the source's free inward temporal reference at D=0. Times use t0=hbar/epsilon. The energy axis is radial kinetic energy above each fixture's own incoming ground, not speed divided by c.

The five specified mean energies are 2.25, 2.275, 2.30, 2.325, and 2.35 epsilon. Every packet has **the same actual root-mean-square energy width 0.035 epsilon on the numerical quadrature**, as well as unit energy norm.

For the common existing energy support, take

    a(K) = Z^(-1/2) exp[-(K-location)^2/(4 scale^2)],
    integral |a|^2 = 1,
    integral K |a|^2 = requested center,
    integral (K-center)^2 |a|^2 = 0.035^2.

The quadrature location and scale are determined from those last two prescribed moments. This avoids silently changing the realized packet width when shifting a truncated Gaussian toward a band edge. The largest scale adjustment from 0.035 is below 9.4e-7 epsilon. All actual locations, scales, moments and amplitudes are saved. This is preparation normalization, not a fit to the resulting flux. Recovering the source's center-2.3 packet provides a separate check.

The real spectral-phase convention is retained; an energy-dependent eigenvector rephasing without changing the packet would constitute a different input. The source's compressed spectral factors retain those phases.

## 3. Coherent time synthesis

For each incoming mode i,

    Psi_i(t) = integral a(K) Phi_i(K) exp[-i(E0+K)t/hbar] dK / sqrt(2pi hbar).

The field Phi_i is the supplied, flux-normalized stationary solution of one unchanged Hamiltonian. Complex amplitudes are integrated before any norm or current is formed. There is no average of fixed-strain probabilities, separately normalized/relaunched merged branch, or product of stage probabilities.

The preserved field factorization is Phi(E)=L(E)R, with the source's recorded elementwise reconstruction error below 6e-15. To avoid reconstructing the entire large field at every time, the new implementation computes small quadratic-form matrices in this retained factor basis. For example, if W_j is the exact source mass/hinge-quadrature weight at strain slice j,

    G_j = R^dagger W_j R,
    P_j(t) = c(t)^dagger G_j c(t),

with the appropriate incoming-mixture average. The code's row-vector storage is the transpose convention of this formula. Direct field reconstruction at three times per packet independently checks the resulting density and derivative. This is a numerical contraction of already preserved data, not a new state-space truncation.

## 4. Separate strain transport from entry and release

Let P_j(t) be unconditioned interaction occupation at strain j, and let J_lambda,j+1/2 be the signed current toward increasing lambda. The source balance remains

    dP_j/dt = J_entry,j - J_exit,j - J_lambda,j+1/2 + J_lambda,j-1/2.

For P=sum_j P_j and mu=sum_j lambda_j P_j/P,

    dmu/dt = R_transport + R_selection,
    R_transport = Delta_lambda sum_j J_lambda,j+1/2 / P,
    R_selection = sum_j (lambda_j-mu)(J_entry,j-J_exit,j) / P.

Negative R_transport means movement toward smaller axial factors **within the occupied interaction subsystem**. It is not the total derivative of the mean, an individual particle's deformation speed, or a probability of a compression history. In particular, selection can oppose internal transport.

Read every peak rate at that packet's maximum connected-plus-switching occupation. This time is selected by the same rule at all energies; it is not chosen by maximizing a favorable compression rate.

## 5. Local sweep results

Rates below are in 10^-3/t0; flux is the percentage of the full incoming preparation exiting into either 2+8 product-record lead. The displayed digits identify the saved moderately refined finite model, not physical precision.

| Mean radial K/epsilon | Transport rate | Selection rate | Net mean rate | Product-record flux |
|---:|---:|---:|---:|---:|
| 2.250 | -6.06894 | 5.66672 | -0.40222 | 0.211859% |
| 2.275 | -5.36358 | 5.14004 | -0.22353 | 0.205230% |
| 2.300 | -4.56228 | 4.42849 | -0.13380 | 0.173201% |
| 2.325 | -3.82125 | 3.61891 | -0.20235 | 0.132182% |
| 2.350 | -3.25755 | 2.73913 | -0.51842 | 0.106948% |

The magnitude of the peak transport contribution decreases by approximately 46.3% between the first and last packet. Product flux decreases by approximately 49.5% over this **local** interval.

The positive entry/release-selection term opposes compression throughout. The actual net mean rates are therefore much smaller. Neither sign can be dropped from the ledger.

## 6. Time-integrated control

Define the unconditioned moment-transport numerator

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t),

and the reporting diagnostics

    C_minus = integral max(-B(t),0) dt,
    C_plus  = integral max( B(t),0) dt,
    signed transport per residence = integral B(t)dt / integral P(t)dt.

C_minus is a weighted moment-transport integral, **not a probability or a percentage of newly compressed collisions**. Positive and negative current components can include coherent return flow. The split into positive and negative parts is a diagnostic of the current, not a monitored history.

| Mean K/epsilon | C_minus | Signed transport/residence (10^-3/t0) | Mean lambda at peak interaction | Energy-resolved product mean lambda |
|---:|---:|---:|---:|---:|
| 2.250 | 0.000182454168 | -5.66546 | 1.082956 | 1.027700 |
| 2.275 | 0.000175269541 | -5.09107 | 1.088233 | 1.027544 |
| 2.300 | 0.000148388134 | -4.41259 | 1.090956 | 1.027429 |
| 2.325 | 0.000113464281 | -3.62677 | 1.090030 | 1.027177 |
| 2.350 | 8.59361028e-05 | -2.71813 | 1.084240 | 1.026123 |

C_minus decreases by about 52.9% across the interval. Its residence-normalized signed rate also weakens, so the peak-rate trend is not solely an artifact of longer/shorter occupation or a shift of the peak time.

The mean occupied geometry is still on the expansion side, around lambda=1.08–1.09, and product means remain around 1.027. A mean above one does not preclude instantaneous transport toward smaller lambda. No persistent free-motion contraction or lambda(v) is inferred.

## 7. Verification and numerical boundaries

Three data contractions are computed: the source primary spatial fixture with 257 energy nodes, the same fixture subsampled to 129 nodes, and the source moderately refined spatial fixture with 129 nodes. Each has all five packets. The primary spatial grid is (strain,tilt,internal modes,radial,hinge)=(9,17,72,10,20); the refined one is (13,17,88,12,24). These are the source's modest time-domain fixtures, not its finest stationary continuum approximation.

The internal preparation is fixed **within** each spatial fixture. Comparing those fixtures changes the approximation of that same specified preparation, not an intentional physical preparation. The refined incoming mean lambda is 1.011304940, with standard deviation 0.302803864.

The independent audit executes 175 checks, including:

- Reconstructing ten stationary downstream solutions directly from the preserved field factors, sparse operator, actual entrance sources, and output logarithmic derivatives; largest normalized residual 3.45e-13.
- Recalculating each time-local strain continuity and conditional-mean identity from the newly computed arrays.
- Verifying normalization, target energy means, and exactly common RMS width for all fifteen packet/grid combinations.
- Checking the spectral energy ledger, finite-time product current against the spectral packet probability, and Parseval residence.
- Checking recovery of the old central packet and unchanged incoming internal density.

The additional per-case implementation ledgers contain 57 checks each, including direct field-versus-Gram density/derivative reconstruction. Counts are bookkeeping, not independent physical theorems.

Observed refinement comparisons:

- Primary 129-to-257 energy-grid change in product probability: at most 1.18e-09 in absolute probability.
- Corresponding peak transport-rate change: at most 7.79e-08/t0.
- Spatial/basis change in product flux: at most 0.005711 percentage points.
- Corresponding peak transport-rate change: at most 0.000201005/t0.

The decrease across the five energies appears in both spatial fixtures and both primary spectral resolutions. These comparisons are not certified continuum error bars, and they do not repair the source's higher closed-mode/continuum uncertainties.

Time integration covers -200 through 400 t0 with sampling 0.5 t0. At the two off-center packets the common-band truncation produces slightly larger long-time tails than at the central packet. The maximum refined finite-window product-current discrepancy is 1.16e-09 in absolute probability. The full spectral probability, rather than a finite-window stop value, is quoted in the tables.

No fresh broad-band full S-matrix scan is claimed. The inherited stationary flux validation remains source evidence; this step freshly checks stationary field equations and the new packet current/energy balances.

## 8. Interpretation and next test

The defensible new result is a **local counterexample to a monotonic energy-to-compressive-transport rule in this admitted toy preparation**: raising the mean radial energy over 2.25–2.35 epsilon weakens the compressive moment transport while also reducing outgoing product-record flux. This does not reject the user's geometric-compression conjecture in general, establish a relation for real electrons, or prove a causal percentage of product formation attributable to compression.

The completed calculation is limited to this local band. A wider sweep would test the extent of the trend; it has not been completed here. Retained limits include phase records rather than independently occupied particles, uncalibrated scales, imposed material connections and collapse boundary, unconverged continuum/high-mode truncation, absent species stability, and no Lorentz-contraction law or 372:1 prediction.

## 9. Reproduction

The companion extension bundle contains the new scripts, all fifteen time/current NPZ datasets, CSV/JSON summaries, the independent verification ledger, and source provenance. It intentionally does not duplicate the 118 MB input archive or claim to contain a regenerated out-of-band spectrum.

Place the previously supplied source archive beside the extracted extension, then run:

```sh
python prepare_sweep.py --source pentachoron_time_resolved_strain_bundle.zip
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python local_energy_sweep.py --case refined
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python local_energy_sweep.py --case primary
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python local_energy_sweep.py --case primary --stride 2
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_local_sweep.py
```

The diagnostics require NumPy and SciPy. No internet access, repository mutation, or additional physical parameters are used. The source archive's own instructions describe regeneration of its stationary data.
