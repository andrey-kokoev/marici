# Isotope / R-space app maintenance

## Source and publication

Edit `research/strominger/demos/particle-overlap-tetrahedron/`, not the copies in `public/` or `website/public/`.

`node research/strominger/checkers/prepare_particle_overlap_viewer.mjs` publishes the explicit asset manifest to both destinations and checks the existing identity receipt and directory ownership. `scripts/prepare-website.mjs` runs that publisher during website preparation.

Before copying, the publisher calls `prepare_isotope_geometry.mjs`. This offline exporter runs all 19 source constructions, checks species counts, finite coordinates and native tetrahedral membership, and runs the existing phase audit through `createPhaseAssembly` for phase-model records. Local references use the existing local-reference display source; the exporter does not claim to rerun all their original research proofs.

It emits `isotope-geometry/grid.json`, one compact JSON file per isotope (species and node indices), and `manifest.json`. The manifest records validation provenance, SHA-256 asset hashes, and a conservative source dependency fingerprint (all authored model modules plus the exporter). Unchanged sources and intact asset hashes skip regeneration. Changed or missing files trigger regeneration; `--check` instead fails. The manifest is written last. Do not hand-edit generated geometry.

The public guide is `website/experiments/isotope-space.md`. Homepage links originate in `docs/landing-page.md`, not generated `website/index.md`.

## Runtime boundaries

- `tessellated-space-viewer.js`: UI state, URL selection, camera, native-grid rendering, and rendering lifecycle.
- `tessellated-space.js`: R-space geometry and batched rendering.
- `isotope-structure-data.mjs`: lightweight selection metadata.
- `isotope-geometry-loader.js`: cancellable fetch, SHA-256 verification, compact record expansion, shared grid and per-isotope session cache.
- `isotope-geometry/`: generated publication assets; no browser research computation.

The default view fetches no isotope geometry. Selecting an isotope enters its native view. Isotope query links without an explicit view retain isotope intent. Request IDs reject stale results and AbortController cancels obsolete fetches. Returning to loaded geometry uses the session cache. Switching to R-space does not cancel a wanted load. Errors expose Retry without breaking R-space.

Results are checked against declared species counts and source lattice cells before display. Native grid context is a bounded face-neighbor expansion, not an R-space embedding. Geometry is disposed when replacing the native scene. Assets use manifest hash query parameters and byte verification to detect mixed or stale publication files. The client requires HTTPS or localhost for Web Crypto.

## Performance and verification

Local observations, not portable timing guarantees:

- Original nitrogen-15 page readiness: approximately 19.7 seconds.
- Isolated phase-model import: approximately 20 ms; construction: approximately 21.7 seconds.
- Export run: boron-10 ~5.8 s, carbon-13 ~14.2 s; nitrogen-15 ~12 ms once retained predecessors were cached.
- Asset-based browser: R-space ~216 ms; nitrogen-15 deep link ~48 ms in the same browser session.
- Nitrogen-15 asset ~1.1 KB; shared native grid ~16 KB, uncompressed.

The improvement comes from removing repeated reference search and certificate construction from visitor sessions, not from a faster solver. Batching also reduces draw calls; individual mesh-per-body picking is not provided.

```sh
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
node research/strominger/checkers/prepare_isotope_geometry.mjs --check
node scripts/test-isotope-space-browser.mjs
pnpm run build
node scripts/test-isotope-space-browser.mjs website/.vitepress/dist
```

Browser coverage includes lazy startup, switching while loading, selection supersession, every isotope rendering, hydrogen and nitrogen-15 counts, grid controls, deep links, mobile layout, failed assets/retry, digest mismatch rejection, absence of research imports, and uncaught errors. These checks validate display behavior, not physical claims. Deployment is separate from building publication assets.
