# A conditional positive metric exists below the collision and degenerates there

**Iteration 7 of the requested ten-turn work-net run.**

**Strength:** exact real two-dimensional invariant-form identities, a checked source Taylor jet and collision asymptotics in a regular frame. Not a source-derived energy metric or normalization operation.

[Previous collision audit](POSITIVE-SPECTRAL-COLLISION.md) · [Checker](check_conditional_boundary_metric.py) · [Receipt](results/conditional-boundary-metric.v1.json)

## 1. Fresh state and normalization boundary

The selected rank-two plane continues for all z>0, but its step has a nonreal conjugate pair only below z_c approximately 2.9433702. At z_c it has a nontrivial Jordan block; above it the selected eigenvalues are distinct negative reals.

Let T be the restricted step in any regular real frame on the selected plane. Write

    T=((a,b),(c,d)),
    tau=a+d, delta=ad-bc, eta=4delta-tau^2.

Below the collision, delta>0 and eta>0. Introduce explicitly the conditional normalization

    U=T/sqrt(delta).

This is an additional scalar weighting of the operation, not a consequence of changing coordinates. Similarity transformations cannot change the eigenvalue moduli. No physical authority for the normalization is asserted.

## 2. Universal exact invariant form

The real symmetric matrix

    G=((-2c,a-d),(a-d,2b))

obeys, coefficient-by-coefficient in a,b,c,d,

    T^t G T = delta G,
    det G = eta.

Hence U^t G U=G. In the elliptic sector, b and c have opposite nonzero signs. Choose the frame orientation/sign so b>0 and c<0; then G is positive definite.

All real symmetric positive invariant forms for this normalized nonreal two-dimensional step are positive scalar multiples of G. Indeed their entries (u,v,w) obey

    (a-d)u+2cv=0,
    bu+cw=0,
    2bv+(d-a)w=0,

which leave one scale. This uniqueness is for real symmetric forms on the real plane, not a classification of arbitrary Hermitian forms on a larger complex carrier.

These formulas construct a conditional invariant metric, not a native physical metric or an independent preparation of the plane.

## 3. Match the actual reference frame locally

Apply the formula to the checked moving-plane step near z=1, with epsilon=z-1. It gives

    G(0)=diag(3,1),
    G'(0)=((21/4,1/2),(1/2,1/4)).

Thus the construction agrees at the base point with the existing reference-plane metric. The checker verifies the unnormalized conformal identity and normalized invariance through order four using the actual source-derived Riccati jet, not only a generic example.

The required positive inverse-square-root factor has expansion

    delta^(-1/2)=1-(5/4)epsilon+O(epsilon^2).

After this normalization the trace is

    trace U=-1-(3/4)epsilon+O(epsilon^2).

Consequently U^2+U+I still has a nonzero first derivative: restoring unit modulus does not restore the original C3 angle. Both weighting and clock/phase interpretation require separate justification.

The fourth-order identities are Taylor identities. The exact invariant-form theorem applies to the actual analytic step; the truncated jet is not presented as an exact global matrix.

## 4. Use a regular frame at the collision

The prior cyclicity certificate supplies a cyclic source vector at z_c. Project it to the selected Riesz plane and use the local frame (v,Tv). It stays regular near the collision; it does not diagonalize the defective step.

In this frame the step and a positive form below the collision are

    C=((0,-delta),(1,tau)),
    H=((1,tau/2),(tau/2,delta)).

Exactly,

    C^t H C=delta H,
    det H=eta/4.

At the double root lambda_c, tau=2lambda_c and delta=lambda_c^2. The limiting form is

    H_c=((1,lambda_c),(lambda_c,lambda_c^2)),

a nonzero positive-semidefinite form of rank one. This loss of rank is not an artifact of a singular eigenvector chart.

## 5. No uniformly positive metric through the collision

Normalize H to trace one. Its determinant is

    eta / (4(1+delta)^2).

The complementary discriminant and inter-sector resultant remain nonzero at z_c, while the full discriminant has a simple zero. Since

    Delta = -eta * Delta_complement * resultant^2,

eta also has a simple zero there. It approaches zero positively from below z_c. The condition number therefore behaves as

    kappa(H) ~ 4(1+delta_c)^2 / eta
             ~ constant / (z_c-z).

Positive scalar multiplication does not change this condition number. Thus no scalar choice of invariant metric yields uniform upper and lower positive bounds through the collision in a regular bounded frame. A singular change of frame can conceal the degeneration only by losing uniform control of the frame/decoder itself.

Above the collision, eta<0. The same companion formula is a nondegenerate indefinite form of signature (1,1), still satisfying the conformal identity. That is not a positive norm or a photon polarization metric. No physical interpretation of the signature change is made.

## 6. Refined source-operation gate

The mathematical situation is now explicit:

- below z_c, determinant normalization gives a conditional positive invariant metric;
- at z_c, every such metric ray degenerates, consistently with the Jordan obstruction;
- above z_c, the continued form is indefinite;
- normalization does not freeze the C3 angle.

The next executable test is whether the declared scalar weighting and changing metric can arise from an existing source-authorized transport with retained records, rather than being parameter-dependent corrections chosen to repair the mode. A successful algebraic normalization is not itself that source mechanism.

Dictionary/control, correlated preparation, rejection records, geometry and independent physical outputs remain open. Existing work-net contracts and formal outcomes are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_conditional_boundary_metric.py
python research/scattering/seed-composition/check_conditional_boundary_metric.py --check
python research/scattering/seed-composition/check_positive_spectral_collision.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker verifies universal polynomial identities and the actual local source jet with exact rational arithmetic. Its rational companion examples test the universal formula; they are not passed off as sampled source z values. Collision asymptotics use the already-certified simple, internally separated collision. Only the new receipt is written; `--check` is read-only.
