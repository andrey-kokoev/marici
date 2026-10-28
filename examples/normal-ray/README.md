# Normal-ray viewer — reference-architecture migration

Authoritative UI and renderer source now lives here, following
`examples/threejs-reference/` and `docs/threejs-pages.md`. This is an actual
compiled Vue SFC migration, not a styling-only change.

- `App.vue`: separate closable process/scene panels, accessible controls,
  imperative handle lifetime, reduced-motion preference, cancellation during
  lazy renderer loading.
- `useViewerModel.js`: reactive inputs and pure computed render packets.
- `scene.js`: owned Three.js/TrackballControls renderer. Objects stay outside
  Vue reactivity; static views render on demand, motion uses bounded elapsed
  time, and offscreen/hidden views suspend frames. Resources, textures, controls,
  observers and event listeners are disposed on teardown/failure.
- `index.html`: meaningful static SVG/text outside the Vue mount, surviving
  missing JavaScript, missing bundles or unavailable WebGL.
- `style.css`: responsive layout with no floating panels over the model on
  narrow screens; visible keyboard focus and independent panel closure.

The matched Three.js **0.180.0** module and TrackballControls addon come from
this repository's pinned package dependency, as in the migrated tetrahedral
planes viewer. No CDN or older global r128 control is loaded. The build copies
Three.js and Vue license files into its generated directory.

## Published native N-cut belt

Public guide: `/experiments/native-belt-guide`. Launch:
`/experiments/native-belt/index.html?preset=native-belt`.
`node scripts/prepare-native-belt-viewer.mjs` rebuilds this viewer and publishes
local assets and licenses; the website build invokes it automatically.
`node scripts/test-native-belt-publication.mjs` checks the published route,
preset, navigation, geometry/wiring switch and reload persistence.

Geometry removes one displayed unit N tip per parent and rigidly docks the
exposed triangle to the central belt-face triangle. Removed records remain in
`parentCutAudit`. Wiring is an expanded diagram, not the metric embedding.
Opaque P/E faces follow the native tetrahedral-orientation color convention;
thick white borders mark the declared inside-N sector. V-labels use screen-space
layout, with V1/V2 suppressed in both belt views. Geometric attachment is checked;
native field transport and physical interpretation remain open.

## From center cell — interface expansion

Select **From center cell — interface expansion** in the process menu at
`research/realization-tower/normal-ray.html`. Previous/Next traverses the dot,
central P, revised P/E/N/N boundary, relocation through native octahedral
wedges, bidirectional meeting guides, and eight typed arrow cells (steps 0–5).
The removed candidate trial is not restored: Step 5 builds the operator's
P [N N] E, P [P P] P, P [N E] N, and P [N P] N assignments.
Existing processes are unchanged.
Progress is saved independently.

Source: `research/realization-tower/center-interface-process.mjs`.
Every displayed cell is selected by exact vertices from the existing esd7
census. The central regular tetrahedron has four neighboring octahedral wedges;
these are not reflected regular tetrahedra. Each boundary identity relocates to
the opposite congruent wedge in its own native octahedron. The source's cyclic
component order supplies the displayed two intervening cells. All consecutive
cells share complete triangular faces, including the middle pair. Source ring
orientation is a display convention, not uniquely forced by P/N/E types.
The remaining fourth wedge in each octahedron is not filled. Geometry membership
is verified; the assigned types do not constitute a native species-law proof.
The incorrect cap dilation and compressed 3/5/9/17 collar display have been
removed. Those earlier screenshots/probes are historical, not this construction.
The native k=7 envelope is a reference only; guides are not certified paths.

Build and check:

```sh
node scripts/prepare-normal-ray.mjs
node --test tests/center-interface-process.test.mjs
node scripts/test-center-interface-process.mjs
```

See [the working approach](../../research/strominger/recursive-interface-realization-approach.md).

## Preserved behavior

The source geometry remains in `research/realization-tower/normal-ray-model.mjs`
and `normal-ray-procedure.mjs`. The viewer does not replace the construction.

- k=1..7, independent procedure stages; changing k recomputes immediately.
- The procedure now follows adjacent surface triangles on the outer face opposite V2; k counts surface-edge crossings, not inward plane depth.
- At k=1, the start and end are distinct primitive cells sharing exactly one edge. Step 2 assigns whole-cell P/E roles again.
- `surface-path-model.mjs` selects a reproducible surface path (first edge-only continuation, then a longest shortest path with cell-ID tie breaks). This is an explicit display-path choice, not an isotope-selection law.
- Orthographic projection, initial/reset azimuth 67°, elevation −68°.
- Envelope barycenter at 62.5% of viewport height.
- Free trackball orbit without pole stops, scroll/pinch zoom and pan.
- Clickable V1–V4 labels toggle fixed rotation anchors without snapping. One anchor allows rotation about its barycenter-to-vertex axis; two stop rotation.
- Both closable panels, appearance controls and optional auto-rotation; the world-orientation overlay has been removed.
- Keyboard orbit/roll/zoom alternatives added; automatic motion starts off.

The role assignments remain trial procedure data, not isotope predictions.

## Isotope-constructor settings

All scene preferences use one app-qualified, versioned localStorage key:
`marici:isotope-constructor:v1:scene-settings` (`settings.js`). It stores k,
appearance and P/N/E label visibility, motion preferences, vertex locks, panel
and section visibility, and camera orientation/roll, pan and zoom. Its `process`
namespace stores the selected construction, k, step, branch, and independent
progress for each construction. Reload resumes the saved selection; older records
without this namespace start at step zero. Camera writes are throttled; unload flushes
pending changes. Reduced-motion safety stops do not erase the saved spin preference.

Legacy `normal-ray:k`, `normal-ray:labels`, and `normal-ray:face-opacity` values
are imported only when the namespaced record is absent. No other application's
keys are changed. Values are validated and clamped; malformed or unavailable
storage falls back safely to defaults. Removing the namespaced key resets the
record (legacy values, if present, will be imported again).

## Process 3

Select **Process 3 — diamond rules** to start the independent clean reconstruction.
The current foundation implements steps 0–4 (seed, three initial rays, atomic
corner diamonds) for every k. Step 5 locates the actual k-envelope centroid:
k=3,5,7 have a unique central P. Step 6 uses a unique four-vertex mapping to add
three P neighbors, leaving the V1-side neighbor unresolved, with dashed geometric
path guides. E is surface-only; the interior E trial has been removed. At k=5 there are nine tied mappings, so the center is shown but shell
orientation remains unresolved. Even k needs an octahedral center rule.
Run `node scripts/inspect-process3.mjs --k 5,7 --step 6` for reproducible overview,
core and axis screenshots plus JSON audits; the tool prints its artifact directory.
It deliberately stops before edge-front filling and N closure; Process 2 remains unchanged. See
[the rule contract and next stages](../../research/realization-tower/process3.md).

## Particle counts

The bottom-right **Counts** panel collapses with its header (mouse or keyboard).
It opens in a compact view: native inventories show their primary whole-cell or
assembly counts; **Breakdown & notes** reveals the retained location, face, void
and trial-channel rows and their scope notes. This is a presentation change only:
no counts, geometry or physical identifications change. The expanded panel scrolls
within the viewport on small screens.

The bottom-right viewport table counts assigned cells, not visible labels or
rendered faces. Surface cells expose a triangular face on the current k-tetrahedron;
all other assigned cells count as interior filler (including edge-/vertex-only
boundary contacts). Each cell is counted once, with P/N/E columns, location
subtotals, and combined totals. Display opacity and visibility do not affect counts.

## Build and test

```sh
pnpm normal-ray:prepare
pnpm normal-ray:test
```

Publisher: `scripts/prepare-normal-ray.mjs`. Only the dedicated generated
`research/realization-tower/normal-ray-viewer/` directory is emptied by builds.
It publishes the compatibility HTML at the **unchanged** URL:

http://127.0.0.1:8777/research/realization-tower/normal-ray.html

The generated directory's own `index.html` is also usable. Serve the repository
root over HTTP; opening files directly is unsupported. Do not hand-edit the
published HTML or hashed assets. The superseded standalone renderer and its
legacy local TrackballControls copy are removed.

## Verification scope

Node checks cover geometry, normality, seven stops, endpoint roles and reactive
state propagation. Browser checks rebuild locally and block external requests.
They cover desktop/mobile Chromium, default view, procedure changes, locks,
keyboard camera controls, opacity without geometry rebuilding, idle scheduling,
independent panels, reduced-motion changes, explicit spin opt-in, offscreen
pause/resume, unmount disposal, pending-start cancellation, unavailable WebGL,
missing application bundle, JavaScript-disabled fallback and the context-loss
handler. A desktop screenshot was inspected during migration.

Not a cross-browser/mobile-hardware certification or real GPU-loss recovery
test. Rendering failure asks for reload, rather than claiming context restoration.
Vite reports a large Three.js renderer chunk; no performance benchmark is
claimed. Broad website publication is separate from this local-viewer build.
