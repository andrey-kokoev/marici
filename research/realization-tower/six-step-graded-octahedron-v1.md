# Six-step graded octahedron: first geometric test

## Proposal and tested interpretation

Operator proposal: select a lattice vertex, count six down, and take the two
positions as opposite vertices of a graded octahedron; conjecturally the
completed construction realizes Pb-208.

For this first test, a step means one FCC nearest-neighbour edge. The developed
region is the **graph interval**: all lattice vertices on shortest paths between
the endpoints. This is an explicit candidate interpretation of development,
not an assertion that a complete WG coherence rule has already been applied.
There are no particle roles or desired isotope counts in the construction.

## Exact result

Use the integer chart m in Z3 with even coordinate sum. The endpoints
(-2,0,0) and (4,0,0) are six graph steps apart. Their graph interval is exactly

    |x-1| + |y| + |z| <= 3, with x+y+z even.

It is a filled octahedral region, graded by distance from the first endpoint:

| Grade | Lattice vertices |
|---:|---:|
| 0 | 1 |
| 1 | 4 |
| 2 | 9 |
| 3 | 16 |
| 4 | 9 |
| 5 | 4 |
| 6 | 1 |

Totals:

- **44 vertices**;
- **168 elementary edges**;
- **32 regular tetrahedral cells**;
- **19 regular octahedral cells**;
- **400 shortest entry-to-exit paths**.

The cell volumes sum to the whole octahedron's volume, 36 in this chart:
32/3 + 19*(4/3) = 36. All 48 signed coordinate permutations preserve the
computed grades. Even-sum lattice translations preserve the construction as
well. The particular coordinate origin is not physically selected.

## What “down” distinguishes

Along a straight nearest-neighbour/root direction, the six-step endpoints
(0,0,0) and (6,6,0) instead have a graph interval containing only seven collinear
vertices. Thus six steps alone does not force an octahedron for every axis.

The octahedral-axis case above has six-edge shortest paths that move among
intermediate vertices; they are not one straight chain of six nearest-neighbour
edges. Its axis is a coordinate/octahedral axis in this chart, not one of the
twelve root directions. This distinction comes from enumerating the existing
lattice, not from imposing a physical preferred direction.

## Pb-208 status

The graded octahedron exists in the explicit graph-interval interpretation.
No proton/neutron assignment or complete coherence readout is provided by the
vertex/cell counts alone. This test neither derives 82+126 nor refutes a
further witnessed role construction. Five intermediate graph grades must not
silently be called five intervening tetrahedral cells.

An older [explicit Pb-208 loadout](../strominger/lead208-outward-chains-v1.md)
starts with assigned particle roles and records a marked-window incompatibility.
It is not evidence that the present endpoint construction derives Pb-208.

## Verification

```sh
python research/realization-tower/check_six_step_octahedron.py
```

Fresh result: **PASS**, using integer enumeration. The
[receipt](results/six-step-octahedron-v1.json) contains every vertex and each
complete tetrahedral/octahedral cell for reuse by a later viewer or closure test.
No earlier viewer, graph proof status or glossary definition was changed.
