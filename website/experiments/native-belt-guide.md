# Native N-cut belt: geometry and wiring

**[Open the full-screen viewer](/experiments/native-belt/index.html?preset=native-belt)** · [Ledger entry 4331](/research/ledger/20261025-4331-native-n-cut-belt-docking-and-separate-wiring-views/) · [Viewer gallery](/experiments/)

The launch link selects the double-ESD7 belt assembly in Geometry view. The workbench also contains other construction processes; they are separate experiments. Assets are bundled locally; WebGL is required for the interactive scene.

For Be-8/Be-9, cellulation, NNPE composition, hex strands and other modes in the same app, use the [construction workbench directory](/experiments/construction-workbench). Those modes have separate source contracts; this page documents the belt only.

## Read the two views

- **Geometry:** the two former N-tip locations carry E-assigned tetrahedra with thick white borders. Their tips touch the opposite tips of an axially aligned, extended belt. Its staggered middle extension uses **20 tetrahedra and 14 whole octahedra**. This is vertex contact, not the earlier reference face docking.
- **Wiring:** one node per whole native cell: **350 parent nodes + 34 belt nodes = 384**. There are **792 shared-face links + 2 separately marked tip-contact links**. Links are undirected; the historical 64-arrow port diagram and two terminal markers are no longer the displayed wiring. Diagram expansion does not change connectivity or imply geometric lengths.
- **Colors:** opaque P/E fills follow the native tetrahedral-orientation convention. Thick white triangle borders mark the declared inside-N / N-less sector. Neither convention supplies a field-transport law.

Select **Geometry** or **Wiring** with the shape-view control. Toggle either parent, the connecting belt, ESD7 planes or the nine native belt cell-centre planes independently (1, 4, 4, 6, 4, 6, 4, 4, 1 nodes). Drag to orbit; use the camera controls for zoom and view direction. V-labels follow the displayed vertices with screen-space clearance and leader lines. Click a visible V-label to fix or release a rotation anchor. V₁, V₂ and V₇ labels are hidden in both belt views because they sit inside the belt.

The viewer retains settings on reload. Opening the launch link above explicitly reselects the belt preset; it is removed from the address after initialization so ordinary reload preserves subsequent view changes.

## What is checked

- Extended belt boundary: **34 vertices, 96 edges, 64 triangles: 32 P and 32 E faces**. Internal faces are excluded.
- Native construction: three translated, overlapping template blocks are deduplicated into 34 whole cells. Complementary lattice steps fix one explicit stagger phase; this is not a uniquely selected extension.
- Each parent has 174 retained positions plus one E replacement at its former N tip. Original N records remain retained separately.
- Native unit edges, connected cell adjacency, closed oriented boundary, tip coincidence and separation of parents from the belt are checked. The earlier 14-cell, 32-face belt and its face-docking check remain reference data.
- Both main shapes use the same native face-coloring and whole-octahedron convention as the belt; each has 119 tetrahedra and 56 octahedra.
- The table has three rows: parents, belt and combined total. **Geometry** counts exposed P/E faces and whole octahedral N fillers: **250 P, 126 N, 206 E**. **Wiring** counts whole-cell nodes: **176 P, 126 N, 82 E**. These are different declared readouts, not interchangeable particle inventories. Explicit E-tip overrides are included; visibility masks do not alter the table totals.
- Face-color coverage, unchanged graph connectivity under diagram expansion, visibility controls and label positioning.

## What remains open

Geometric gluing does not establish native field transport, a global lattice-phase registration, mechanical stability, a particle identity or a binding energy. Shared-face adjacency and point contact do not supply directed field maps. The historical port diagram remains available as reference code, not the current native wiring. The earlier intact-parent face-normal obstruction remains valid; the single-tip cut changes the attachment boundary.

[Construction and test packet](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/belt-parent-gluing.md) · [Source viewer](https://github.com/andrey-kokoev/marici/tree/main/examples/normal-ray) · [Label mechanics](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/vertex-label-positioning.md)
