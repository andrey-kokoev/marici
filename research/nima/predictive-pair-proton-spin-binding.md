# Proton request action now intertwines the retained spin extension

## Result

**36 exact checks pass.** All six proton arrow requests now have a checked raw
spin action for either candidate lift sign. Together with the earlier electron
binding, both species have source-compatible candidate spin actions on their
existing retained encodings. This closes the missing proton intertwiner, not
the remaining joint interaction policy.

## Actual retained carrier reused

The checker verifies the existing proton Merkle source, reconstructs its twelve
ordered triangle modes and recovers the contact model's normalized 36-coordinate
vector v. Its unnormalized norm squared is 80. The declared spin extension is

    W_p = v tensor I_2 : logical doublet -> 72 raw coordinates.

The full encoding is isometric. No extra coefficient state was selected by a
desired result.

For each actual source generator g, reuse the raw action D_g of
`check_native_operation_energy_lift.py`: permute triangle records by left
multiplication of their retained rotation frames and apply the spatial rotation
to each three-coordinate block. The checker reconstructs this action from the
source, checks its record permutation and orthogonal blocks, and verifies

    D_g v = v.

The candidate-lift tetrahedral frame is also checked against the native source
frame, rather than identified by matching dimensions.

## The missing square now closes

For either source-compatible SU(2) lift U_g, define the extended raw action by
the tensor action already appropriate to the declared spin extension. Check
both columns of the entire encoding:

    (D_g tensor U_g) W_p = W_p U_g.

The checker also verifies recovery of U_g by W_p* and preservation of the
encoded metric. Both lifts are retained for both generators, covering AB, BC,
CA, AD, DB and BA. Neither lift sign is promoted to a physically selected rule.

This mirrors the electron cell/face intertwiner previously checked. It supplies
consistent encoded actions; it does not prove that the chosen spin extension
was forced by the original central-even proton geometry.

## Remaining joint boundary

The species-local action interfaces are now available as a family of candidates.
A joint interaction still requires:

- a specified relative proton/electron spin frame and lift choices;
- a logical pair preparation;
- an action or scheduling semantics for relative position and mediator records;
- a policy specifying which relation is protected or allowed to evolve.

The existing relative-motion Hamiltonian does not assign a displacement or
elapsed time to each internal arrow. No such assignment is made here. Hence no
closed contact-preserving transition graph, physical clock or energy calibration
is claimed.

## Verification

    python research/nima/checkers/check_predictive_pair_proton_spin_binding.py

Receipt: `results/predictive-pair-proton-spin-binding.json`.
It exports generator/request bindings, logical matrices, record permutations,
return signs and source hashes. The candidate-lift checker is freshly rerun;
the Merkle source is freshly verified. Owner files are not modified. The complete
native energy calculation and the electron producer are not rerun by this test.
