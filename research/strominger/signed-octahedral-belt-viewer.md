# Separate process: two signed octahedral parents and the existing belt

Select **Octahedral pair + belt — ±P / ±N / ±E** in the normal-ray viewer's process dropdown (`signed-octahedral-belt`). The ESD7 assembly and its experimental P-first trim remain separate and unchanged.

## Construction

- Two copies of `buildPESymmetricSector(radius)`, not relabelled ESD7 tetrahedra.
- Each octahedral parent has three opposite signed boundary-port pairs: **+P/−P, +N/−N, +E/−E**.
- The same 34-cell staggered extended belt used in the ESD7 view is retained at unchanged unit edge length.
- Rigid parent placement puts the original parent's −E port and the second parent's +E port at opposite belt poles.
- Both contacts are checked against actual cell vertices. No shared facet is invented there.
- Wiring uses one node per native cell, ordinary shared-face adjacency, and two separately marked vertex-contact links. It is undirected.

**Scope of the split:** all three signed boundary pairs are explicitly represented. Their axis assignment is a declared convention. These port labels are not cell-role assignments: the native cells occupying the octahedral poles are octahedra, not fabricated E tetrahedra. No sign-dependent field transport, particle charge, or full-state duality dynamics has been derived. Native spatial P/E inversion is distinct from reversal of a signed port pair.

## Controls and counts

First selection defaults to parent edge length 5. Select edge lengths 1, 3, 5 or 7, switch Geometry/Wiring, and hide either parent or the belt independently. Size and process selection persist on reload. Counts remain whole-cell counts in both views; hiding geometry does not redefine the inventory.

| Parent edge | Combined P | Combined N | Combined E | Total |
|---:|---:|---:|---:|---:|
| 1 | 10 | 16 | 10 | 36 |
| 3 | 42 | 52 | 42 | 136 |
| 5 | 170 | 184 | 170 | 524 |
| 7 | 458 | 476 | 458 | 1392 |

At size 5, each parent has 80 P, 85 N and 80 E cells. The belt contributes 10 P, 14 N and 10 E. The assembled graph has 1,184 shared-face links and 2 tip-contact links, 1,186 total. These counts are not a Pb-208 claim.

Geometry displays exposed native P/E triangles. Octahedral fillers remain N nodes in Wiring. The signed labels mark the six actual macro-vertices of each parent; the old tetrahedral V-labels and ESD7 reference grid are not used.

## Checks

- `tests/signed-octahedral-process.test.mjs`: all four sizes, connected graphs, exact two pole contacts, six ports per parent, equal P/E inventories, native unit edges, visibility and settings registration.
- `scripts/test-neutron-belt.mjs`: dropdown selection, Geometry/Wiring, table, 12 signed labels, all sizes, visibility and reload, alongside regression coverage of the ESD7 assembly.
- `scripts/test-native-belt-publication.mjs`: existing published route and launch preset remain intact.
