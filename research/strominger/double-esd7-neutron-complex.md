# Neutron-corner neighbourhood inspection

Reproduce: `node scripts/analyze-double-esd7-neutron-complex.mjs`.
Machine-readable output: `results/double-esd7-neutron-complex.json`.

Uses the four-rule completed double ESD7 (114 P, 124 N, 112 E). No cell assignments are changed.

## Metric and seeds

Grow breadth-first neighbourhoods from the two +N corner cells and, separately, the two −N corner cells. These are four distinct cells at two shared geometric vertices, not four neutron vertices.

Distances here count shared-facet links in the geometric cell graph. This is an inspection metric, **not propagation word length**: the process's zero-move interface identification is not counted as a particle transition or used to merge geometric cells.

## Results

- Minimum +N-to−N distance: 12 shared-facet links.
- Equal-radius fronts first overlap at radius 6.
- First overlap: four tetrahedra, **2 P + 2 N**, no E.
- Union of all shortest connecting paths: **36 distinct cells**, comprising **22 P + 14 N**, no E.
- Those 36 cells consist of 24 tetrahedra and 12 octahedra.
- The 12 octahedra on the shortest-path union are all P. Their complete face-neighbour signatures are 2P/3N/1E (four octahedra) or 3P/3N/1E (eight).

| Radius | New shell from either N corner (P/N/E) | Overlap (P/N/E) |
|---|---|---|
| 0 | 0 / 2 / 0 | 0 / 0 / 0 |
| 1 | 2 / 0 / 0 | 0 / 0 / 0 |
| 2 | 2 / 4 / 2 | 0 / 0 / 0 |
| 3 | 4 / 2 / 0 | 0 / 0 / 0 |
| 4 | 6 / 6 / 6 | 0 / 0 / 0 |
| 5 | 6 / 6 / 0 | 0 / 0 / 0 |
| 6 | 12 / 8 / 12 | 2 / 2 / 0 |

## Interpretation limits

Enumeration finds no three-link cycles. Within a half the links alternate tetrahedra and octahedra; the seam also has tetrahedron–tetrahedron links. That does **not** exclude larger triangular arrangements of cells; it means that a triangular complex needs an explicit geometric definition beyond a graph triangle.

The computed connection is an electron-free corridor between the neutron vertices, not yet evidence that it should count as a neutron or that cells should be removed from the particle tally. No Pb-208 correction is inferred.
