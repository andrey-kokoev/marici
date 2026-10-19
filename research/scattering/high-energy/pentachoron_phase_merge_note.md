# Local phase-compatible pentachoron merging gate

Date: 2026-10-11  
Status: Constructive extension with exact finite-matrix checks. Not a physical electron–positron scattering result.

## Result

At the previous toy's complete ABE contact, the marked geometry and the source's chiral face-projector formula supply explicit cross-body selected-line maps. In the inherited common Pauli frames, opposite chiralities admit these maps; the same-chirality minimal-fold overlap is zero.

The shortest normal fold with its positive-trace spin lift contributes the phase

    mu = (sqrt(10) + i sqrt(6))/4 = exp(i alpha),
    alpha = acos(1/4)/2 = 37.7612439070 degrees.

A new **match-enabled switching rule** then produces a unitary gate between the old and crossed face-pairing records. It retains mismatch in the original-pair sector. For equal-strength boundary inputs with phase difference varphi measured after the fold comparison, the gate gives

    P_merge = cos(varphi/2)^2 sin(theta)^2,
    theta = pi T_ABE/(2 tau).

The microscopic gate time tau is not determined. This is a conditional probability in a local linear phase-record model, not a calibrated annihilation or scattering probability.

## 1. Inputs and new choices

### Inherited from the supplied files

The preceding boundary-gluing bundle provides the centered regular pentachoron, the mirrored pair, its x–w rotation, the full ABE contact triangle, the two admitted face-pairing records, their inverse operation, and the triangular-comparator time window on the unmodified classical trajectory.

The actual four cut face occurrences, in order, are

    L_omit_C:ABE, L_omit_D:ABE, R_omit_C:ABE, R_omit_D:ABE.

Their fixed induced signs in that checker are

    +1, -1, -1, +1.

The original pairings are (0,1) and (2,3); the admitted crossed pairings are (0,2) and (1,3). All tetrahedron/face occurrences and the original pairing instruction remain registered. The topology checks are rerun here, but the classical trajectories are reused from their hash-bound receipt, not reintegrated after merging.

The repository supplies two further mathematical ingredients:

* `pentachoron-geometric-spin-interfaces.md`: chiral bivector directions, native rank-one face projectors, and the minimal-fold spin lift.
* `native-operation-energy-lift.md`: the positive operation-defect rule, including its involution specialization. Its physical time/energy conversion remains unspecified.

Source URLs, source blob identifiers and input-file SHA-256 hashes are recorded in the result JSON. Reusing formulas is not a rerun of those repository checkers' entire historical proof chain.

### Explicit new interaction choices

1. Test the opposite-chirality pair in the existing frozen mirrored geometry and common Pauli-frame convention. This is not an identification of chirality with charge or positrons.
2. Compare crossed ports by the shortest cross-body normal fold and its positive-trace spin lift. The inter-chirality reference identification in these frames is part of the local sewing convention, not a globally derived Pin transformation.
3. Permit the whole topological pairing switch only on the matching linear phase-record sector. Other sewing/trigger rules are possible; this one is not forced by the mere existence of a gluing face.
4. Retain mismatch in the original-pair sector rather than erasing or renormalizing it away.
5. Use the common positive involution generator with gate time tau, and omit an independent energy detuning between topology sectors in the bare gate.
6. Let the pre-switch trajectory's triangular comparator activate the gate. The comparator is not a second realized physical configuration, and the present gate is not yet coupled back to translational or rotational motion.

## 2. Reconstruct the actual chiral face records

At delta_c = atan(1/sqrt(5)), the contact triangle is at constant x. Its retained edge Gram matrix remains

    [[8,4],[4,8]] ell^2.

Using b=(B-A) wedge (E-A), its positively ordered chiral directions in the fixed axes are

    n_+(b) = (0,-1/sqrt(2),-1/sqrt(2)),
    n_-(b) = -n_+(b).

These use precisely the source definitions

    s_eta(b) = (b_yz + eta b_xw,
                b_zx + eta b_yw,
                b_xy + eta b_zw),
    n_eta = s_eta(b)/(4 sqrt(3)),
    P_eta = (I - n_eta.sigma)/2.

Insert the four occurrence signs before forming the projectors. For either crossed seam in this pose:

* Same chiralities give complementary selected lines.
* Opposite chiralities give equal selected lines in the declared common frame.

This statement concerns these ports and this comparison convention. It is not a global selection rule for every geometry or possible spinor interface. Internal source folds are still curved, and their original zero-parallel-state obstruction is not removed.

## 3. The cross-body fold supplies a complex phase

The outward unit four-normals of the two cells omitting C, after the common internal rotation, are

    nu_L = (sqrt(6),-sqrt(5),sqrt(5),0)/4,
    nu_R = (-sqrt(6),-sqrt(5),sqrt(5),0)/4.

For the cells omitting D, reverse the signs of the y and z components. For both seams,

    nu_L.nu_R = 1/4.

The shortest proper rotation between these normals fixes both actual ABE edge vectors. With c=1/4, K=nu_R nu_L^T - nu_L nu_R^T, it is

    R_fold = I + K + K^2/(1+c).

Apply the source spin-lift formula:

    a = sqrt((1+c)/2) = sqrt(10)/4,
    U = a I - i s_eta(nu_L wedge nu_R).sigma/(2a).

The checker verifies R_fold's action, orthogonality and determinant, U's unitarity and determinant, and covariance on all six independent bivectors for both chiralities.

For left chirality + and right chirality -, both crossed selected-line maps satisfy

    P_R U P_L = mu P_L,
    (P_R U P_L)^dagger(P_R U P_L) = P_L,
    mu = (sqrt(10)+i sqrt(6))/4.

For the reversed chirality assignment the scalar phase is conjugated. For the same-chirality comparison, P_R U P_L=0 on both crossed seams.

The phase is an operator coefficient in fixed port frames, not an independently measurable universal angle. Rephase a port and the link must rephase with it. Reversing the lift sign while holding source inputs and frames fixed changes the model's seam comparison; changing frames consistently does not change a probability. Neither extra fold paths nor their signs are inferred from counting endpoint bijections.

## 4. Keep matching and mismatch information

Let x=(x_C,x_D) and y=(y_C,y_D) be the selected scalar face-line coefficients on the left and right. They are linear phase records, with declared norm

    ||psi||^2 = ||x||^2 + ||y||^2,   psi=(x,y).

This is a local direct-sum mode model. It is not a construction of the tensor-product Hilbert space of two independently prepared particles, and the Born probability rule is inherited from the coherent-operator framework rather than derived from arrow counts.

Transport right coefficients into the left comparison frame and form

    r = (x + mu^* y)/sqrt(2),
    d = (x - mu^* y)/sqrt(2).

Both are retained. The full encoder and decoder are

    B = (1/sqrt(2)) [[I, mu^* I],
                    [I,-mu^* I]],
    B^dagger B = B B^dagger = I,
    x = (r+d)/sqrt(2),
    y = mu(r-d)/sqrt(2).

Thus ||r||^2+||d||^2=||x||^2+||y||^2. Averaging is not identification of two unknown states and not a cloning operation.

Write Q=diag(I_2,0_2), P=B^dagger Q B, and A=Q B. Then

    A^dagger A = P,   A A^dagger = Q.

P is the source matching projector. A transfers only its two-dimensional image into the connected branch's matched coordinates. Its two-dimensional kernel is not deleted; it stays in the old topology sector.

The connected branch retains all original occurrence labels, the gluing instruction and a mismatch register. The latter is zero on a newly transferred matched component. Applying B^dagger reconstructs the four original independent port records on that component. Nothing is deduplicated just because two occurrences have coincident vertex labels.

## 5. A genuine unitary topology-switch operator

Take the direct sum of an original-pair phase-record space and a connected-boundary phase-record space, both C^4. Define

    J = [[I-P, A^dagger],
         [A,   I-Q    ]].

Exact calculation gives

    J^dagger=J,   J^2=I.

It exchanges the matching parts of the two topology sectors and fixes the unmatched parts. Geometric cell/provenance records are spectators except for the already verified reversible pairing instruction. A topology-only relabeling without this declared operator would not constitute dynamics.

Reusing the source involution-defect rule, with a physical clock conversion written explicitly, gives

    H(t) = [pi hbar/(4 tau)] chi_ABE(t) (J-I)^dagger(J-I)
         = [pi hbar/(2 tau)] chi_ABE(t) (I-J).

The common normalization is inherited; tau and its relation to mechanical toy units are not supplied. The gate is positive semidefinite. In units g=pi hbar/(2 tau), its eigenvalues are 0 with multiplicity six and 2 with multiplicity two.

Because the fixed generator commutes with itself at different times,

    theta = [pi/(2 tau)] integral chi_ABE(t) dt,
    U_gate = exp(-i theta)[cos(theta) I + i sin(theta) J].

Starting entirely in the original-pair sector,

    psi_O,out = (I-P)psi + exp(-i theta) cos(theta) Ppsi,
    psi_C,out = i exp(-i theta) sin(theta) Apsi.

Their squared norms sum to ||psi||^2 for every complex input, not just selected examples. At theta=pi/2 the matching part is switched completely and mismatch stays unchanged. A reverse gate recovers all the input information.

## 6. Phase-dependent merging, not probabilities from arrow counts

For a normalized input, let w_match=||Ppsi||^2. Then

    P_merge = w_match sin(theta)^2.

For equal-strength inputs y=exp(i phi)x, with ||x||^2=1/2,

    w_match = [1+cos(phi-alpha)]/2,
    P_merge = cos((phi-alpha)/2)^2 sin(theta)^2.

Here varphi=phi-alpha is the phase difference **relative to the sewing transport**, not to an arbitrary plotting convention.

| varphi | Matching fraction | P_merge |
|---|---:|---:|
| 0 | 1 | sin(theta)^2 |
| pi/2 | 1/2 | sin(theta)^2/2 |
| pi | 0 | 0 |

For equal raw coefficients, phi=0, the matching fraction is (4+sqrt(10))/8. This is not an unpolarized beam prediction or a special observed number. It changes when actual prepared relative phases or the supplied comparison law change. An incoherent mixture must be evaluated as tr(rho P), not treated as a phase-aligned pure input.

Two allowed topologies do not give a probability of one half. The same graph can have no merging, partial merging or complete transfer under different matching states and gate durations.

## 7. Use the previous contact windows without inventing a clock

The preceding validated pre-switch trajectories give:

| Incoming speed | Triangular-comparator duration T_ABE |
|---|---:|
| 0.70 v0 | 0 |
| 0.90 v0 | 0 |
| 1.20 v0 | 0.209512825652 t0 |

Here t0=ell sqrt(m/E_*), and v0=sqrt(2E_*/m), not c. For the last run,

    theta = 0.329101976950 (t0/tau).

Thus the first two trajectories do not activate this particular merging gate. The last has a nonzero gate window, with merging still dependent on phase and the undetermined time ratio. It need not have nonzero transition probability for every state or every pulse area.

The old trajectories and their time windows are inputs to this test. The code does not claim they remain correct after amplitude occupies the connected branch. No new threshold in units of c or 372:1 ratio is derived.

## 8. Energy and global-state limitations

The bare gate treats the original and connected topology records as energetically degenerate apart from its own defect energy. The source does not yet supply the connected boundary's autonomous energy. This matters: adding an offset Delta to the connected sector changes the active two-level result to

    P_merge = w_match * g^2/[g^2+(Delta/2)^2]
              * sin( T sqrt(g^2+(Delta/2)^2)/hbar )^2

for constant g, T and Delta. A numerical matrix-exponential control checks this formula. The original arrow count and gluing geometry are unchanged.

The same-chirality zero is a limitation of the tested projected shortest-fold sewing, not a theorem prohibiting other spinor couplings. The opposite-chirality success is local: it does not show compatibility with every seam or loop of the newly connected boundary. Original within-body defects and spin-lift choices remain meaningful. A full post-gluing native Hamiltonian and an incoming tensor-product state space are still needed.

Finally, prescribing chi_ABE(t) externally yields a unitary record evolution, but not an autonomous energy-conserving particle collision. A future joint Hamiltonian must make the gate coordinate-dependent, account for branch energies, and let momentum respond to it. No post-merger force, stable outgoing particle, or photon multiplicity follows from this gate alone.

## 9. Verification and reproduction

Run

    python pentachoron_phase_merge.py --rerun-topology

with `pentachoron_boundary_gluing_bundle.zip` beside the script, or specify its path with `--input-bundle`.

The completed run passes 111 checks, including fresh input topology checks, exact native-projector and fold identities, full gate unitarity and inversion, mismatch retention, phase-frame covariance, and a lift-sign control. Exact algebra uses SymPy rational/algebraic expressions; the independent numerical checks use SciPy matrix exponentials and both DOP853 and RK45 integration of the time-dependent local gate.

In the supplied run, the largest analytic-versus-matrix-exponential residual is 2.39e-16, the numerical unitarity residual is 4.45e-16, and the time-dependent ODE residuals are below 1.90e-14. These are implementation checks in model units, not experimental error bars.

Artifacts:

* `pentachoron_phase_merge.py`: standalone construction/checker.
* `pentachoron_phase_merge_results.json`: matrices, input hashes, phase links, tests, inherited windows and claim boundaries.
* `pentachoron_boundary_gluing_bundle.zip`: unchanged preceding construction, included for reproducibility.

Next construction: the native all-cell phase energy on the crossed boundary, with every retained cell/face occurrence kept distinct. This would determine the newly connected branch's modes and energy differences before the gate is coupled back to collision motion.
