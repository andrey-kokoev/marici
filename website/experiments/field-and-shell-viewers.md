# Switched-attractor field and ESD7 shell: controls and limits

**Public selection for the reviewed source build; live deployment acceptance remains T14.** These are intended public routes, not a statement that the current remote deployment serves this revision. Public selection is not deployment acceptance. The source build and local runtime can be checked without granting commit or deployment authority.

| Viewer | What to explore | Model boundary |
|---|---|---|
| [Open the switched-attractor toy field](/experiments/two-attractor-field/index.html) | Place one test particle, vary two prescribed weights and damping, and inspect momentum through a switched attraction. | A supplied numerical toy model, not a derived gravitational, electromagnetic or nuclear interaction. |
| [Open the ESD7 outer shell](/experiments/simplex-step-span/index.html) | Rotate a tetrahedral subdivision boundary and vary its surface opacity. | A specified combinatorial/geometric shell, not nuclear geometry, a growth law or a Ramsey-forcing certificate. |

## Switched-attractor toy field

The two poles are fixed at A = (−3, 0) and B = (3, 0) in a supplied XY plane. Weights range from 0 to 5; softening is 0.8 and damping ranges from 0 to 3. Before placement the arrows preview **both fields**. Once a particle is placed, **one active pole** supplies its force; this is not simultaneous two-pole orbital motion.

Clicking the plane replaces the single particle at rest, clears its trail and starts motion. Dragging the camera does not place particles. The nearest pole attracts first, except a click on that pole selects the opposite one. A closest pass within 0.6 units switches attraction without resetting velocity. The gold ring identifies the active pole.

Use **Pause**, **Clear particle**, **Reset parameters** and **Reset view** separately. Low damping can permit repeated passes; strong damping or a zero-weight active pole can stall the trajectory. This is **not a guaranteed periodic orbit**. The integration is a numerical approximation with a fixed 120 Hz simulation step and capped frame elapsed time, not exact energy conservation. Unit mass, force law and simulation seconds are chosen conventions, not independently calibrated physical inputs.

Source and reproduction: [examples/two-attractor-field/README.md](https://github.com/andrey-kokoev/marici/blob/main/examples/two-attractor-field/README.md), [scripts/prepare-two-attractor-field.mjs](https://github.com/andrey-kokoev/marici/blob/main/scripts/prepare-two-attractor-field.mjs), [tests/two-attractor-field.test.mjs](https://github.com/andrey-kokoev/marici/blob/main/tests/two-attractor-field.test.mjs).

## ESD7 outer simplicial shell

The historical `simplex-step-span` URL now displays only the boundary of the declared order-seven Freudenthal subdivision of a tetrahedron: **100 vertices, 294 edges, 196 triangles**, with **49 triangles** on each outer face. A chosen regular tetrahedral embedding has side length 7. Interior tetrahedra are used to identify the boundary but are not drawn.

Use camera buttons or drag/zoom and the surface-opacity slider. This is **not a 23-step path**: the old path, routing, arrows and growth controls are absent. Shell counts and surface incidence test the implementation of the specified geometry, not nuclear geometry, isotope stability, particle content or physical dimensions. A side length in display units is not a measured nuclear length.

The existing model test compares every boundary triangle with the owner-local ESD7 census and checks surface incidence and Euler characteristic. That comparison is not a new formal proof or replay of the census supplier.

Source and reproduction: [examples/simplex-step-span/README.md](https://github.com/andrey-kokoev/marici/blob/main/examples/simplex-step-span/README.md), [scripts/prepare-simplex-step-span.mjs](https://github.com/andrey-kokoev/marici/blob/main/scripts/prepare-simplex-step-span.mjs), [tests/simplex-step-span.test.mjs](https://github.com/andrey-kokoev/marici/blob/main/tests/simplex-step-span.test.mjs).

## Runtime and reproducible publication

Both use the pinned local r128 Three.js/OrbitControls pair with its MIT license and bundled Vue code. Serve over **HTTP**, including for offline use; retain the complete generated directory and local assets. Saving one HTML file is **not a complete offline bundle**. Source links need network access, but the scenes do not require a CDN.

WebGL and JavaScript are required for interactive rendering. Each page retains a **static fallback** and model explanation if JavaScript, WebGL or assets are unavailable. A schematic fallback does not reproduce the full interactive scene. The field starts empty and paused; a placement is an explicit request to start motion. Camera buttons supplement drag controls; pointer placement is not a claim of full keyboard or screen-reader equivalence.

Edit the authoritative `examples/` sources, not `website/public/experiments/` bundles. Normal website preparation invokes both publishers. To rebuild them separately:

```sh
node scripts/prepare-two-attractor-field.mjs
node scripts/prepare-simplex-step-span.mjs
node --test tests/two-attractor-field.test.mjs tests/simplex-step-span.test.mjs
```

The publication regression also rebuilds both in isolated fixtures, checks byte-identical output on repeated builds, verifies local vendor/license bytes and rejects stale assets. Local desktop/mobile Chromium checks exercise the actual built-site links, controls, fallbacks and same-site assets. These are software checks, **not physical validation**, broad cross-browser certification, real-device acceptance or live release evidence.

After an authorized release, `node scripts/test-curated-viewers.mjs --live` checks these routes and exact viewer asset bytes on the deployed site. An unrun or failed live check cannot satisfy T08/T14. [Construction gallery](/experiments/) · [Viewer authoring conventions](https://github.com/andrey-kokoev/marici/blob/main/docs/threejs-pages.md).
