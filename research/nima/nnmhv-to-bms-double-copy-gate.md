# NNMHV Coherent Resolution to BMS: double-copy gate

## Question

Do the constructed Coherent Resolution, real celestial kinematics, and exact soft family define the requested radiative-GR generator map?

## Type boundary

The source is the planar `N=4` super-Yang--Mills amplituhedron. Its external physical states have gauge-theory helicity and color-ordering structure. Bondi shear/news and BMS charges belong to a gravitational spin-two phase space.

The celestial momentum map and the `epsilon -> 0` family identify kinematic variables only. They do not change the theory or supply a spin-one to spin-two state map.

A gravitational map therefore requires a typed factorization

\[
CR_m^{\rm SYM}
\longrightarrow
CR_m^{\rm BCJ}\otimes CR_m^{\rm BCJ}
\xrightarrow{\mathrm{double\ copy}}
R_\bullet^{\rm grav}
\longrightarrow
R_\bullet^{\rm Bondi/BMS}.
\]

The first arrow requires Jacobi-satisfying numerator data compatible with the CR differential. The second requires a second gauge copy, state pairing, and projection to the graviton sector rather than the dilaton/two-form sector. The last requires Bondi normalization and the radiative differential.

## Available inputs

The current work supplies:

- an exact finite-rank CR differential at every type-A rank;
- real celestial incoming/outgoing generators at every finite multiplicity;
- an exact momentum-conserving soft-frequency family;
- canonical physical weights and boundary coefficient completion for the selected component.

It does not supply a CR-compatible BCJ numerator functor, second-copy pairing, graviton projector on these generators, or Bondi shear/news chain complex. Existing inverse-KLT and scalar conductor objects do not construct those maps.

## Disposition

The absent radiative generator map is now localized at the double-copy interface rather than at celestial kinematics or the soft limit. Mapping the SYM CR directly to BMS data would conflate gauge and gravitational theories.

Verification:

- `research/nima/results/carrier_gravitational_soft_double_copy_gate.json`
- `research/nima/results/arbitrary-n-real-celestial-kinematics.json`
- `research/nima/results/arbitrary-n-exact-soft-family.json`
- `research/nima/results/radiative-generator-map-no-go.json`
