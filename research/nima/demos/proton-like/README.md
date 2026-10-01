# Proton-like carrier — Three.js view

[Open the interactive viewer](index.html)

Open `index.html` directly in a WebGL-capable browser. No server or network connection is needed; Three.js and OrbitControls are reused from the adjacent `paw-cycle/vendor` directory.

- Drag to orbit; scroll or pinch to zoom.
- Choose surface, surface plus interaction net, or the interaction net alone.
- Click a triangle or choose its label to inspect its three endpoint pairs.
- Adjust surface opacity, labels, phase guides, and view rotation.
- Reset restores the camera and clears orbit inertia. Reduced-motion preferences pause phase playback initially.

The surface has four tetrahedral corners and four shared face centres, with twelve oriented triangles and eighteen shared edges. The dual has twelve triangle agents, eighteen wires, four triangular cycles, and four hexagonal cycles. In the overlay, wires pass over shared edges; in the isolated dual view they are straight links between the same agents.

Moving marks are synchronized orientation/phase guides. They are not a computed particle trajectory or an electromagnetic simulation. The grid is a viewing aid.

## Verification

```text
node research/nima/demos/proton-like/check.mjs
```

The browser test checks offline loading, agreement with the existing source triangle records, positive cone volumes and total volume 8/3, opposite seam orientations, dual incidence and cycles, raycast and dropdown selection, pause/resume, orbit/reset, reduced motion, and mobile layout. `verification.json` records the result; `preview*.png` show the rendered views.
