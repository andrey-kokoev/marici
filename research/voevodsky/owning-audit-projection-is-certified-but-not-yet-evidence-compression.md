# Owning audit projection is certified, but not yet evidence compression

## Delivered gate

Eliminate audit h=x_0 from the actual uniform joint dictionary for schema {0}, together with retained evidence U=h and h<=1. The complete dictionary supplies source compatibility; the two orientations of U=h and the audit upper bound supply run-specific evidence.

The producer uses Grothendieck's JointAuditModel.cuts, applies exact one-variable Fourier--Motzkin elimination, and then removes redundant projected rows sequentially. Every deletion carries a nonnegative combination of currently retained other rows whose normal is identical and whose upper bound is no larger. Sequential validation prevents circular redundancy claims.

The independent verifier reconstructs the owning dictionary from residual slopes and capacities without importing that model. It checks elimination derivations and complete pair coverage, then every row-deletion certificate. This establishes equality of the full projected set and the final summary, not merely equality of sampled objective values.

## Source-relative reverse lift

U=h and source nonnegativity force every atom other than x_0 to zero. Therefore the public image is exactly

    V=U, 0<=U<=1.

Conversely every such point has the old-compatible source lift (U,0,...,0), satisfying all caps and retained evidence. The final projected rows have exactly the segment endpoints as vertices; boundedness is inherited from certified equivalence to the bounded source projection.

## Results and honest storage ledger

For m=3,4,8, the unreduced projections have 19,29,89 rows. Independent replay certifies 125 deletions in total, leaving four rows in each case. These are valid summaries but not necessarily the shortest rational encoding of the segment.

| m | Original evidence alone | Materialized source plus evidence | Retained summary | Migration packet |
| --- | ---: | ---: | ---: | ---: |
| 3 | 57 bytes | 282 bytes | 64 bytes | 2112 bytes |
| 4 | 57 bytes | 395 bytes | 66 bytes | 3469 bytes |
| 8 | 57 bytes | 1064 bytes | 74 bytes | 13611 bytes |

All counts use compact JSON for the named fields. The migration packet includes original rows, projection derivations and removal certificates, excluding the subsequently appended cost report. These measurements are not minimal coding lower bounds and do not include every external source/schema binding.

The summary is smaller than a materialized source-and-evidence table, but that is not the correct baseline for claiming evidence compression when the source already has a shared generator. Against the 57-byte evidence tuple, even the standalone summary is larger. Keeping the migration proof increases retained storage further. No run-specific storage saving is demonstrated.

A different retention policy could verify a migration once and discard its proof, but the remaining state then relies on that trusted migration event. It would not independently replay its provenance from the summary alone. A self-contained replayable state and a compact checked state are distinct storage contracts.

## Disposition

The pending owning-source projection gate is now implemented for this controlled family. Exact projected semantics and certified redundancy removal work. The experiment does NOT establish general compact projection, a scalable elimination algorithm or evidence compression. Further work should target a genuinely compressible retained history under a declared storage/proof policy, rather than count eliminated source rows as reclaimed run-specific information.

## Reproduction

    uv run --with sympy python research/voevodsky/checkers/check_owning_audit_compression.py
    python research/voevodsky/checkers/verify_owning_audit_compression.py

Artifacts:

- `results/owning-audit-compression.json`
- `results/owning-audit-compression-verification.json`

This run independently reconstructs the finite source dictionary but does not freshly replay upstream all-m analytical admission. The checker verifies controlled rational linear presentations, not authenticated source observations.
