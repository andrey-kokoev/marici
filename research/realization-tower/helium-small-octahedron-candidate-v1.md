# Helium candidate: smallest octahedral interval

At the operator's request to try helium first, test the smallest nondegenerate
octahedral graph interval. The choice of two nearest-neighbour steps is a
minimal geometric trial, not an operator-specified helium size or an isotope
fit. Particle roles are not assigned in the construction.

In the even-sum integer FCC chart, take entry (0,0,0) and exit (2,0,0).
Their shortest-path interval has grades **1,4,1**:

- entry: (0,0,0);
- intermediate square: (1,-1,0), (1,0,-1), (1,0,1), (1,1,0);
- exit: (2,0,0).

Each intermediate site is one step from both entry and exit. The four sites
form a square cycle. The full complex is one regular octahedral honeycomb
cell: **6 vertices, 12 edges, 8 triangular faces**. It has four shortest
entry-to-exit paths of length two, no complete tetrahedral honeycomb cells
inside it, and no FCC vertex at its geometric centre (1,0,0).

The four intermediate sites are vertices, not four tetrahedra or four already
identified nucleons. Reading them as a helium-4 nucleus would additionally
require the two-proton/two-neutron roles and the witnessing/completion rule.
No electron assignment is made by selecting the two poles.

## Size comparison, not isotope assignment

| Graph steps | Grades | Vertices | Tetrahedral cells | Octahedral cells |
|---:|---|---:|---:|---:|
| 2 | 1,4,1 | 6 | 0 | 1 |
| 4 | 1,4,9,4,1 | 19 | 8 | 6 |
| 6 | 1,4,9,16,9,4,1 | 44 | 32 | 19 |

These are all shortest-path intervals along octahedral axes. As in the earlier
six-step test, a straight root-direction interval instead degenerates to a line.
The role/readout question is separate from the verified interval geometry.

## Verification

`python research/realization-tower/check_small_octahedra.py` freshly passed.
The checker verifies interval membership, neighbour incidences, grade counts,
cell enumeration and total cell volume. It separately checks the four-site
cycle and its adjacency to both poles.

[Exact receipt and coordinates](results/small-octahedra-v1.json).
No prior proof outcomes or glossary definition changed.
