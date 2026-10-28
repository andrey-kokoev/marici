# Trace of parent branch/return structure toward L1

## Scope correction after prior-work search

See `belt-parent-fibration-prior-search.md`. Existing marked sector-table fibration already supplies twelve directed rows grouped into four triples, with shared whole-state data and retained histories. The geometric ancestry overlap below does not obstruct such a four-fiber presentation. It only rejects treating the first four BFS branches as disjoint geometric feeds. The constructor-to-table and full-packet transport machinery must be reused when investigating the actual belt attachment.

## What was traced

`buildFoldedFibration()` constructs outward and return breadth-first admission histories from actual shared whole faces. These are incidence/confirmation traversals, not a supplied physical flow law. The trace follows their recorded witnesses, without assigning rates or importing the displayed star layout.

For each parent, start at its external P endpoint (`original:tet-88` or `clone:tet-88`) and use the traversal directed toward the former shared seam. The first round reaches one neutron-role octahedral mediator. The next round contains four tetrahedra:

| Source geometry | Source particle role | Reachable seam faces |
|---|---|---:|
| tet-41 | electron | 49 |
| tet-86 | proton | 36 |
| tet-87 | proton | 36 |
| tet-103 | proton | 36 |

The same source-geometry identities occur on both parents. Their roles are source labels, not assignments of sector-space P/E flux.

## Four early roots do not partition the boundary

Already in the following round, three octahedra each have witnesses from two roots: the common tet-41 root and one of the other three. Propagating root ancestry to the 49 seam faces gives, on each side:

- 6 faces reachable from two roots;
- 27 reachable from three roots;
- 16 reachable from all four roots;
- no face reachable from only one root.

Thus the first four-way split is not four disjoint geometric feeds that can simply be identified with the four L1 stars. It is an overlapping common-plus-three incidence pattern. This is a reachability statement, not a claim that the common mode or three contrast modes have been derived. Merging paths does not prove dependence of full fibers; independent branch/history labels may still be retained.

Both existing traversals cross all 49 former seam faces, with exactly reversed owner pairs and shared-face witnesses. There is therefore a real bidirectional structural route to inspect, rather than a need to invent geometric parent connectivity. The traversal still supplies neither numerical transport rates nor a boundary fiber map.

## Implication for attachment

The simple identification “four first branches = four L1 stars” is unsupported. A fiber adapter could exist, but it must explicitly retain overlapping path histories and provide a justified map to the four displayed stars. One may not partition the faces arbitrarily and call that an inherited native construction.

The unrelated four-depth × four-comparison-slot filler is algebraic: `four-by-four-filler-v1.md` explicitly distinguishes its slots from physical particles and geometric boundary maps. The four N occurrence complexes likewise comprise two seed occurrences per parent, not four equivalent star feeds per parent (`four-neutron-occurrence-complexes.md`). Neither supplies the missing identification.

No parent wiring or geometry was changed.

## Reproduce

- `node scripts/trace-belt-parent-branches.mjs`
- `node --test tests/belt-parent-branch-trace.test.mjs`
- Receipt: `results/belt-parent-branch-trace.json`

Tests verify early witness faces against both owning cells, the exact overlap histogram, the parent source-geometry correspondence, and all 49 reversed seam crossings.
