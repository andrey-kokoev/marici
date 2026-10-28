# Critical review of the Three.js reference

**Historical baseline:** this review evaluated the initial vanilla-JS reference. A subsequent operator-requested Vue migration split `App.vue`, `useViewerModel.js` and `scene.js`, added scoped reactive/computed UI state and cancellable startup, aligned keyboard navigation with camera orbit, fixed terminal spinning state and formatted CSS. Node model tests and browser checks now also cover computed propagation, elevation controls, reduced-motion changes, startup cancellation and no-JS/missing-app fallback. The r128 renderer, transparency tradeoffs and untested cross-browser/visibility/BFCache behavior remain limitations. Line numbers below refer to the pre-migration source.

## Verdict

Useful small example, **not yet a modern community reference or demonstrably optimized implementation**. The previous description should be narrowed accordingly. Its strongest decisions are local assets, one demand-driven scheduler, bounded frame deltas, explicit ownership/disposal, native controls and an HTML/SVG fallback. Passing its own browser suite does not establish broader best-practice compliance.

Scope: source review of `examples/threejs-reference/`, its publisher and browser test. Fresh `node scripts/test-threejs-reference.mjs` passed. Evaluating the vendored bundle in an isolated Node VM reports `THREE.REVISION === '128'`. No fresh online survey or performance benchmark was performed; the official documentation links below are comparison references, not claimed live-source verification.

## Findings, in priority order

### 1. High: a legacy dependency architecture is being presented as a general reference

**Where:** `app.js:47–62`, `scripts/prepare-threejs-reference.mjs`.

The viewer loads the r128 global build and legacy OrbitControls sequentially with injected scripts. This reuses a compatible local pair but teaches global state, manual dependency ordering and an obsolete installation pattern. It also lets a change in an unrelated research demo's vendor directory silently change the reference's dependency.

**Recommendation:** use a deliberately selected, pinned modern Three.js release and matching ES-module addons. Bundle with the project's build tools, or publish a local ESM bundle/import map. Keep license/provenance and a reproducible dependency declaration. Do not use an unpinned CDN and do not merely swap filenames: test color-management, material and addon migration behavior. If retaining r128 for compatibility, explicitly label this a legacy-compatible example rather than the preferred new-project template.

**Reference:** https://threejs.org/manual/en/installation.html

### 2. High: keyboard interaction is not equivalent to pointer orbit

**Where:** `app.js:87–90`, `index.html` controls.

Pointer OrbitControls changes the camera's azimuth AND elevation. The keyboard alternatives rotate the OBJECT only around its y axis and offer zoom. They cannot reach the same viewpoints, especially after the camera has already orbited. Native buttons are a good start, but the claim that they provide equivalent interaction is too broad.

**Recommendation:** expose camera orbit left/right/up/down and zoom with one camera/target model shared by pointer and keyboard. Avoid changing scientific model transforms merely to navigate the camera. Give the canvas a stable description linked to the instructions. Test reachability and camera/target changes, not merely `mesh.rotation.y > 0`.

**Reference:** https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html

### 3. Medium: no owned instance lifecycle; asynchronous startup is outside lifecycle control

**Where:** module-level state; `loadScript`; lifecycle listeners registered at `app.js:102–103` after both awaits.

This is a single-page script, not a reusable viewer component. A second viewer would share selectors, global THREE and the diagnostic handle. There is no cancellation/ownership check after dependency loading. A pagehide or host removal while startup is pending is not handled by this instance; after back-forward restoration, startup timing may differ from the already-initialized path. This is a lifecycle risk, not a reproduced BFCache failure.

**Recommendation:** `createViewer({host, controlsRoot})` with explicit `start`/`dispose`, idempotent teardown and an initialization generation or aborted-state check after asynchronous work. Register lifetime handling before startup. Prefer module imports over per-instance dependency injection. Keep standalone HTML as one consumer of this lifecycle, rather than introducing a framework just for the example.

### 4. Medium: resize handling misses display-density changes and repeats buffer sizing

**Where:** `app.js:65`, `104–109`.

Pixel ratio is sampled once. Moving between displays or changing browser zoom can change DPR without a useful container-size change. Every ResizeObserver callback calls `setSize` even if the effective drawing-buffer dimensions are unchanged. Tiny here, but undesirable as a copied pattern, especially on larger scenes.

**Recommendation:** compare desired dimensions before resizing; handle capped DPR changes, and choose one clear drawing-buffer strategy. Keep camera aspect based on CSS dimensions. Avoid mixing manually scaled dimensions with an additional renderer pixel-ratio multiplier. Consider a maximum pixel budget for very large viewports only after measuring a need.

**Reference:** https://threejs.org/manual/en/responsive.html

### 5. Medium: error reporting and runtime-failure coverage are incomplete

**Where:** `app.js:47–56`, `render`, final catch.

Startup failures all become a generic status with the underlying error discarded. Dependency loads have no application timeout/retry. The top-level try/catch does not cover later animation or ResizeObserver failures. Static fallback remains available for failed startup, which is good; that should not be confused with covering every runtime failure.

**Recommendation:** retain actionable diagnostics (asset URL and original error), provide an explicit retry/reload path, and make startup timeout policy deliberate. If runtime rendering fails, stop that viewer and preserve its fallback rather than repeatedly throwing. Do not blanket-catch unrelated application exceptions or automatically retry permanent errors in a tight loop.

### 6. Medium: tests are narrower than the reference's intended guarantees

**Where:** `scripts/test-threejs-reference.mjs`.

Current checks validate UI state and at least one draw call, not pixels. They do not exercise pointer/touch orbit, full keyboard view navigation, display-density changes, reduced-motion preference CHANGES, hidden-tab/offscreen scheduling, BFCache restore, repeated mount/dispose, module failure or actual graphics-context loss/restoration. The context-loss test dispatches a synthetic event; it does not lose the GPU context. Desktop/mobile are two Chromium viewport sizes using software WebGL, not physical devices or multiple browser engines.

**Recommendation:** prioritize behavior tests for the guarantees this example teaches: no idle frames; offscreen/hidden suspension and resumption; camera equivalence; pending-start disposal; repeated lifecycle; meaningful fallback. Add screenshot review/baselines for the tetrahedron and transparency at opacity0,0.35,1. Use `WEBGL_lose_context` where available for a real loss test, retaining a synthetic handler test separately. Add Firefox/WebKit smoke coverage before claiming cross-browser validation. Keep hardware performance claims separate from software-renderer tests.

### 7. Low/medium: rendering choices are illustrative, not established visual defaults

**Where:** `app.js:78`, `style.css`.

Double-sided transparent faces with depth writes disabled are a deliberate tradeoff, not a generally correct transparency solution. The material remains transparent even when the slider reaches1. Depending on version, overlapping/back-facing triangles and edges can produce unexpected visual order. The example has no visual assertion of those outcomes. Conversely this tiny unlit tetrahedron does NOT need instancing, shader tricks, a BVH, adaptive quality or a game-style continuous loop.

**Recommendation:** define intended opacity/end-point behavior and inspect representative views. Prefer an opaque baseline if transparency is not the lesson. Keep transparency-specific tradeoffs explicit; do not advertise depthWrite=false as a universal fix. Format CSS into readable rules: source readability matters more than manually minifying a reference; compression/minification belongs in publication tooling.

### 8. Low: teardown and diagnostic state disagree

**Where:** `dispose`, `window.ReferenceViewer`.

After disposal while spinning, `snapshot().spinning` can remain true even though motion is stopped and aria-pressed is false. The global diagnostic closure also retains references to disposed scene objects. This is not evidence of an unreleased GPU allocation, but it muddies lifecycle semantics and does not scale to multiple viewers.

**Recommendation:** set terminal logical state consistently and expose diagnostics per instance/in tests rather than through one production global. Use separate DOM-event and Three EventDispatcher subscriptions: Three's dispatcher does not implement AbortSignal cleanup. The existing explicit `removeEventListener` correctly compensates for its controls change listener; preserve that distinction.

## What to retain

- Local licensed dependencies and authored-source/public-copy separation.
- One coalesced requestAnimationFrame scheduler; do not replace it with an always-on loop merely because many tutorials do.
- Demand rendering for a static model; no damping tail is a reasonable minimal choice.
- Elapsed-time animation, bounded resume delta, default motion off and explicit user opt-in.
- Container-based sizing, limited camera range and a DPR cap.
- Explicit geometry/material disposal and separate observer/listener cleanup.
- Static content before JavaScript, fallback on unavailable WebGL and readable interpretation limits.
- Native, labelled controls with visible keyboard focus.

## Recommended correction sequence

1. Label the current example as legacy-compatible; do not claim modern or benchmarked optimization.
2. Modernize/pin the dependency boundary and establish one owned viewer instance lifecycle.
3. Unify pointer and keyboard camera navigation; fix terminal state and diagnostic/error handling.
4. Add missing lifecycle/DPR/navigation tests and visual review, then measure actual frame work before performance tuning.

This review changes no renderer or scientific model. The existing browser test was rerun successfully; the findings above describe gaps beyond that test's current assertions, not newly failed tests.
