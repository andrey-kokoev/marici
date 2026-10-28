# Vue + Three.js reference viewer

See [the authoring guide](../../docs/threejs-pages.md) for the review, checklist and verification scope.

## Boundaries

- `App.vue`: nested Vue panel sections and scoped component lifecycle.
- `useViewerModel.js`: reactive inputs and multi-level computed summaries/render-state packet; independently testable without WebGL.
- `scene.js`: imperative scene/camera/resources, demand rendering and cancellable startup. Three.js objects never enter Vue's deep reactivity.
- `app.js`: Vue mount and small diagnostic interface.
- `index.html`: readable HTML and SVG fallback outside the Vue mount.
- `theme.css` / `palette.js`: shared saffron/ochre colors from `examples/tetrahedral-planes/original.html`, reused by the normal-ray viewer. Dark navy scene, warm brown panels, ochre controls and saffron surfaces; semantic particle/axis colors remain separate.

Edit this directory, not generated files in `website/public/experiments/threejs-reference/`.

```sh
pnpm threejs:prepare
pnpm threejs:test
```

Public route: `/experiments/threejs-reference/`. Serve over HTTP. The publisher uses Vite + the Vue SFC plugin to compile and bundle local runtime assets; the browser does not compile templates. Normal website preparation runs the same publisher.

Vue, Vite and the Vue plugin are explicit pinned build dependencies in the project manifest/lockfile. The existing legacy r128 Three.js, matching OrbitControls and MIT license are still copied from `research/nima/demos/paw-cycle/vendor/`. Modernizing that renderer dependency is separate from this Vue migration. No scientific results are computed or certified here.
