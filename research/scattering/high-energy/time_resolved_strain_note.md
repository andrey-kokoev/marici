# A time-resolved scattering packet with strain transport retained

Date: 2026-10-12  
Status: Conditional finite-basis wavepacket diagnostics of the supplied quantum-strain model. No physical electron–positron result, classical strain trajectory, new Hamiltonian, or continuum-convergence claim.

## 1. Result

A normalized incoming scattering packet produces a compressive strain current during the main encounter even though the occupied connected/switching subsystem remains expanded on average. These statements are compatible: the strain current transports amplitude toward smaller lambda, while selective entry and release mostly offset the corresponding change in the conditional mean.

The moderately refined fixture has incoming mean lambda 1.011305, mean lambda 1.090956 at maximum connected-plus-switching occupation, and outgoing energy-resolved product mean 1.027429. None of these means is an individual history or a proof that every record was first compressed and later expanded.

## 2. Sources and unchanged model

The immediate input is `pentachoron_strain_diagnostics_bundle.zip`, SHA256 `6dd9a3d601c82c89af1ed3db2421f8d1f36f613e51d4d16c2fa656b9b18407b0`. Its full 42-entry manifest was checked before each stationary sweep. Source code and nested archives are retained unchanged under `source/`.

The supplied `strain_diagnostics_note.md`, sections 4, 5 and 7, distinguishes signed currents, interfering strain amplitudes, and final energy-resolved strain distributions. It explicitly requests a time-dependent packet. The supplied `quantum_strain_route.py` supplies the unchanged Hamiltonian, including the same quantum strain/tilt law, elastic energy, material-frame connections, finite-domain choices, square-root radial dispersion, full face-switch graph, pose continuation and product leads.

Read-only hooks expose the already solved downstream state and entrance forcing. No gate is switched by time, no absorbing term is added, no strain is prescribed, and no rare component is normalized and propagated as the whole input. The connection and domain choices inherited from that model remain assumptions, not consequences of geometry alone.

## 3. New preparation, not new dynamics

Use the same equal incoherent mixture of the four incoming ground modes of one conserved pose block. Its symmetry copies are not counted as extra incident probability. For each mode, form a coherent Gaussian superposition in radial energy K:

    a(K) proportional to exp[-(K-K0)^2/(4 sigma_K^2)],
    K0 = 2.3 epsilon, sigma_K = 0.035 epsilon,
    integral |a(K)|^2 dK = 1.

The native incoming state is unchanged as K varies. It already contains its quantum strain width; its strain kinetic and elastic energies are included in the common energy reference. The packet has no independently supplied connected amplitude or strain kick.

The phase of a(K) is real at the origin used by the source scattering amplitudes. Define t=0 by the maximum of the free inward temporal reference at D=0. This is a reference convention, not a unique arrival-time observable. The Gaussian has temporal-reference standard deviation 1/(2 sigma_K) = 14.285714 hbar/epsilon. It is an asymptotic scattering-continuum preparation, not a compact initial state exactly disjoint from contact at a chosen finite time. No bound-state component is added.

The spectral integral is sampled on 2.09 <= K/epsilon <= 2.51, six standard deviations each side. Renormalizing this negligible-tail truncation defines the actual numerical packet. There are 257 energy nodes on the primary spatial fixture and 129 on the refined spatial fixture. Subsampling the first sweep to 129 supplies an independent energy-grid refinement comparison without changing its Hamiltonian or basis.

All stationary states are kept in fixed incoming, material and output phase frames across energy. Arbitrary energy-dependent rephasing without also rephasing a(K) would change the packet.

## 4. Coherent time synthesis and normalization

For each prepared incident mode i and its unit-flux stationary solution Phi_i(K):

    Psi_i(t) = (1/sqrt(2 pi hbar)) integral a(K) Phi_i(K)
                exp[-i(E0+K)t/hbar] dK.

All complex amplitudes are summed before taking squared norms or currents. The common E0+K0 phase can be removed when computing densities. It does not remove relative energy phases. The mixture average is then taken over i.

This construction uses the scattering-continuum normalization of the source self-adjoint problem. The numerical work directly audits the downstream time-domain equation and current ledger, the spectral full S-matrix and energy ledger, and Parseval identities. It does not directly integrate the entire original square-root half-line field at every time to give a second full-space norm audit.

For the finite downstream subsystem, occupation includes hinge quadrature weights and all sixteen localized pairing records. Product trace nodes have no independent stored norm: their kinetic and internal energies belong to their infinite output leads. No extra boundary-node occupation is invented.

## 5. Time-local current and moment balances

At strain node j, define P_j(t) as the unconditioned occupation of the hinge and both switching graphs at that strain. Let J_entry,j and J_exit,j be the signed net currents through its entrance and product couplings. Positive J_lambda,j+1/2 means transport toward increasing lambda. Direct wavefunction reconstruction verifies

    dP_j/dt = J_entry,j - J_exit,j
                - (J_lambda,j+1/2 - J_lambda,j-1/2).

The probability P(t)=sum_j P_j is conditionalized only in readout. For mean mu(t)=sum_j lambda_j P_j/P, the exact finite-grid identity is

    dmu/dt = [sum_j (lambda_j-mu)(J_entry,j-J_exit,j)]/P
               + [Delta_lambda sum_j J_lambda,j+1/2]/P.

The first term is the effect of entry/release selecting strain records. The second is actual transport between strain values within this subsystem. This separation is a current/moment identity, not an exclusive assignment of individual events to pre-existing versus impact-created compression.

At maximum occupation on the refined fixture:

| Contribution to d mean(lambda)/dt | Value in epsilon/hbar |
|---|---:|
| Transport between strain slices | -0.004562285 |
| Entry/release selection | 0.004428487 |
| Total | -0.000133798 |

Hence there is compressive redistribution even while the conditional mean exceeds one. A mean length alone would miss that transport. Net currents can reverse and must not be converted into positive first-passage probabilities or percentages of newly compressed collisions.

## 6. Packet sequence and output

Time units are hbar/epsilon. Temporal extrema below refer to the stated pulse, reference phase and sampling step 0.5; they are not exact event times or calibrated clocks.

| Observable | Primary grid | Moderately refined grid |
|---|---:|---:|
| Peak net entrance-current time | -3.0 | -2.5 |
| Peak connected-plus-switching occupation time | 8.5 | 9.0 |
| Peak product-current time | 13.5 | 14.0 |
| Maximum interaction occupation | 0.074662% | 0.073452% |
| Mean lambda at that maximum | 1.092269 | 1.090956 |
| Standard deviation at that maximum | 0.306511 | 0.309207 |
| Integrated product flux | 0.167933% | 0.173201% |
| Outgoing energy-resolved product mean lambda | 1.027398 | 1.027429 |
| Outgoing energy-resolved product standard deviation | 0.300266 | 0.303104 |

Peak occupation and integrated product flux are different quantities; they are not mutually exclusive probabilities to add. The original-output probability is the complement of the integrated product flux, approximately 99.83 percent in this pilot. There is no permanent connected capture in the prepared scattering-continuum packet.

The hinge alone has mean lambda approximately 1.2004 at its own occupation peak. Combining it with switching records changes that conditional mean to about 1.09. This distinction prevents exchanging a whole interaction-region average with a hinge-only or final-product average.

The output strain readout follows the predecessor: resolve outgoing native internal energy first, retain coherence within exactly degenerate energy subspaces, then report a positive strain distribution, averaged over packet energy. It is not the instantaneous signed boundary current by strain and is not a single object's strain history.

## 7. Conservation and refinement actually checked

Primary basis: 9 strain nodes, 17 tilt nodes, 72 one-body internal modes, 10 entrance radial cells and 20 hinge intervals. Refined basis: 13, 17, 88, 12 and 24 respectively. Both keep the same strain upper boundary 2.4 and the same physical/model coefficients. The internal ground energy changes with discretization, so radial K is always measured above that fixture's own ground mode, as in the source.

The internal states and both output fields retain all open channels. Higher closed modes are truncated. This is a modest time-domain pilot, not a refinement beyond the source's 25-strain-node stationary calculation. The source's known continuum and high-mode sensitivity remains unresolved.

There are 386 newly solved stationary energies, with full S matrices checked at each. Their largest unitarity residual is 1.17e-13. The subsequent packet audit performs 34 tests per fixture, including direct raw-field reconstruction rather than trusting saved pass flags.

Actual checks:

- Independent reconstruction of stationary downstream equations from the stored sparse operator, sources and lead logarithmic derivatives.
- Explicit energy summation versus the batched Fourier occupation and derivative at five times.
- Time-domain Schrodinger equation on all internal mass-carrying nodes.
- Every strain-slice continuity equation and the conditional-mean decomposition.
- Time-integrated product current versus spectral probability average; disagreement below 1.69e-12 in absolute probability over the recorded window.
- Parseval comparison of integrated interaction occupation against stationary residence averaged over energy.
- Common-energy incoming/output ledger, including the existing internal strain energy and common pose reference.
- Temporal reference-phase translation and time-step quadrature refinement.
- Primary 129-to-257 energy refinement: maximum occupation change 1.64e-10, packet product-probability change 1.01e-11.
- Spatial refinement changes the peak interaction mean lambda by 0.001313 and product flux by 0.005268 percentage points.

Time sampling covers -200 through 400 in model units. Residual interaction occupation at those boundaries is below 1e-12. This is a finite-window diagnostic; the analytical scattering preparation, not an arbitrarily chosen stop time, excludes independent bound-state capture.

Small conservation residuals are not continuum error bars or experimental accuracy. No new all-energy scan, fully independent entrance-PDE solver, or particle identification is claimed.

## 8. What advanced

The stationary strain redistribution now has a time-resolved realization using one unchanged Hamiltonian and one incoming packet. At the main encounter, compressive transport and population selection act in opposing directions. Final output means and source-bin squared amplitudes alone could not reveal that distinction.

This does not establish an exclusive causal fraction of products created by compression, a classical sequence for each event, persistent velocity contraction, a calibrated lambda(v), independently occupied physical particles, photons, three-output production, or 372:1. A monitored first-passage/history experiment would require additional measurement operations that could change interference.

The next controlled test is to repeat this packet preparation and bandwidth at several radial energies, resolving the same moment and current balances. That would test energy dependence without replacing the internal preparation or reading a speed law from one packet.

## 9. Reproduction

Dependencies: Python, NumPy and SciPy; the unchanged nested source also uses SymPy. No network access or repository mutation is required.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python collect_packet.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python analyze_packet.py --name primary
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_packet.py --name primary

For the refinement:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python collect_packet.py --name refined --nlam 13 --N 17 --nm 88 --nD 12 --nu 24 --points 129
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python analyze_packet.py --name refined
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_packet.py --name refined

The bundle retains compact spectral-field factors, phase-coherent amplitudes, sparse operators, time series, source archive manifests, and the independent verifier. The complex128 field factors reconstruct the original saved fields with maximum entry errors below 6e-15; the raw-field audit was rerun using those factors. This is numerical data compression, not a new Hamiltonian truncation. `field_io.py` loads either raw regenerated fields or the supplied factors automatically. `comparison.json` records the actual refinement deltas. `time_series.csv` is a convenience export; raw NPZ/NPY files retain the signed per-strain currents and complete complex spectral information.
