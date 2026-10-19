# Dynamics selection: exact rivals and a conditional uniqueness theorem

## Disposition

The `passive-port-fock-memory.v1` geometry supports the desired conditional optical/instrument model. Its weak conservation and low-sector properties **do not select that model uniquely**.

This audit constructs two optical phase controls and a detector CP-completion rival. It also identifies the additional optical premise that makes the passive lift unique. The [contract](contracts/physics-dynamics-selection-audit.v1.json) records the bounded claims and their remaining source-justification requirements. Central dynamics selection remains open.

## Optical phase rival

Let N be total photon number. For a one-particle unitary W and additive model duration t, define

`U_chi(W,t) = exp(i chi t N(N-1)) Gamma(W)`.

Because number commutes with every passive lift,

`U_chi(V,s) U_chi(W,t) = U_chi(VW,s+t)`.

The family preserves norm, photon number and vacuum, and agrees with `Gamma(W)` on the complete vacuum/one-photon subspace. Every routed test from iteration 2 stays in that subspace, so all its record probabilities remain unchanged.

This global phase control establishes insufficiency of those weak premises. It is not local to a single cavity component: its phase can involve future input modes. To test the actual spectator constraint as well, the checker also constructs

`K_I Gamma(W_I),  K_I=exp(i chi t N_I(N_I-1))`,

where I is the active four-port set and W_I is identity on spectators. This local alternative leaves future input modes untouched. Ordered histories use the ordered products of these local maps; a multi-round history is not collapsed to a global Kerr formula. Each generator is unitary and number preserving, agrees on total N<=1, and retains spectator coherence. Locality therefore does not itself supply the missing linearity premise.

At `chi*t=pi/2`, the number-sector phase is `(-1)^(n(n-1)/2)`. All executed controls use exact rational coefficients and signs.

## Exact higher-sector discriminator

In the unnormalized creation basis, prepare the mathematical vector

`psi=(e_vac + e_1x + e_2x)/2`.

The basis weights are 1,1,2, so its norm is one and its mean photon number is 5/4. Before the first cavity map, its mean annihilation amplitude is 3/4. The phase control changes that mean to -1/4 while preserving its number distribution.

After the first nominal cavity map, reflected field means are

- passive reference: **3/5**;
- global and active-port-local phase rivals: **-1/5**.

Both keep mean photon number 5/4. Thus a scalar energy or a one-photon test does not establish the full field law.

The test vector is an exact finite-sector discriminator, not a claimed available physical preparation. The frozen coherent-state task also separates the laws analytically: for coherent input z and `lambda=||z||²`, the global rival has

`<a_j> = (Wz)_j exp(lambda*(exp(2 i chi t)-1))`.

At `chi*t=pi/2`, this becomes `(Wz)_j exp(-2 lambda)`, rather than the passive mean. For the local rival the same formula applies to active output modes with lambda restricted to the active coherent input. This violates the general coherent recovery requirement. Independent phase-referenced preparation/readout and a fixed parameter policy would be needed to use it experimentally.

## What does select the passive lift

Suppose U is unitary, preserves the finite-particle core, fixes vacuum, and satisfies

`U a_j† = (sum_i W_ij a_i†) U`

on that core. Applying this equation successively to every creation monomial on vacuum gives exactly the symmetric-power substitution defining `Gamma(W)`. Equality on the dense core extends by continuity to the whole Hilbert space.

Therefore **vacuum fixing and linear creation covariance select `Gamma(W)` uniquely** at the supplied W. The phase rivals violate this covariance. The executable reference passes 110 creation squares; the global rival fails 100, and the local rival fails 16 active-port squares while preserving 66 spectator squares. A concrete residual has squared norm 8.

This is a conditional uniqueness theorem. The covariance premise, numerical W, physical clock and energy conventions still need independent source or apparatus justification. The theorem does not derive linear optics from a common software schema, dimension or conservation law.

## Classical detector records do not determine the full quantum completion

Keep the source's click operators and classical ready/dead transition probabilities. In its no-click branch, replace the two separate operators

`K_vr=|0R><0R|`, `K_ds=(4/5)|0D><0D|`

by the single operator `K_vr+K_ds`. All other Kraus operators remain unchanged. Orthogonal output memory states make the cross terms in `K†K` vanish, so completeness and complete positivity survive.

On every diagonal joint input, both instruments have exactly the same outcome maps. Sharp zero/one optical preparation preserves that diagonal state family, so induction gives identical complete classical record laws for all such histories. The checker confirms 252 history cases through three bins.

For the hypothetical coherent-memory input `( |0R>+|0D> )/sqrt(2)`, both no-click outputs have populations `(17/25,8/25)`, but their off-diagonal entries are 0 and 2/5. The memory-X expectation is therefore 0 versus 4/5.

Frozen classical record recovery survives. A claim about the larger CP completion requires the environmental-label premise or additional coherent-memory preparation and observation. Those interventions are outside the charter and are not silently added here.

## Verification and integration

The [checker](checkers/check_physics_dynamics_selection_audit.py) verifies source hashes, 66 timed composition columns, creation-covariance controls, the exact field-mean discriminator, unchanged low-sector routed records, two detector completeness identities, eight diagonal outcome-map equalities and 252 classical histories. It imports only the side-effect-free functions of the geometry checker; source-owner programs and receipts are untouched.

```
python research/nima/checkers/check_physics_dynamics_selection_audit.py
python research/aspect/scc/scc.py check physics-dynamics-selection-audit-v1
```

The three current packets now provide:

1. a typed observation/resource interface with physical slots exposed;
2. an explicit conditional geometric candidate and composed source/instrument map;
3. exact nonuniqueness controls and a conditional optical selection theorem.

The interface and geometry are now accepted by `contracts/physics-interface-geometry-admission.v1.json`. Dynamics selection remains open. A concrete gain-robust two-intensity field-mean discriminator is supplied by `contracts/physics-phase-discriminator.v1.json`; independent justification or testing of creation covariance is the next source-law step. The existing native-source operation obstructions remain in force.
