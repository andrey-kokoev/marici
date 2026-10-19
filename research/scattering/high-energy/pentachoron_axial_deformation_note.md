# Active axial strain of the entrance comparison at fixed kinetic baseline

Date: 2026-10-11  
Status: Conditional geometric and scattering sensitivity calculation. **Not an electron–positron prediction, a derivation of Lorentz contraction, or a fully strained native phase model.**

## 1. Result

Prescribed axial strain changes the retained configuration-comparison potential and its marked ABE-active region. With the source square-root radial kinetic law, incoming preparation, material-reference phase matrices, and downstream switching network held fixed, these geometric changes alter asymptotic 2+8 record flux. The effect has no universal sign in the tested family.

The exposure angle stays `delta_c=atan(1/sqrt(5))=24.0948425521 degrees`. The maximum entrance separation for ABE decreases to `lambda * 8/sqrt(30) ell`. At half axial length, the eligible patch has approximately 19.3% of its original area in the retained configuration measure. Nevertheless, conversion increases at two lower sampled energies and decreases at two higher sampled energies.

The strain factor lambda is an independently prescribed parameter. No lambda(v) is assumed. A fixed strain is not silently changed from channel to channel using the total collision energy. There is one conservative Hamiltonian per strain factor, not yet a single Hamiltonian that dynamically generates compression.

## 2. Source retained and explicit new choices

The supplied `pentachoron_relativistic_kinetics_bundle.zip` is extracted unchanged under `source/`. Its spectral-resolvent code, compact upstream inputs, and the geometric-source 25-file manifest are retained. The source provides the nonlocal half-line square-root entrance solver and the complete downstream hinge, face-switch, memory and output model.

New choices:

1. Physically strain the **entrance comparison vertices** along the laboratory collision axis after their material x–w rotation: `C_lambda=diag(lambda,1,1,1)`, with `0<lambda<=1`.
2. Keep the ambient Euclidean metric fixed when measuring those vertex displacements. This is active geometric strain, not a coordinate relabeling with a compensating metric change.
3. Keep actual center separation D in the original length unit. Strain each body about its own center; do not simultaneously rescale D and claim a new physical result.
4. Keep all kinetic operators and the reference configuration measure unchanged to isolate comparison-geometry effects. In particular, the original rotor coefficient and its reference measure are not rederived from the strained vertex inertia.
5. Preserve the prior normalized, uniform patch-sampling rule, replacing only its geometric support and its normalization by the strained patch. Its strength remains 2 epsilon; no coefficient is fitted to conversion data.
6. Preserve H_O, H_C, P and downstream native/material-reference operators. They are NOT claimed to be freshly derived Euclidean spin-fold operators of fully strained pentachora. Section 8 explicitly calculates a fold that would change in that fuller model.
7. Keep the same incoming angular flux coefficients, phase reference D=4 ell, four-ground-mode mixture, and rho=mc^2/epsilon=1. No measured energy, speed, probability, or particle mass is used.

These rules define a controlled entrance-comparison perturbation. They do not account for the work needed to prepare or maintain material strain, determine how free particles acquire strain, or rebuild the complete elastic/phase Hamiltonian of both objects. Since lambda is fixed during each autonomous scattering solve, no unaccounted time-dependent switching work is introduced in that solve.

## 3. Exact strained comparison

Use the centered retained vertices in units ell:

    A=( 1, 1, 1,-1/sqrt(5)),
    B=( 1,-1,-1,-1/sqrt(5)),
    C=(-1, 1,-1,-1/sqrt(5)),
    D=(-1,-1, 1,-1/sqrt(5)),
    E=( 0, 0, 0, 4/sqrt(5)).

Their centered covariance is Q^T Q=4 I_4. Rotate in x–w by delta, then apply C_lambda to each body; mirror the right body across the spatial midplane. The center positions stay +/-D/2.

For a candidate comparison pose (D_hat,t), the exact ten-vertex displacement sum is

    (5/2)(D_hat-D)^2 + 16 ell^2 (1+lambda^2) [1-cos(t-delta)].

For lambda=1 this recovers the supplied coefficient 32 ell^2. The cross term between center translation and internal change vanishes because all five retained vertices are centered.

Write d=D/ell and

    a(t)=max(|cos t|-sin(t)/sqrt(5), 4 sin(t)/sqrt(5)).

The projected head-on non-overlap condition is D_hat/ell >= 2 lambda a(t). The dimensionless comparison cost becomes

    v_lambda(d,delta) = min_t {
        (5/2) [2 lambda a(t)-d]_+^2
        +16(1+lambda^2)[1-cos(t-delta)] }.

This is a minimum over the entire angle circle, not only a presumed local extremum. The code enumerates support-branch endpoints, real stationary quartic roots, zero-overlap roots, and angular-cost stationary points. An independent dense-bracketing minimizer checks sampled results.

At fixed d,delta, both nonnegative terms for every candidate decrease or remain equal when lambda decreases. Therefore

    0 <= v_lambda(d,delta) <= v_1(d,delta),    0<lambda<=1.

The shrinking patch and lower correction cost compete; neither one alone determines flux.

### Active versus passive strain

At zero tilt, edge AC has squared length `4 ell^2(1+lambda^2)` instead of `8 ell^2`. Thus an intrinsic Euclidean length actually changes.

For a passive coordinate change r'=C_lambda r, using instead `G'=C_lambda^(-T) C_lambda^(-1)` gives exactly `r'^T G' r'=r^T r`. Changing both coordinates and the full metric consistently would not reproduce the active cost above. This algebraic control passes.

C_lambda remains invertible for every positive lambda. It does not change simplex dimension or the incidence of corresponding faces under the common affine map. The limiting map at lambda=0 is singular and is not included in the scattering calculations. Effective thinness must not be identified with an already reduced topological dimension.

## 4. Strained canonical contact region

The equality between the original exposed edge AB and the fifth vertex E has the common factor lambda. It therefore still occurs at

    delta_c=atan(1/sqrt(5)).

Define

    d_lambda = 8 lambda/sqrt(30),
    q=d_lambda-d,
    b_lambda=5 lambda/[4 sqrt(6)(1+lambda^2)].

For `0<=d<d_lambda`, the marked ABE cusp is the unique nearest comparator precisely on the local marked region

    delta_c - asin(b_lambda q)
       <= delta <=
    delta_c + asin(2 b_lambda q).

For d>d_lambda there is no such region. At d=d_lambda only the zero-area boundary point remains. Equivalent angles are taken modulo 2pi with the marked material-frame branch retained.

This follows from the two one-sided derivative inequalities at the support cusp. It has no adjustable angular cutoff.

### Global sufficiency

Writing u=(cos t,sin t), the disk extension of the objective is convex:

    (5/2)[2 lambda max(u_x-hu_y,-u_x-hu_y,4hu_y)-d]_+^2
       +16(1+lambda^2)(1-u.v_delta),    h=1/sqrt(5).

On the stated patch, a subgradient at u_c is `-Lambda u_c`, with

    Lambda=16(1+lambda^2) cos(delta_c-delta)
             -10 lambda q a(delta_c).

For 0<lambda<=1, the bound inherited at maximal width gives cos>=2/3 and Lambda>=32/3>0. The convex lower support inequality is therefore strict at every other disk point. This proves the selected cusp is the unique global minimum there. The one-sided derivative conditions, together with the reflected equal-support cusp, exclude other angles from this marked patch. Six hundred random global-minimum classification checks independently exercise the formula.

### Patch size in the retained measure

Keep `y=(4/sqrt(5)) ell delta` because the kinetic/reference measure is deliberately fixed. With this measure:

| Axial factor lambda | Maximum D/ell | Patch area / ell^2 | Fraction of unstrained patch |
|---:|---:|---:|---:|
| 1 | 1.46059349 | 1.52181029 | 100% |
| 0.75 | 1.09544512 | 0.80420998 | 52.8456% |
| 0.50 | 0.73029674 | 0.29378287 | 19.3048% |
| 0.25 | 0.36514837 | 0.04297932 | 2.8242% |

The exact area follows by integrating the two arcsines. As lambda tends to zero,

    |Omega_lambda| = (16/sqrt(30)) ell^2 lambda^3 + O(lambda^5).

This is a configuration-space area law, NOT an annihilation cross section or an amplitude power law. The normalized patch sampler and wavefunction response remain in the scattering solve.

At the exposure cusp, ABE is at constant x. Its retained edge Gram matrix stays `ell^2 [[8,4],[4,8]]` under this strain: compressing its normal direction does not alter its tangent edge lengths. Its intrinsic area remains `2 sqrt(3) ell^2`; its spatial projection is still a line in this pose.

## 5. Fixed kinetic and phase baseline

Retain the source square-root radial law

    T_rho(k)=2rho[sqrt(1+k^2/rho)-1],    rho=1,

the material rotor energies `5n^2/32`, and every downstream kinetic coefficient. The asymptotic energies and incident flux modes therefore remain unchanged between strain columns. The full nonlocal free resolvent is used, including its real correction and closed-channel continuation; merely substituting a wave number into a local derivative equation is not used.

Replace only the old potential by epsilon v_lambda and its patch by Omega_lambda in

    2 epsilon integral_Omega_lambda
      ||P Psi - (1/sqrt(|Omega_lambda|)) sqrt(ell) P chi(0)||^2.

All diagonal/off-diagonal terms survive. The comparison remains positive and its entrance sample is bounded in L2; the unchanged one-dimensional hinge trace is controlled by its kinetic form. Thus the same lower-bounded, time-independent form construction gives a conservative model for each fixed lambda. This is a mathematical statement about the declared model, not its physical identification.

The continuum entrance interaction vanishes beyond 4 lambda ell. The numerical radial support is reduced accordingly, but the incoming phase reference remains D=4 ell. The exterior is still the infinite spectral half-line, not a finite reflecting wall. Reducing the finite interaction support is not a rescaling of the incident momentum or kinetic law.

## 6. Outgoing flux

At total energy E=e0+K, retain the same angular flux coefficients on n=-2,...,2 and the same four-mode native mixture. K includes radial and rotor energy. The table sums both symmetry-related 2+8 record exits:

| K / epsilon | lambda=1 | lambda=0.75 | lambda=0.50 |
|---:|---:|---:|---:|
| 1.0 | 0.00323905% | 0.00839914% | 0.01361236% |
| 2.3 | 0.02891909% | 0.05836459% | 0.04186873% |
| 4.0 | 3.58386139% | 3.70452031% | 1.52042274% |
| 6.0 | 1.01795071% | 0.47912199% | 0.27205507% |

Appropriate summaries use fewer digits: 0.0032/0.0084/0.0136 percent, 0.029/0.058/0.042 percent, 3.6/3.7/1.5 percent and 1.02/0.48/0.27 percent.

The compressed columns use 48 radial cells, 64 rotor nodes and 320 hinge intervals. The unstrained low-energy baseline was freshly reproduced at 40x48; high-energy unstrained reference values are the retained source 48x64 receipt, after fresh 40x48 agreement. Receipt provenance is explicit in `axial_deformation_results.json`.

This table is not a speed–compression curve: each row compares different prescribed geometries at the SAME incident energy and preparation. Conversion is enhanced at K=1 and suppressed at K=6 as compression grows. At K=4 moderate compression slightly enhances conversion but stronger compression suppresses it. Four energies do not identify all extrema or a universal response law.

The product states remain the inherited direct-sum phase records, not two independently occupied physical particles. No species, photon, rest mass, or 372:1 ratio is inferred.

## 7. Numerical and nonuniqueness controls

The completed record includes:

- 34 geometry-verification groups: exact symbolic covariance and displacement identities, active/passive metric comparison, 250 direct vertex comparisons, 600 global-cusp classifications, 40 independent dense-bracketing minima, 150 recovery tests of the old comparator, analytical area versus quadrature, 50 independently integrated patch cells, and 36 projected-hull contact tests.
- 32 newly calculated main stationary solves across the three factors and refinements. Every saved new solve computes the complete open-channel S matrix, not only the four prepared columns.
- Maximum new main-solve S-unitarity residual approximately 3.58e-13; all common-energy ledgers pass. Flux conservation is NOT an estimate of continuum discretization accuracy.
- The largest final 40x48 to 48x64 product-fraction change is about 0.0138 percentage points, at lambda=0.75,K=4. The qualitative low-energy enhancement and high-energy suppression remain.
- Independent unstrained source-class recovery, with the same discretization.
- Zero-entry and zero-additional-switch controls: both give exactly zero product flux.
- At K=4 on the 20x24 control grid, altering only the potential gives about 1.011% flux; altering only the patch gives about 0.849%; changing both gives about 1.483%. These are explicitly changed models, not separate probabilities to multiply.

No full new two-dimensional independent continuum scattering solver or 501-energy scan was performed. The conservative nonlocal scattering algorithm is inherited, while the new geometric cost and patch have independent tests. Source archival hashes are retained; upstream particle identifications are not certified by these checks.

## 8. An additional geometric phase change that the flux control does not include

A full physical strain model would also change native fold operators. At ABE, correctly transforming the outward normals by C_lambda^(-T) and renormalizing gives

    nu_L.nu_R = (5lambda^2-3)/(5lambda^2+3).

The retained positive-trace fold convention consequently gives the selected-line coefficient

    mu_lambda = (sqrt(5)lambda+i sqrt(3))/sqrt(5lambda^2+3).

For lambda=1 this is the previous `(sqrt(10)+i sqrt(6))/4`. Direct matrix checks confirm the coefficient and that the transformed normals are orthogonal to the actual strained facets. The contact triangle stays isometric while the normal-fold phase changes.

This geometric calculation is deliberately NOT silently inserted into the flux table: changing this one coefficient while keeping all other strained cell folds and spectra unexamined would not be a complete metric-consistent update. The table isolates entrance cost/support with material-reference phase operators fixed. It is not the final predicted response of fully deformed phase-carrying pentachora.

## 9. Boundary and next calculation

The experiment supports a concrete HOW: a specified axial deformation changes the configuration comparison, its active region, and the amplitudes propagated through an otherwise fixed coherent network. It also demonstrates that smaller active area does not imply proportionally smaller conversion.

Still missing: dynamical production of lambda from incoming momentum, an elastic/compression energy and its preparation, a metric-consistent strained phase/kinetic reconstruction, a fully covariant relativistic theory, independently occupied particle states, physical calibration, and a three-output geometric route.

The next native step is to propagate the strain through the geometric fold and phase-comparison operators, before promoting a prescribed lambda family to a collision-driven lambda(v) law. Simply setting lambda=1/gamma separately at each energy is not a derivation of one autonomous deformation dynamics.

## 10. Reproduction

From this directory:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_geometry.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python axial_deformation.py --alpha 1 .75 .5 --nD 20 --nt 24 --ns 160 --output rerun_coarse.json
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python axial_deformation.py --alpha .5 --K 4 --nD 48 --nt 64 --ns 320 --output rerun_fine.json
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_controls.py
    python verify_study.py

The last command audits the retained production receipts. Dependencies are Python, NumPy, SciPy and SymPy. No internet connection, repository changes, fitted experimental constants, or font files are required. The bundle contains the unchanged source scripts and payloads, new implementation and verification scripts, saved receipts, controls, and this note.
