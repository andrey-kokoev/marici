# Charged-face grouping test on the current belt assembly

Active obligation: candidate readout grouping of retained exposed-face records. This bounded geometry test does not resolve an upstream native field-transport map or certify particle readout descent.

## Fixed inputs and rules

Use the current two native-cellulated parents, two explicit E-tip replacements, the staggered extended belt, and actual Geometry-view tip contacts. Retain every exposed face's identifier, role, vertices, cell owner and shape. Do not count interior faces. The inventory is 250 P faces, 206 E faces and 126 whole octahedral fillers.

Three rules are tested without changing them to fit a target:

1. Same-role faces joined transitively by a complete shared edge.
2. Same-role faces joined transitively by any shared vertex, including existing tip contacts.
3. Same-role faces with the same native cell owner. This rule may group disconnected faces; it is an owner quotient, not a connected-patch claim.

## Result

| Rule | P groups | E groups |
|---|---:|---:|
| Shared edge | 176 | 194 |
| Shared vertex | 3 | 1 |
| Same native cell | 167 | 127 |

**None gives 82 P and 82 E for the assembly.** The 126 filler count is unchanged because this test groups only P/E boundary records.

The shared-edge result decomposes as follows:

| Shape | P groups | E groups |
|---|---:|---:|
| Original parent | 73 | 82 |
| Second parent | 73 | 82 |
| Belt | 30 | 30 |

Each parent's 82 E groups is a local clue, not a global result: both parents and the belt remain present, and the same rule does not give 82 P. On each parent, one E group contains six faces and the other 81 groups are single faces. There is no edge adjacency across the vertex-only parent/belt contacts.

Under vertex adjacency all 206 E faces connect through the E tips into one group. This demonstrates how strongly the answer depends on the proposed adjacency rule; point contact cannot simply be treated as an unexamined particle identification. P has one vertex-connected component per shape.

## Verification and reproducibility

- Checker: `node research/strominger/checkers/check_belt_charged_face_components.mjs`.
- Complete face records, component membership and ownership: add `--full`.
- Regression: `node --test tests/belt-charged-face-components.test.mjs` (2 passing tests).
- Each rule partitions all 456 exposed faces exactly once, preserves role and cell-owner provenance, and has identical counts at coordinate-key precisions 1e-6, 1e-8 and 1e-10.

No viewer geometry, count table, source roles or particle assignments were changed. The next stronger proposal needs a source-defined grouping/identification or transport law; connectedness alone has not produced the Pb-208 charged inventory. These results exclude only the three tested conventions, not every possible grouping.
