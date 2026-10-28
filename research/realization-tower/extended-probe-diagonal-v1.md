# Extending the probe diagonal by one lattice-axis unit

## Specified extension

Operator confirmed extending entry/exit poles from (0,0,0)–(2,0,0) to
(0,0,0)–(4,0,0). The increment (2,0,0) is the next FCC vertex spacing along
this octahedral axis. It increases nearest-neighbour graph separation from
two to four steps. (3,0,0) would not be an FCC vertex in this chart.

This extends the **point-pole experiment**, not the positions of the six
retained tetrahedral particle carriers. Those are distinct probe interfaces.

## Compare-first continuation search

Each pole has twelve first channels. For every depth h=1,2,3, enumerate h-edge
walks from each pole, keeping their first channel and whole path. Each of the
144 first-channel comparison slots matches coincident codomain endpoints.
A slot may carry multiple endpoints and multiple path-pair witnesses.

| Depth from each pole | Comparison slots | Matching slots | Distinct meeting vertices | Joined walk witnesses |
|---:|---:|---:|---:|---:|
| 1 | 144 | 0 | 0 | 0 |
| 2 | 144 | 16 | 9 | 36 |
| 3 | 144 | 96 | 53 | 6,840 |

First meetings appear at depth two per side: **one additional level from each
probe**, or two extra edges in the combined entry–exit path. The two-extra-level
budget is sufficient, but depth three is not needed for the minimal connection.

## Recovered region

Joining all matching depth-two paths produces exactly 36 distinct shortest
entry–exit paths. Their union equals the independently defined four-step graph
interval, with grades

    1, 4, 9, 4, 1.

The region contains 19 lattice vertices, 8 primitive tetrahedral cells and
6 octahedral cells. The cells are the full geometric interval's honeycomb
cells, not automatically proton/neutron/electron roles.

Thus the compare-first method recovers the same minimal geometric region as
the graph-interval construction in this case, rather than assuming that region
before searching. At depth three, six-edge joined walks include detours and
backtracking; their matches must not all be relabelled as minimal completion.

## Scope and next gate

The need for deeper continuation with larger separation survives this test.
The number of outer comparison slots remains 144 while the number of retained
witnesses grows. No coefficient matching, arbitrary domain-to-codomain map,
particle census or complete higher-coherence filler was supplied by this
incidence calculation.

The next separate question is which matched path families admit the intended
coherence witnesses and which actual tetrahedral carrier roles they induce.
No atomic species is assigned from the cell count.

## Verification

`python research/realization-tower/check_extended_probe_diagonal.py` freshly
passed. It verifies the absence of one-step matches, exact depth-two meetings,
all 36 shortest paths, equality of their union with the full interval, and the
retained size distinction at depth three. Cell counts are cross-checked against
the earlier exact small-octahedra receipt.

[Full receipt, 144-slot tables and depth-two paths](results/extended-probe-diagonal-v1.json).
