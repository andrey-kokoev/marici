# The unchanged coefficient law cannot supply the complete two-rim contact core

## Result

An exact reconstruction from the existing source matrices excludes the direct core bridge, not just whole-scattering equivalence.

For the principal autonomous two-rim contact, no linear map from the unchanged naturally complexified coefficient dynamics can both intertwine the generators and contain the actual contact ports, even after an arbitrary real nonzero common time scale and scalar energy shift.

This is a scoped candidate exclusion. It does not reject scattering, a new source law, a lead-driven representation, or the possibility of a common process account. The latest strained pentachoron model is not identified with this two-rim model.

## Fresh source reconstruction

The audit imports the owning S4 classification implementation, not a saved spectral summary. It reconstructs the eleven-arrow skew action and the 137-slot tensor-sum generator A. Exact calculation gives

    charpoly(D11) = x^9 (x^2 + 32),
    A (A^2 + 32I) (A^2 + 128I) = 0.

Skew symmetry makes these operators diagonalizable after complexification. For Q=iA in the supplied model-time convention, the five distinct bands are

    -2 omega, -omega, 0, omega, 2 omega,       omega=sqrt(32).

Their multiplicities per complexified scalar response channel are 1,18,99,18,1. Four response channels repeat the bands; they do not add new frequencies. Under Q'=delta I+cQ, c nonzero, the five bands remain an arithmetic progression.

The actual finite-source packet is `research/strominger/results/neutron-two-rim-contact-binding.json`. It supplies raw core K, metric M and rim columns W_raw with

    K^T M = M K,       W_raw^T M W_raw = 3I.

The autonomous-contact implementation whitens M and divides the whitened rim columns by sqrt(3). Therefore the principal eta=2 dressed core is, in raw coordinates,

    D = K + (2/3) W_raw W_raw^T M.

The audit regenerates the Krylov span of the ACTUAL ports under D. Its dimension is five. An exact rational basis B and metric left inverse L give

    DB = B D_bright,       B L W_raw = W_raw.

The bright metric is positive definite, D_bright is metric-self-adjoint, and its characteristic polynomial has five distinct roots. The full 24-coordinate core is not discarded: this calculation isolates the contact-generated subspace; the other directions remain outside this tested port task.

Its characteristic polynomial factors exactly as

    (3292 x^2 - 11069 x + 4198)
    * (10837264 x^3 - 65023584 x^2 + 115350575 x - 53719961)
    / 35676273088.

At the existing unit convention this polynomial is coprime to x(x^2-32)(x^2-128). Thus there is no nonzero generator intertwiner into the bright core even before requiring contact preservation. A dark-sector map is not ruled out by this bright-sector calculation and would not reproduce these contact ports.

## Why adjusting common units cannot repair the contact-complete bridge

Let J map coefficient states into the bright core, with

    D_bright J = J Q',
    range(W_bright) contained in range(J).

The image of J is D_bright-invariant. Since the two contact columns generate all five bright directions by repeated application of D_bright, J must be onto the five-dimensional bright core.

An onto intertwiner from a diagonalizable Q' transfers only eigenvalues present in Q'. The target has five distinct eigenvalues and Q' has at most the five arithmetic-progression bands above. Hence all five target eigenvalues would have to form an arithmetic progression.

For five distinct equally spaced real eigenvalues, center the operator at its mean and write

    m2 = trace((D_bright - mean I)^2),
    m4 = trace((D_bright - mean I)^4).

The five centered values are -2d,-d,0,d,2d. Therefore m2=10d^2 and m4=34d^4, so the necessary identity is

    50 m4 - 17 m2^2 = 0.

For the reconstructed source this exact defect is

    -3497205675098849 / 22938728712050,

which is nonzero. A shift cancels on centering and a nonzero rescaling multiplies this defect by its fourth power. No common affine energy/time convention can fix it.

This also explains why selecting a convenient five-coordinate boundary solve is insufficient: the actual port-generated invariant operator, not the coordinate count, determines the response poles.

## Other encodings and remaining work

The positive-frequency interpretation of the same rotation planes has at most three distinct bands, 0,omega,2omega. The energy Hessian has the three bands 0,16,64. Neither can autonomously cover a five-distinct-band port-generated core through a single affine convention. This is a band-count observation, not a derivation of either encoding as physically authorized.

A new band-dependent redefinition, oscillator quantization on a larger Hilbert space, separately scaled response channels, time-dependent map or changed source generator is a changed bridge contract, not an exception silently admitted here. Such constructions require their own source-operation and energy comparisons.

The executable continuation is to derive the actual two-port rational response from D_bright and its metric/contact columns, construct its minimal retained conservative memory realization, and identify precisely which source operations generate its poles and couplings. This keeps the existing contact model rather than fitting its amplitudes to the excluded coefficient law. Independent justification of the continuum/contact choices remains open.

## Verification and net integration

Checker: `research/nima/checkers/check_scattering_core_bridge_spectrum.py`.

Receipt: `research/nima/results/scattering-core-bridge-spectrum-v1.json`.

Initial successful execution: `structured_command_execution:e_12616_1791930005722025700_112`, exit 0, 22 exact checks. After adding this report and the local work contract, the checker is replayed with their hashes and scope controls included.

The checker uses exact SymPy rational algebra, validates positive metric and square-free target polynomial, and tests shift/rescale and non-progression controls. The source-specific spectral inference above is written mathematics, not a new formal-kernel theorem. No stationary scattering solutions or physical calibration are produced; no source-owner suite is relabeled freshly rerun.

Local research decomposition: `research/nima/contracts/scattering-core-bridge-work-net.v1.json`. The direct affine/core candidate has a scoped rejected verdict; formal outcomes and the broader bridge root remain unassigned. The frozen base net and the historical Strominger overlay remain unchanged.

Freshness warning: the historical overlay's retained-observer hash differs from the current observer note. This work snapshots the current bytes and source matrices separately; it does not silently repin or treat the old overlay validation as live proof admission.
