# Collective P*/E* comparison cell

In **12x12 fibration**, state 49 follows operator application (47) and reconstruction confirmation (48). It creates a composite carrier record and marks its existing boundary port **P*** on the opposite sheet or **E*** on the original sheet. Previous removes this comparison record without changing the tiling.

## Construction

`../realization-tower/collective-pair-cell.mjs` finds the minority sector directly from the folded geometry: positive-sheet E / negative-sheet P. Its 36 members are connected by 121 neutral-mediated links and have exactly one exposed member cell. The construction rejects a missing or non-unique exposed member, or a disconnected sector. The visible marker uses that member's existing center, not an invented extra tetrahedron.

The comparison cell stores all member IDs, mediating neutral cells, the averaging row (36 unit numerators / 36), and 35 anchor contrasts. For scalar member coordinates x_i, retain S = sum x_i and d_i = x_i − x_0. Recover x_0 = (S − sum d_i)/36 and x_i = x_0 + d_i. Apply componentwise to all five complex coefficients. These are symbolic member coordinates: no independent native 36-site excitation or numerical native member field is asserted. Tests of every basis vector verify the reversible coordinate change.

## Counts and limits

The new external-comparison rule replaces the 36 minority readings by one, while retaining all original geometry and internal coordinates:

| Comparison sheet | P | N | E | Carriers |
| --- | ---: | ---: | ---: | ---: |
| Original | 81 | 58 | 1 | 140 |
| Opposite | 1 | 58 | 81 | 140 |

Thus **81 + 1 = 82 external P readings**, and likewise 82 E readings. These are dual-labelled shared carriers, not 164 independent charged particles. The N rows are linked and are not summed. The viewer retains the raw geometric counts alongside these effective counts: **175 cells = 119 tetrahedra + 56 octahedra**. No physical 82nd P tetrahedron is claimed.

The 36→1 collective-carrier rule is an additional declared coarse-graining, **not a consequence of the 4×4 operator Q**. The fourteen filler directions are not the 35 internal contrasts here, and are not added to N counts. This implements a visible, information-retaining comparison cell, not a native geometric particle realization or Pb-208 derivation.

Verification: `tests/collective-pair-cell.test.mjs`, `tests/filler-viewer-process.test.mjs`, and `scripts/test-fibration12-process.mjs`. Browser checks cover materialization, both displayed labels, counts, reload, backward stepping, and restart. Screenshot: `results/fibration12-viewer/collective-cell.png`.
