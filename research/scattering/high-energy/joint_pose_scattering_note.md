# Joint incoming modes connected to pose-covariant product channels

Status: A new, conditional continuation of the supplied phase-record model. **Not physical electron–positron scattering, not a strain-versus-speed law, and not a certified continuum flux curve.**

## 1. Result

The previously constructed joint tilt–phase/strain-direction eigenmodes now have an explicit conservative entrance comparison and outgoing 2+8 record channels. The axial strain is propagated through the original and connected seam matrices, the matching projector, the rigid-hinge endpoint and kinetic metric, the three additional face-switch gates, and the separated product seam matrices.

A necessary extension choice has been made explicit: the whole encounter, its collision/comparison frame, and each pairing configuration are transported with the pose register. In transported comparison frames, the same five-pose cycle energy occurs on every sector. It is not added a second time as the older fixed-cell material-history cycle.

This choice changes the exit bookkeeping. The geometric pose cycle preserves the transported identity of each product and has no links crossing between products. The earlier eight-slot memory encoder stored a different fixed-cell cycle's four crossing links. That older exit gate is not silently reused, and these numerical fractions are not a controlled update of the old flux table at otherwise identical preparation and dynamics.

There is no multiplication of incoming probability by five. Pose labels and native cell records remain in the complete Hilbert space. Ordered paths on the three-switch graph are coherent; there is no extra measurement copying every traversal into a which-path register.

## 2. Sources and new assumptions

The unchanged input is `inputs/pentachoron_joint_incoming_bundle.zip`. Its manifest, its own unchanged strained-phase archive, and the nested ancestral payload manifests are checked. The source supplies the joint incoming operator and pose reduction, native strained geometry and folds, inherited positive comparison coefficients, and the earlier nonlocal separation resolvent.

The immediate source note states that the downstream comparison has not yet been extended to its enlarged incoming space; its sections 2, 6, 8 and 10 distinguish the new preparation from the old beam fixture. Its formulas and explicit boundary are retained here.

New or clarified choices in this step:

1. Transport the complete encounter and its comparison frame with the pose record. Pose-qualified contacts are copies of the same metric comparison in those frames. This is a **pose-covariant interaction contract**, not proof that a laboratory beam aligned to one fixed axis realizes that contract.
2. Retain the new geometric pose-cycle operator throughout the route. Do not also append the superseded fixed-cell material-cycle operator. Each face-switch mask and each product identity is transported with its cell labels.
3. Compare incoming material coefficients with the corrected ABE configuration in its retained material-reference frame. The identity of those coefficient frames across the nonrigid nearest-configuration correction is an admitted adapter; geometry alone does not select it.
4. Use the same normalized uniform sampling of the ABE patch and positive coefficient 2 epsilon. All entry-side, hinge-side and cross terms remain.
5. Freeze the strain at contact and follow the previously admitted rigid counter-hinge path. Recompute its kinetic metric from the actual strained vertices.
6. Continue the full-spinor three-switch gates with coefficient 2 epsilon. Strict selected-line matching is not substituted for that larger operation.
7. Release the final twenty cell records into twenty outgoing cell-record modes by a positive identity-comparison contact. The pose register follows them. The old memory swap is not applied to a cycle which no longer has inter-product links. This is an explicit changed exit prescription, not information erasure from the older model.
8. Prepare the source's equal mixture of lowest joint incoming modes, at fixed lambda and rho=mc^2/epsilon=1. Lambda is not dynamically generated. The preparation dimension differs at lambda=1 and at the compressed values.

All coefficient spaces remain direct sums of phase records. They do not describe two independently normalized, simultaneously occupied physical particles.

## 3. Retain the pose register analytically

In each pose's transported reference frame, let `H_route(lambda)` denote the complete separation/tilt, connected-hinge, face-switch and product operator constructed below. Define the five-site shift by

    S_anti e_j = e_(j+1)    for j=0,...,3,
    S_anti e_4 = -e_0,
    C_pose = 2I - S_anti - S_anti^dagger.

The full operator is unitarily equivalent to

    H_full = I_5 tensor H_route(lambda)
             + epsilon C_pose tensor I_route.

The unitary is the direct sum of the source's successive cell/spin transports, applied consistently on every field and finite pairing configuration. It is independent of the propagation coordinates in these reference frames. The kinetic, contact and exit maps are transported too.

The exact cycle energies are

    c_k = 2 - 2 cos((2k+1)pi/5), k=0,...,4.

Their distinct values are `(3-sqrt(5))/2` twice, `(3+sqrt(5))/2` twice, and 4 once. The cycle spectral channel is conserved by this newly chosen entire-route continuation. The populated lowest cycle channels therefore each see the same scattering problem, shifted by

    c_0 epsilon = (3-sqrt(5)) epsilon / 2.

That energy is retained on both incoming and outgoing sides. Its common shift cancels from their kinetic differences. Taking the equal mixture of the two lowest cycle modes does not multiply or divide the final probability by five.

### Product identity follows the cycle

If `Q_small` selects the two small-product cells in reference pose zero and `V_j` is the j-th source transport, the full small-product projector is

    Q_small,full = direct-sum_j V_j Q_small V_j^dagger.

Both the geometric cycle and the final native operator commute with this product projector. At the cell-label level, `(pose j, cell c)` moves to `(j+1,c+1)`; the small cell label in pose j is also shifted by j. Zero cycle links cross the transported product partition.

Freezing the small-cell label while cycling the pose would instead create spurious crossing links. That is not the product-identification convention used here. Matrix commutators and an independent discrete label census check this distinction for both exits and four strains.

This is not the earlier claim that the fixed-cell operator X had no crossing links. That earlier operator did have them. The enlarged incoming pose-cycle and this entire-route extension are different dynamical data.

## 4. Incoming eigenchannels and contact comparison

For one body retain exactly the source eigenproblem

    h_lambda = -alpha_lambda d_delta^2 + L_0(delta,lambda),
    alpha_lambda = 5/[16(1+lambda^2)]

in the fixture epsilon=hbar=m=ell=1. The opposite-chirality mirror supplies the second body sector by its retained constant unitary. The full source modes have energies `epsilon(e_a+c_k)`.

For radial kinetic energy K above the new lowest joint incoming mode, use common total energy

    E_total = epsilon(e_ground+c_0)+K.

In the reduced populated pose channel, use `E=E_total/epsilon-c_0` in the numerical boundary solve. For an original eigenchannel with rotor/seam energy e_a, put z_a=E-e_a. Its radial square-root dispersion is unchanged:

    k_a = sqrt(z_a+z_a^2/(4rho)),
    v_a = 2 k_a/[1+z_a/(2rho)]       for z_a>0.

The incoming amplitude has factor `1/sqrt(v_a)`. The eigenfunction in tilt and phase already includes its angular kinetic energy. **K here is radial energy, not the older combined separation-plus-free-rotor K.** Closed channels are retained in the projected solve; the code refuses a mode cutoff omitting any propagating channel.

### The geometric patch and its measure

The strained comparator and ABE patch are inherited unchanged. With d=D/ell,

    d_lambda = 8lambda/sqrt(30),
    b_lambda = 5lambda/[4sqrt(6)(1+lambda^2)],
    delta_c = atan(1/sqrt(5)),

    0<=d<d_lambda,
    delta_c-asin[b_lambda(d_lambda-d)]
       <=delta<=
    delta_c+asin[2b_lambda(d_lambda-d)].

The scalar correction cost is also unchanged:

    v_lambda(d,delta) = min_t {
        (5/2)[2lambda a(t)-d]_+^2
        +16(1+lambda^2)[1-cos(t-delta)] },
    a(t)=max(|cos t|-sin(t)/sqrt(5),4sin(t)/sqrt(5)).

Use incoming material coefficients normalized in ddelta. The physical metric factor between y and delta is constant for each fixed lambda. Transforming both the wavefunction and normalized patch sampler to ddelta cancels that factor; it is not accidentally counted twice in the contact energy.

Let `A_delta` be the patch area in dD ddelta, `f=1/sqrt(A_delta)` on the patch, and `P_lambda` the rebuilt rank-two ABE matching projector. The reference-pose entry form is

    Q_join = 2epsilon integral_patch
        ||P_lambda Psi(D,delta) - f sqrt(ell) P_lambda chi(0)||^2 dD ddelta.

Take its pose-covariant direct sum before performing the analytical cycle reduction. This retains mismatch and unsampled incoming modes. The coefficient-frame adapter and uniform sampler are model choices.

## 5. Rebuild the hinge and all native product comparisons

The rigid hinge endpoint is inherited from the strained geometry:

    theta_*(lambda)=2 atan(sqrt(5/3)lambda).

Applying the same equal-vertex inertial weights to the counterrotating, centroid-fixed path gives the new exact metric

    I_hinge(theta,lambda)
        = m ell^2 [6+8lambda^2-2lambda^2 cos(theta)]/15.

At lambda=1 this is the previous `(14-2cos(theta))/15` result. At zero angle it is `(2/5)m ell^2(1+lambda^2)`. The exact symbolic derivation evaluates all ten vertex velocities and subtracts their common centroid velocity.

Use arc length `s(theta)=integral_0^theta sqrt(I_hinge/m) dtheta`. The kinetic form is `(hbar^2/2m) integral ||d_s chi||^2 ds`. In the populated pose sector its native potential is

    F(theta) L_C(lambda) F(theta)^dagger,

with no second fixed-cell cycle added. The source's continued cross-seam spin folds and all selected/complementary components are retained. Both endpoint seam operators agree with this transported connected operator.

Each endpoint has eight pairing masks, their rebuilt seam energies, and the three inherited full-spinor matching projectors Q_f. Neighboring masks are coupled by

    2epsilon ||Q_f(eta_b-eta_b')||^2.

The final mask has the same 2+8 cell partition and a block-diagonal product seam matrix L_F(lambda). Its release comparison is

    2epsilon ||sqrt(ell) zeta(0)-eta_111||^2,

with outgoing half-line energy

    integral [kappa_F ||zeta'||^2 + epsilon zeta^dagger L_F zeta] dy,
    kappa_F=1 in the numerical fixture.

The pose cycle is present on each of those records in the full operator. The product blocks remain independent because it preserves the transported partition. This release law is not the older memory swap applied under another name.

## 6. Conservative scattering and numerical method

Every local interaction is a positive squared comparison. The original geometric potential is bounded on its compact support. Its patch sample is bounded in L2, and all point samples are traces of one-dimensional hinge/output H1 fields. The circle rotor and the source's positive square-root Neumann separation operator retain their specified domains. Together these forms define a lower-bounded self-adjoint time-independent operator in the declared model. Total norm and energy are conserved.

The numerical entrance is a Galerkin projection onto joint internal eigenmodes and normalized radial cell functions. All retained radial Green kernels use the source's complete nonlocal square-root resolvent, including its real correction and closed-channel continuation. It is not a local wave equation with a substituted wave number.

The downstream hinge uses exact constant-midpoint-potential segment solutions; an independent finite-element control converges toward it. The endpoint finite-record graphs and outgoing logarithmic derivatives are retained directly. The two parts are connected through the rank-two matching trace, rather than multiplying earlier stage probabilities.

The complete scattering matrix is formed over all propagating incoming and outgoing channels of the **populated conserved pose-energy block**. Other pose-energy blocks are invariant by the analytical factorization; they are not all independently scanned numerically here.

At a fixed total energy, the asymptotic ledger is

    P_original + P_product,- + P_product,+ = 1,
    K_out,a = E_total - E_internal,a.

A numerical energy ledger at one energy is a consistency test, not an independent proof of time-dependent conservation.

## 7. Calculated flux ranges

The following ranges span three actual sets of calculations: a principal basis/grid, a spatial refinement, and an internal-mode-cutoff refinement. **They are not rigorous continuum error bars, confidence intervals, or a converged physical prediction.**

Input: equal mixture of the new lowest joint modes at each lambda; rho=1; pure radial K above the corresponding joint ground. Both symmetry-related 2+8 output routes are summed.

| K/epsilon | lambda=1 | lambda=0.75 | lambda=0.5 |
|---:|---:|---:|---:|
| 1.0 | 0.0532–0.0541% | 0.5835–0.5995% | 0.6246–0.6322% |
| 2.3 | 0.1039–0.1066% | 0.9415–0.9780% | 0.5398–0.5465% |
| 4.0 | 1.4874–1.4942% | 2.3558–2.4366% | 0.6341–0.6440% |
| 6.0 | 0.8534–0.9343% | 0.0754–0.0825% | 0.2729–0.2902% |

The ranges support a nonmonotonic response over these samples. They do not locate resonances or give a universal monotonic strain law. The two route fluxes are equal to the recorded precision for this symmetric lowest-mode preparation and pose-covariant continuation; this is not a universal left/right selection rule.

The uncompressed lowest-mode ensemble has sixteen modes in the full enlarged register; the compressed ensembles have eight. The old uncompressed source beam had four native modes and a different angular preparation. The new table must not be used as an otherwise-identical comparison with the old percentages.

All entries are phase-record flux fractions. The lower energy of a normalized direct-sum product mode does not establish two independently occupied product rest energies, and a record lead does not identify a stable free particle.

## 8. Verification actually performed

`verify_joint_flux.py` records 285 passing checks, including repeated conservation/cutoff checks on the saved solves. This count is not 285 independent theorems.

- Exact symbolic strained hinge inertia and unstrained recovery.
- Exact antiperiodic five-cycle polynomial and fifth power.
- Pose-cycle reduction, contact covariance, output-projector commutators, and a separate label-level crossing-link census.
- Strained endpoint recovery, product block structure and incoming-mode normalization.
- Positivity of the projected patch comparison, with a separately checked area quadrature.
- A separate full coupled entrance-plus-downstream block solve on a small fixture, agreeing with the modular elimination.
- Full scattering-matrix covariance under consistently changed incoming eigenchannel phases.
- Tighter quadrature for the nonlocal radial resolvent.
- No-entry and no-switch controls: exactly zero product flux.
- Independent finite-element versus exact-segment hinge calculations. In the stated small control, the difference reduces from about 1.28e-5 to 3.24e-6 in absolute product probability as finite elements double from 80 to 160.
- Thirty-six production solves covering three strains, four energies, and three resolution/basis choices.

Across those production solves, the largest numerical S-unitarity residual is approximately `1.313e-12`; the largest energy-ledger residual is approximately `2.23e-14 epsilon`. The final observed spatial-refinement change is at most about **0.00942 percentage points**. The internal-mode refinement changes a sampled flux by as much as **0.08084 percentage points**. The latter prevents interpreting the much smaller conservation residual as a continuum accuracy bound.

All propagating original modes are below the retained cutoff. High closed modes are necessarily truncated and varied. The pilot code deliberately refuses its K=6 solve when a requested smaller basis would omit an open channel; its earlier three pilot rows are retained separately, not included in the 36 production rows.

No independent full two-dimensional continuum solver, all-energy maximum, 501-energy scan, or experimental check is claimed. The source's ancestral checker chains are not all rerun; their archive and payload hashes are checked.

## 9. Research boundary

Established: one positive, pose-retaining entrance-to-product Hamiltonian; a consistent cycle convention and product partition; strained joint incoming modes; a rebuilt strained hinge and face-switch route; and conservative numerical flux with explicit basis sensitivity.

Not established:

- a microscopic reason for the whole-encounter pose-covariant contract instead of fixed-laboratory-axis pose-selective contact;
- a derived physical beam preparation of the enlarged pose register;
- a converged continuum scattering curve;
- a dynamical strain variable, an elastic energy budget, or lambda(v);
- a Lorentz-covariant many-particle theory;
- independently occupied outgoing particles, stability, charge or species identity;
- photons, a three-output geometric scattering route, or 372:1.

A useful next construction is an autonomous strain coordinate and its energy, so incoming momentum creates or maintains compression rather than selecting a different fixed-lambda Hamiltonian by hand. The present cutoff sensitivities remain part of the numerical record.

## 10. Reproduction

The bundle contains the unchanged immediate input archive, the solver, the independent verifier, and all numerical receipts. No network access or repository changes are required.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_pose_scattering.py \
      --lambda 1 .75 .5 --K 1 2.3 4 6 --nD 16 --nm 100 --N 65 --ns 160 \
      --nquad 160 --output main.json

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_refinements.py

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_joint_flux.py

`joint_flux_summary.json` states the changed rules and aggregates the ranges. `main.json`, `radial_refinement.json`, and `mode_refinement.json` contain every production row, channel count, prepared degeneracy, cutoff and residual. `verification.json` contains the exact identities, discrete structural controls and independently solved small tests.
