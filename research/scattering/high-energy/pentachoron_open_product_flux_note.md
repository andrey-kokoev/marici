# Open hinge endpoints with retained face switches and product flux

Date: 2026-10-11  
Status: New, conditional quantum-configuration scattering calculation. **Not a physical electron–positron result.**

## 1. Result and exact scope

The source's reflecting hinge endpoints are replaced by two explicit product exits. Each exit retains the three remaining face switches, their intermediate pairing configurations, native phase energy, and the reversible memory encoder. A single, time-independent joint model now carries nonzero asymptotic flux from the original 5+5 record channel to a 2+8 product-record channel.

No angular-region probability, intermediate occupation, or earlier conditional exit percentage is reused as a splitting probability. The result comes from a new full boundary-value scattering solution, including all propagating and evanescent native modes.

**The additional switches are not automatic.** Their native selected lines do not admit the unchanged exact unitary sewing rule. An explicitly enlarged full-spinor switching rule is supplied below. The existence of outgoing flux, as well as its numerical value, is conditional on that extension and on the new endpoint couplings.

## 2. Source boundary

The unchanged supplied quantum-hinge archive provides:

- original and connected C20 native operators H_O and H_C, with retained cycle comparisons;
- the rank-two entrance matching projector P;
- the hinge generator A and H_C(theta)=F(theta)H_CF(theta)^dagger;
- F(theta)=exp(i theta A), A^2=I/16;
- the angular interval +/-theta_*, theta_*=acos(-1/4);
- the arc coordinate s(theta), |s|<=s_*=1.692754342871824 ell;
- the original encounter line and kinetic coefficients kappa_O=1, kappa_C=1/2 in model units;
- the equal mixture of four lowest original native modes.

The supplied geometric-split archive provides the metric endpoint poses, the triangle-pairing rules, the 2+8 components, and the full-spinor half-turn continuation convention. The supplied exit-gate archive provides the residual-memory construction and its common energy reference.

All source archives were read from the mounted attachments. Their SHA256 hashes and the hashes of the compact extracted payloads are recorded in `input_hashes.json`. The new audit checks those payloads and reconstructs the endpoint matrices from them. It does not claim to rerun the ancestral topology census, experimental correspondence, or repository checker chains. No network request or repository modification is used.

## 3. Additional assumptions

1. Each complete-tetrahedron contact has eight localized pairing configurations: the original ABE merger plus every subset of its three additional eligible face switches. They have their own C20 records; they are not eight outgoing particles.
2. A face switch is controlled by full-spinor matching under the retained geometric folds. This extends the original selected-line trigger; it does not silently pretend the selected lines already match.
3. Every one-bit neighboring pair is coupled by the same positive involution-defect energy, coefficient 2 epsilon. The six shortest switch orders interfere within this graph. They are not six incoherent event weights.
4. The hinge endpoint couples to its zero-extra-switch record through a positive point-sampling comparison. The final pairing couples through the memory encoder to an outgoing half-line. Both trace-to-record coefficients are set to 2 epsilon, with sampling length ell. These dynamical choices are not selected by incidence alone.
5. Keep the native seam and transported source-cycle operators in every finite pairing state. Keep eight local memory coordinates with the same positive memory operator before and after exit.
6. Use outgoing kinetic coefficient kappa_F=1, as in the previous reduced exit model. In particular, reduced mass is not inferred from the 2:8 cell partition.
7. Use **stationary, monochromatic** incoming native-ground modes, averaged equally. This is not the previous finite-bandwidth packet, although its internal mixture is the same.
8. Preserve the same dimensionless scale choice epsilon=hbar=ell=m=1. None of the numerical energies below is a calibrated particle energy or a speed divided by c.

The calculation still conditions on initial access to ABE. It does not generate the original compression, axial tilt, or an experimentally defined electron–positron encounter.

## 4. Endpoint geometry and phase sewing

At +theta_* the coincident tetrahedron is ABDE. The required additional switches are BDE, ADE, ABD. At -theta_* it is ABCE, with switches BCE, ACE, ABC. Both are actual retained geometric endpoints, with the right and left bodies counterrotated consistently. The two route labels are different lead histories, not different output multiplicities.

For every face, retain two crossed seams: between the two occurrences of the omitted small-product cell, and between the other corresponding cells. The native full-spinor maps U have the prescribed positive/continued spin-lift conventions. At antipodal normals the face plane determines the half-turn, with the uniform sign continued from ABE.

For a selected incoming face projector p_L and outgoing projector p_R, exact calculation gives

    (p_R U p_L)^dagger (p_R U p_L) = c_face p_L.

| Positive-route face | c_face | Complementary squared component |
|---|---:|---:|
| ABE, already switched | 1 | 0 |
| BDE | 7/9 | 2/9 |
| ADE | 7/9 | 2/9 |
| ABD | 1/9 | 8/9 |

Both incident seams have the same value on a face. The negative route has the symmetry-related values. These are **selected-line overlaps, not probabilities of a complete splitting event**.

For each additional face, strict equality y=Ux with x in im(p_L), y in im(p_R) has no nonzero solution in the selected line, because 1-c_face>0. Renormalizing p_R U p_L to a unitary would discard its complementary component and alter the operation. The present model instead keeps the complete two-component native records.

On the two full spinor records of a crossed seam define

    q_U = (1/2) [[I,U^dagger],[U,I]].

Then q_U^dagger=q_U and q_U^2=q_U. The two disjoint crossed seams on a face give a rank-four projector Q_f in the existing C20 record space. Complementary amplitudes remain in that record space. No nonlinear normalization or destructive projection is used.

Between neighboring pairing sectors b,b' the corresponding involution is

    J_f = [[I-Q_f,Q_f],[Q_f,I-Q_f]],  J_f^2=I,

and its positive energy is

    epsilon (J_f-I)^dagger(J_f-I)
        = 2 epsilon [[Q_f,-Q_f],[-Q_f,Q_f]].

This is the explicit new full-spinor topology-switch rule. It is not a proof that nature supplies that operator.

### Coherent order dependence

The three Q_f do not commute. Their six shortest ordered products therefore cannot be replaced by six copies of one amplitude. On the common four-coordinate doubled-cell pair, exact algebra gives

    B = sum_over_six_orders q_f3 q_f2 q_f1,
    B^2 = (4/9) I_4,    tr(B)=0.

The corresponding leading operator on all twenty cell records has this block and is zero on the other sixteen coordinates. Higher-order propagation includes native evolution and revisits to pairing states. This is an operator sum, not a derivation of amplitudes from an unsigned history count. Ordered traversal histories are not separately measured or permanently copied into additional history registers; they remain coherent paths on the retained configuration graph.

## 5. Native endpoint records and memory

For each b in {0,1}^3, reconstruct its twenty seams from the actual face-pairing pattern and use

    H_b = epsilon (L_b + X_endpoint).

All cells and seam occurrences remain. The b=000 operator agrees with F(+/-theta_*) H_C F(+/-theta_*)^dagger. Seven of the eight states are connected; b=111 is the 2+8 split. The oriented manifold interpretation is inherited from the source's exact local pairing census; this new script separately checks connectivity and the retained adjacency records.

At each endpoint the four cycle comparisons crossing between prospective products form D:C20->C8. Define

    M=DD^dagger,
    W=M^(-1/2)D,
    N=I-W^dagger W,
    U_exit=[[N,W^dagger],[W,0]].

Retain exactly

    spectrum(M) = {1,3}, each fourfold,
    U_exit^dagger U_exit=I_28,
    W^dagger M W = D^dagger D.

The final localized record is z=(eta_111,w) in C28. Its native energy before release is H_111 direct-sum epsilon M. The outgoing operator is

    H_F = epsilon [(L_F+D_internal^dagger D_internal) direct-sum M].

It is block diagonal between the small-with-memory twelve-coordinate sector and the large sixteen-coordinate sector. Memory placement and interpretation remain the prior explicit convention. A memory-only amplitude is not evidence that two independent physical particles have simultaneously been occupied.

The positive endpoint's memory and outgoing matrices agree with the supplied exit matrices after the required common spin-frame rotation. The negative endpoint is separately rebuilt at its actual pose rather than being assigned an unexplained copy of the positive matrix.

## 6. One autonomous open system

Use the Hilbert space

    H_original = L2(R) tensor C20,
    H_hinge    = L2([-s_*,s_*]) tensor C20,
    H_end,+/-  = (direct-sum of eight C20 pairing records) direct-sum C8 memory,
    H_out,+/-  = L2(R_+) tensor C28.

There are 168 finite record coordinates per endpoint. They are not extra geometric tetrahedra. The norm is the sum of all field integrals and finite-record squared norms.

Retain the source's kinetic and native hinge/original forms and original-to-hinge contact at zero. Add, at each endpoint:

    sum_b eta_b^dagger H_b eta_b + epsilon w^dagger M w,

    2 epsilon sum_edges ||Q_f(eta_b-eta_b')||^2,

    2 epsilon ||sqrt(ell) chi(+/-s_*)-eta_000||^2,

    2 epsilon ||sqrt(ell) zeta_+/-(0)-U_exit(eta_111,w)||^2,

and the outgoing half-line form

    integral_0^infinity [kappa_F ||zeta'||^2 + zeta^dagger H_F zeta] dy.

Every coupling retains its diagonal and off-diagonal terms. No contact-dependent scalar energy offset is dropped. The closed lower-bounded quadratic form on the one-dimensional H1 fields and finite records defines a self-adjoint, time-independent joint Hamiltonian: the trace terms are bounded in the H1 form norm and all finite native matrices are bounded Hermitian positive operators. This is the same form construction used in the source, now with actual output leads.

There is no prescribed time pulse, independent residence-time clock, imaginary absorbing sink, or multiplication of the earlier stage probabilities. Motion and all internal records share one total energy.

## 7. Scattering and flux

Outside contact, for an outgoing native eigenvalue e_n and total energy E,

    k_n = sqrt((E-e_n)/kappa),
    v_n = 2 kappa Re(k_n)/hbar.

Open modes use positive k_n and unit flux normalization 1/sqrt(v_n). Closed modes use k_n=i sqrt((e_n-E)/kappa); they stay in the boundary solve and have zero asymptotic current.

The original line has two asymptotic directions. Each product endpoint has its own outward half-line. Eliminating those exterior fields gives their exact outgoing logarithmic-derivative operators, not phenomenological decay widths. All incident directions are also included when constructing the full scattering matrix S.

Green's identity for the conservative interior form cancels every internal current and leaves

    S^dagger S=I,
    R_original + T_original + P_exit,- + P_exit,+=1.

The common-energy channel ledger gives

    E_kin,out,n = E-e_n.

For the inherited ground mixture, the entrance still has two dark native combinations and a decoupled odd spatial component. Only one quarter of that incoming mixture can access the interacting even/bright sector, so

    P_exit,- + P_exit,+ <= 1/4.

This is a feature of the chosen point-contact preparation, not a general limit on electron annihilation.

## 8. Stationary numerical results

The original native ground energy is

    e0=(11-2sqrt(6)-sqrt(5))/2 = 1.932476268466933... epsilon.

For equal incoherent incoming ground modes, at E=e0+K:

| Incoming K/epsilon | Original topology, both directions | Negative hinge product route | Positive hinge product route | Total 2+8 product flux |
|---:|---:|---:|---:|---:|
| 1.00 | 99.963446% | 0.009778% | 0.026776% | 0.036554% |
| 2.30 | 99.947642% | 0.026381% | 0.025978% | 0.052358% |
| 4.00 | 97.747755% | 1.404601% | 0.847644% | 2.252245% |
| 6.00 | 99.571255% | 0.293976% | 0.134768% | 0.428745% |

The displayed output channels correspond to symmetry-related versions of the same two-boundary geometry. They are not two-versus-three particle outcomes.

These are stationary flux fractions, not the source's finite packet occupations. The numerical values depend on the new full-spinor face gates and endpoint trace couplings. In particular, the curve is not monotone: the value at 6 epsilon is smaller than at 4 epsilon even though the same face-switch graph is available.

### Common energy reference

Both reflected/transmitted original modes and product modes are included in these mean-energy values:

| Incoming K/epsilon | Total E/epsilon | Mean outgoing native/memory energy | Mean outgoing kinetic energy |
|---:|---:|---:|---:|
| 1.00 | 2.932476268467 | 1.932321441082 | 1.000154827385 |
| 2.30 | 4.232476268467 | 1.977512332569 | 2.254963935898 |
| 4.00 | 5.932476268467 | 1.961694077683 | 3.970782190784 |
| 6.00 | 7.932476268467 | 1.957706245292 | 5.974770023175 |

The last two columns add to the second, within the recorded numerical residuals. An outgoing product mode can gain or lose native energy relative to an original mode; its kinetic energy changes by the opposite amount. No energy is attributed merely to an arrow count.

### Contact-law sensitivity, not a fitted constant

Changing only the coefficient of the three face-switch gates, leaving geometry, matrices, endpoint sampling, and incoming preparation fixed, changes the result:

| Incoming K/epsilon | Switch coefficient / epsilon | Product flux |
|---:|---:|---:|
| 2.30 | 1.0 | 0.005843% |
| 4.00 | 1.0 | 0.862394% |
| 2.30 | 2.0 | 0.052358% |
| 4.00 | 2.0 | 2.252185% |
| 2.30 | 4.0 | 0.925394% |
| 4.00 | 4.0 | 1.105292% |

The primary value 2 is inherited from the chosen involution-defect normalization, not optimized against any output. The sensitivity is evidence that the numerical fractions are not forced by geometry alone.

## 9. Verification

The supplied result JSON records all checks and residuals. Verification includes:

- exact selected-line overlaps and their complementary components;
- exact full-spinor matching projectors and topology involutions;
- the exact six-ordered-path identity and noncommuting face gates;
- both endpoint geometries, native matching at the hinge trace, 8-state connectivity, and outgoing component independence;
- memory-encoder inversion, unchanged stored comparison energy, and positive memory spectrum;
- the full scattering matrix on a fixed 501-energy scan from K=0.05 to 8 epsilon;
- direct boundary-current cancellation, independently of summing squared scattering amplitudes;
- no-entry, no-switch, and closed-endpoint controls, all giving zero product flux;
- consistent full-record phase-frame covariance;
- finite-element refinement at 80, 160, 320 angular intervals;
- an independent exact-per-segment differential solver at 80, 160, 320 intervals.

The second spatial method holds the smooth native potential constant at each segment midpoint and solves that segment analytically. Its endpoint matrix has diagonal kappa k cot(k ds) and off-diagonal -kappa k csc(k ds), with analytic removable-singularity limits. It is not the finite-element stencil under another name. Both discretizations converge to the same smooth-potential interval problem.

Primary values use 320 exact segments. At the four reported energies, the 160-to-320 exact-segment product-flux changes are below 1e-6 in absolute probability, and the 320-segment versus 320-element differences are below 5e-6. Numerical mesh size is not a physical geometric tolerance.

The full-matrix scan has maximum unitarity residual 4.794e-13, maximum common-energy bookkeeping residual 3.908e-14 epsilon, and maximum relative stationary-equation residual 2.525e-13. These are numerical implementation diagnostics, not experimental errors. The form and current identities provide the analytic conservation argument.

No extremum of the sampled scan is asserted to be a global maximum or an exactly located resonance. Narrow spectral features need energy-specific resolution before being quoted as continuum predictions.

## 10. What has advanced and what has not

The model now supplies one conservative amplitude calculation through

    original encounter -> connected hinge -> retained face-switch graph
      -> memory-preserving exit -> outgoing 2+8 record channel.

It retains unsuccessful and reversed paths; they are not discarded to force an output. The result is not obtained by normalizing and launching a rare connected branch as the entire original state.

Still absent:

- a derivation of the full-spinor exit rule from the original rank-one port prescription;
- a physical realization and microscopic selection of endpoint sampling and couplings;
- collision-driven compression and access to the initial ABE interface;
- a tensor-product preparation and energy law for two independently occupied physical products;
- stability, species identity, photons, an admitted three-output geometric path, physical velocity calibration, or a 372:1 prediction.

The next useful connection is the compression-and-tilt stage, so collision speed determines access to the initial triangular interface as well as subsequent propagation through this already constructed route.

## 11. Reproduction

Keep `inputs/` and `input_hashes.json` beside the two scripts. Run

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_open_products.py

For a single stationary test:

    OPENBLAS_NUM_THREADS=1 python open_product_solver.py --ns 160 --K 1 2.3 4 6

Dependencies: NumPy, SciPy, SymPy. The calculations require no network access. The bundle contains the compact retained inputs, script hashes, result JSON, and endpoint matrices. The source archives remain unchanged outside the new bundle.
