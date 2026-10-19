# Higher closed-mode cutoff on the 49 × 32 grid

Date: 2026-10-12  
Status: **Completed numerical test of the unchanged supplied finite phase-record model. Not a continuum certificate or physical electron–positron prediction.**

## Result

Raising the internal selection threshold from 14.307336567826175 to 16 epsilon
changes the peak-time signed internal transport by +14.514780%.
The new rate is +1.696480071 in units 10^-3/t0.
Whole-packet transport changes by +8.059088%, and
product-record flux changes by +0.001130753
percentage points. These are finite-cutoff differences, not bounds on the
uncomputed tail or estimates of experimental error.

## Fixed model and input

The unchanged input is `pentachoron_radial_only_refinement_bundle.zip`.
Its manifests and nested source hashes are checked by the inherited reproducer.
The fixed grid has 49 positive strain nodes, 32 radial cells, 25 material-tilt
nodes and 32 hinge intervals. The strain domain ends at 2.4, the radial
Galerkin support spans 9.6 ell, and the source quadratures remain 64 and 24.
The infinite exterior resolvent, physical/model couplings, metric and material
connections, elastic law, geometric patch, native phase operators, switching
rules and incoming ground-mixture rule are unchanged.

The Gaussian packet has radial center K=3.30 epsilon and RMS width
0.035 epsilon. All 33 stationary energies on [3.09,3.51] epsilon share one
fixed eigenbasis and fixed comparison/output frames. Radial energy is measured
above the same joint ground, 3.560628202170 epsilon. No
energy-dependent rephasing or re-preparation is spliced into the packet.

## The enlarged cutoff

The new selection keeps complete multiplets below 16 epsilon: 420 one-body
modes rather than 312. Its last retained full internal energy is
15.999288899093 epsilon; the first omitted
energy is 16.010209874972 epsilon. The old
first omitted energy was 14.316474854345 epsilon. An initial 448-column
basis calculation also reproduces the old ground and cutoff energies.
The compatibility probe's original `keep=312` field refers to the old
selection threshold; the actual new threshold and 420 retained modes are
recorded in the collection and model-configuration receipts.

Every newly retained mode is closed throughout the packet band. No previously
omitted propagating channel or new physical output reaction is introduced.
Higher closed modes remain truncated. The original Hamiltonian is not altered
when its Galerkin representation is enlarged.

## Signed observables

With P(t) the hinge-plus-switching occupation and J_lambda the signed current
toward increasing axial factor, the unchanged definitions are

    B(t) = Delta_lambda sum_j J_lambda,j+1/2(t)
    R_peak = B(t_peak)/P(t_peak), t_peak maximizing P(t)
    R_packet = integral B(t)dt / integral P(t)dt.

Whole-packet integrals use Parseval identities. Conditionalization is a readout,
not normalization and relaunch of a rare branch. Positive transport points
toward larger axial factors. It is not the full mean-strain derivative,
which also contains selective entry and release. Product-record flux is a
separate probability.

Rates below use 10^-3/t0, t0=hbar/epsilon. Flux is a percentage of the entire
incoming unit preparation.

| Selection threshold / epsilon | Modes | Peak transport | Whole-packet transport | Product flux | Peak time / t0 |
|---:|---:|---:|---:|---:|---:|
| 14.307336567826, supplied | 312 | +1.481450755 | +2.428447461 | 0.565834671% | 8.776620429 |
| 16, newly calculated | 420 | +1.696480071 | +2.624158188 | 0.566965424% | 8.783334690 |

The baseline coherent kernels and all 33 prepared scattering arrays were freshly
replayed, not counted as new stationary solutions. The second row is a new
33-energy solve and coherent packet reconstruction.

For the new packet the conditional mean axial factor at peak occupation is
1.075079811, with standard deviation
0.402007411. Selective entry/release contributes
-0.002261709199/t0, and the complete mean-rate is
-0.000565229128/t0. These remain distinct from internal transport.

## Verification actually executed

There are 33 new stationary solutions, each for four prepared incoming columns.
**No new full scattering matrix is computed.** The source-format field
`unitarity_residual` on those rows is a four-column Gram/flux check; the rows
explicitly retain `full_S_computed=false`.

| Check | Largest residual |
|---|---:|
| Prepared-column flux orthogonality | 1.37114e-12 |
| Full iterative-equation relative residual | 1.95941e-12 |
| Common-energy bookkeeping, epsilon units | 5.32996e-12 |
| Downstream stationary equations | 6.01475e-13 |
| Independent raw-field audit | 1.245e-12 |

All 53 raw-field checks pass. They independently
reconstruct every saved downstream stationary equation, prepared-column fluxes,
time-dependent wavefunctions, signed strain currents, strain-slice continuity,
the internal Schrodinger equation, conditional moments and Parseval sums.
A separate direct energy-space Gram calculation bypasses the spectral-field
SVD; its peak-rate difference from the primary reconstruction is
5.31611e-11/t0. This is an implementation audit, not a
second continuum discretization. The optional alternative-preconditioner
control in the reproducer was not executed for this extension.

## Energy-quadrature control

Subsampling the same band from 33 to 17 energies and rematching its Gaussian
moments changes the peak rate by
2.17498755e-06/t0
(0.128206% of its magnitude).
The whole-packet rate changes by
3.4289228e-06/t0;
product flux changes by
0.000371172792 percentage points.
The control time window excludes periodic Fourier replicas. These observed
differences are not rigorous bounds on all unsampled spectral structure.

## Limits and next check

The spatial grids were not refined in this extension. Omitted higher modes,
spatial discretization, strain-boundary and material-connection choices remain.
No sign-change energy is located, and no continuum limit follows from the sign
or from small conservation residuals. The source remains a direct sum of phase
records with uncalibrated scales, not independently occupied physical particles,
a photon identification, Lorentz-contraction law or a physical branching ratio.

An estimate of the omitted-mode contribution is the next useful check; a stable
sign alone is not a quantitative convergence criterion.

## Reproduction

`replay.py` audits the packaged coherent kernels and actual four-column arrays.
`reproduce.py` uses the unchanged included source archive to rebuild the basis,
stationary fields, packet and independent raw-field audit. Large working
caches and wavefunctions are regenerated rather than duplicated in the compact
bundle. No network access or repository mutation is used.
