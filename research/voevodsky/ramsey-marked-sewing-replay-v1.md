# Marked sewing replay: eight admitted histories, not all24

## Frozen attempt and failure

The prospective claim replayed Strominger's existing two histories unchanged under all24 seed markings, using `GenerativeAssemblyRules({seedBindings})`. Contexts were kept separate; no union of incompatible role assignments was requested.

The first SCC invocation incorrectly sent the JavaScript checker to Python. This was a harness failure, not scientific evidence. A Python entry point was added and the attempt refrozen at `scc-freezes/ramsey-marked-sewing-replay-v1.297b721e5e491af7.json` before executing the replay.

That correctly launched challenge fails scientifically: marking `[0,1,3,2]`, second retained history, operation index1, requests a neutron `reader-phase-advance` after PN. The unchanged source offers only `inverse-PN` and `NE`. Thus the stronger all24 unchanged-history replay is false. No successful full-covariance receipt was produced.

The source contains a real geometric gate here: `completeN` requires the reference neighbor across the proposed face to be proton geometry; otherwise it returns null. `outgoing` omits null completions. A tetrahedral coordinate permutation is not automatically a symmetry of the selected split-cell history.

## Diagnostic census

A separate post-failure diagnostic, `checkers/diagnose_ramsey_marked_sewing_replay.mjs`, replays all24 contexts without changing either word or manufacturing a missing move. Each available transfer is validated. Every complete replay is checked for certified exits, witnessed contacts and zero pending contacts.

-8 contexts complete both histories and pass those assembly checks.
-16 contexts encounter an unavailable requested operation.

The successful markings are:

    [0,1,2,3] [0,3,2,1] [1,0,3,2] [1,2,3,0]
    [2,1,0,3] [2,3,0,1] [3,0,1,2] [3,2,1,0]

Their C-vertex sets are exactly `{0,2}` and `{1,3}`. Thus the surviving family includes contexts for the two previously missing facets. In particular `[1,0,3,2]` supplies the complementary role partition while replaying the original histories to certified exits.

This is useful positive coverage, not an all-markings covariance theorem. The post-failure diagnostic is not the frozen full-reference/field-covariance test and must not be reported as having passed that stronger test. It retains complete executed operations, first failures and assembly audits in `results/ramsey-marked-sewing-replay-diagnosis-v1.json`.

## Next narrowed construction

Use the two successfully replayed contexts `[0,1,2,3]` and `[1,0,3,2]` as independent assemblies. Verify their complete reference correspondence and the source-derived44-channel field/coefficient binding in their respective frames. Then define cross-context edge/vertex restrictions with both triangle permits retained.

Do not repair the failed all24 claim by changing its history after the fact. A narrower eight-marking covariance claim or a new schedule for the other16 is a new prospective obligation. No full cross-context field intertwiner, common occupied assembly, higher-WG restriction derivation or parent descent result follows from this diagnostic census.

No owner source files, graph verdicts or net revision were changed. No Git checkpoint was performed.
