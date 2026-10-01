# Native target audit: where flatness enters

## Exact origin of the normalization restriction

In `agda/DependentNormalizationCoherence.agda`, a Presentation includes an equivalence `coordinates` to ONE fixed normal-value space. A CoherentMap P R supplies, for every x, an output y with

    coordinates_R(y) = coordinates_P(x).

Because coordinates_R is an equivalence, its fiber over that value is contractible. This yields `map-contractible`, then `compare-maps`, then `route-comparison`. For P=R, every admitted map agrees with identity on every payload. `NativeNormalizationRouteCompiler.effects-agree` carries this fact to sequential route execution.

Hence the identity effect in `SeedTriangleRouteBinding.closed-effect` is forced by ALL-PAYLOAD coordinate preservation, not by a general principle that any endpoint-returning route must act trivially. A route may still have three steps and distinct retained provenance.

`advance` can incorporate a supplied equivalence by changing the target presentation's coordinates. Returning to the same underlying type does not necessarily return to the same full Presentation. Calling the latter an exact loop while forgetting its changed coordinates would hide this assumption.

## Broader pointed interface

`agda/BoundaryGeneratedQuestions.agda` defines

    Filler a b = equivalence e together with e(value a)=value b.

A closed filler preserves the distinguished point, NOT necessarily every payload. The source already supplies `swap-filler : Filler fourQ fourQ` on Bool x Bool. It fixes the marked (false,false), but swaps (false,true) and (true,false). `fillers-distinct` proves it differs from identity. Thus the broad interface admits nonidentity pointed loops without sacrificing the required endpoint-mark equality.

This is not permission to use the previous vertex cycle g as an A-pointed loop: g moves A and fails even the weaker marked-point requirement. A different fiber/value adapter would still be required. Nor does the Boolean swap identify a seed transport or physical reference.

Fresh safe/cubical closure of `BoundaryGeneratedQuestions` passes, including that existing nonidentity-loop proof. No new example was substituted for the actual seed.

## What the seed findings do and do not require

| Seed construction | Established requirement | Does it imply flat payload transport? |
|---|---|---|
|AB-BC-CA endpoint loop|Terminal vertex equals initial vertex|No|
|Retained execution history|Ordered occurrences survive return|No; history is not erased|
|Triangle slot successor C|C^3=I on declared three-slot coefficients|Only that operator; not a derived edge-fiber holonomy|
|Short half-phase S|S^2=C, S^6=I under its declared branch|No identification with one full primitive traversal|
|Full tour slot successor|Six-step permutation return on occurrences|No physical-fiber interpretation supplied|
|Retained rung presentation|Decode recovers original records|Representation recovery, not identity of executed effects|
|Global vertex actions g,h|Noncommuting permutations on four vertices|Not pointed A-loop transport|

None of these inspected results supplies the all-payload common-coordinate law required by the normalization binding. Conversely, none derives a nonidentity pointed seed holonomy. The physical choice remains open.

## Target recommendation, with scope

Use the existing GENERAL pointed-comparison interface as the requirements boundary for a proposed seed transport: actual packages, actual equivalences and marked-value witnesses. It admits both identity and nonidentity loop effects instead of deciding the question by definition. This is a recommendation for an interface, not a constructed source binding or a proof that every physical seed operation is an equivalence.

Keep `SeedTriangleRouteBinding` as an optional STRONGER specialization. Instantiating it is justified only when the source supplies global coordinates and all-payload preservation. Its flatness is not a result derived from the original seed.

The next missing evidence remains the interpretation of the seed's vertices/occurrences as complete packages and supplied pointed comparison witnesses. Do not build another holonomy example or force the Boolean route into that role. Retained-history recovery and physical execution/calibration remain separate obligations.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module BoundaryGeneratedQuestions -Fresh

Passed. Existing receipt: `results/agda-BoundaryGeneratedQuestions.json`. This turn inspected the normalization definitions and freshly rechecked the broader counterexample; it did not claim a new Agda seed-binding theorem.
