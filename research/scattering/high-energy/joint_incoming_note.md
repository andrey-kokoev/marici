# Joint incoming tilt–phase modes with a retained strain-direction cycle

Date: 2026-10-11  
Status: Conditional incoming-eigenmode extension of the supplied pentachoron model. **No new electron–positron scattering probabilities, physical speed calibration, or dynamical compression law.**

## 1. Result and source boundary

The previous strained-phase note reconstructed native full-spinor comparisons and showed that the original native spectrum depends on material tilt once axial strain is active. It therefore did not license reusing a free rotor multiplied by one constant native ground vector. Its section 7 also supplied a five-pose strain-direction register, without assigning that register an incoming preparation or kinetic law.

This calculation supplies one explicit joint incoming operator. Its modes include material tilt, the ten cell-spinor coordinates of a body, and the five retained cycle poses. The two original bodies remain the inherited **direct sum** of phase records, not two independently occupied physical particles.

For a specified lowest-mode mixture, compression changes both the internal channel energies and the angular density. At half axial length, the material-tilt density at 90 degrees is about 2.30 times its value at zero degrees. This is a ratio of angular probability densities, not a conversion probability, angular tolerance, or measured scattering observable.

The full downstream scattering calculation has NOT been rerun with these new channels. The previous 2+8 flux table cannot be relabeled as its result.

## 2. Inherited inputs and new choices

The unchanged immediate input is `inputs/pentachoron_strained_phase_bundle.zip`, SHA256:

    ab5d991d5cc0127089c245c492990a57ed4f8510ebbf7b97ece04d36bb2e7341

Its manifest and nested source manifests are checked before source functions or payloads are used. The retained ingredients are the marked regular vertices, active compression with a fixed Euclidean metric, opposite chiralities, positive-trace full-spinor normal folds, the source five-cycle and its spin lift, equal seam-defect coefficients, and the material-frame periodic rotor convention.

New or extended rules:

1. A cycle arrow transports **both** the compression direction and the tilt plane. The five physical pose families are related by fixed rigid rotations and label transport. This makes their tilt kinetic metrics identical. This is a specified extension of the previous strain-direction register.
2. The ordinary rotor derivative acts on periodic **material-frame** phase coefficients. It is not an ordinary derivative on the corresponding ambient spinor coefficients. The connection and spin-lift boundary change are retained in the frame control.
3. Give the pose register the same positive cycle-defect term `epsilon(2I-T-T†)`, with no additional pose-dependent energy bias. This is an admitted dynamical rule, not an energy cost implied merely by storing a pose name.
4. Recompute tilt inertia using the inherited equal-vertex displacement-cost convention. Set `m ell^2 epsilon/hbar^2=1` for numerical examples; no physical value is inferred.
5. For the angular-density diagnostics, choose an equal mixture of the full operator's lowest modes. This is an explicit changed preparation, **not** proof that the old four-mode incoming beam prepares this mixture.
6. Lambda remains a fixed externally specified parameter in each operator. No strain potential, momentum-to-lambda law, elastic work ledger, or physical laboratory mechanism producing the register is supplied.

In particular, the five pose copies are not silently declared gauge duplicates. They carry different strain/tilt directions. A beam aligned with one laboratory direction need not occupy the equal-pose mixture. That requires a preparation and entrance-interface specification.

No QED interaction, measured mass, experimental energy, or branching ratio is used.

## 3. A geometric family that makes the cycle and kinetic law compatible

Let q_i denote the source's centered vertices in its ABE reference orientation, and let R0 send source label i to i+1 modulo five. Let Q(delta) be the source x–w rotation by delta-delta_c, with delta_c=atan(1/sqrt(5)).

The primary physical strained family is

    r_i^(0)(delta) = C_lambda Q(delta) q_i,
    C_lambda = diag(lambda,1,1,1).

Define the other physical poses, with labels retained, by

    r_i^(j)(delta) = R0^j r_(i-j)^(0)(delta), j=0,...,4.

This is a rigid rotation of the entire primary family plus its source label transport. Its compression direction is R0^j e_x and its tilt plane is the corresponding rotated x–w plane. It is not re-compression along one unchanged laboratory axis for all pose labels.

Pull back to each pose's material frame. If

    n(delta) = Q(delta)^T e_x,
    C_lambda(n) = I+(lambda-1) n n^T,

the material vertices are

    v_i^(j)(delta) = C_lambda(R0^j n(delta)) q_i.

For j=0 at delta_c this is precisely the preceding ABE strained geometry. Every cycle step is a rigid geometric comparison between the enlarged pose records. Direct vertex and tangent-normal reconstructions verify this family, not only its assigned phase dimension.

Let Tb be the source's ten-coordinate cell-permutation/spin-lift matrix for one body, so Tb^5=-I. Rebuilt native seam matrices obey

    L_j(delta,lambda) = Tb^j L_0(delta,lambda) (Tb†)^j.

The right body, with its reflected geometry and opposite chirality, is related to the left native and cycle matrices by the constant unitary `I_5 tensor sigma_x`. It therefore has the same spectrum in this convention. This mirror identity is checked against independent right-body folds, not assumed from equal dimensions.

## 4. Kinetic cost follows the retained vertex metric

The exact regular-vertex covariance gives, for every pose,

    sum_i ||d r_i^(j)/d delta||^2 = 4 ell^2 (1+lambda^2).

With the source inertial weight m/5 on each of a body's five vertices, and the same common tilt on the mirrored pair, the kinetic energy is

    T_delta = (4/5) m ell^2 (1+lambda^2) delta_dot^2
            = I_delta delta_dot^2/2,
    I_delta = (8/5) m ell^2 (1+lambda^2).

The pair coefficient is used even though the phase records remain a direct sum, just as in the preceding entrance model. It does not identify a phase-record norm with two occupied particles.

Under the admitted periodic material-frame quantization,

    K_delta = -[5 hbar^2/(16 m ell^2 (1+lambda^2))] d_delta^2.

At lambda=1 this recovers the source coefficient 5/32 in epsilon=hbar=m=ell=1 units. Holding the unstrained coefficient fixed under compression would be a different kinetic model.

## 5. The full incoming internal operator

For one body use

    H_in / epsilon = -alpha_lambda d_delta^2 I_50
                     + diag_j L_j(delta,lambda)
                     + 2I - T - T†,
    alpha_lambda = 5/[16(1+lambda^2)]

in the displayed scale fixture. Its Hilbert space is

    L2(S1,d delta) tensor C^5_pose tensor C^10_cell-spinor.

The full original record includes two such body sectors, for 100 internal coordinates per tilt. The rotor coefficient concerns the pair's common tilt. The enlarged cycle is

    (T z)_(j+1) = Tb z_j,
    T†T=I, T^5=-I.

The diagonal native operator is bounded, Hermitian and positive for positive lambda. The circle rotor and finite cycle-defect form are also nonnegative. Their sum on the periodic rotor domain is self-adjoint, with a discrete internal spectrum and a common conserved norm/energy. This is a mathematical operator statement under the declared prescription, not a derived relativistic field theory.

### Exact reduction of the pose coordinate

Apply the constant unitary W=diag(I,Tb,Tb^2,Tb^3,Tb^4). In its frame:

- every native block is L_0(delta,lambda);
- the derivative is unchanged because W is delta independent;
- the cycle is a five-site shift with a minus sign on its closing link.

Consequently the problem separates as

    H_in/epsilon ~ I_5 tensor h_lambda + C_anti tensor I_10,
    h_lambda = -alpha_lambda d_delta^2 + L_0(delta,lambda),
    C_anti = 2I - S_anti - S_anti†.

The exact cycle energies are

    c_k = 2-2cos((2k+1)pi/5), k=0,...,4.

They are `(3-sqrt(5))/2` twice, `(3+sqrt(5))/2` twice, and 4 once. If u_a(delta) solves h_lambda u_a=e_a u_a, the full modes are explicitly

    Phi_(a,k),j(delta) = exp[-i(2k+1)pi j/5] Tb^j u_a(delta)/sqrt(5),
    E_(a,k) = epsilon(e_a+c_k).

Thus the five-pose coordinate is retained analytically; it is not thrown away to reduce the computation. **Tilt and native phase do not separate in h_lambda.**

### Even material-rotor mixing

Since n(delta+pi)=-n(delta), the material compression tensor and L_0 have period pi. Its Fourier coefficients therefore connect only rotor indices whose difference is even. The incoming internal model preserves rotor parity. This is not asserted to be conserved by the later spatial contact patch, which has its own angular support.

## 6. Source recovery does not remove the new register

At lambda=1, L_0 is constant and commutes with Tb. The isometric map

    J z = (z,z,z,z,z)/sqrt(5)

intertwines the enlarged operator with the old source operator `L_0+2I-Tb-Tb†`, including its rotor term. The old unstrained model is recovered on this invariant subspace.

It is **not** the whole enlarged space. With both original record sectors, the enlarged ground multiplicity is 16 at lambda=1, versus 4 in the old source. It is 8 at the three compressed values tested here. The eigenvalue agrees in the unstrained case, but the available preparation space has grown. A unique physical beam state has not been derived by matching the old lowest energy.

## 7. Calculated low incoming modes

All energies below are in the unspecified epsilon unit. They include the cycle-defect contribution. The gap is to the first distinct internal joint mode; it is not an experimentally established reaction threshold or a guarantee that the later gate couples to that mode.

| Axial factor lambda | Lowest joint energy / epsilon | First distinct joint gap / epsilon | Tilt-density ratio p(90 deg)/p(0 deg) |
|---:|---:|---:|---:|
| 1 | 1.932476 | 0.156250 | 1.00 |
| 0.75 | 1.879395 | 0.102369 | 1.61 |
| 0.50 | 1.813046 | 0.158491 | 2.30 |
| 0.25 | 1.773782 | 0.165287 | 2.86 |

The density uses the equal lowest-mode mixture and measure d delta. Each cycle ground eigenvector has uniform pose modulus; the displayed angular marginal is the same after tracing the pose register. Zero and 90 degrees are reporting locations, not tolerances. No statement is made about reaching a contact simply because the density is larger there.

The corresponding mean rotor kinetic energies are 0, 0.007389, 0.029195 and 0.066134 epsilon. Their inclusion prevents a lowest-local-eigenvalue construction from silently assigning zero angular localization cost.

A basis-independent mixed-ground diagnostic also detects tilt/phase correlation: the Hilbert–Schmidt distance between the joint lowest-mode density operator and the product of its reduced tilt and cell density operators is 0, 0.04662, 0.08619 and 0.13774, respectively. This is a correlation between the model's coordinate and phase-record spaces, not a claim about two physical particles.

The lowered mode energies do not establish that compression releases usable energy. The model has no elastic energy for producing or holding lambda, and no physical rest-energy interpretation for these normalized record eigenvalues.

## 8. Incoming radial channels can now be typed consistently

Hold lambda fixed. For each joint internal eigenvalue E_a, the far-separated entrance has the inherited radial square-root dispersion. In dimensionless units, at common total energy E set

    z_a=E-E_a,
    k_a=sqrt(z_a+z_a^2/(4 rho)),
    v_a=2 k_a/[1+z_a/(2 rho)], rho=mc^2/epsilon.

For z_a>0 an incoming channel is

    Psi_a(D,delta,j) = exp(-i k_a D) Phi_a(delta,j)/sqrt(v_a).

It has unit incoming radial flux when Phi_a is normalized. Channels with z_a<=0 are not open incident plane waves; their appropriate closed-channel continuation remains part of a future full scattering solve. The code tests this dispersion and normalization on the computed low modes.

One can now specify one internal-mode mixture and hold it fixed as radial energy changes. This is different from imposing the previous angular Fourier coefficients multiplied by a constant native ground vector. The new pure radial K=E-E_ground should not be confused with the previous source's combined motional K relative to its old constant native reference.

This step constructs an asymptotic basis and a declared lowest-mode preparation, **not the new complete entrance-to-product scattering matrix**. The entrance patch, its comparator, and the downstream pose/phase records must be connected consistently to this enlarged space first.

## 9. Controls and verification

The completed run records 95 checks. They include:

- source archive and nested manifests; no ancestral physical claims are upgraded;
- exact symbolic vertex kinetic metric and recovery of the unstrained rotor coefficient;
- independent tangent-nullspace normals and fold reconstructions;
- geometric pose-cycle, full-spinor covariance, antiperiodic ring reduction, and opposite-chirality mirror comparison;
- unstrained source embedding, normalization, and spectrum controls;
- Fourier collocation at 65 and 129 modes, solving the coupled ten-coordinate periodic problem;
- an independent second-order finite-difference circle operator at 128, 256 and 512 nodes for lambda=0.5 and 0.25;
- consistently transformed ambient-frame kinetic operator and spin-lift boundary convention;
- incoming-channel unit-flux normalization and free joint-mode propagation energy/norm ledgers.

Maximum change in the first twenty Fourier eigenvalues on refinement is about 1.24e-12 epsilon. Numerical eigenpair residuals are below 2.7e-12. Independent finite-difference errors decrease by approximately four on each doubling; at 512 nodes, the first-six-level discrepancies are below 9e-6 epsilon. This independent discretization bound is distinct from the much smaller algebraic residuals. The displayed rounded density ratios pass independent finite-difference checks as well.

Two changed-model controls matter:

1. Rotating the native matrices but omitting the kinetic connection shifts the half-strain ground energy by approximately +0.03327 epsilon. A basis change cannot justify dropping that term. With the periodic material convention, the corresponding continuous ambient spinor section is antiperiodic under the 2pi lift.
2. Retaining the old rotor coefficient 5/32 instead of the rebuilt value changes the half-strain joint ground energy from 1.813046 to 1.797207 epsilon and the 90-to-zero density ratio from 2.304 to 3.764. Geometry-only updates are not equivalent to this updated kinetic construction.

No full scattering-flux scan, outgoing conversion percentage, or physical energy-to-speed law is produced. The independently checked values concern the incoming internal spectrum and preparation.

## 10. Reproduction and next interface

Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_incoming.py

The `--quick` option omits the largest independent finite-difference grids and marks that choice in its receipt. Keep the unchanged predecessor archive under `inputs/`. Dependencies are Python, NumPy, SciPy, and SymPy. No network or repository modification is used.

`joint_incoming_modes.npz` contains the Fourier indices, low-mode coefficients, eigenvalues and angular densities. The five-pose and mirror modes are reconstructed by the explicit isometries above. `joint_incoming_results.json` retains source hashes, all checks, refinement results, controls, model choices and limitations.

The next construction is the entrance comparison on this enlarged joint-mode space, including its retained pose labels and matching phase frames. Only after that comparison and the downstream channels are transported consistently can the 2+8 product flux be recalculated. Generating strain from collision momentum remains a separate missing dynamical law.
