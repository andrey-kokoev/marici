# Working branch: the {2,2} wiring family

## Decision

Use **{2,2}** as the explicit operator-chosen working family. This closes the family-selection question for subsequent work under this assumption; it does not establish a native selection law or a C5 identification.

All eight labelled candidates are retained:

```
1, 3, 5, 7, 8, 11, 12, 13
```

These are source indices into the sixteen localized survivors, not new physical labels. There are two working candidates in each of the four complete middle covers. No representative is chosen and no provenance quotient is taken.

The {2,10} candidates remain separately available as controls:

```
0, 2, 4, 6, 9, 10, 14, 15
```

They are not declared inconsistent or physically excluded.

## Retained input for subsequent work

`results/su32-working-wiring-family-v1/verification.json` is the checked working-family input. It contains:

- every working and control pair placement, with its original candidate ID;
- each complete middle assignment and its original reference/operand annotations;
- the candidate-specific selected-pair restrictions to the six cones;
- the original registry, entry/exit reference presentations and entry-side assignments;
- both full central reconciliation trees;
- the source-hash-pinned global-plan construction and cover index for each candidate.

Common data are retained once, not replaced by newly independent records. All eight working candidates should be propagated through subsequent tests; the control family can be used for differential checks without reopening the selection decision.

## Verification

Policy: `contracts/su32-working-wiring-family-v1.json`.

```sh
node research/strominger/checkers/check_su32_working_wiring_family.mjs
```

Fresh execution passed source-hash validation, exact partition of all sixteen candidates, two-per-cover checks, rejection of an unknown class, and exact serialization recovery of placements, restrictions, records and central provenance.

No previous construction, native operation, physical interpretation or cyclic action was modified.
