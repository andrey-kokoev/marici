# Sulfur-32: empty handlebody view

In the Process panel choose **Sulfur-32 → View → Handlebody — empty tubes**.

The view thickens the actual native shared-face incidence graph:

- 19 N-cell locations become chambers;
- 32 P/E-cell locations remain neutral junction spaces, without role colours;
- 104 actual shared-face connections become necks;
- six boundary mouths attach at the original N tips.

No wires, signed pair assignments, arrows or payloads are displayed. Matching rim colours retain the three opposite-tip identities. Those identities are not rendered as tubes cutting through the carrier. The earlier periodic seam comparisons are also excluded from the spatial tube body.

This is a schematic regular-neighborhood presentation of the retained incidence graph, not a selected six-pair routing or a newly derived physical tube cross-section. Chamber and neck radii are display parameters. The graph remains independent of the process stage and P|E reading. Existing geometry, wiring and history records are unchanged.

## Surface and controls

A single marching-cubes union surface joins the chambers and necks, rather than overlapping transparent cylinders with internal end caps. Six extended terminal caps are clipped at the mouth planes. The skin encloses an empty connected space; no solid cell interiors or wire meshes are drawn. Cell-face opacity controls the skin opacity. Geometry and Wiring views remain available, and the view choice survives reload.

The uncut sampled skin has 20,670 welded vertices, 62,328 edges and 41,552 triangles. Every edge has two oppositely oriented incident triangles; the mesh is connected. Its Euler characteristic is −106, matching the native incidence graph's cycle rank 54 before the six mouth cuts. The test uses the current 96-grid presentation and six-decimal vertex welding; this is a finite mesh check.

## Files and verification

- Carrier: `../realization-tower/sulfur-32-handlebody.mjs`.
- Surface renderer: `../../examples/normal-ray/sulfur-handlebody-renderer.js`.
- Tests: `../../tests/sulfur-32-handlebody.test.mjs`.

```sh
node --test tests/sulfur-32-handlebody.test.mjs tests/sulfur-32-process.test.mjs tests/single-octahedral-process.test.mjs
node scripts/prepare-native-belt-viewer.mjs
node scripts/test-sulfur-32.mjs website/public/experiments/native-belt/index.html
```

Ten tests pass. Browser checks cover empty-view rendering, six mouths, absence of wire tables and particle inventory, reload persistence, and return to the unchanged wiring stage/direction. Both research and locally built public viewer assets were rebuilt; no remote deployment was performed.
