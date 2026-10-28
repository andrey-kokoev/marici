# Native neutron node-count audit

The 1050-cell viewer belt was introduced by `refined-neutron-belt.mjs`: six copies of an entire 175-cell ESD7 subdivision. That resolution choice is not supplied by the prior neutron construction and is not evidence for its native node count.

Direct incidence enumeration from `research/voevodsky/results/four_six_center_cones.json` gives:

| Object | Count |
| --- | ---: |
| Rim vertices (two triples) | 6 |
| Center vertex | 1 |
| Total geometric vertices of cone complex | 7 |
| Geometric edges | 18 |
| Distinct triangular faces | 18 |
| Tetrahedral cones / cell-dual nodes | 6 |
| Shared-face dual links | 6 |
| Boundary triangular faces | 12 |

The six shared-face pairs, with source zero-based cone indices, are `(0,4), (0,5), (1,3), (1,4), (2,3), (2,5)`. Thus the native cell graph is C6. Its source grouping is three adjacent pairs, or 3 × 2 cells, not 32 cells.

The distinct surface coefficient construction splits each of the six outer triangles into three centroid-edge patches. It has 12 surface vertices, 18 small triangles and 24 shared-edge adjacency links. Its 36 intrinsic coordinates are two axes per small triangle, not 36 volumetric cells. The 1836 protocol transfers are not geometric graph edges.

No 32-node belt construction was located in the searched neutron/belt research. This does not establish that no such alternative exists; it does rule out attributing that count to the inspected source. The source does not require copying a resolution-7 complex into each cone.

Fresh verification: `python research/strominger/checkers/check_neutron_real_complex_arrows.py` passes all 20 controls. The separate incidence enumeration above reconstructs faces and edges from the stored tetrahedral vertex lists.

Viewer unchanged during this audit. Before replacing its over-refinement, distinguish rim-edge attachment of the native six-cell carrier from a conforming full-face lattice insertion: the existing attachment is rim-based. Do not silently equate these incidence contracts or claim that removing refinement supplies a new propagation law.
