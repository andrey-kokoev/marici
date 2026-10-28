# Surface N cells and connected filler voids

The single edge-7 octahedron already contains 146 surface N octahedra. The former P/E-only face-orientation colouring concealed their owning cell type. **P / N / E cell roles** is now the default surface colouring in this process; **P / E face orientations** remains selectable as reference. This changes the displayed readout, not the lattice or cellulation.

The exposed boundary has 392 triangles:

- By native triangle orientation: 196 P, 196 E.
- By owning cell: 84 P, **224 N**, 84 E.

White N faces visualize the boundaries of N regions; they do not assert those volumes contain occupied material. Thick white native-cell borders remain enabled.

## Void counting hypothesis

For this experiment, treat P/E cell interiors as occupied and N octahedra as empty. Connect two empty cell interiors only across a complete shared triangular face (a positive-area passage). Edge/vertex contacts are measured separately and are not silently used as volumetric openings.

Actual result:

| Measure | Count |
|---|---:|
| Empty N cells | 231 |
| Shared N–N faces | 0 |
| Empty regions restricted to the carrier | 231 |
| Enclosed filler voids | **85** |
| Surface-opening regions within the carrier | 146 |
| Components if edge-touching closures are joined | 1 |
| Components if vertex-touching closures are joined | 1 |

All 146 surface openings communicate through the unbounded exterior. If exterior space is included, there are **85 bounded cavities plus one exterior component**. The exterior is not counted as an additional neutron cavity.

Thus counting contiguous open filler volumes gives 85 for this geometry, but this equality with the old interior-octahedron count is now checked, not assumed. The N cells touch along edges but lack open shared-face passages. Changing the connectivity convention to closed-set touching yields a very different answer (one touching network), so the convention is visible in the UI.

The table retains separate whole-cell, surface/interior-cell, void-region, native-face-orientation and face-owner readouts. These are not additive inventories. No neutron particle count is inferred merely by identifying an empty cavity.

## Verification

`tests/native-empty-regions.test.mjs` checks the actual 85/146 partition and edge-contact diagnostic. A counter-test empties the P/E separators in a small native sector: shared-face passages then merge all 51 cells into one open volume. `tests/single-octahedral-process.test.mjs` and the viewer browser checks verify N-owned surface colouring, reference-mode switching and the new table rows.
