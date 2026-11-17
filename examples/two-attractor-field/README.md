# Two-attractor momentum field — Three.js reference derivative

Rebuilt directly from `examples/threejs-reference/`: the reference `app.js`, panel-host HTML structure, styles/theme/palette, cancellable local vendor loading, owned renderer lifecycle, OrbitControls, keyboard camera controls, demand scheduling, and Vue computed-model boundary are retained. `fieldLayer.js` replaces the tetrahedron content; `model.js` implements the pure dynamics. Uses the reference's pinned local r128 Three.js/OrbitControls pair and MIT license.

Authoritative source: this directory. Published copy: `website/public/experiments/two-attractor-field/`. The former `public/experiments/two-attractor-field/` viewer was deleted. Publication is registered in `scripts/prepare-visualization-assets.mjs`. Selected for the reviewed public source build, with [model/control limits](../../website/experiments/field-and-shell-viewers.md), gallery navigation and static model disclosure. Local selection is not a claim that the current deployment serves these bytes; live acceptance remains T08/T14. `node scripts/test-curated-viewers.mjs` checks the complete built-site route; `--live` is a separate post-release check.

```sh
node scripts/prepare-two-attractor-field.mjs
node --test tests/two-attractor-field.test.mjs
node scripts/serve-two-attractor-field.mjs
```

The dedicated server prints its actual URL (default `http://127.0.0.1:8788/index.html`). Under the website server the route is `/experiments/two-attractor-field/index.html`; do not assume an unrelated server on port 5173 serves the website.

Weights range from 0 to 5. The active pole exerts softened inverse-square attraction with softening 0.8; the other pole is inactive. Sources A and B are fixed at (-3,0) and (3,0). The nearest pole attracts first (clicking exactly on a pole selects the other). Attraction switches when the radial position–velocity dot product changes from negative to nonnegative within 0.6 units of the active center: a local closest pass. Velocity is preserved, so the particle overshoots before returning. A gold ring highlights the active pole, and arrows update to show its force (lengths compressed with tanh). Before placement both fields are previewed. High damping can prevent a pass, and zero weight can stall traversal; this is not a guaranteed periodic orbit for arbitrary parameters.

Green particles obey dx/dt = v and dv/dt = F(x) - γv, with unit mass. The side-panel damping slider ranges from 0 to 3 s⁻¹ (default 0.3). Initially the plane has no particles and motion is paused. Clicking to place a particle starts (or resumes) motion automatically; Pause remains available. Clicking the scene raycasts onto the XY plane and places one particle at rest, replacing any previous particle and clearing its trail. Camera drags do not place particles. No automatic emission or spawn-rate control remains. Clear particle removes the particle and trail without changing parameters. Camera reset is separate. Integration uses symmetric drag/kick/drift/kick/drag splitting at 120 Hz, caps elapsed frame time at 50 ms, and suspends while hidden/offscreen. Trails retain 40 samples at 30 Hz. Numerical trajectories are approximate, with no exact energy-conservation claim.

Tests cover field symmetry/superposition, alternating pole passes with velocity continuity, momentum persistence, force-free velocity decay, finite trajectories, local-only Three.js rendering, reference camera controls, weight/damping controls, click placement/replacement and drag exclusion, run/pause/reset, idle rendering, mobile overflow, synthetic context loss, unavailable WebGL and JavaScript-disabled fallback. No cross-browser or deployment claim.
