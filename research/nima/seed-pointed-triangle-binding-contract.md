# General pointed triangle binding, with explicit source admission

`agda/SeedPointedTriangleBinding.agda` reuses the existing `BoundaryGeneratedQuestions.Filler` and `Application.perform` interfaces, at their existing universe level. It supplies a conditional contract, not a binding of the actual seed.

## Required input

The module parameters are an admission predicate `Admit` and an occurrence type. A Binding contains:

- actual complete packages A,B,C;
- actual `Resolve Admit` derivations of all three endpoints;
- actual supplied fillers AB,BC,CA, including equivalences and marked-value paths;
- distinct occurrence identities for the three supplied primitive roles.

No endpoint package is admitted automatically. No canonical Boolean package, inverse CA, global coordinate system or physical schedule is selected.

## Conditional outputs

The existing comparison-rule application constructs a derivation for EACH edge from its supplied filler and endpoint derivations. Ordered filler composition constructs `holonomy : Filler A A`. Its `fixes-mark` theorem retains the actual proof that the composite preserves the distinguished value of A. It does not conclude identity on the rest of A's carrier.

A composite comparison derivation is separately produced by the existing rule, with A's endpoint premises. This does not pretend to be a new recursive compilation theorem deriving that comparison from the three edge derivations. The complete binding, including edge witnesses and endpoint derivations, is retained in a higher-level package; all three edge derivations and the composite remain reconstructible from it. The ordered occurrence list and retained composite witness also have recovery definitions/theorems.

This module works through the established whole-package comparison boundary (`WholePackageResolution`), not a newly proved translation into the independent `NativeTableResolution` target. Existing equivalence machinery is not silently treated as a newly instantiated transfer theorem.

## Difference from the flat contract

`SeedTriangleRouteBinding` required common-coordinate CoherentMaps and used the normalization route compiler. That implies identity effect for a closed route.

Here only marked-value preservation is required. The source's existing Boolean-pair swap counterexample is imported as a negative control against claiming all pointed loops are identity. It is not used to instantiate the seed or to choose its holonomy. Neither contract proves that the original seed actually meets its required fields.

## Remaining authority and provenance boundary

Occurrence identities are supplied and distinct within one binding; they are not runtime-generated execution IDs or evidence of global freshness. Applying the comparison constructor does not by itself authorize a physical traversal, energy charge or reset. The source binding and execution interpretation remain inputs.

The useful advance is that the interface now exposes BOTH missing witnesses: actual edge compatibility and actual endpoint admission. The physical loop action is left open rather than fixed to identity by a normalization target.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedPointedTriangleBinding -Fresh

Fresh safe/cubical/guardedness verification passed. Receipt: `results/agda-SeedPointedTriangleBinding.json`. No postulates, concrete seed instance, or new physical law were added.
