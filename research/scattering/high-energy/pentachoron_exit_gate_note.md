# Reversible storage of cross-product comparisons and an autonomous exit interface

Date: 2026-10-11  
Status: Conditional extension of the supplied geometric and phase-record toys. Not an electron–positron scattering prediction.

## 1. Result

The four persistent cycle-comparison links obstructing independent 2+8 outputs can be converted into a retained local memory, without discarding their complex amplitudes or their comparison energy. The construction moves the mismatch subspace out of the native cell slots; it does not copy an unchanged native state into extra coordinates.

There are eight independent complex mismatch coordinates. Their natural memory operator has eigenvalues 1 and 3, each with multiplicity four, in the existing common phase-energy unit epsilon. A reversible gate encodes the mismatch in these slots and leaves the complementary native cell information in place. The eight slots are attached, by a new explicit convention, to the doubled-tetrahedron output. No tetrahedral cell or gluing instruction is removed.

This gate does not, on its own, conserve the complete native energy. A second, explicit construction realizes it as a time-independent one-dimensional spatial junction. In that model, outgoing kinetic energy supplies or receives the remaining native-energy difference. A 501-energy scan, one-sided threshold tests, and independent junction solutions verify flux conservation.

This is an **exit-stage** calculation. Its incoming state is the already geometrically split 2+8 assembly with its four persistent comparisons, at the full-tetrahedron pose. It is not the original far-separated 5+5 electron/positron preparation, and it does not generate the preceding hinge motion or the three face switches.

## 2. Retained inputs and additional choices

The unchanged `inputs/pentachoron_geometric_split_bundle.zip` is included. Its script and nested-input hashes are checked. The new script uses its exact product seam matrix and endpoint hinge generator, and the nested connected-phase receipt's source-cycle transport. The new receipt records the source archive and receipt hashes. It does not claim to rerun the ancestral 3500 topology/geometry checks.

Source conclusions retained:

- the geometrically admitted split consists of cells L_C,R_C (the doubled tetrahedron) and the other eight cells (the bipyramid boundary);
- all ten cells and twenty seam comparisons remain;
- the full product seam matrix L_F is block diagonal between the two components;
- four source-cycle comparisons remain across that partition: L_B→L_C, L_C→L_D, R_B→R_C, R_C→R_D;
- the phase space is a **direct sum** of twenty cell coordinates, not a tensor product of two independently occupied particles;
- a common positive squared-defect energy coefficient epsilon is supplied by the previous model and has no physical calibration.

New choices:

1. Add eight independent complex linear-memory slots, initially carrying zero amplitude. These are not eight new spatial cells, physical bits, or identified particles.
2. Use the polar-normalized mismatch operator as a reversible state encoder.
3. Give memory the operator epsilon DD† on BOTH sides of the exit. Empty incoming memory is a preparation, not a change in the reference energy operator.
4. Put all memory on the small output. In particular, keep the two comparison records incident on each C-cell together. Other placements would be different physical implementations.
5. At the exit, retain every remaining native seam and within-product cycle comparison unchanged, but replace live cross-product comparisons by the encoded historical record. Memory stores a snapshot; it does not continue comparing the remote outputs.
6. Realize the encoder as a sharp, lossless one-dimensional unitary interface. A finite-range implementation has not been derived and can produce different transmission probabilities.
7. For examples, prepare an equal mixture of the two lowest cell modes of the coupled post-hinge assembly, with no incoming memory amplitude.

No experimental branching ratio, physical mass, speed calibration, or QED expression is used. No repository file is changed.

## 3. Transport the actual source cycles through the hinge

The right-body source spin frame must follow the supplied proper spatial hinge. From the retained hinge generator, its spin lift is

    S_h = [[sqrt(6)/4 + i sqrt(5)/4,   sqrt(5)/4],
           [-sqrt(5)/4,               sqrt(6)/4 - i sqrt(5)/4]].

Let F act as identity on the left five cells and S_h on each right cell. Set

    T = F T_source F†,
    X = 2I - T - T†.

Exact checks verify S_h†S_h=I, T†T=I, T^5=-I, and commutation of X with the **original**, unrewired seam operator evaluated at the same endpoint pose. This transports phase frames, not merely cycle labels. It does not assert that T is a symmetry of the final product seams.

## 4. Separate the four crossing comparisons

For a directed cycle link i→j with transported spin matrix V_ij, its two-component residual is

    d_ij z = z_j - V_ij z_i.

Stack the four cross-product residuals to obtain D:C^20→C^8. Stack the other six cycle residuals to obtain D_int. Then exactly

    X = D†D + D_int†D_int.

Define dimensionless native operators

    A = L_F + X,
    A_0 = L_F + D_int†D_int.

Thus A=A_0+D†D. A_0 has no coupling between the two product cell sets. Its small native block is still 4I_4; its large block has dimension sixteen.

Each body's two removed links form a three-cell path, B→C→D. For consecutive transports V_1,V_2,

    D_b D_b† = [[2I, -V_2†],
                 [-V_2, 2I]].

Because V_2 is unitary, this matrix has eigenvalues 1 and 3, each twice. For both bodies, the memory matrix

    M = DD†

has eigenvalues 1 and 3, each four times. Exact checks establish

    (M-I)(M-3I)=0,
    P_1=(3I-M)/2,  P_3=(M-I)/2,
    P_1+P_3=I,  P_1P_3=0,
    tr(P_1)=tr(P_3)=4.

M is invertible, so D has rank eight. Eight complex slots are necessary to store all these residuals by an injective linear encoding. This is not a universal bound on every physical memory or a particle-count rule.

## 5. Move information, rather than duplicate it

Use the positive metric polar factor

    W = M^(-1/2) D,
    M^(-1/2) = P_1 + P_3/sqrt(3),
    Q = W†W,  N=I-Q.

Then

    WW†=I_8,  Q^2=Q=Q†,  rank(Q)=8,
    DN=0,  W†MW=D†D.

The ready-input encoder is

    z -> (Nz, Wz).

The native twenty slots keep the residual-free component Nz; memory keeps Wz. Their squared norms sum to ||z||^2. The inverse on the encoded image is

    z = Nz + W†(Wz).

The full operator on native cells plus memory is

    U_exit = [[N, W†],
              [W, 0 ]],
    U_exit†=U_exit,  U_exit^2=I_28.

It can act reversibly on arbitrary initially occupied storage as well. No unrecorded projection, renormalization, or amplitude deletion is performed. Original cell labels and the gluing instruction are retained as metadata.

A control illustrates the distinction: for a unit amplitude on one C-cell spin coordinate, ||z||^2=1 but ||(z,Dz)||^2=3. Keeping z unchanged and appending its residuals is not an isometry. The new gate avoids that duplication.

## 6. Store the comparison energy, but account for the other energy too

Assign the local memory operator

    H_memory = epsilon M.

For ready memory, r=Wz obeys exactly

    r† H_memory r = epsilon ||Dz||^2.

Thus the deleted live comparisons' initial quadratic energy is present in the stored record. The final internal operator is

    H_R = epsilon [A_0 direct-sum M].

After placing all memory on the small output, it is block diagonal as a twelve-coordinate small-with-memory sector and a sixteen-coordinate large sector. The small-with-memory spectrum is epsilon times {1,3,4}, each of multiplicity four. This is a local phase-record spectrum, NOT three physical particle masses or two occupied-particle rest energies.

The same apparatus before exit has

    H_L = epsilon [A direct-sum M].

For initial (z,0), the total native-energy change under the bare gate is

    Delta E(z)/epsilon = z†(N A_0 N - A_0)z.

Only the D†D part is guaranteed to move unchanged into memory. Other native terms act on the cell component changed by the encoder. The exact energy-difference matrix is nonzero; numerically its extreme eigenvalues are approximately -6.23206139 and +0.93434257. There is no universal sign for this change.

For an equal mixture of the incoming coupled-cell ground doublet:

    E_before/epsilon = 1.71267929526477,
    E_after_bare_gate/epsilon = 2.24128173579999,
    increase/epsilon = 0.52860244053523.

The bare gate cannot be declared an isolated energy-conserving switch. Calling the record free or simply dropping the cross links would conceal this difference.

## 7. An autonomous energy-conserving exit realization

Introduce a new one-dimensional signed exit coordinate x. Its negative half-line is an incoming lead for the coupled post-hinge assembly; its positive half-line describes the decoupled output-record sector. This is a reduced progress/separation coordinate, not a derivation of geometric centre trajectories.

On each side let

    H = -kappa d^2/dx^2 + H_L  (x<0),
    H = -kappa d^2/dx^2 + H_R  (x>0),
    kappa = hbar^2/(2 mu) > 0.

At the junction require BOTH

    Psi(0+) = U_exit Psi(0-),
    Psi'(0+) = U_exit Psi'(0-).

These are additional dynamical boundary conditions. They realize the reversible gate through spatial encounter instead of a prescribed timed pulse. They do not derive a microscopic gate duration or hinge force.

Analytical conservation argument: transform the wavefunction on x>0 by U_exit†. The new wavefunction and derivative are continuous. The Hamiltonian becomes the ordinary full-line kinetic operator plus the bounded Hermitian step potential H_L on the left and U_exit†H_R U_exit on the right. This explicitly establishes self-adjointness. Time independence gives energy conservation. Unitarity of U_exit also makes the probability current continuous directly.

Every outgoing internal energy e_n leaves kinetic energy E-e_n at the same total E. E<e_n is a closed, decaying channel, not additional outgoing flux. No external switch-on work, imaginary absorbing potential, or tuned output width is included.

### Stationary solution and independent test

In model units epsilon=hbar=1, let

    K_L = sqrt((E-H_L)/kappa),
    K_R = sqrt((E-H_R)/kappa),

using positive real roots for open channels and positive imaginary roots for closed ones. In common cell/memory coordinates the left interface value f solves

    (K_L + U_exit† K_R U_exit) f
      = 2 K_L a_L + 2 U_exit† K_R a_R.

The right value is U_exit f. Incident/outgoing propagating modes use flux normalization with velocity 2 kappa k/hbar. The full left/right scattering matrix is unitary. A separate 56-coordinate solve, keeping both junction values as unknowns, checks the reduced 28-coordinate solve.

This particular sharp interface has no length scale and uses the same kappa on both sides; its flux probabilities do not change under a common rescaling of kappa. That property belongs to this interface, not the preceding finite-contact collision toy or a physical universality claim.

## 8. Numerical exit examples

Prepare the equal incoming coupled-cell ground-doublet mixture described above. Its internal energy is 1.71267929526477 epsilon. K_in is the kinetic energy of the **exit coordinate**, in the same uncalibrated unit.

| K_in/epsilon | Reflected to coupled-side lead | Transmitted to separated-output lead | Mean outgoing kinetic energy / epsilon |
|---:|---:|---:|---:|
| 0.05 | 52.807710% | 47.192290% | 0.34517544 |
| 0.50 | 25.726449% | 74.273551% | 0.95424828 |
| 1.00 | 18.605458% | 81.394542% | 1.41772761 |
| 2.00 | 22.108837% | 77.891163% | 2.20280102 |
| 3.00 | 7.569468% | 92.430532% | 2.76328167 |
| 5.00 | 1.793033% | 98.206967% | 4.60624571 |
| 10.00 | 0.348822% | 99.651178% | 9.46911288 |

The outgoing mean includes reflected and transmitted channels and all their native/memory energies. For example, at K_in=10 epsilon,

    E_in/epsilon = 1.71267929526477 + 10,
    E_out/epsilon = 2.24356641563950 + 9.46911287962526.

These agree; outgoing motion supplies the increased internal energy. At some lower energies the allowed outgoing mixture has lower native energy and greater kinetic energy instead. An energy-conserving scattering solution is not the same state as applying the bare gate instantaneously without regard to closed channels.

Transmission is nonmonotonic across the displayed 1-to-2 interval. The encoder and the number of comparison records are unchanged. Channel energies and coherent matching, not counts alone, set the amplitudes in this declared interface.

These are conditional exit probabilities. In particular, a transmitted memory-mode amplitude is not a separately detected particle or evidence that two physical product particles are simultaneously occupied. The inherited direct-sum interpretation is retained.

## 9. Verification and boundaries

The supplied run passes 37 exact algebraic tests, five provenance checks, one cross-link-count check, and numerical checks including:

- a 501-energy scan plus 36 one-sided threshold checks;
- independent full and reduced junction solves at nine energies;
- consistent phase-frame covariance;
- identity-interface/no-step perfect-transmission control;
- common kinetic-coefficient rescaling control;
- exact and numerical encoder inversion and stored-comparison-energy identities;
- positive native/memory operators and local output block structure.

The largest full scattering-unitarity residual in the scan and supplementary energy tests is approximately 1.03e-13. The largest mean-energy accounting residual is approximately 3.56e-14 epsilon. These are numerical verification residuals, not experimental error bars. Mean-energy accounting is a consistency check of fixed-energy channel bookkeeping; the time-independent self-adjoint Hamiltonian supplies the conservation argument.

The current construction does not establish:

- a physical implementation of eight local memory coordinates;
- an entrance-to-exit collision trajectory or a hinge driven by the incoming collision;
- a tensor-product preparation of two occupied particles;
- stability or species identity of the doubled tetrahedron or bipyramid;
- a photon, a three-output channel, a physical speed scale, or the ratio 372:1.

The next useful calculation is a dynamical hinge coordinate controlling access to this exit interface. The new encoder and conserved-energy junction are available as explicit endpoint data; they must not be treated as proof that a generic incoming electron–positron collision reaches that endpoint.

## 10. Reproduction

Keep the unchanged archive under `inputs/` and run:

    OPENBLAS_NUM_THREADS=1 python pentachoron_exit_gate.py

Dependencies are NumPy, SciPy, SymPy. No network access is used. For a shorter numerical scan add `--scan-points 51`; all exact constructions still run. The result JSON contains exact matrices, source hashes, all check names, thresholds, the numerical scan and its scope. The NPZ contains the corresponding numerical matrices.
