# Full-packet refinement from 64 to 128 closed-response directions

Date: 2026-10-12  
Status: **Completed fixed-grid, fixed-energy-quadrature response-space test. Not a complete omitted-space solution, continuum certificate, or physical electron–positron prediction.**

## 1. Result

Doubling the residual-adapted response space from 64 to 128 directions lowers the
packet's peak signed internal transport by 0.176213%.
The new rate is +1.726498059 in units 10^-3/t0, with
t0=hbar/epsilon. The expansion-directed sign survives.

Whole-packet signed transport decreases by 0.139927%.
Product-record flux changes by -0.000066207 percentage points.
These are differences between two numerical response spaces, not remaining-error bounds.

The source supplied a complete 64-direction packet but only a central stationary
128-direction check. This extension completes the 128-direction packet over the
same energy band. It does not infer a packet result from the central solution.

## 2. Unchanged model and numerical design

- All 420 original internal eigenmodes remain unchanged.
- Spatial grid: 49 positive strain nodes, 32 radial cells, 25 material-tilt nodes,
  and 32 hinge intervals. Strain boundary 2.4 and radial support 9.6 ell remain.
- Hamiltonian coefficients, geometric contacts, phase connections, elastic law,
  output definitions, and incoming lowest-mode ensemble are unchanged.
- The packet has radial center K=3.30 epsilon and RMS width 0.035 epsilon.
- Both compared packets use 17 energy samples on [3.09,3.51] epsilon and the
  same moment-matched Gaussian convention. Complex amplitudes are combined before
  probabilities and currents are calculated.
- The joint ground reference is approximately 3.560628202170 epsilon. Source
  eigenvalues and the prior central response diagnostics are reproduced.

The supplied `pentachoron_closed_mode_feedback_bundle.zip` and the unchanged
`pentachoron_higher_closed_cutoff_bundle.zip` were read from the conversation.
Archive and nested source manifests were checked. Their hashes and the original
solver-script hashes are retained in `input_provenance.json`.

## 3. What was enlarged

The additional 128 directions are the larger prefix of the source's same
residual-adapted hierarchy. They are not the next 128 eigenmodes and not new
physical reaction channels. The raw internal body grid has 12,250 directions;
420 are retained computed low eigenmodes. The central frozen-source inverse defines an
ordered response hierarchy in their orthogonal complement.

The 128-direction space is orthonormalized and Rayleigh–Ritz diagonalized, giving
548 retained directions per body. Its radial dynamics and diagonal contact terms
are included in the same conservative equations. The entrance and downstream
state respond self-consistently; neither is held at its old solution.

This does **not** regenerate the hierarchy from the corrected 128-direction
residual. Agreement within this fixed hierarchy is not a certificate that every
remaining omitted direction is negligible.

## 4. Packet readouts

Let P(t) denote occupation of the hinge and both localized switching graphs.
Positive strain current points toward larger axial factor lambda. Use

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t),
    R_peak = B(t_peak)/P(t_peak),  t_peak = argmax_t P(t),
    R_packet = integral B(t) dt / integral P(t) dt.

The integrated ratio uses Parseval identities. Conditional normalization occurs
only in readout. Selective entry and release remain a separate contribution to
the full conditional mean-length derivative. Neither signed rate is a fraction
of individually compressed events.

Rates below use 10^-3/t0. Product flux is a percentage of the unit incoming
preparation.

| Response space beyond 420 modes | Peak internal transport | Whole-packet transport | Product-record flux | Peak time/t0 |
|---|---:|---:|---:|---:|
| 64 directions, supplied packet replayed | +1.729545741 | +2.647663647 | 0.565308729% | 8.788339158 |
| 128 directions, new complete packet | +1.726498059 | +2.643958850 | 0.565242522% | 8.788400266 |

The 64-direction row is a replay of supplied complex kernels, not a new
stationary solve. The 128-direction row uses 17 newly computed stationary
solutions. The old 420-mode central solve was separately regenerated to build
the response snapshots; it is not counted as another 128-direction packet row.

The central stationary current-to-residence ratio reproduces the earlier
128-direction control within 8e-17/t0. Nevertheless, the *packet* peak rate changes
by about 0.18% relative to 64 directions. Single-energy agreement was not a
band-wide bound.

## 5. Energy quadrature remains a separate uncertainty

Subsampling the same solutions from 17 to 9 nodes, with Gaussian moments matched,
gives peak rate 1.480563161
instead of 1.726498059, in units 10^-3/t0.
This is a 14.244725% change in the absolute
128-direction peak rate. Product flux changes by
+0.007972174 percentage points.

The paired 64-to-128 change keeps the same negative sign under this coarse
control, but paired cancellation is not absolute energy-quadrature convergence.
The 9-node rule is under-resolved. No new 33-node 128-direction packet has been
computed, and the 17-node result is not certified against all unsampled spectral
structure. Peak searches use -100<t/t0<100 to exclude periodic replicas of the
coarse spectral sampling.

## 6. Checks actually executed

All 17 new stationary solutions keep four prepared input columns. **No new full
scattering matrix is computed.** Prepared-column orthogonality is not relabeled
as full S-matrix unitarity.

| Diagnostic | Largest recorded residual |
|---|---:|
| Prepared-column flux orthogonality | 1.15867e-12 |
| Full iterative-equation relative residual | 2.12498e-12 |
| Common-energy bookkeeping, epsilon units | 5.67546e-12 |
| Downstream stationary equations | 4.40483e-13 |
| Direct fields versus Gram peak rate, 1/t0 | 1.51962e-15 |

The supplied independent raw-field audit passes 40 entries, including every
prepared-column Gram, stationary downstream equations at five energies,
time-dependent wavefunctions, the interior Schroedinger equation, strain-slice
continuity, and the conditional mean-current identity. A packaged version of
that audit was executed again using the delivered raw fields and sparse operator;
this is a reproducibility check, not forty additional independent physical results.

The frozen positive closed-block action at the center reproduces
0.00769299080409 hbar. The independently written closed inverse and
Lippmann–Schwinger equations agree, and the updated self-consistent tail satisfies
its closed equation. Source central-product and residence values are also
recovered. The corresponding receipts are included.

These numerical residuals verify algebra and implementation, not continuum or
experimental accuracy.

## 7. Interpretation and next check

The full packet now supports near-agreement between 64 and 128 directions from
this particular response hierarchy. The expansive sign survives, while the
current magnitude has a small but resolved response-space change.

Finite spatial discretization, energy sampling, omitted response outside this
hierarchy, material connections and the source's physical interpretation remain
unresolved. No physical beam speed, Lorentz-contraction law, independently
occupied product species, photon identity, or electron–positron branching ratio
is inferred.

The next focused test is 17-to-33 energy sampling with the 128-direction space
held fixed. A response space built from the corrected residual remains a separate
omitted-tail test.

## 8. Delivered data and reproduction

`packet_comparison.json` and `energy_sampling_control.json` record the numerical
contrasts. `baseline64/` retains the supplied packet kernels and receipts.
`results/response128/` contains all 17 prepared scattering arrays, raw spectral
fields, sparse numerical operators, packet kernels and audit receipts.
`central_recovery.json` records the independently regenerated central check.

`compare_response_spaces.py` replays the packet comparison.
`verify_raw_fields.py response128` reconstructs the wavefunction/current audit
without needing the large working cache. `run_packet.py` regenerates the
stationary calculation using the unchanged supplied solvers and the earlier
higher-cutoff source archive. See README.md for commands and the distinction
between replay, raw-field audit, and fresh stationary solutions.
