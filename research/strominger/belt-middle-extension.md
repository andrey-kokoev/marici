# Native staggered middle extension

## Construction

The Geometry-view belt now has **64 exposed unit triangles: 32 P + 32 E**. This is a count of boundary faces, not cells, directed sides or wiring nodes.

`research/realization-tower/belt-middle-extension.mjs` starts from the original 14-cell native octahedron. Let d be its chosen opposite-vertex displacement in the integer barycentric lattice. Its coordinates comprise two +1 and two −1 entries. Split d into two complementary sum-zero nearest-neighbor steps u and v using the first positive and negative coordinate indices for u, with v=d−u.

Take the union of three complete native blocks translated by 0, u and −v. Deduplicate cells and faces by their actual native vertices. Rigidly recenter at the midpoint of the two extreme poles. The end block centres then lie half a pole displacement on either side of the axis midpoint. The middle block supplies an explicit stagger phase; it is not replaced by a fitted prism, and the choice is not claimed unique.

This produces:

- 20 tetrahedra and 14 whole octahedra: 34 cells;
- 37 total vertices, 130 edges, 128 distinct triangular faces;
- 64 internal faces and 64 exposed faces;
- boundary: 34 vertices, 96 edges, Euler characteristic 2;
- exactly 32 P and 32 E exposed faces under the existing native tetrahedral-orientation color rule.

The earlier belt had 16 P + 16 E boundary faces. The extension therefore adds 16 of each. A different trial using straight full-pole translations −d,0,d gave 40 P + 40 E; it was not selected.

## Presentation and scope

The existing two E replacement tips touch the extended belt poles. Parent translation is now 1.5√2 native edge lengths from the reference N-tip position, keeping both contacts while preserving cell sizes. Rays remain absent. Geometry uses the extension; the 64-node wiring diagram is unchanged, and no new face-to-wire transport map is inferred from matching cardinalities.

The N-sector face convention remains separate from parent cell-role accounting. No combined P/N/E total, Pb-208 identification, mechanical stability or field law is established by this extension.

## Verification

`tests/belt-middle-extension.test.mjs` checks lattice coordinates, source-template translations, whole-cell deduplication, connected face adjacency, oriented boundary incidence, counts and preservation of source records. `tests/belt-wiring-layout.test.mjs` checks unit edges, unchanged parent geometry, pole-axis alignment, exact E-tip contact and opposite-half-space separation. `tests/pne-inventory.test.mjs` checks that the table counts the 64 exposed faces, not the 128 distinct faces or the 34 supporting cells. The public browser test checks the displayed count row and extension audit.
