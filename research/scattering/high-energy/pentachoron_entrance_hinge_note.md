# Entrance-prepared hinge response with the contact reaction retained

Date: 2026-10-11  
Status: Conditional, autonomous one-dimensional entrance / classical mean-hinge / coherent-record calculation. Not a physical electron–positron result.

## 1. Result

The existing incoming-packet model and the dynamical hinge can be coupled without independently preparing a post-merger phase or supplying a hinge kick. The coupling exposes an important distinction: the connected record is only partially occupied, and its contact gate contributes to the hinge torque along with its native Hamiltonian.

Under the explicitly adopted co-moving entrance comparison, the complete stationary entrance torque is zero. A finite packet nevertheless produces transient phase-dependent rotation. Three finite-duration numerical tests, with one fixed incoming ground-mode mixture and packet width, give maximum mean hinge angles of about 0.0034, 0.0296 and 0.0606 degrees. None reaches the 104.4775-degree splitting contact during the first 25 time units.

These are mean-coordinate trajectories, not probabilities for rare individual connected branches. They do not disprove the larger geometric construction or prove that every possible preparation fails to split.

## 2. Sources retained

The two supplied archives are included unchanged:

- `inputs/pentachoron_autonomous_contact_bundle.zip`: the original native matrix H_O, connected native matrix H_C, rank-two matching projector P, positive point-contact energy, and continuum kinetic convention.
- `inputs/pentachoron_dynamical_hinge_bundle.zip`: F(theta), its generator A, the connected matrix at zero hinge angle, the centroid-fixed hinge inertia, and the geometric endpoint.

The new script verifies both source manifests and the numerical-matrix payloads. Five inherited algebraic identities are rechecked exactly from the source expressions: A is Hermitian, A²=I/16, P is Hermitian, P²=P, and PAP=0. The identities are not an independent rerun of the earlier geometry, topology, or particle-identification claims.

The source relation is

    H_C(theta) = F(theta) H_C F(theta)†,
    F(theta) = exp(i theta A),
    A² = I/16,
    I(theta) = m ell² (14 - 2 cos(theta))/15.

The endpoint is theta_* = acos(-1/4). The old hinge simulations used normalized connected states chosen independently of the entrance. That preparation is not reused here.

## 3. New assumptions

1. **Co-moving entrance comparison.** Transport the connected side of the entire contact operator with F(theta), not only the connected native matrix. This is a coherent extension of the inherited frame convention; it is not yet uniquely derived from the complete microscopic contact geometry.
2. **One classical mean coordinate.** All incident phase preparations act through their ensemble-averaged force on one classical hinge, with the previously supplied inertia. The inertia does not become a branch-dependent quantum operator when connected occupation is small. This is a substantive semiclassical modeling choice.
3. **Incoming preparation.** Use the same equal incoherent mixture of four lowest original native modes at every energy. Give them an inward Gaussian spatial packet of standard deviation 2 ell, initially centered 14 ell from the contact. There is no separately set connected-phase angle and no initial hinge momentum.
4. **Existing uncalibrated scales.** Use epsilon=hbar=m ell²=1 and the inherited continuum kinetic coefficient kappa=1. These are numerical model units, not fractions of c.
5. **Local scope.** The original entrance still conditions on access to ABE. It does not generate the prior compression, x–w tilt, or contact eligibility. Neither the three later face switches nor the exit-memory gate is executed here.

This is a different packet from the earlier narrow Gaussian in energy. The packet width is fixed across the three new runs; the central inward momentum changes.

## 4. One joint energy, including the contact reaction

Let psi(x) be the twenty-component original-topology field, and chi the twenty-component connected record. The former includes the incoming and outgoing spatial directions. In dimensional notation the newly connected energy is

    E_total = p² / [2 I(theta)]
       + integral [kappa ||psi'(x)||² + psi(x)† H_O psi(x)] dx
       + chi† F(theta) H_C F(theta)† chi
       + 2 epsilon ||P[ sqrt(ell) psi(0) - F(theta)† chi ]||².

The original and connected native matrices include the retained five-cycle comparisons. Their common energy reference is unchanged. For the incident mixture, the quadratic field terms and force are averaged with the same weights.

At theta=0 this is exactly the earlier autonomous contact form, plus the ready hinge. At other angles it is a newly specified extension. It has no externally prescribed time pulse, no imaginary loss term, no independently fitted phase, and no erasure of the contact mismatch.

Writing F_total = identity_on_original_continuum direct-sum F gives

    H_enter(theta) = F_total H_enter(0) F_total†.

The interaction is therefore isospectral as an entrance family under this convention. Its matrix derivative need not vanish. Both its diagonal and off-diagonal contact terms must be differentiated.

## 5. Torque from the entrance-prepared record

Extend A by zero on the original continuum, calling the result A_core. Then

    dH_enter/dtheta = i[A_core, H_enter].

For the actual, unnormalized connected amplitude define

    a(t) = sum_j w_j chi_j(t)† A chi_j(t).

The complete coherent evolution gives

    tau(theta) = -sum_j w_j <Psi_j, dH_enter/dtheta Psi_j>
               = hbar da/dt.

This is an identity of the declared entrance extension, not a universal torque law for arbitrary collision models. It includes the contact reaction.

The quantity chi†chi is connected occupation. Replacing chi by chi/||chi|| would condition on and amplify a transient component, change the full normalization, and cease to represent the same autonomous entrance state. No such replacement is made.

For constant inertia and an initially empty core at rest, p=hbar a. With the exact angle-dependent inertia, define q=p-hbar a. The exact equations instead are

    theta_dot = p/I(theta),
    q_dot = p² I'(theta)/[2 I(theta)²].

The contact supplies a transient angular response, not an independent prescribed kick. Since A has eigenvalues +/-1/4,

    |a(t)| <= P_connected(t)/4.

This bounds the instantaneous generator expectation by the actual core population. It does not bound all future angles or the motion of a postselected branch.

### Stationary cancellation

For a stationary entrance eigenfunction the core quadratic expectation a is time independent. The native and contact contributions cancel. The new checker solves the full forty-coordinate contact equations at eleven test energies and checks this cancellation separately for each of the four incoming ground modes, as well as frozen-geometry scattering-flux normalization.

For example, at incoming kinetic parameter 4 epsilon the native-only average torque is about -0.11116 in the stationary unit-flux normalization. The contact reaction cancels it. Interpreting the first term alone as an entrance-generated hinge force would give a different, incomplete dynamics. Unit-flux residence and force coefficients are not normalized-packet occupation probabilities.

## 6. Coupled propagation rather than a post-collision handoff

Transform only the connected record to the co-moving frame, u=F(theta)†chi. On the complete field the evolution becomes

    i hbar Psi_dot = [ H_enter(0) + hbar theta_dot A_core ] Psi.

The connection term is retained. Together with the equations for theta and q, this follows from the autonomous moving-frame Hamiltonian

    E = (q+hbar a)²/[2 I(theta)]
        + sum_j w_j <Psi_j,H_enter(0)Psi_j>.

Consequently total energy and total probability are conserved analytically. The full coupled evolution is state-dependent through the classical mean coordinate; it is not a single linear unitary scattering operator on a joint quantum hinge and pair state.

The field evolves continuously through entrance, partial core occupation, and return to the original-topology continuum. The code never cuts out a normalized connected state and evolves it as if the entire incoming packet had merged.

## 7. Numerical realization and probability normalization

Reflection symmetry of the original one-dimensional point-contact model separates spatially even and odd fields. Only the even field couples at the origin. Of the four degenerate incident ground modes, the rank-two contact has two bright combinations; two orthogonal ground combinations remain dark. The ground restriction of P has spectrum {0,0,1/5,1/5}.

The calculation evolves the two bright even components. Each has ensemble weight 1/4 and initial even norm 1/2. Their total dynamic norm is therefore 1/4 of the full incoming preparation. The remaining 3/4 is a free, dynamically decoupled spectator; its norm and constant energy are retained in the ledger. Connected occupation is always quoted relative to the original full unit-normalized mixture.

The even field is discretized on a half-line box. Half endpoint integration weights and the corresponding symmetric finite-volume kinetic matrix implement the natural endpoint convention. The contact energy uses

    psi_full(0) = z_even,node0 / sqrt(h)

in orthonormal grid coordinates, accounting for both the parity fold and the half endpoint weight.

The solver uses reversible Cayley steps for the complete fixed-geometry finite-grid Hamiltonian, not separate unbalanced force kicks. Each such step preserves its norm and native energy. A mechanical substep advances the exact one-dimensional metric arc

    s(theta) = (4/sqrt(5)) EllipticE(theta/2 | -1/3)

and rotates the connected record by its required connection. A symmetric fourth-order composition couples these flows. Negative intermediate time steps are algorithmic inverse operations, not negative physical kinetic energies.

Grid spacing h and time step are numerical resolution parameters. They are not the proposed physical geometric tolerance.

## 8. Computed incoming-packet response

Use h=0.1 ell, time step 0.025 hbar/epsilon, half-line length 100 ell, and observe the first 25 hbar/epsilon after initial preparation. The angular momentum and hinge angle initially vanish.

| Central kinetic parameter K/epsilon | Peak connected occupation | Maximum absolute mean hinge angle |
|---:|---:|---:|
| 1.0 | 1.1412% | 0.0033916 degrees |
| 2.3 | 2.9385% | 0.0295858 degrees |
| 4.0 | 2.1875% | 0.0606069 degrees |

K is the kinetic energy of the packet's central momentum. The continuum Gaussian mean kinetic energy is K+epsilon/16; finite-grid dispersion changes it slightly. The full conserved energy, not the nominal central K alone, is used by propagation.

For K=2.3 the finer grid h=0.05 gives a maximum angle of 0.0296256 degrees; halving the time step at h=0.1 gives 0.02958584 degrees. The K=1 and K=4 refined maxima are 0.0033738 and 0.0607435 degrees. These support the small-angle conclusion, not all quoted decimal digits as exact continuum results.

The geometric contact required for the next splitting stage is 104.477512 degrees. No test reaches it within the stated window. Residual connected occupation is still nonzero at the end: roughly 0.17%, 0.49%, and 0.54% for the three primary cases. Thus these are neither infinite-time final angles nor a proof that every longer evolution fails.

## 9. Verification and controls

The receipt records source hashes, exact inherited algebra checks, the stationary torque and flux tests, and numerical propagation controls.

- Primary runs: maximum energy drift below 3.2e-12 epsilon and dynamic norm drift below 2.9e-13.
- Refinement runs: maximum recorded energy drift below 3.6e-12 epsilon. This is numerical conservation, not experimental precision.
- Spatial refinements h=0.2, 0.1, 0.05 at K=2.3; h=0.1 versus 0.05 at K=1 and K=4.
- Time refinement 0.025 to 0.0125 at K=2.3.
- Exterior box increase 100 to 120 ell: indistinguishable hinge response over the tested interval within the reported numerical comparison.
- Negative control: omitting the phase backreaction while keeping the same energy definition produces a ledger error about 3.41e-7 epsilon in the K=4, h=0.2 test. It is not used as a valid conserved-energy trajectory.

The operator formulation establishes the analytical conservation law. Numerical residuals check implementation. No claim is made that the point-contact prescription, classical mean-field reduction, finite prepared packet, or inherited physical scales are uniquely implied by arrow counting.

## 10. What this advances and what remains

The entrance now determines the transient connected phase record and mean hinge momentum continuously. This closes a specific preparation gap: a separately chosen normalized high-energy connected record is no longer being passed to the hinge as though it were the actual incoming collision's full output.

The completed connection does not automatically reproduce the earlier large hinge rotations. The contact reaction and partial occupation matter. The toy does produce increasing small excursions across these three energy settings, but this does not establish a universal monotonic speed law.

Important limits remain:

- The hinge is one classical ensemble-mean coordinate with fixed geometric inertia. It does not resolve the distribution of conditional hinge trajectories or rare fully quantum branches.
- Both incoming and outgoing records still use the inherited direct-sum phase spaces, not a construction of two independently occupied particles.
- Access to ABE, Lorentz-like compression, the earlier internal tilt, and the final face switches remain outside the propagated coordinate family.
- Neither a permanent output, a photon, physical speed, charge, mass, nor a 372:1 ratio is obtained.

The next useful construction is a branch-resolved joint hinge/phase state. It must preserve total norm and kinetic energy while allowing the connected sector's geometric motion to differ from the original sector, rather than interpreting a small mean angle as a bound on every individual branch.

## Reproduction

Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python pentachoron_entrance_hinge.py

The equivalent stages are `--stage primary`, then `--stage central`, then `--stage other`. Keep `entrance_hinge_solver.py` and the inputs directory beside the driver. No network access is used. Dependencies are NumPy, SciPy and SymPy.

Each trajectory NPZ contains columns:

    time, theta, physical_hinge_momentum, connected_probability,
    dynamic_norm_error, total_energy_error.

The JSON contains all check names, refinements, source hashes, stationary torque components, model choices and finite-observation limits. The input archives are unchanged; no repository file was written.
