# Tetrahedral planes · Vue viewer

This is the Vue migration of the downloaded `tetrahedron_planes_free_rotation.html`, following the [reference viewer's UI/scene boundary](../threejs-reference/README.md). `original.html` preserves the imported source for comparison; it is not the published app.

## Edit and publish

- `App.vue`: nested reactive panels for planes, layers and camera.
- `usePlanesModel.js`: input → planes → repeated planes / bounded region → intersection segments / summaries / geometry packet.
- `geometry.js`: pure half-space and finite-disk calculations, tested without a renderer.
- `scene.js`: imperative Three.js and TrackballControls; no Vue proxies around renderer objects.
- `app.js`, `index.html`, `style.css`: mount, accessible fallback and responsive reference-based layout.

```sh
pnpm planes:prepare
pnpm planes:test
```

Normal website preparation also builds this viewer. Vite compiles Vue SFCs and bundles **pinned Three.js 0.180.0 with its matching TrackballControls** locally. No CDN or browser template compiler is required. The renderer loads as a separate chunk; disposal while loading prevents a late mount.

Public routes (same generated application):

- `/experiments/tetrahedral-planes/index.html` (explicit HTML path works in VitePress dev and production)
- `/experiments/tetrahedron_planes_free_rotation.html` (original URL retained)

Published output under `website/public/experiments/` is generated; edit this source instead. The publisher adjusts asset paths for the original HTML alias, publishes `preview.svg`, and includes the Three.js MIT license. The Constructions gallery links its preview card to the explicit HTML route with `target="_self"`, avoiding VitePress SPA routing of static viewers.

## Preserved behavior and deliberate changes

All original controls remain: opacity, distance, repeats, radius, disk intersections, tetrahedron edges/interior and camera reset. Repeats retain alternating offsets d,-3d,5d,-7d,… for each normal. At d=0 the bounded region is one point with zero volume. Disk clipping does not change the region defined by the four base half-spaces.

Trackball rotation still permits free camera roll, with keyboard yaw/pitch/roll and zoom alternatives added. Damping is now disabled (`staticMoving=true`), so there is no perpetual idle rendering loop; dragging and wheel input still update the camera. Opacity changes only the material. Geometry updates are coalesced into rendering frames, share disk geometry/material, and dispose replaced resources. The panel uses computed summaries and half-space volume; the camera and renderer remain non-reactive.

The imported full-screen overlay is replaced by the reference's responsive viewer/panel layout. Desktop view sticks alongside the controls; mobile uses normal vertical scrolling. The SVG outside Vue remains readable without JavaScript or WebGL.

## Verification and limits

Node tests check half-space vertices/faces/volume, point collapse, repeat offsets, finite-disk intersection endpoints and independence of reactive geometry/appearance computations. Chromium browser checks cover both URLs, desktop/mobile, local-only assets, all controls, keyboard camera movement, actual pointer Trackball drag, idle scheduling, bounded geometry counts after rebuilds, teardown, pending renderer cancellation, unavailable WebGL, a synthetic context-loss handler test, failed renderer chunk and JavaScript-disabled fallback.

`tests/tetrahedral-planes-navigation.spec.mjs` additionally exercises the public site's Constructions navigation → preview card → WebGL viewer → gallery return. Run with `pnpm exec playwright test tests/tetrahedral-planes-navigation.spec.mjs --config playwright.local.config.mjs` against the site dev server.

These are not a cross-browser/physical-device audit, actual driver-loss recovery test, visual screenshot approval or performance benchmark. Transparent overlapping surfaces retain the imported depth/order tradeoffs. No scientific claim is established by the rendering.
