# V-label positioning

V-label placement is now one screen-space pipeline for geometry and wiring views.

1. `scene.js::rotationVertices()` supplies displayed anchors. Wiring applies the same parent translation as the diagram; geometry retains the docked coordinates. Rotation controls and labels use this same anchor set.
2. Project each anchor and its own parent's centroid through the current camera. For non-paired shapes use the whole shape centroid. Do not assume special vertex indices, tip indices, or shared-face planes.
3. `vertex-label-layout.js::layoutVertexLabels()` offsets labels outward by 36 CSS pixels, independent of world scale or zoom. A stable candidate search resolves label-box collisions and clamps to the viewport. If no collision-free candidate fits, it minimizes overlap rather than changing the anchor.
4. Leader lines connect label positions to true anchors; only label positions move. Hidden/off-screen anchors do not participate in collision placement. Existing click-to-lock semantics are unchanged.

This replaces the old world-space percentages and special reflected offsets for V2/V6. Equal-height anchors with equivalent projected outward directions get equal-height labels. Arbitrary camera projections need not put unrelated vertices on the same screen row.

Checks: `tests/vertex-label-layout.test.mjs` covers consistent spacing, translation/zoom independence, eight coincident anchors, bounds, hidden anchors and deterministic placement. The rebuilt viewer passes `scripts/test-neutron-belt.mjs` and `scripts/test-cell-vertex-view.mjs` (locks, zoom, pan, vertex selection, persistence).
