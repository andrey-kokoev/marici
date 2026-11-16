# Isotope wiring: validation and export limits

[Return to the editor](/experiments/isotope-wiring) · [Separate 3D workbench](/experiments/construction-workbench)

The hosted editor embeds `examples/isotope-wiring/index.html`. Its counts, delta compiler and File operations belong to the legacy implementation. The independent structural machinery described below is pending local development, **not connected to the visualization** in this publication checkpoint. A valid definition or matching inventory does not establish nuclear geometry or isotope stability.

## Legacy failures and precautions

| Case | Retained failure | Precaution |
|---|---|---|
| Replay an identity delta | An empty identity delta can select the mutable registry definition rather than reconstruct the supplied snapshot. | Retain an independent absolute snapshot and test the actual replay. |
| Base-only metadata | A graph projection can match while base-only metadata survives reconstruction. | Inspect the entire definition, not just its graph records. |
| Coordinate IDs | Coordinates `(1,10)` and `(11,0)` can produce the same concatenated identifier. | Do not assume generated IDs uniquely identify larger-shell coordinates. |
| Mutable base | Changing a mutable base can change a compiled target without changing the saved delta. | Keep the actual base and its provenance, not merely its name. |

The identity-delta, base-only metadata and coordinate-ID cases are unresolved regression requirements at this checkpoint. **TODO failures are not passes**. A successful process exit with expected TODO failures does not certify those requirements as repaired.

Retain project exports and **absolute definitions** outside the app before editing. Compare metadata as well as graph records. This is a caution, **not a certified persistence or roundtrip guarantee**; displayed counts and an unchanged drawing are not a backup test.

## Independent machinery is not editor integration

The inspected pending local development includes the following headless layers. Their paths are provenance locators, not stable public APIs; these files may be absent from a clean checkout of the published revision.

| Layer | Implemented local scope | Remaining boundary |
|---|---|---|
| `core/finite-diagrams.mjs` | Checked finite-incidence diagrams, structural maps and bounded incidence constructions. | This is not a formal proof of implementation correctness or model validity under arbitrary composition. |
| `core/legacy-adapter.mjs` and attributed adapter | Structural import and retained-source recovery. | Recovery retains the original source; it is not an inverse of bare incidence or an exporter for modified/glued diagrams. |
| `core/model-predicates.mjs` | Explicit model predicates with verified/refuted/unknown/notApplicable findings. | Z/N and shell data are supplied targets, not derived observables. Model-valid objects are not composition-closed under the tested gluing. |
| `core/revisions.mjs` | In-memory revisions, explicit ground rewrites, before-image undo and dependency-complete bundle replay. | Browser autosave and legacy delta compilation do not use this revision engine. Generic matching, cross-engine migration and selective evidence transport remain separate. |

The local `examples/isotope-wiring/MACHINERY.md`, `core/CLOSURE.md`, `core/ADAPTER.md`, `core/MODEL.md` and `core/REVISIONS.md` discuss these boundaries. They are not linked as though committed public dependencies. A source fixture can retain unresolved placement despite passing predicates; no software result here derives experimental nuclear content.

## Reproduction and verification scope

In a development checkout containing the pending suites:

```sh
node --test tests/isotope-wiring-core.test.mjs
node scripts/test-isotope-wiring-website.mjs
node --test tests/isotope-wiring-category.test.mjs tests/isotope-wiring-adapter.test.mjs tests/isotope-wiring-model.test.mjs tests/isotope-wiring-revisions.test.mjs
```

At the publication audit checkpoint, the legacy suite had seven passing checks and three expected TODO failures. The four independent machinery suites had 51 passing bounded software checks. The existing browser smoke test covered rendering, theme synchronization without text loss, isotope selection/counts and mobile width; it did not repair the delta compiler or integrate the independent kernel.

Test totals and implementation claims are checkpoint-specific. Later editor repair/integration must be reviewed with its own source and regressions rather than inferred from this guide. The standalone source and `website/.vitepress/components/IsotopeWiring.vue` identify the actual running implementation. No formal correctness proof, physical adequacy or scientific acceptance is asserted.
