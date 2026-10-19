# Residual-based estimate of the omitted closed-mode response

Date: 2026-10-12  
Status: New numerical evaluation of analytical fixed-grid Schur bounds. No new
packet-current prediction, self-consistent tail correction, continuum certificate,
or physical electron–positron prediction.

## 1. Result and precise scope

The remaining internal modes can be included in an a posteriori inverse bound
without enumerating their complete eigenbasis. At radial K=3.30 epsilon, the
420-mode retained scattering solution drives an omitted-component response with
frozen-source residence at most about 0.00176448 t0. This is about 1.342% of the
retained hinge-plus-switching residence at that monochromatic energy.

**That is not a 1.342% error bound on the strain current, packet, or product flux.**
The retained state is held fixed while estimating the omitted response. Its
self-consistent change under feedback has not been bounded or solved. The previous
packet rate +1.696480071 x 10^-3/t0 is not replaced by a corrected rate here.

The same calculation at one packet RMS width below and above the center gives
comparable frozen-source bounds. Only three stationary energies are recalculated;
no new 33-energy coherent packet or error interval is claimed.

## 2. Source retained

The unchanged input is `pentachoron_higher_closed_cutoff_bundle.zip`, SHA256
`988b7c752018d80924991c454542cbc5077b85ea6dadb22976f37728cb2fa7e4`. Its 97 archived manifest entries
were checked. The source's saved baseline and 420-mode packet kernels and all
33 prepared scattering arrays for each cutoff were replayed separately. Such a
replay is not counted as a new stationary solution.

The native Hamiltonian, comparison/patch law, elastic energy, material frames,
pose convention and output-record definitions are unchanged. Fixed settings:
49 positive strain nodes, 25 tilt Fourier nodes, 32 radial cells, 32 hinge
intervals, strain boundary 2.4, radial support 9.6 ell, quadratures 64 and 24,
rho=1, and complete internal multiplets below 16 epsilon. All four incoming
ground-record columns retain the same preparation convention.

All quantities retain the source's direct-sum phase-record interpretation.
They are not independently occupied physical particles. No outside theory,
measured energy, new fit, or repository write is used.

## 3. Spectral gap and numerical count

Each one-body raw strain/tilt/spin grid has 49 x 25 x 10 = 12,250 directions.
The retained spectral subspace has 420 directions, leaving 11,830 internal
directions per body. The mirror body is retained by the source's unitary copy.

Rebuilding 448 eigenvectors reproduces the source ground and cutoff energies.
An independent block-LDL/Sturm inertia count of the full raw internal matrix
finds **exactly 420 eigenvalues below 16 epsilon**. The smallest absolute block
pivot eigenvalue is about 0.0434 epsilon, and its largest block-solve residual
is below 1e-13. This is a numerical spectral-order check, not interval arithmetic.

The next numerical internal energy is 16.010209874972 epsilon. Bounds deliberately
use the slightly lower, declared threshold 16 epsilon. With the common pose shift
included, the total packet band extends up to 7.070628202170 epsilon. Thus

    Delta(E) = 16 epsilon - E >= 8.929371797830 epsilon

on that band. Positivity of the omitted-sector radial kinetic energy and its
entrance comparison terms preserves this lower gap. A gap by itself does not
bound a scattering observable without information about its coupling.

## 4. The new residual estimator

Let Pi retain the 420 internal entrance modes and ALL existing downstream records.
Let Q retain the omitted entrance modes on the same raw strain/tilt grid. This Pi
is not the model's rank-two interface-matching projector.

For a 420-mode stationary solution Psi_N, form the complete localized residual

    r = Q H Pi Psi_N.

It contains the original entrance geometric potential, its diagonal matching
term, and the source from the actual solved hinge trace. It does not replace the
self-consistent source by a free incoming state or by an independently normalized
connected component.

The source's radial-cell and angular quadratures are reconstructed BEFORE the
internal eigenmode projection. Projecting this raw forcing back into Pi reproduces
the original retained RHS to relative error 2.23e-15.
The remainder is explicitly projected orthogonal to all 420 columns. Consequently
this diagnostic includes more than the next 28 computed high eigenvectors.

At fixed E below Q's threshold, define

    D_Q(E) = Q H Q - E,
    C(E) = Pi H Q D_Q(E)^(-1) Q H Pi.

Eliminating Q changes the retained effective operator by **-C(E)**. C(E) is
positive semidefinite. This fixed-energy form ordering does not determine the
sign of a strain-current change or a nonlinear packet diagnostic.

## 5. Bound the frozen-source response

Write h_int for the complete raw internal strain/tilt/native operator, including
the common pose shift. The source's radial kinetic and diagonal interaction terms
are nonnegative, so on Q

    D_Q(E) >= Q(h_int-E)Q >= Delta(E) Q.

For each incident column define

    beta(E) = <r, [Q(h_int-E)Q]^(-1) r>.

The omitted-block feedback satisfies the analytical bounds

    0 <= <Psi_N,C(E)Psi_N> <= beta(E) <= ||r||^2/Delta(E).

The omitted state driven by this FIXED retained source is

    Psi_Q,frozen = -D_Q(E)^(-1) r,
    ||Psi_Q,frozen||^2 <= beta(E)/Delta(E).

The last inequality uses D_Q^(-2) <= Delta^(-1) D_Q^(-1), not an invalid general
claim that squaring preserves matrix order.

Beta is evaluated by sparse solves of the full 12,250-direction internal matrix,
with the retained subspace deflated. No truncation at eigenvector 448 is used in
that inverse. The largest recorded inverse-equation residual is
5.95e-14.

Because input columns are unit-flux stationary states, their finite squared
norms are **residence times**, not probabilities. Beta has units of action
(energy x time). Tables use t0=hbar/epsilon and give mean values over the four
prepared columns. The source wavefunctions are not full-line normalized packets.

| Radial K/epsilon | Gap Delta/epsilon | Feedback-action bound beta/hbar | Frozen-tail residence bound / t0 | Bound / retained downstream residence |
|---:|---:|---:|---:|---:|
| 3.265 | 9.174372 | 0.01596297 | 0.00173995 | 1.632% |
| 3.300 | 9.139372 | 0.01612624 | 0.00176448 | 1.342% |
| 3.335 | 9.104372 | 0.01628438 | 0.00178863 | 1.068% |

At K=3.30, the gap-only feedback bound is 0.02211483 hbar; retaining the actual
internal inverse reduces it to 0.01612624 hbar. The source's retained downstream
residence there is 0.13150130 t0.

These ratios compare two different finite residence measures; they do not bound
the relative error of the retained state. Their energy trend is not a compression
law. In particular, the ratio can fall while the absolute upper bound rises.

## 6. The tail is not confined to the next few modes

At the center, about 2.298% of the complete localized
forcing's squared norm lies outside the retained 420-mode space. This fraction is
a residual diagnostic, NOT a fraction of physical events or an error probability.

The explicit modes 421–448 account for
13.988% of beta. The rest of that
positive inverse-weighted diagnostic lies higher in the raw internal spectrum.
This does not assign the same percentages to the actual full omitted self-energy:
beta has dropped positive radial and interaction terms and is an upper bound.

For comparison on the SAME current 420-mode source, the 313–420 shell contributes
0.00939787 hbar to the analogous inverse-internal weighted sum. Neither comparing
that number with beta nor comparing the previous packet rates supplies a valid
extrapolation of the remaining current error.

## 7. Actual verification and limits

Executed: three new stationary solves, four prepared columns each; source-equation
recovery at the central energy; independent raw quadrature/projection checks;
full raw-matrix block inertia; all-high-mode inverse residual and positivity checks;
and 15 independently constructed finite-matrix controls of the Schur inequalities.

The existing central monochromatic product probability is recovered within
6.99e-16 in absolute probability. This is about 0.5274905%, NOT the source's
energy-averaged packet output of about 0.5669654%.

Largest new prepared-column flux residual: 9.93e-13.
Largest retained stationary linear-equation residual:
1.63e-12.
No new full S matrix was computed. The 26 estimator residual checks are numerical
implementation checks, not independent physical theorems.

The bounds are analytical for the stated finite raw-grid model, with numerical
inputs and spectral ordering checked in floating point. They are not an interval
certificate, a bound on discretization beyond that raw grid, or a rigorous
continuum statement. Higher Fourier/strain resolution, other material connections,
and physical identifications remain outside the estimate.

Crucially, reinserting the omitted response changes the retained source itself.
An error bound for R_peak additionally needs control of that feedback, coherent
energy dependence, and the location of the occupation maximum. This calculation
does not turn a frozen-source norm bound into such an error bar.

The next constructive step is to solve the positive omitted-block response and
feed it back into the retained equations, then recompute the coherent packet.

## 8. Reproduction

The compact delivery omits the unchanged 32 MB source archive and large regenerated
matrices. Place the previous archive alongside the new scripts, or supply its path:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_from_archive.py \
      --source /path/to/pentachoron_higher_closed_cutoff_bundle.zip

Dependencies: Python, NumPy, SciPy, SymPy, threadpoolctl. No network access.
The driver verifies source manifests, rebuilds the source basis and retained
model, and runs the three-energy estimator. `verify_schur.py` independently
exercises the estimator inequalities. Saved JSON/NPZ files retain all numerical
results, per-input norms, bounds, prepared scattering columns, and check residuals.
