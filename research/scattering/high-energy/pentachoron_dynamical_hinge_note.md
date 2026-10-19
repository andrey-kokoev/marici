# A dynamical hinge driven by retained phase records

Date: 2026-10-11  
Status: Conditional classical-hinge/coherent-record extension. Not a physical electron–positron scattering theory.

## 1. Scope and starting point

The preceding exit-gate note began with the completed 2+8 geometric split and explicitly did not generate the earlier hinge. This calculation instead starts at the connected ten-tetrahedron boundary, with only the ABE face-pairing switch completed. It evolves the hinge up to the next complete-tetrahedron contact. It stops **before** the three additional topology switches and the memory-transfer exit gate.

The source archive `inputs/pentachoron_exit_gate_bundle.zip` is retained unchanged. The script checks its manifest, the nested geometric-split script and inputs, and the connected-phase receipt. It does not claim to rerun the old topology census or all ancestral checkers.

Inherited inputs:

- The centered, marked regular pentachoron and the mirrored pair with common ABE triangle.
- The spatial hinge generator that fixes ABE, with endpoint angle theta_* = acos(-1/4).
- The native twenty-coordinate connected seam matrix L_C, the two retained five-cycle comparison terms X, and the matching projector P.
- The opposite-chirality, common-reference spinor convention and the positive-trace geometric folds, continued through the hinge.
- The prior equal-local-displacement-cost hypothesis assigning inertial weight m/5 to each retained vertex of a body with total mass parameter m.

New modeling choices:

1. Use a **one-dimensional constrained geometric family**: the two bodies counterrotate symmetrically by minus/plus theta/2 about their common triangle, and their joint centroid is fixed. Other rotations, translations, and deformations are not evolved. This is not a proof that an unconstrained collision remains on this path.
2. Treat theta and its momentum as classical variables. Let the normalized complex cell record follow the instantaneous native phase Hamiltonian, and let its energy gradient act back on theta.
3. Use fixed ambient phase frames for this dynamical law. Changing to moving frames requires the connection term derived below; silently dropping it defines another dynamics.
4. Test specified initial phase records at ABE contact. The entrance collision has not been shown to prepare them.
5. Freeze epsilon = hbar = m ell^2 = 1 for the numerical fixture. This fixes a previously uncalibrated inertia-to-phase scale for the test. It is not a relation to c.

No QED formula, experimental branching ratio, fitted speed threshold, or adjustable angular contact tolerance is inserted.

## 2. The native hinge spectrum is flat

Let a be the two-by-two Hermitian spin generator of the retained proper spatial hinge. In the source axes,

    a = (sigma_y + sigma_z)/(2 sqrt(2)).

On all ten cells define

    A = diag(-a/2 repeated five times, +a/2 repeated five times),
    F(theta) = exp(i theta A),
    H_0 = L_C + X.

The hinge-dependent native operator is exactly

    H(theta) = F(theta) H_0 F(theta)^dagger.

This is not merely assumed for the crossing seams. The script reconstructs their shortest-fold spin lifts from the moving normals and proves the scalar and bivector identities as rational functions of tan(theta/2). The half traces remain positive on the open admissible interval. At either endpoint, the continuous lift supplies the corresponding antipodal half-turn. Within-body folds and the source-cycle comparisons transform covariantly. An independent seam-by-seam build checks the full matrix along the path.

Consequently every native eigenvalue, including the lowest one, stays unchanged throughout the hinge. In the retained-cycle convention,

    min spectrum H(theta) = 1.70536038448384... .

There is **no scalar ground-energy slope or barrier** selected by this native operator. It does not prefer theta = theta_* over theta = 0.

This does not make the matrix derivative zero:

    H'(theta) = F(theta) i[A,H_0] F(theta)^dagger.

A stationary eigenstate has zero mean torque, because its expectation of the commutator i[A,H] vanishes. A nonstationary superposition need not. Unitary equivalence of matrices is not permission to discard the connection in a moving-coordinate dynamics.

## 3. Hinge inertia from the retained vertex metric

Use the source hinge generator Omega, satisfying Omega^T = -Omega and Omega^3 = -Omega. For the stored left and right vertices L_i,R_i about the shared ABE centroid, set

    l_i(theta) = exp(-theta Omega/2) L_i,
    r_i(theta) = exp(+theta Omega/2) R_i.

Remove the mean of all ten vertices. Then the kinetic energy of the prescribed relative path is

    T = (m/10) sum_i (|d l_i/dt - d centroid/dt|^2
                     + |d r_i/dt - d centroid/dt|^2)
      = I(theta) theta_dot^2 / 2,

with the exact inertia

    I(theta) = m ell^2 [4/5 + (4/15) sin(theta/2)^2]
             = m ell^2 (14 - 2 cos(theta))/15.

It grows from (4/5)m ell^2 at the original ABE contact to (29/30)m ell^2 at full tetrahedron contact. This is the metric of the **specified symmetric, centroid-fixed path**, not a derivation of all possible two-body kinetic motion or physical electron mass.

The two shared-triangle occurrences move together. Equal and opposite ordinary contact forces at that ideal hinge have zero relative virtual work there. Contact incidence alone therefore does not supply a hinge-driving impulse.

## 4. An autonomous coupled dynamics

For a normalized ambient-frame record z in C^20, define the Hamiltonian function

    E(theta,p,z) = p^2/[2 I(theta)] + epsilon z^dagger H(theta) z.

The newly admitted backreaction law is

    theta_dot = p/I(theta),
    p_dot = p^2 I'(theta)/[2 I(theta)^2]
            - epsilon z^dagger H'(theta) z,
    i hbar z_dot = epsilon H(theta) z.

This is a classical coordinate coupled to a coherent linear record, not a fully quantum joint position–phase scattering state. Conditional on theta(t), phase evolution preserves norm; the coupled flow depends on the state and is not a single linear unitary scattering matrix. Its trajectories must not be interpreted as quantum branching probabilities.

The equations conserve total energy exactly:

    dT/dt = -epsilon theta_dot z^dagger H'(theta) z,
    dE_phase/dt = +epsilon theta_dot z^dagger H'(theta) z.

No externally prescribed switching pulse is used. No record is discarded or renormalized during integration.

For computation use u = F(theta)^dagger z. Then

    i hbar u_dot = [epsilon H_0 + hbar theta_dot A] u,
    p_dot = p^2 I'(theta)/[2 I(theta)^2] - epsilon u^dagger C u,
    C = i[A,H_0].

The theta_dot A term is necessary. Independent ambient-frame integration tests it, and an intentionally omitted-term control fails the energy ledger.

A ground eigenstate at theta = 0 with p = 0 remains there exactly. The model therefore does not automatically produce the split from an initially stationary native ground state.

## 5. Phase-sensitive initial hinge force

The two normalized columns

    b_C = P e_4 / sqrt(P_44),
    b_D = P e_6 / sqrt(P_66)

fix a reproducible basis for the inherited rank-two matching space, in the stored raw coordinate ordering. Both records can pass the earlier matched-sector gate. They are not incoming physical particle spin states.

For

    u_phi = [b_C + exp(i phi) b_D]/sqrt(2),

the exact restriction identities give

    B^dagger H_0 B = [[5,-1/2],[-1/2,5]],
    B^dagger C B = -(sqrt(3)/12) sigma_x,
    B = [b_C,b_D].

Thus the initial native energy and torque at rest are

    E_phase(0) = epsilon [5 - cos(phi)/2],
    torque(0) = epsilon sqrt(3) cos(phi)/12.

Phases are defined relative to these retained records and the transported operators. A consistent phase-frame change leaves the trajectories unchanged. A bare numerical phase without its reference is not a physical observable.

In particular phi = +pi/2 and -pi/2 have identical mean initial native energy 5 epsilon and zero initial hinge kinetic energy. Both have zero instantaneous initial torque, but internal phase evolution produces the exact initial torque derivative

    torque_dot(0) = +/- epsilon^2 sqrt(10)/(12 hbar).

Their first nonzero hinge response is opposite; at rest theta'''(0) = torque_dot(0)/I(0). This demonstrates a phase-to-motion mechanism without supplying an initial hinge impulse. The receipt checks the two-by-two commutator identity exactly.

## 6. Numerical endpoint tests

All three un-kicked preparations start with zero hinge momentum. Times below are in hbar/epsilon for the frozen dimensionless inertia m ell^2 epsilon/hbar^2 = 1.

| Preparation | Initial native energy / epsilon | Result | Arrival time / (hbar/epsilon) | Final hinge kinetic energy / epsilon |
|---|---:|---|---:|---:|
| Native ground eigenstate, at rest | 1.705360384484 | Remains stationary; exact stationary solution | — | 0 |
| (b_C + i b_D)/sqrt(2) | 5 | Reaches +theta_*: ABDE contact | 120.702603632 | 0.001577701573 |
| (b_C - i b_D)/sqrt(2) | 5 | Reaches -theta_*: ABCE contact | 128.279761697 | 0.000727018971 |

The first two **nonstationary** preparations have the same initial total energy and no imposed hinge kick; their retained phase difference changes the direction reached. Both contact endpoints correspond to symmetry-related versions of the same 2+8 geometric split, not new multiplicities or two newly identified physical species.

Their mean native energy decreases by the hinge kinetic energy gained. For the positive route, the final ledger is approximately 4.998422298377 + 0.001577701573 = 5. These are deterministic trajectories of the newly declared coupled model, not conversion probabilities.

Ground-state kick controls (the kick is supplied, not derived from collision speed):

| Supplied initial hinge kinetic energy / epsilon | Time to +theta_* / (hbar/epsilon) | Final hinge kinetic energy / epsilon |
|---:|---:|---:|
| 0.001 | 45.817038320 | 0.000749980875 |
| 0.01 | 14.825814711 | 0.005920794070 |
| 0.1 | 4.606726490 | 0.046659399745 |
| 1 | 1.225253046 | 0.882603918452 |


The positive endpoint is the previously derived ABDE contact. The negative endpoint is its other geometrically admitted hinge direction, reaching ABCE instead. It has the same geometric threshold magnitude; it is not a third output or a new particle channel. Only access to the contact is calculated here.

The initial quarter-turn preparations are nonstationary high-energy native records, not ground states. Their angular kinetic energy comes from changes in that internal expectation. Preparing such a state must itself be accounted for by an entrance model; there is no claim of free energy.

The receipt additionally tests ground-state inputs with small **supplied** angular kinetic energies. These are controls on hinge dynamics, not a derivation of how incoming translational speed injects angular momentum. They do not establish a universal positive speed threshold.

## 7. Verification and limits

The completed main run passes 152 named checks: 21 exact algebraic checks, 12 provenance checks, 118 numerical checks, and one deliberately invalid-model negative control. A separate exact endpoint check verifies the ABCE coincidence at the negative hinge angle.

- Exact identities: source fold continuation along the whole admissible interval, preparation normalization and membership in the old matching space, kinetic metric, and initial torque matrices.
- Independent seam reconstruction at 81 hinge angles: maximum full-matrix discrepancy 1.10e-11.
- Seven primary DOP853 trajectories: maximum total-energy drift 7.15e-11 epsilon and maximum norm drift 7.97e-12.
- Independent RK45 integrations of both long zero-kick trajectories: arrival-time differences below 4.06e-9 hbar/epsilon, full-state differences below 2.25e-8, and energy drift below 2.53e-9 epsilon.
- Independent ambient-frame versus moving-frame integration of the positive route: arrival-time difference below 4.48e-12 hbar/epsilon.
- Complete reverse integration, stationary-eigenstate control, constant phase-frame covariance, and analytic-versus-finite-difference force checks.
- Deliberately omitting the moving-frame connection changes the model and produces an energy-ledger discrepancy of about 0.00459023 epsilon in the selected eight-unit test. It is not used for any reported trajectory.

The analytical Hamiltonian identities establish norm and energy conservation. These residuals assess numerical implementations, not physical accuracy or experimental uncertainty. The constrained reduction has not supplied a complete free two-body angular-momentum balance; collective rotation and other modes remain outside the calculation.

The test preserves all twenty connected phase coordinates. The exit-stage memory can remain an unoccupied spectator until the later operation; this calculation neither populates it nor reuses its exit probabilities.

Remaining boundaries:

- The earlier collision's center separation and internal x–w tilt are not integrated here.
- The entry model has not determined the hinge momentum or the phase preparation.
- The symmetric one-coordinate family and energy-gradient backreaction are explicit new modeling choices.
- Neither geometric endpoint automatically executes the three remaining face switches.
- The subsequent exit gate has a different incident native operator and preparation. Its probabilities cannot be multiplied by these classical trajectories.
- This remains a direct sum of cell records, not two independently occupied particles. No stable product, photon, three-product scattering channel, relativistic speed scale, or 372:1 law is inferred.

The next constructive connection is the post-merger phase preparation and hinge momentum generated by the entrance dynamics, followed by explicit phase-compatible switching at the reached tetrahedron contact.

## Reproduction

    OPENBLAS_NUM_THREADS=1 python pentachoron_dynamical_hinge.py

Keep the unchanged input archive under inputs/. Dependencies are NumPy, SciPy, and SymPy. No network access or repository mutation occurs. The JSON contains exact matrices, source hashes, declared choices, numerical residuals, and the named check ledger. NPZ files contain the retained numerical matrices and sampled trajectories. The --quick option omits the longest independent integrations and is identified in the resulting receipt.
