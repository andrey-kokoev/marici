# Branch-resolved entrance and a quantum hinge on the connected boundary

Date: 2026-10-11  
Status: New conditional quantum-configuration model extending the supplied mean-hinge calculation. No physical electron–positron or completed-product prediction.

## 1. Result

Giving the connected topology its own angular wavefunction produces a broad conditional angle distribution, despite a small conditional mean angle. In the refined reflecting-endpoint fixture, root-mean-square angles at maximum connected occupation are approximately 69.5, 55.2, and 75.0 degrees at incoming central kinetic parameters 1, 2.3, and 4 epsilon. Actual connected occupations remain approximately 1.12%, 1.49%, and 1.43% of the original full preparation.

This is NOT obtained by normalizing a small core record and evolving it as a fully merged collision. Both topology sectors are propagated together by one time-independent linear Hamiltonian. Conditional normalization is used only in computing observables after propagation.

The broad distribution persists when the connected native matrix is made angle independent. Most of this effect is quantum angular spreading after entry, not a stronger directed torque. Endpoint conditions matter: at K=2.3, replacing zero-derivative reflection by zero-value reflection changes the refined conditional RMS from about 55.2 to 40.9 degrees. Neither closure permits outgoing product flux. A wide distribution is not a probability of first reaching or crossing the splitting contact.

## 2. Source and changes of model

The unchanged `inputs/pentachoron_entrance_hinge_bundle.zip` is the source. Its manifest and the two copied matrix payloads are checked by `verify_study.py`. Its source note explicitly leaves branch-resolved motion open (sections 3, 9–10). It supplies:

- original and connected twenty-coordinate native matrices H_O and H_C, including retained cycle comparisons;
- the rank-two matching projector P;
- the hinge generator A, with A^2=I/16 and F(theta)=exp(i theta A);
- H_C(theta)=F(theta)H_C F(theta)^dagger;
- I(theta)=m ell^2 (14-2 cos(theta))/15;
- the geometrically admitted angle interval -theta_* <= theta <= theta_*, where theta_*=acos(-1/4);
- the incoming four-ground-mode mixture and the one-dimensional original encounter line.

New assumptions in this calculation:

1. The connected sector alone has a quantum hinge coordinate; the original sector retains its encounter coordinate. These are alternative configuration spaces, not a common classical mean coordinate.
2. Quantize the specified hinge metric using the arc-length kinetic quadratic form, equivalent to the Laplace–Beltrami choice. Other quantization prescriptions have not been excluded by geometry.
3. Admit entrance at hinge angle zero only. Compare the original amplitude at x=0 with the connected angular amplitude at zero arc length. This is a NEW point-to-point sampling law, not an exact consequence of the old finite-core contact model.
4. Use the existing length ell also to normalize the new angular contact sample. The angular sampling scale is not independently derived.
5. Close both hinge endpoints by zero normal derivative in the ambient phase frame. Also test zero-value endpoints as a different conservative closure. The actual three face switches and exit-memory gate are not executed.
6. Retain epsilon=hbar=ell=m=1, original kinetic coefficient 1, and the same incoming packet. The quantum hinge kinetic coefficient in arc coordinates is consequently 1/2.

The previous mean-hinge trajectory is not a theorem about the new quantum model, and the new angular distribution is not a numerical refinement of that classical trajectory. This is an explicitly changed dynamical model.

## 3. A metric coordinate with no angular-resolution parameter

Define the physical arc coordinate

    s(theta) = ell integral_0^theta sqrt((14-2 cos(u))/15) du
             = (4 ell/sqrt(5)) EllipticE(theta/2 | -1/3).

Then

    ds/dtheta = sqrt(I(theta)/m),
    s_* / ell = 1.692754342871824,
    theta_* = 1.8234765819369754 radians = 104.4775121859 degrees.

The classical kinetic energy on the constrained path is m s_dot^2/2. Its admitted quantum counterpart in L2(ds) is

    T_C = -(hbar^2/(2m)) d^2/ds^2.

The probability measure in theta includes the Jacobian ds/dtheta. A density per unit arc length must not be interpreted as the same density per unit angle.

The mesh spacing used below is numerical resolution. It is neither a physical geometric tolerance nor an additional angular cutoff.

## 4. The joint state and contact form

Take

    Hilbert space = [L2(R,dx) tensor C^20]_O
                   direct-sum [L2([-s_*,s_*],ds) tensor C^20]_C.

Write its components psi(x) and chi(s). The full norm is

    integral ||psi||^2 dx + integral ||chi||^2 ds = 1.

With kappa_O=hbar^2/(2 mu) and kappa_C=hbar^2/(2m), the energy form is

    Q[psi,chi] = integral_R [kappa_O ||psi'||^2 + psi^dagger H_O psi] dx
               + integral_interval [kappa_C ||chi'||^2
                   + chi^dagger F(theta(s)) H_C F(theta(s))^dagger chi] ds
               + 2 epsilon ||P[sqrt(ell)psi(0)-sqrt(ell)chi(0)]||^2.

In this display H_O,H_C are physical energy matrices; the NPZ stores their dimensionless values in epsilon units. The existing finite-core amplitude has been replaced by an angular field, so its contact trace requires the extra square-root-length factor.

The form domain is H1(R;C^20) direct-sum H1(interval;C^20) for the primary reflecting closure. For the alternative closure, use H1_0 at the two outer connected endpoints. Point evaluation on these one-dimensional form domains is bounded in their H1 norm. The finite positive contact form and bounded Hermitian native potential give a closed lower-bounded form and thus a self-adjoint Hamiltonian. Its time-independent evolution conserves total norm and total energy.

At the interior junction both fields are continuous along their own coordinate. Their derivatives satisfy

    kappa_O [psi'(0+)-psi'(0-)] = 2 epsilon ell P[psi(0)-chi(0)],
    kappa_C [chi'(0+)-chi'(0-)] = 2 epsilon ell P[chi(0)-psi(0)].

The two contact contributions exchange probability; their sum supplies no loss or external pulse. The primary outer conditions are chi'(-s_*)=chi'(s_*)=0. The control uses chi(-s_*)=chi(s_*)=0. Both give zero endpoint current.

All twenty phase coordinates remain at each connected point. The old direct-sum interpretation of those coordinates remains: this is not the tensor-product construction of two independently occupied physical particles.

## 5. Moving-frame covariance

For chi=F(theta(s))u, the native potential becomes H_C, but the kinetic derivative becomes

    d/ds + i A dtheta/ds.

Thus the transformed kinetic form is

    kappa_C integral ||u' + i theta'(s) A u||^2 ds.

The contact is unchanged because F(0)=I. Zero-derivative endpoints become covariant zero-derivative endpoints in this frame. Discarding the connection changes the operator even though it makes the native potential look constant.

The checker constructs the complete discrete unitary transformation, including the kinetic links and endpoint conditions, and propagates in both frames. The actual angle densities agree. A separate CONSTANT-NATIVE control deliberately changes the model by using H_C at every angle with ordinary derivative kinetics. It is not mislabeled as a coordinate change.

## 6. Incoming preparation and normalization

Use the same equal incoherent mixture of the four lowest original native modes as the source. The incoming spatial Gaussian has standard deviation 2 ell, initial center 14 ell from contact, and inward central momentum with nominal kinetic energy K. Initially chi(s)=0 everywhere. There is no separately chosen connected spinor, angular packet, or angular momentum kick.

The original point-contact model separates odd and even encounter fields. Only the even field couples, and only two of the four original ground-mode combinations are bright. The ground restriction of P has spectrum {0,0,1/5,1/5}. As in the source, propagate the two bright even records, each with norm 1/2 and mixture weight 1/4. Their combined dynamic probability is 1/4; the remaining 3/4 is a free spectator. Its norm and unchanged energy remain in the ledger.

The spectator energy uses the actual finite-grid prepared kinetic expectation, not merely the nominal K. In the continuum Gaussian, mean kinetic energy is K+epsilon/16. Finite-grid dispersion changes it slightly.

There is no division by connected occupation in the evolution equations. Define after propagation

    P_C(t) = sum_j w_j integral ||chi_j(s,t)||^2 ds,
    rho_C(s|t) = sum_j w_j ||chi_j(s,t)||^2 / P_C(t),
    mean_C(theta) = integral theta(s) rho_C(s|t) ds,
    RMS_C(theta) = sqrt(integral theta(s)^2 rho_C(s|t) ds).

Conditional RMS is not angular velocity, directed travel, a first-passage probability, or a classical path. Positive and negative angular components can make the mean small while leaving RMS large.

## 7. Numerical results

All times below are in hbar/epsilon. Observation ends at t=25. The refined runs use original spacing 0.05 ell, 160 angular intervals, and timestep 0.0125. Each row is evaluated at the sampled time of maximum connected occupation in its run; sampling is every 0.1 time units.

| Central K/epsilon | Peak time | Peak connected probability | Conditional mean angle | Conditional RMS angle |
|---:|---:|---:|---:|---:|
| 1.0 | 8.2 | 0.01117336597 | 0.03024 deg | 69.4811 deg |
| 2.3 | 7.7 | 0.01491095224 | 0.60098 deg | 55.1594 deg |
| 4.0 | 5.6 | 0.01428791745 | 0.89118 deg | 74.9895 deg |

Rounded values, rather than all displayed digits, should be used as continuum-level descriptions. Combined grid/time refinement changes these peak occupations by less than 0.000064 in absolute probability and the RMS angles by less than 0.14 degrees.

As an additional diagnostic, at K=2.3 and its peak time,

    Pr(|theta| > theta_*/2 AND connected) = 0.00563330990,
    Pr(|theta| > theta_*/2 | connected)   = 0.37779679045.

The half-angle is an arbitrary reporting partition of the distribution, NOT an interaction tolerance or a revived version of the previously rejected half-normal-angle contact rule. These are instantaneous region probabilities, not probabilities that the trajectory ever crossed that region or reached an endpoint.

The final connected occupations at t=25 are still approximately 0.00677, 0.01153, and 0.00798. These are not asymptotic capture fractions.

## 8. Controls that limit the interpretation

### Native angle transport versus quantum spreading

At K=2.3 on the primary grid:

| Angular potential convention | Peak P_C | Mean angle at peak | RMS angle at peak |
|---|---:|---:|---:|
| Inherited F(theta)H_CF(theta)^dagger | 0.0149748 | 0.5921 deg | 55.2283 deg |
| Constant H_C, deliberately changed dynamics | 0.0148697 | approximately 0 | 54.0737 deg |

Large spreading therefore does not require the angle-dependent native transport. The inherited transport affects asymmetry and the detailed state, but the large RMS cannot be advertised as evidence of a strong source-derived phase torque.

### Endpoint dependence

At K=2.3 on the refined grid:

| Conservative endpoint rule | Peak P_C | RMS angle at peak |
|---|---:|---:|
| Zero normal derivative | 0.0149110 | 55.1594 deg |
| Zero value | 0.0116945 | 40.8564 deg |

Both remain broad, but their detailed predictions differ. Reflection has had time to affect the reported distributions; these are not measurements of the pre-reflection first excursion. Neither endpoint rule is selected by the available geometry or the prior exit gate. Both deliberately prevent output flux. Boundary amplitude is not an emitted-product count.

### Other checks

- Zero contact leaves connected occupation exactly zero.
- Ambient and consistently covariant moving-frame propagation agree.
- Enlarging the exterior encounter region from 100 to 120 ell leaves the reported observables unchanged within the numerical checks.
- An independent sparse matrix exponential tests the complete joint wavefunction on a smaller grid, rather than just testing conservation within the primary integrator.
- Reverse propagation recovers the two initial bright inputs.

## 9. Energy accounting

The numerical ledger retains five dynamic terms: original translation, original native energy, connected angular kinetic energy, connected native energy, and positive contact energy. A common original ground-energy shift and the constant spectator energy are restored when total energies are quoted.

Angular kinetic energy is explicitly present. The connected angular field is not given a normalized high-energy initial preparation for free. Its occupation, energy, and coherence arise through the same autonomous contact that modifies the original field.

For example, at K=2.3 in the refined run the conditional angular kinetic expectation at maximum connected occupation is approximately 0.746991 epsilon. That is an expectation conditioned on a finite-time component, not a fixed-energy asymptotic channel or an energy cost to multiply by an independently postulated branching probability.

## 10. Verification and reproduction

The final receipt records 163 passing checks, including provenance, matrix identities at stated numerical precision, point-sampling normalization, conserved probability/energy, frame covariance, refinement, endpoint controls, independent propagation, and reversibility. The analytical form construction supplies the self-adjointness and conservation argument; floating-point tests are implementation checks, not exact symbolic proofs or experimental uncertainties.

Across the saved runs, maximum recorded energy drift is 2.13e-12 epsilon or less. The independent sparse-exponential comparison has whole-state error approximately 4.07e-6 on its stated smaller grid and timestep.

Refinement history is retained: the first 80-to-160 angular trajectory comparison had error 2.35397e-5, slightly above its initial 2e-5 target. Refining to 320 intervals passes that unchanged target. This initial missed target is recorded in the JSON rather than erased or relabeled a pass.

Run:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_cases.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify_study.py

The saved runs can be audited with the second command alone. Dependencies are NumPy, SciPy, and Python. The input predecessor archive is unchanged. No repository mutation or external source lookup is used by these scripts.

## 11. Research boundary and next construction

The source's small mean classical response was not a bound on a conditional quantum angle distribution. This new model constructs that distribution without inflating a transient core state. It demonstrates the distinction but does not select its own endpoint rules or prove the actual pentachoron collision obeys this quantum-configuration prescription.

Still absent: compression and access to ABE, two independently occupied particle preparations, a physical sampling scale, the three subsequent phase-compatible face switches, independent products, a relativistic law, or a speed/energy calibration. Nothing here determines the 372:1 target or identifies a photon.

The next concrete operation is to replace the reflecting endpoints by the already identified face-switch and retained-memory exit channels within the same self-adjoint joint model. Then outgoing flux, rather than angular spread or a conditional normalization, can define a splitting probability.
