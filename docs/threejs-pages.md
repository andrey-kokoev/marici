# Three.js pages: project conventions and reference

**Review caveat:** the [critical source review](threejs-reference-review.md) records the initial vanilla-JS implementation's gaps. The reference now uses Vue 3 compiled SFCs, layered computed panel state and an owned imperative scene handle, with keyboard camera elevation/azimuth and cancellable startup. The r128 renderer/addon pair remains intentionally unchanged; this is not yet a fully modernized or benchmark-optimized renderer template.

## Review outcome

No dedicated Three.js best-practices guide was found in `docs/`, the root instructions or the reviewed viewers. There are good practices distributed across existing implementations. This guide consolidates those practices and adds a small reference; it does not certify every existing viewer or change their scientific content.

Reviewed implementations:

| Implementation | Practices to retain | Gaps / cautions |
| --- | --- | --- |
| `research/voevodsky/demos/minimal-data-packet/{index.html,scene.js}` and `tests/minimal-data-packet.spec.mjs` | Local dependencies with license; meaningful SVG fallback; model/scene separation; labelled controls; capped device pixel ratio; container resize; desktop/mobile and failure browser tests | Lifecycle/animation behavior needs explicit policy for each embedding; reuse the architecture, not every viewer-specific assumption. |
| `papers/witness-generators/proton-neutron-assembly.html` | Change-driven rendering and bounded transition animation; geometry/material replacement disposal; reset, layer controls and responsive container resize | Large monolithic page couples many independent models; avoid copying it as a minimal template. |
| `papers/witness-generators/three-arrow-receiver.html` | Capped pixel ratio, controls and container resize | Unconditional animation loop runs even for an idle scene; not the default for new static viewers. |
| Imported tetrahedral planes, archived at `examples/tetrahedral-planes/original.html` | Pinned matching Three.js/TrackballControls versions; pixel-ratio cap; disposal during rebuild; useful sliders and camera reset | Original used a CDN, lacked a static fallback and used full-window overlays. Now migrated to the Vue/local-bundle viewer described below. |
| `scripts/prepare-visualization-assets.mjs`, `scripts/check-construction-gallery.mjs` | Authored-source/public-copy separation, local vendor assets, return links and real browser checks | Generated files are not the editing source; build checks do not verify mathematical or physical claims. |

This is a repository review, not an external literature survey. Useful upstream references: [installation](https://threejs.org/manual/en/installation.html), [responsive rendering](https://threejs.org/manual/en/responsive.html), [rendering on demand](https://threejs.org/manual/en/rendering-on-demand.html), [resource disposal](https://threejs.org/manual/en/cleanup.html), [WebGLRenderer](https://threejs.org/docs/#api/en/renderers/WebGLRenderer). Check upstream APIs against the version actually installed: current documentation may describe a newer release.

## Applied example: tetrahedral planes

The imported planes example is now a [Vue application](../examples/tetrahedral-planes/README.md), using the reference's panel/imperative-scene separation and responsive styles. It preserves all plane controls and free Trackball rotation, adds keyboard roll, uses locally bundled Three.js r180 and matching controls, computes region/segment summaries through Vue, and avoids rebuilding geometry for opacity changes. Its pure geometry has separate Node tests.

Both `/experiments/tetrahedral-planes/index.html` and the original `/experiments/tetrahedron_planes_free_rotation.html` serve the migrated viewer. The Constructions gallery includes a preview card pointing to the explicit HTML path; directory URLs can hit VitePress's page router in dev mode. Run `pnpm planes:prepare` or `pnpm planes:test`. Unlike the minimal reference's retained r128 pair, this applied example uses the imported viewer's r180 version through a pinned package dependency.

## Applied example: normal-ray lattice

The [normal-ray viewer](../examples/normal-ray/README.md) now follows the reference's
Vue SFC/computed-model/owned-renderer structure, using the pinned r180 module and
matching TrackballControls. Its process and scene panels remain separate and
closable; geometry remains in the original research modules. `pnpm normal-ray:prepare`
preserves the existing `/research/realization-tower/normal-ray.html` repository-server
URL. The website also publishes the same bundled viewer at
`/experiments/native-belt/index.html?preset=native-belt`, with a
[public guide](../website/experiments/native-belt-guide.md). Its publisher is
`scripts/prepare-native-belt-viewer.mjs`, invoked by the website build. `pnpm normal-ray:test` runs model and local-only Chromium lifecycle/fallback
checks. This local research viewer is not automatically a public-site deployment.

## Selected public derivatives: switched-attractor field and ESD7 shell

The [public selection guide](../website/experiments/field-and-shell-viewers.md) distinguishes a prescribed switched-force numerical toy from a static order-seven subdivision boundary. Both retain local r128/OrbitControls, an SVG fallback and model disclosures outside the JavaScript mount. Authoritative sources remain in `examples/two-attractor-field/` and `examples/simplex-step-span/`; their existing publishers are invoked by normal visualization preparation. The historical shell URL no longer denotes a 23-step path or growth process.

`node scripts/test-curated-viewers.mjs` checks the actual production-build paths with same-origin assets at desktop/mobile sizes. `--live` additionally requires exact served viewer bytes matching the local build and is a separate post-release acceptance step. Source selection and local browser checks do not satisfy T08's deployed-route requirement or authorize release. Existing model and fallback tests remain required; these checks are not physical validation.

## Reference implementation

- **Edit:** `examples/threejs-reference/`: `App.vue` (panel), `useViewerModel.js` (reactive/computed state), `scene.js` (imperative renderer), `app.js` (mount), plus HTML/CSS.
- **UI:** Vue 3 Composition API and compiled single-file components; no browser template compiler, CDN or runtime `eval`.
- **Publisher:** `scripts/prepare-threejs-reference.mjs`; Vite and the Vue plugin compile local hashed assets, also invoked by normal visualization preparation.
- **Published copy:** `website/public/experiments/threejs-reference/`.
- **Public URL:** `/experiments/threejs-reference/index.html` (use the explicit HTML route in VitePress dev mode).
- **Browser check:** `node scripts/test-threejs-reference.mjs`.

The standalone publisher can run without regenerating unrelated research receipts:

```sh
node scripts/prepare-threejs-reference.mjs
pnpm threejs:test
```

Serve over HTTP, not `file://` (ES module restrictions differ). Use the ordinary site dev server or another static server rooted at `website/public`. The browser check starts its own loopback server and requires installed Playwright Chromium. It validates the reference only, not the complete VitePress build or a deployment.

### Reactive UI boundary

The example uses `reactive` for nested appearance/motion input and `ref` for lifecycle state. Its computed graph is input opacity → bounded opacity → percentage/surface classification → appearance summary → combined panel summary. A computed render-state packet crosses into Three.js via a scoped `watch`; ordinary `computed` getters remain side-effect free. Native collapsible sections organize camera, appearance and motion controls.

The renderer handle and all Three.js objects stay in plain variables, outside deep Vue reactivity. `onMounted` starts rendering; `onUnmounted` aborts pending startup and disposes the handle. The static SVG sits outside the Vue mount, so missing Vue/JavaScript cannot erase it. Panel computations have independent Node unit tests in `tests/threejs-panel.test.mjs`.

The example intentionally renders a simple tetrahedron rather than importing a scientific model. It uses the already-vendored, mutually compatible **legacy** Three.js/OrbitControls pair from `research/nima/demos/paw-cycle/vendor`, with its MIT license. This avoids an extra CDN or package dependency, but is not a recommendation to adopt that old version for every new project. Upgrade the renderer and addons together, update the local provenance/license, and rerun browser tests. Never mix the imported tetrahedron's r180 addons with the legacy global build.

## Authoring checklist

### Structure, provenance and publication

1. Keep authoritative source separate from published copies. Register a deterministic copy/build step; do not rely on hand-editing generated assets.
2. Prefer small `model`, `scene`, and UI modules as complexity grows. Pure geometry and scientific calculations belong outside the rendering loop and need separate numerical tests.
3. Pin matching renderer/addon versions. Prefer local licensed assets for public pages; if a CDN is necessary, document the network requirement and test its failure. Do not silently use `latest`.
4. Include page title, viewport, description, readable purpose, gallery return link and interpretation limits. A compelling rendering is not a proof, experiment or physical prediction.
5. Use URL-relative asset paths that survive directory publication. Check actual HTTP responses and MIME types. Deployment and cache freshness are separate from local checks.

### Layout and accessibility

6. Size the renderer from its container with `ResizeObserver`, not just `window.innerWidth`. Update camera aspect/projection; guard zero-size containers. Keep CSS and drawing-buffer sizes distinct.
7. Cap pixel ratio (the reference uses 2). Choose sensible near/far planes and zoom limits rather than huge arbitrary ranges.
8. Keep instructions and controls outside overlays that can hide the model or trap mobile scrolling. Use native buttons, labels, outputs and visible focus. Test narrow screens and browser zoom.
9. Supply keyboard alternatives to drag-only actions. A canvas label alone is not equivalent access. Preserve a meaningful diagram and textual explanation without JavaScript/WebGL. Do not use color as the only identifier in more complex models.
10. Start with automatic motion off. Respect reduced-motion changes, offer pause and reset, and announce state via a status region rather than updating an aria-live region every frame. Explicit user opt-in can enable animation even under reduced motion.

### Rendering and lifecycle

11. Render on changes for static models. Use one coalesced animation scheduler, elapsed-time motion and bounded deltas; do not allocate geometry every frame. If damping is enabled, schedule its settling frames deliberately. The reference disables damping for clarity.
12. Pause work when hidden or offscreen. Restart cleanly after visibility/intersection changes; handle back-forward cache deliberately. Avoid duplicate loops after reset or remount.
13. Own and dispose geometries, materials, textures, controls and renderer; disconnect observers, remove listeners and cancel frames. Track shared resources once. `scene.remove()` does not release GPU resources. The reference uses no textures; textured derivatives must own and dispose their maps too.
14. Treat missing dependencies, renderer creation failure and context loss as normal failure paths. Keep the fallback visible until initialization succeeds. The reference deliberately stops on context loss and asks for reload rather than pretending to restore resources.
15. Transparent surfaces require intentional `depthWrite`, face orientation and draw ordering. Transparency is not a substitute for correct geometry. Keep edges and labels legible, and bound tessellation and object counts.

### Verification before publication

16. Test real desktop and mobile Chromium with WebGL, not just DOM snapshots. Assert a successful draw, nonzero canvas dimensions, aspect ratio, UI effects and absence of overflow/errors. Capture screenshots when visual placement matters; draw-call checks cannot establish visual correctness.
17. Block external requests to verify local-only operation. Test missing dependencies and unavailable WebGL; simulate context loss. Test controls by keyboard, resize, pause, reset, teardown and idle scheduling.
18. Test visibility/offscreen and navigation restoration for interactive embeddings. Check Firefox/Safari and touch devices before claiming broad compatibility. An automated synthetic context-loss event tests the handler, not full driver recovery.
19. Validate geometry/model invariants independently. Browser tests establish display behavior, not mathematical truth or experimental validity.

## Current verification scope

`test-threejs-reference.mjs` covers desktop/mobile rendering with external requests blocked, keyboard camera azimuth/elevation, opacity and zoom controls, reactive derived summaries, camera reset, reduced-motion initial state and preference changes, explicit animation/pause, idle scheduling, viewport resize, overflow, explicit teardown, pending-start cancellation, missing vendors, WebGL creation failure, the context-loss handler, missing app bundles and JavaScript-disabled fallback. It reports uncaught script errors. It does not claim a cross-browser audit, physical mobile-device validation, screenshot review, actual GPU-loss recovery, or automated back-forward-cache/visibility coverage.

The tetrahedral-planes viewer has been migrated; other existing pages have not been mass-migrated. Improve older pages in bounded changes with their original model tests retained.
