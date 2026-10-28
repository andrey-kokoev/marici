# Applicability of Strominger's native sewing to the Ramsey facet cover

## What was reused

This audit imports the actual `channel-assembled-native-fixture.json` and `strict-native-comparison.json`, not a new field model. The comparison verification receipt and its direct source hashes pass, as do the direct hashes of the underlying field-sewing receipt. Imported exact matrix checks were not rerun. Neither Strominger's artifacts nor his native grammar were changed.

The prospective policy and checker were frozen in `scc-freezes/ramsey-strominger-sewing-bridge-v1.c35e696e94aa37b7.json` before testing. The SCC challenge passes the applicability audit, not a claim of four-facet descent.

## Exact coverage result

The fixture contains five presentations of the Ramsey root tetrahedron: packets 0,2,4,6,24. All use the same geometric C/M partition. Their different origins, reader frames and coefficient histories are retained.

Three actual PN operation occurrences leave that chamber:

| Operation | Source → target | Facet opposite vertex index | Context matches | Exact state matches |
|---|---|---|---|---|
| 0 | 0 → 1 | 0 | Ramsey chart 0 or 16, face 0 | chart 0, face 0 |
| 6 | 6 → 7 | 2 | Ramsey chart 0 or 16, face 2 | none |
| 32 | 24 → 23 | 2 | Ramsey chart 0 or 16, face 2 | none |

Context matching checks the common geometric triangle, source and target species, and **both complete alias packets**, including C2. Exact matching additionally checks both endpoints' origin and five-slot permutation. Matching local allocation IDs is neither required nor sufficient.

Consequently the imported fixture supplies facets 0 and 2, but not facets 1 and 3 (opposite `0,1,0,0` and `0,0,0,1`). This is a scope fact about the existing fixture, not a theorem excluding other assemblies, rotated copies or context-indexed extensions.

The two unmatched-state PN occurrences must not be collapsed to the stored Ramsey face-2 record just because their geometry and aliases agree. They carry different source histories; an extension must include those inputs or construct explicit history/phase transport.

## Comparisons that really are available

All25 ordered pairs of the five root presentations occur in Strominger's checked comparison table, with full-field readout and coefficient-binding squares. In particular packets6 and24 have identity field comparison but coefficient permutation `[1,4,0,2,3]` of order five. Their readouts and bindings differ.

This positively supplies a source-bound example of retained contextual comparisons. It does **not** change the root's geometric C/M partition or create its two missing PN facets. The coefficient permutation acts on coefficient slots, not automatically on geometric role assignments. Nor is a sector-field comparison automatically an admitted higher-WG derivation between our String-valued record packages.

## Revised construction target

Do not extend the Boolean role-fiber audit as if it were the only available comparison. Use the existing field/coefficient construction as the regression model, but add the following explicitly:

1. Generate independently validated chart contexts covering the missing facets, with full five-reference packets and separate histories. Frame rotations may generate candidates, but cannot silently merge incompatible role assignments into one occupied assembly.
2. Supply a source-backed field action and five-slot binding for each added context. Verify the readout square on the full44-coordinate field, not merely prepared coefficients. A freely chosen frame making a square commute is not independent source selection.
3. Specify edge and vertex restriction objects retaining both parent contexts and their own triangle permits. The inherited pairwise field cocycle alone has no such geometric restriction type.
4. Bind those structured objects to actual native higher-WG inputs and construct the restriction/comparison and triple-vertex witnesses. Preserve the nontrivial coefficient history even if a field map is identity.

Strominger's seven-position edgewise refinement is a relevant model for retaining background occurrences rather than assigning a single chart to each fine vertex. It does not supply the missing PN-context field bindings by itself.

The first missing input for direct reuse is therefore **coverage by source-bound role contexts**, before a claim that the existing comparison triangles solve four-facet incidence descent. The Ramsey parent remains open; no net verdict or physical/global claim is changed.

Artifacts: `checkers/check_ramsey_strominger_sewing_bridge.py`, `results/ramsey-strominger-sewing-bridge-v1.json`, and `contracts/ramsey-strominger-sewing-bridge-attempt.v1.json`. No graph publication or Git checkpoint was performed.
