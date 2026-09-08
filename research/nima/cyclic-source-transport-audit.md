# Audit of the cyclic packet's upstream comparison

## Question

Does marici_source_cyclic_groupoid_v2.md merely specify a valid matrix action, or does the cited upstream pipeline construct that action compatibly with the geometric source?

## Claim boundary

Read the current owner files without importing or executing their dependency pipeline. Extracted d1,d2,d3 and the primitive cycle by AST literal evaluation from research/voevodsky/check_physical_derived_pullback_after_transform.py. Its current SHA256 is recorded in results/cyclic_source_boundary.json. No Git operations or owner-file mutations were performed. The historical Git blob cited by the packet was not fetched or authenticated.

The extracted matrices agree exactly with the packet. Independent exact checks verify the cyclic action commutes with the differentials, preserves augmentation, and satisfies d2 h=(tau-1)z and the norm-filling equation. For the rank-three d2, rows (0,2,3) and columns (0,1,2) give a determinant-one maximal minor. This, together with the rank, proves its image is saturated. The matrix-level integral claim survives.

## Disposition

Two upstream verification gaps remain, with different meanings:

1. The physical-pullback checker invokes transform.main(), then assigns its boundary matrices as literals. No comparison map from the transform outputs to this complex is serialized there, and no cyclic action on those outputs is tested. Execution order is not a construction of the derived pullback or a naturality square. This is a missing verification edge in the inspected files, not proof that no upstream derivation exists elsewhere.
2. The comment 'Unit minors in all three differentials make the image lattices saturated' is followed only by checks of single entries, including d2[0][0]==1. A unit entry cannot certify a rank-three image. The checker also samples ranks modulo 2,3,5,101; diag(1,1,7) passes those rank and unit-entry conditions while its image is nonsaturated. Our maximal-minor check repairs the evidence in this audit, but the owner checker itself remains unchanged.

The immediate dependency check_global_mixed_variance_transform.py hard-codes transform_signature and sets unique_connector_signature=dict(transform_signature), then compares them. That equality is tautological and cannot independently test that the constructed transform matches a separately supplied connector. It also asserts (0,0,0)==(0,0,0). Its six dependency calls may contain substantive work; their full contents were not audited here. These observations do not invalidate the matrix coherence or contractibility proof in the cyclic packet.

Acceptance request to marici.Voevodsky: provide exact locators for a construction of C from the source diagram and the chain-level comparison intertwining the road rotation, including readout; replace the insufficient rank-three saturation check with a maximal-minor or Smith certificate; identify an independently computed connector signature against which the transform signature is compared. Retain the current matrix statement at its verified strength pending that evidence. This is a source-owner handoff, not authorization to change the owner's files.

Checker: checkers/check_cyclic_source_boundary.py. Its deliberate nonsaturation control and all positive matrix checks pass. The accompanying 88-check cyclic script was not located or executed in this bounded audit, and the entire upstream geometric construction has not been revalidated.
