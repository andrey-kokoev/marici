# Covariant escape lift: lab translations and invariant-mass retention

[Contract](contracts/covariant-escape-lift.v1.json) · [checker](check_covariant_escape_lift.py) · [receipt](results/covariant-escape-lift.v1.json)

## Result and new postulates

The positive [rest escape model](PHOTON-ENERGY-TAIL.md) now has a declared **active-sector Poincare completion**, with commuting conserved four-momentum, correct free photon lab translations and complete wave operators on its specified scattering subspace. Combining it with the [full packet isometry](TOTAL-MOMENTUM-PACKET.md) supplies a normalizable photon outgoing readout that intertwines active translations and Lorentz transformations.

This adds a conserved velocity carrier, imported spin assignments and interacting momentum P^mu=u^mu*H_rest. It does not derive those resources from native L/G/N operations or identify the charged source with an actual relativistic electron/positron preparation. Poincare covariance is not locality, cluster separability or microcausality.

A separate exact control shows why lab energy and invariant mass must not be conflated: a boosted bound cloud can have continuous lab energy and a decaying return amplitude while retaining its full bound mass weight.

## 1. Positive mass operator and velocity carrier

For J=0,1 let h_J be the earlier source plus old band plus added energy-tail Hilbert space. The rest mass operator A_J is the self-adjoint positive H_rest with epsilon=3, g_s^2=1/4 or g_t^2=2, delta=1/4. The triplet copies have identical radial operators, so A_J commutes with all imported spin rotations. Its positive quadratic-form triplet margin is 29/32. The active rest mass has purely ac spectrum on M>0; no eigenstate at zero is inserted.

Use

```
H_active = direct_sum_(J=0,1) L2(Hyperboloid+,dmu(u); h_J tensor C^(2J+1)),
dmu=d^3uvec/u0,
P^mu=u^mu*A_J,
H_lab=P0=u0*A_J.
```

These products are defined by the joint spectral calculus of velocity multiplication and A_J, on the domains where their squared norms are integrable. They are self-adjoint, strongly commute, and satisfy

```
P0>=0,
P.P=A_J^2.
```

Compact velocity and bounded mass spectral support give a dense common core for the joint calculus. Total velocity and full interacting four-momentum are conserved. Bare source momentum 3*u is **not** the conserved full interacting momentum operator when the source has a mass distribution.

Let B(u) and W(L,u) be the canonical boosts/Wigner rotations from the packet construction. Define

```
(T(L)psi)(u)=D^J[W(L,L^(-1)*u)]*psi(L^(-1)*u).
```

The radial mass operator commutes with D^J. Invariance of dmu and the Wigner cocycle make T a strongly continuous unitary Lorentz representation. In the active convention,

```
T(L)^(-1)*P^mu*T(L)=L^mu_nu*P^nu.
```

Together with exp(-i*a.P), this yields a positive-energy Poincare representation. This is a conditional mass-operator/velocity construction, not a local charged field theory.

The twelve other fermion occupations and sixty raw-pair complement records are retained unchanged in a separate bookkeeping block. **No Lorentz action or physical mass is silently assigned to those untyped records.** Covariance claims apply to the declared active carrier; they are not a full native-source Poincare extension. Auxiliary declared records can also be carried by identity tensor factors without tracing them out.

## 2. Lab wave operators, without a global trace-class shortcut

Let h_out be the old free half-line plus the added energy continuum, M_out its rest energy, and I_out its inclusion into h_J. The established rest wave operators are

```
Omega_rest,+/- = strong-lim_(s->+/-infinity)
                exp(i*A_J*s)*I_out*exp(-i*M_out*s).
```

On a velocity fiber the lab generators are u0*A_J and u0*M_out. Since u0>0, the lab limit is the same rest limit with s=u0*t. For any square-integrable velocity packet the error is bounded by twice its fiber norm, so dominated convergence gives

```
Omega_lab,+/- = I_velocity tensor Omega_rest,+/-.
```

This is a direct-integral proof. The fiber's finite-rank perturbation need not be trace class after tensoring with an infinite velocity space; no global trace-class theorem is improperly invoked.

Rest spectral intertwining and scalar spin action give, in bounded spectral/exponential form and on the corresponding generator domains,

```
P^mu*Omega_lab = Omega_lab*P_out^mu,
T(L)*Omega_lab = Omega_lab*T_out(L),
Omega_lab*Omega_lab^dagger = I_velocity tensor P_ac(A_J).
```

For delta=1/4 this range is the entire active carrier. The open model has no remaining active mass-bound cloud. This says nothing about the separately retained source spectators.

## 3. Actual full photon readout

The old Dirichlet lead's flat-energy spectral transform sends site n>=1 to

```
phi_n(M)=sqrt(rho_band(M))*U_(n-1)((2-M)/2),
rho_band(M)=sqrt(M*(4-M))/(2*pi), 0<M<4,
```

where U_k is the second-kind Chebyshev polynomial. The sine transform proves this map unitary onto L2((0,4),dM). The added channel already uses flat energy dM. Retain both transforms and zero-extend the old band coefficients outside (0,4).

Compose the adjoint wave operator with these free spectral transforms and the packet isometry J:

```
R_out = J * F_out * Omega_lab^dagger * Q_ac_mass,
Q_ac_mass=I_velocity tensor P_ac(A_J).
```

This is an isometry on the active scattering subspace into a selected **full** Bose-Fock subspace, not onto all photon states. It intertwines the active conserved four-momentum with summed photon momentum and the active Lorentz action with the standard photon action, retaining the earlier mass coarea, factorials, boost records and helicity phases.

For a model with mass point spectrum, retain Q_pt_mass*psi alongside R_out*psi. Append the untouched spectator block too. The completed vector readout is isometric; its components are orthogonal records, not outcomes renormalized after deleting failed release. Relative phases are retained in this direct sum.

## 4. Lab clocks are not a calibrated moving lifetime

For a fixed u, literal lab time uses exp(-i*u0*A_J*t). Along the trajectory with v=uvec/u0, the combined translated generator is

```
P0-v.Pvec = A_J/u0,
u0-v.uvec=1/u0.
```

At q=(1/8,0,0), u0=65/63: the fixed-origin generator coefficient is 65/63, whereas the co-moving translated coefficient is 63/65. The latter gives proper-time dilation along that trajectory. The former must not be relabeled as an experimentally observed accelerated or dilated lifetime.

The internal source projector |e0><e0| is not yet a localized detector following a physical encounter. For a velocity superposition the co-moving expression is a fiberwise diagnostic, not a single spacetime translation or a universal detector protocol. No source clock, lifetime or lab detector law is calibrated here.

## 5. Bound mass can survive continuous lab energy

Repeat the lift for the cutoff control delta=0, retaining the decoupled tail. The rest triplet has bound mass E_b=2+sqrt(5). An initial contact source retains

```
||Q_pt_mass psi||^2=Z=1/sqrt(5),
late internal source-site probability=Z^2=1/5,
free photon outgoing norm=1-Z.
```

Use the prior normalized continuous boost envelope b(q). On the bound subspace, lab energy is E_b*u0(q), which has an absolutely continuous distribution: away from the measure-zero r=0 point,

```
E_lab(r)=E_b*(1+r^2)/(1-r^2),
dE_lab/dr=4*E_b*r/(1-r^2)^2>0.
```

Radial coarea on the cube produces an L1 energy density. The bound contribution to the global return amplitude therefore tends to zero by Riemann-Lebesgue, **although its invariant-mass bound norm remains Z**. The rest ac return contribution also vanishes. In particular the normalizable packet has zero lab-energy point weight and vanishing global return amplitude, but nonzero retained mass/cloud weight.

Internal source-site probability integrates |A_rest(u0*t)|^2 over velocities. Dominated convergence gives the same plateau 1/5; it does not disappear merely because a coherent boost-averaged return amplitude dephases. Co-moving fiber clocks give the same late plateau.

Consequently in this control

```
range(Omega_lab) = Q_ac_mass H_active,
Q_ac_mass != P_ac(P0).
```

Completeness in the free photon **channel** sense cannot be inferred merely from ac lab energy. The mass-bound packet is a different asymptotic sector. This is an exact declared-model counterexample, not physical capture evidence.

## 6. Verification and next gate

Exact tests cover common-factor four-momentum commutation/Casimir/covariance identities, a six-polynomial Chebyshev/semicircle Gram identity for the free lead, the two clock coefficients, positive margins and retained mass/cloud/outgoing norm accounting. The small matrix used for the common-factor algebra test is **not** a finite approximation used to decide the infinite spectrum. Self-adjoint joint calculus, Poincare strong continuity, direct-integral wave limits, Fock intertwining and the dephasing argument are documented analytic proofs, not machine-formalized results.

The [local-source audit](LOCAL-SOURCE-VERTEX.md) now constructs conditional Dirac/Maxwell Wick-density candidates with nonzero gauge-invariant two-/three-photon vertices. It excludes exact reproduction of the chosen rational envelope by finite-derivative point-current tree contacts alone, not by composite sources or local UV completions. Next compute full helicity/profile projections with omitted amplitudes retained and bind an actual incident source/current matrix element. Native locality and cluster behavior remain open. Bind an actual native encounter and incident packet independently. A concrete continuation is to examine the position-space kernel implied by the chosen rational mass envelope and test locality assumptions before promoting a Poincare representation to a field-theory interaction. Do not infer a field commutator's support from a one-packet amplitude: specify the operator algebra and distinguish effective-vertex nonlocality from packet tails. Omitted photon profiles, source preparation, dimensional calibration and detector/flux binding remain explicit gates; covariance alone selects none of them.

C1–C12 and exhausted C12 effort remain unchanged; high-energy execution stays paused. Historical source/owner warnings are preserved. No physical outcome, annihilation rate or branching ratio is admitted.

```sh
python -S research/scattering/low-energy/check_covariant_escape_lift.py --check
python -S -m unittest discover -s research/scattering/low-energy -p test_covariant_escape_lift.py
```
