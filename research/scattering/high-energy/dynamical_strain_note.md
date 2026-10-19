# Contact-driven dynamical strain with an explicit restoring energy

Date: 2026-10-11  
Status: **New conditional semiclassical entrance diagnostic.** No new full quantum product flux, electron–positron identification, Lorentz-contraction law, or calibrated physical speed.

## 1. Result and relation to the last calculation

The supplied `joint_pose_scattering_note.md` constructs a conservative quantum scattering model at each fixed axial factor lambda. Its final section explicitly leaves dynamical strain, elastic work and a momentum-to-strain law unconstructed. This step makes the axial factor a dynamical variable rather than selecting it separately for each incoming energy.

The test is intentionally **not the full source scattering problem with one more solved quantum coordinate**. Separation and strain are classical ensemble-mean coordinates, while the source's periodic material tilt and native cell-spinor field evolve coherently. No topology-switch or outgoing-product gate is activated. This is an autonomous mechanical-preparation test, not a recalculation of the 2+8 percentages.

In the tested common-stiffness fixture, incoming radial energies 1, 2.3 and 4 produce minimum axial factors about 0.83, 0.71 and 0.54. All start with lambda=1 and zero strain momentum. The same initial phase ensemble is propagated throughout; it is not replaced by a different lowest-energy ensemble whenever strain changes. Shapes rebound and can stretch beyond lambda=1.

## 2. Provenance

The sole archive input is the unchanged user-supplied `pentachoron_joint_flux_bundle.zip`. Its manifest and nested source manifests are checked before functions and geometry are used. The new files use:

- the source marked centered vertices and covariance;
- the source material-frame native ten-coordinate seam operator L_0(delta,lambda);
- the source geometric pose-cycle reduction and opposite-chirality mirror map;
- the source incoming uncompressed lowest-mode ensemble;
- the previous global strained nearest-nonoverlapping comparator;
- the prior separation square-root kinetic law and its uncalibrated rho=1 fixture.

No repository or external source is changed or searched. Hash verification does not rerun the ancestral topology census or establish physical particle interpretations. The new vectorized native matrices are checked against the source's actual functions. The scalar global-minimum comparator is checked against the old function on its original compression domain and against an independent dense-bracketing minimization on the newly admitted expansion domain.

## 3. New assumptions, stated separately

1. Add a preferred uncompressed reference metric and a positive energy proportional to the minimum squared vertex displacement back to a rigidly moved reference. Geometry fixes the dependence on lambda **after this rule is chosen**; it does not derive the physical restoring law or its coefficient.
2. Give lambda its own momentum and use the inherited equal mass m/5 per retained vertex. Continue the same geometric family to all positive lambda so elastic rebound may produce temporary expansion. The degenerate lambda=0 simplex is excluded.
3. Treat D and lambda as classical mean coordinates. The full retained periodic tilt–phase field feels their instantaneous values and exerts its ensemble-averaged energy-gradient force back on them. This is not a distribution of rare quantum compression branches and not one linear scattering matrix for the joint quantum system.
4. Identify coefficient spaces at different lambda through the source's fixed material-frame convention, with no separately added strain connection. A fully quantum strain metric/domain/connection construction remains to be done.
5. Reuse v_lambda(D,delta) as the instantaneous contact energy. Its nearest comparator preserves the current strain; it minimizes separation and tilt corrections, not an additional candidate strain.
6. For the main test set the new elastic coefficient epsilon_el equal to the existing phase/geometric unit epsilon. A double-stiffness control is also computed. This is a frozen test choice, not a fitted or geometry-forced physical modulus.
7. Start at D=8 ell with inward radial momentum, lambda=1, zero strain momentum, and the equal uncompressed lowest-mode mixture. There is no preloaded strain excitation. Downstream reconnection is disabled in this entrance-only diagnostic; the amplitudes are not conditioned on merger.

The source's rho=mc^2/epsilon=1 and m ell^2 epsilon/hbar^2=1 remain numerical choices. The separation kinetic energy has a square-root form, while strain and tilt remain nonrelativistic internal coordinates. This is not a Lorentz-covariant extended-particle model.

## 4. Derive the new kinetic metric

Let q_i be the five centered reference vertices. The retained identity is

    sum_i q_i q_i^T = 4 ell^2 I_4.

For a body with material tilt R(delta) and C_lambda=diag(lambda,1,1,1), its centered shape is C_lambda R(delta) q_i. The mirrored pair has centers at plus/minus D/2. Differentiating every vertex and using the covariance gives the exact ten-vertex velocity sum

    (5/2) D_dot^2
      + 8 ell^2 lambda_dot^2
      + 8 ell^2 (1+lambda^2) delta_dot^2.

All mixed terms vanish. With kinetic weight m/10 per squared vertex velocity,

    T = (m/4) D_dot^2
        + (4m ell^2/5) lambda_dot^2
        + (4m ell^2/5)(1+lambda^2) delta_dot^2.

Hence

    M_lambda = (8/5) m ell^2,
    I_delta(lambda) = (8/5) m ell^2 (1+lambda^2).

M_lambda is the inertia of a dimensionless deformation coordinate, not an electron mass prediction. The second expression recovers the previous fixed-strain rotor coefficient. The new test retains the earlier square-root separation kinetic energy rather than replacing it with the quadratic D term; the calculation above supplies the internal lambda/tilt metric and its low-speed consistency.

## 5. A rotationally invariant restoring cost

For one centered body, minimize the squared difference from a rigid copy of its uncompressed marked reference. Because the reference covariance is isotropic, this equals

    4 ell^2 min_(O in SO(4)) ||C_lambda-O||_F^2
      = 4 ell^2 (1-lambda)^2.

The first equality here uses the rotation already absorbed into O; the overall factor 4 ell^2 multiplies the Frobenius norm. For positive lambda, the cross term is maximized by O=I: tr(C_lambda O) <= lambda+3 since each diagonal entry of an orthogonal matrix is at most one. Thus the minimizer is a genuine proper rotation and the expression is exact.

Both bodies together give 8 ell^2 (1-lambda)^2. Applying the NEW restoring-energy interpretation with coefficient epsilon_el/ell^2 gives

    U_el(lambda)=8 epsilon_el (1-lambda)^2.

This penalizes actual distortion but not rigid reorientation. Its stiffness near lambda=1 is 16 epsilon_el, and its isolated geometric small-oscillation frequency is sqrt(10 epsilon_el/(m ell^2)). Native phase/tilt backreaction can change the actual coupled oscillation; this isolated frequency is not a derived particle clock.

## 6. Retain the quantum tilt–phase state

Use u_g(delta) in L2(S1,d delta) tensor C10. In the numerical fixture,

    h_lambda = -5/[16(1+lambda^2)] d_delta^2 + L_0(delta,lambda).

The four uncompressed lowest rotor/seam states are evolved with equal weights. The mirror sector gives the same motion under its constant retained unitary, and the two populated pose-cycle eigenvalues give the same constant energy c_0=(3-sqrt(5))/2. These symmetry copies are retained analytically rather than multiplying probabilities. The effective four-state mixture represents the source's full uncompressed sixteen-mode mixture for this scalar, topology-preserving entrance diagnostic.

The initial rotor is uniform and the seam ground energy is 4-sqrt(6). Individual basis vectors need not have zero strain force, but the specified mixed lowest projector has zero mean strain force at lambda=1. Without contact the same mixture remains stationary internally, so arbitrary uniform incoming radial motion alone does not compress it.

No conditional state is normalized and relaunched as a merged particle. No instantaneous ground-state or adiabatic approximation is used during the encounter. Excited tilt and cell modes remain in the propagated field.

## 7. One time-independent energy and the force law

Let eta=epsilon_el/epsilon. In epsilon=hbar=m=ell=1 and the populated pose block, define

    H = 2 rho [sqrt(1+p_D^2/rho)-1]
        + p_lambda^2/(2 M_lambda)
        + 8 eta (1-lambda)^2
        + average_g <u_g, [h_lambda+v_lambda(D,delta)] u_g>
        + c_0.

The scalar v_lambda is the unchanged source minimum

    min_t { (5/2)[2lambda a(t)-D]_+^2
             +16(1+lambda^2)[1-cos(t-delta)] },
    a(t)=max(|cos t|-sin(t)/sqrt(5),4sin(t)/sqrt(5)).

Its extension to expansion uses the same expression and a newly checked positive-lambda domain.

The dynamical equations are

    D_dot = 2p_D/sqrt(1+p_D^2/rho),
    p_D_dot = -average <u, partial_D v u>,
    lambda_dot = p_lambda/M_lambda,
    p_lambda_dot = -16eta(lambda-1)
                  -average <u, [partial_lambda h_lambda
                                 +partial_lambda v_lambda] u>,
    i u_dot = [h_lambda+v_lambda]u.

The derivative of the rotor coefficient is included. Omitting it would lose part of the strain/tilt energy exchange. Native derivatives are computed analytically from the inverse-transpose normals and normal-fold formula; finite differences independently check them.

For a selected global comparison angle t, put q=[2lambda a(t)-D]_+. The envelope derivatives are

    partial_D v = -5q,
    partial_lambda v = 10q a(t)+32lambda[1-cos(t-delta)] >= 0.

The contact term therefore pushes toward smaller lambda. The restoring term opposes compression; native phase and rotor terms contribute additional state-dependent forces. This supplies a concrete cause of compression, not an assigned compression-versus-speed curve.

The Hamiltonian/Schrodinger equations give dH/dt=0 and d||u_g||^2/dt=0 analytically. Classical forces and internal energy exchange cancel term by term. Conditional on the coordinates, internal evolution is linear and norm preserving; the coupled mean-coordinate flow itself is state dependent and is not a quantum scattering matrix.

## 8. Numerical encounters

The radial energies K are above the same initial uncompressed joint energy 1.932476268466929 epsilon. Only initial radial momentum changes. All other preparation, energy coefficients, geometry, and force rules are held fixed. No reference-pose collapse or zero-separation wall reflection occurs in the reported runs.

The following digits describe the saved finite-grid trajectories. Appropriate physical-model summaries are minimum axial fractions about 0.83, 0.71 and 0.54, and outgoing radial energies about 0.48, 1.52 and 2.85 epsilon. They are not calibrated beam quantities or precision continuum predictions.

| K/epsilon | Angular nodes | Minimum lambda | Maximum lambda | Minimum D/ell | Outgoing radial K/epsilon |
|---:|---:|---:|---:|---:|---:|
| 1 | 25 | 0.830655218 | 1.137094888 | 1.322824898 | 0.481390906 |
| 2.3 | 33 | 0.709170091 | 1.203545629 | 0.693308278 | 1.515835208 |
| 4 | 25 | 0.541469417 | 1.246724460 | 0.219289048 | 2.846380252 |

Extrema are taken from dense integration output sampled at intervals no larger than 0.05 hbar/epsilon. They are not root-isolated exact extrema. Positive native/kinetic energies imply the bound

    |lambda-1| <= sqrt[(H-c_0)/(8eta)].

For the tested total energies, D=8 ell is outside all possible subsequent contact extents under that bound. Once a trajectory returns outward to D=8, its radial momentum is therefore asymptotically unchanged even though internal strain/tilt motion can continue. The outgoing kinetic column is not an artificially switched-off interaction.

### Energy ledger at K=2.3 epsilon

| Energy term / epsilon | Incoming | At outgoing free reference |
|---|---:|---:|
| radial | 2.300000000000 | 1.515835207676 |
| strain_kinetic | 0.000000000000 | 0.161937742926 |
| elastic | 0.000000000000 | 0.047410889863 |
| tilt | 0.000000000000 | 0.534146223601 |
| seams | 1.550510257217 | 1.591180123379 |
| contact | 0.000000000000 | 0.000000000000 |
| pose | 0.381966011250 | 0.381966011250 |

The radial motion loses approximately 0.784164792 epsilon. That difference is retained as strain motion, deformation, and tilt/phase excitation. There is no dissipation, radiation channel, or externally prescribed compression work. The two total energies agree within the recorded integration residual.

### Stiffness control

At K=2.3 on the same 17-node angular grid, doubling epsilon_el changes minimum lambda from 0.708689591 to 0.848306605. This is a substantial dependence on an admitted constitutive law, not evidence of a uniquely derived modulus. The minimum strain along a collision depends on preparation, restoring coefficient, phase state and contact history, not on speed alone.

## 9. Verification and numerical limits

The bundle records source recovery, native Hermiticity, analytic derivative checks, direct ten-vertex kinetic and elastic comparisons, symbolic metric identities, conservative equation checks and independently computed trajectory controls.

- Source versus vectorized native matrices: maximum sampled entry discrepancy about 3.11e-15.
- Analytic native strain derivative versus centered differences: about 2.74e-10.
- Comparator envelope derivative control: about 3.43e-9.
- Independent dense-bracketing checks cover lambda>1 rebound configurations.
- DOP853 and RK45 at the central energy and same angular grid agree in sampled minimum lambda within 1.41e-7.
- Angular refinement at K=2.3 from 17 to 25 to 33 points changes minimum lambda by about 0.000390 and then 0.0000904. The final outgoing radial energy changes by about 0.00326 and then 0.00120 epsilon. These are observed convergence changes, not rigorous error bounds.
- The refined primary runs have maximum total-energy drift 1.17e-06 epsilon and maximum phase-norm drift 6.45e-10. The coarser exploratory runs and their larger residuals remain saved; their maximum energy drift is about 4.59e-5 epsilon.
- The energy/flux terminology is not interchangeable: no new full scattering S matrix is built here. The independently conserved Hamiltonian function is that of the explicitly semiclassical diagnostic.

The verifier's 96 passing entries include repeated audits of saved trajectories; they are not that many independent theorems. Ancestor physics, global numerical convergence, relativistic covariance, and product identities are not certified by these checks.

## 10. What this does and does not establish

This test closes a specific gap: compression is no longer supplied as an independent number for each incoming energy. An admitted reference-metric cost gives an elastic energy, the vertex metric gives its inertia, and contact/native forces evolve strain while accounting for its energy.

It produces **temporary impact deformation and rebound**, not uniform-motion Lorentz contraction. It does not derive lambda=1/gamma. It supplies classical mean strain rather than a branch-resolved quantum strain distribution.

The complete incoming-plus-hinge-plus-face-switch Hamiltonian has not been extended and solved in this turn. In particular, it would be inconsistent to insert a trajectory's minimum lambda into the source's fixed-strain scattering table and call the result a new conservative product probability. The current result has no recombination fraction, no independent occupied-particle interpretation, no physical energy/speed calibration, and no new three-output route.

The next concrete construction is to give strain its own quantum coordinate, common energy reference and cross-strain connection on the full retained route, using this tested elastic proposal as an explicit input. The numerical cutoff issues in the source scattering model remain separate.

## 11. Reproduction

See `README.md` for all actual run commands and the saved-receipt audit. The directory contains the unchanged immediate input archive, the new solver, the independent verifier, JSON ledgers and NPZ trajectories. No network access is required and no GitHub file was modified.
