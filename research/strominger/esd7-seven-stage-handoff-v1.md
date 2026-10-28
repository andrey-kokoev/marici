# esd7: recovered seven-stage blocks, central flags and signed chart handoff

Search aliases: coherence pyramid, esd7, esd_7(Delta^3), seven-stage block, convolution-depth profile, quarter-turn handoff, central cell.

## Fresh extraction from the actual prior layout

Input: `research/voevodsky/results/esd7_explicit_analytical_census.json`. The checker reads that existing file without modifying other owners' artifacts. It reconstructs signed boundaries and the documented cyclic barycentric action

    rho(a1,a2,a3,a4) = (a4,a1,a2,a3).

All1807 cells are present:120 vertices,560 edges,784 faces,343 tetrahedra. Every cell has a valid rotated image. Signed boundary naturality and boundary-squared-zero hold throughout; four rotations restore every oriented cell.

## A seven-presentation central passage exists

The central tetrahedron is **T184**, with vertices given by the four permutations of (1,2,2,2). Its centroid is exactly (7/4,7/4,7/4,7/4).

Take a complete flag vertex < edge < face < T184, and the rho-rotated flag. Join the first ascending flag to the descending rotated flag, sharing T184 once. One actual extracted instance is

```text
V051 -> E270 -> F403 -> T184 -> F538 -> E368 -> V072
  1       2       3       4       3       2       1
```

The lower row is simplex dimension plus one. All six adjacencies exist in the census. No new cells were invented. There are24 such bridges, one per ordered vertex flag; rho preserves the entire family.

This is a concrete incidence realization of the proposed **3+1+3 with a shared depth-four center**. Identifying that incidence rank with convolution depth is the next binding, not an output of geometric enumeration.

Important distinctions for implementation:

- Seven cell presentations give six between-cell incidence transitions. The stage law must specify whether a stage evaluates a presentation or traverses an arrow.
- The endpoints here are vertices of the central cell, not outer tetrahedron corners.
- The descending leg records reverse incidence. It is not permission to invert a noninvertible analytical inclusion; use the actual contravariant/fibration or comparison interface.
- T184 is fixed setwise by rho, with orientation sign -1. Signs must travel with the chart action; this chart permutation is not being called a rigid proper spatial quarter-turn.

## Seven-edge conductor blocks also exist, but are a different object

The four boundary conductors run successively between the outer corners 1->2->3->4->1. Each has eight vertices and seven actual edges. Rotation maps every oriented step to the corresponding step of the next conductor. The four conductors concatenate into a28-edge boundary loop.

Their middle edges and vertices do not pass through T184. Therefore that loop cannot simply be renamed the proposed center-to-vertex trace. This is why the checker locates both structures rather than selecting a path by its count.

Also, incidence naturality maps an edge's source to its rotated source and its target to its rotated target. Concatenating paths by shared endpoints is not by itself the full-state handoff at the end of a block.

## What is now executable

The output retains:

- actual IDs and oriented edges for all four conductor blocks;
- incident faces for each conductor step;
- all24 seven-presentation central flag bridges;
- central-cell faces and their signed boundaries;
- source and checker hashes.

The tested geometric form of the chart law is the signed chain equality

    boundary rho_* = rho_* boundary.

The existing universal-category law q u=rho(u)q and q^4=Sigma provides the presentation-level target. This new check does not independently prove its analytic realization or the P/E readout.

## Next precise test

The subsequent [FCC-first adapter](fcc-first-sector-transport-v1.md) recovers the full S4-covariant tetrahedral/octahedral carrier and retains the esd7 split as frame-dependent presentation data. It names all224 actual comparison faces relating subdivision diagonals to two-root transport paths. Use this ambient transport before choosing the subdivided chart.

Use the central flag bridge, not the outer boundary loop, as the first depth-profile candidate. Bind its ascending/descending incidences to the existing fibration/reciprocal maps and retain the actual face comparison records. Test whether the resulting7 presentation updates supply the next rotated block's whole-state input. Then connect the local central vertices to the outer E-vertex presentation through the existing cone/reader data, rather than identify them by name.

## Reproduction

```sh
python research/strominger/checkers/check_esd7_seven_stage_handoff.py
```

**19 exact checks pass**, including all-cell signed rotation naturality and the24 central bridges. Receipt: [esd7-seven-stage-handoff.json](results/esd7-seven-stage-handoff.json).

## Prior source entry points

- [Recovered layout and analytical prototype registry](esd7-coherence-layout-recovery.md).
- [Complete analytical coverage ledger](../voevodsky/eight-node-lattice-analytical-form-coverage-ledger.md).
- [First elementary tetrahedron: six edges, four faces, one higher equation](../voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md).
- [Four-chart helix and incidence compatibility](../voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md).
- [Full graded realization](../nima/full-esd7-graded-tate-torus-realization.md).
