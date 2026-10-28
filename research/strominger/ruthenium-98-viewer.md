# Ruthenium-98 viewer process

Choose **Ruthenium-98** in the Process panel. The viewer follows Sulfur-32's native whole-cell presentation, on the five-unit tetrahedral carrier.

- **Geometry:** 65 retained native cells; render only their 100 carrier-boundary triangles, with native cell-role colours and the same white cell borders as Sulfur-32.
- **Wiring:** all 65 cell-centre nodes and 120 actual shared-face links.
- No outward-chain stage or appendages. Old saved extension stages normalize to stage zero. The view selector persists independently of Sulfur-32.

The carrier contains 35 tetrahedra of P orientation, 10 of E orientation, and 20 octahedra. The P/N/E inventory table counts the retained Ru assignment: **44 P, 54 N, 44 E**, total **142**, derived from its records. The table is labelled “Ruthenium-98 inventory”; its note distinguishes those records from the displayed carrier geometry.

`buildRuthenium98Carrier()` supplies the viewer geometry. `buildRuthenium98()` supplies the inventory records: 44 P sites, ten N witnesses, 44 N connectors and 44 E endpoints. Its outward extensions are not rendered. Both Geometry and Wiring retain the same Ru inventory.

- Model: `../realization-tower/ruthenium-98-model.mjs`
- Process: `../realization-tower/ruthenium-98-process.mjs`
- Tests: `../../tests/ruthenium-98-process.test.mjs`

```sh
node --test tests/ruthenium-98-process.test.mjs tests/sulfur-32-process.test.mjs
node scripts/prepare-native-belt-viewer.mjs
node scripts/test-ruthenium-98.mjs
node scripts/test-sulfur-32.mjs website/public/experiments/native-belt/index.html
```
