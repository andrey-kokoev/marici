# Can native rules generate the seam comparisons from incidence alone?

## Actual signatures inspected

`WholePackageResolution.compare-rule` and `NativeTableRules.compare-kind` require a supplied equivalence AND its marked-value path. `higher-rule` / `higher-kind` require the actual higher equality alpha as part of their parameters. `Resolve.apply` requires a formed rule and its endpoint premises. These constructors retain/apply supplied witnesses; they do not search for or synthesize an equality merely from matching endpoint labels.

Identity, inverse, composition and congruence can generate further witnesses from their actual inputs. No relevant initial comparison for AB versus AD DB or BA versus BC CA has been found in the inspected seed declarations. This is not a global impossibility theorem for every possible interpretation or derivation.

## Formal control on the exact seed boundaries

`agda/SeedSeamPathComparisonBoundary.agda` imports the actual seed table and forms the free endpoint-typed path datatype on its six occurrences. It defines

    x0=AB, x1=AD DB : Path A B
    y0=BA, y1=BC CA : Path B A.

A one-step discriminator proves x0 != x1 and y0 != y1. Moreover no map, hence no equivalence, can both send either direct path to its indirect alternative AND preserve that declared discriminator for all paths. The obstruction is therefore to a history-observation-preserving identification, not to every unrestricted equivalence between packages.

The module retains each ordered pair as a comparison QUESTION with recovery. It adds no equality identifying their members. The free-path interpretation is explicit: these proofs do not rule out equality of outputs under a separately supplied effect semantics that retains histories in another channel.

## Three different operations

1. **Endpoint comparison:** the paths already have the same endpoint type. This types their comparison boundary but does not identify the paths.
2. **Effect comparison:** needs an interpretation of each path and an actual equality/equivalence of those effects. The Boolean normalization fixture demonstrates this pattern under supplied flip laws, not for the seed itself.
3. **Discrepancy retention:** the formal mixed four-word chain can remain nonzero. No equality between direct and indirect histories is required. A numerical or DG reading of that discrepancy needs its own interpretation.

The prior shared-leg DG model explicitly adjoins degree-one h,k with boundaries x1-x0 and y1-y0. Such DG witness adjunction is not automatically a native identity path between the free path records. The distinction between these witness types cannot be erased by using the same word 'comparison'.

## Result

The architecture provides an actual typed boundary and retention, but the inspected comparison constructors do not derive the missing leg-effect witnesses from incidence alone. The formal mixed rectangle is available as retained word data; its filler and numerical interaction remain conditional on a supplied response/witness law.

This rules out pretending that common endpoints automatically furnish a history-preserving identification. It does NOT require choosing arbitrary matrices or normalizing the discrepancy to zero. The two direct/indirect pairs can be retained as unresolved comparisons until an independently justified effect semantics is supplied.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedSeamPathComparisonBoundary -Fresh

Fresh safe/cubical/guardedness closure passes. Receipt: `results/agda-SeedSeamPathComparisonBoundary.json`. The module proves path distinction, observation-preserving-map obstructions and retained-boundary recovery. No native seed filler or physical interaction was postulated.
