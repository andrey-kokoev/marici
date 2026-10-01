# Conditional native contract for the directed seed triangle

`agda/SeedTriangleRouteBinding.agda` supplies a parameterized contract over the existing `NativeNormalizationRouteCompiler`. It does not instantiate a Boolean example or assert a binding to the actual seed.

## Required input

For a chosen normalization code Q and occurrence type, `Binding` requires:

- three presentations A,B,C;
- supplied coherent maps AB:A->B, BC:B->C, CA:C->A;
- three supplied occurrence identities and pairwise inequality witnesses.

CA is an independent required field. No inverse AC is substituted. The common-coordinate coherence certificates are carried by `CoherentMap`; these are substantive assumptions, not inferred from endpoint labels.

## Checked conditional output

Given a binding and an input value:

- `loop` constructs the exact ordered AB-BC-CA route;
- `three-steps` proves its route length is three;
- `occurrence-at` assigns each native compilation slot its corresponding supplied occurrence identity;
- `BoundRun` retains the complete binding and input;
- its `compilation` uses the existing `retain-compilation`, including native derivation and canonical-boundary certificates;
- `retains-binding`, `retains-route` and `retains-occurrences` recover that data.

The occurrence IDs are supplied, not allocated as runtime events. Distinct IDs within one triangle do not establish global freshness across executions. This contract is not a physical event emitter or reset authority.

## Important restriction: flat coherent effects

`closed-effect` proves `execute(loop b,x)=x`, by the existing compiler's comparison of any two coherent routes with the same endpoints, here against stop. Thus this interface accepts coordinate-coherent, identity-effect loops. It does NOT formalize arbitrary nontrivial holonomy. The retained route still has three steps even though its effect equals identity.

This restriction must be checked when an actual seed binding is proposed. One cannot fill this contract and simultaneously interpret its closed payload action as an arbitrary nonidentity triangle permutation. The previous global vertex actions and packet-slot successors are different constructions.

## Open source obligation

No term witnessing `Binding` for the original seed was constructed. Still needed is an independently justified interpretation of its packages, primitive arrow witnesses and occurrences satisfying these coherence conditions. The module's A/B/C names do not themselves prove that interpretation.

This is now a precise conditional interface rather than a further scheduling prototype. If the intended seed has nontrivial closed transport, this normalization compiler may be the wrong target, and a broader admitted comparison interface would need to be selected explicitly.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedTriangleRouteBinding -Fresh

Fresh safe/cubical/guardedness closure passed after adding the slot-to-occurrence binding. Receipt: `results/agda-SeedTriangleRouteBinding.json`. No postulate, concrete filler or physical calibration was introduced.
