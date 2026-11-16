# ESD7 outer simplicial shell

This viewer now shows only the boundary of esd_7(Delta^3). The previous 23-step path, color routing, arrows, compass and growth controls have been removed.

`model.js` follows the Freudenthal ordered-chamber construction in `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`. It selects triangles incident to exactly one tetrahedron and retains only their vertices and edges. The resulting shell has **100 vertices, 294 edges, 196 triangles**, with 49 triangles on each outer face. No interior cells or interior edges are rendered. Barycentric coordinates embed the shell into a regular tetrahedral envelope of side length 7.

The model test compares every boundary triangle against `research/voevodsky/results/esd7_explicit_analytical_census.json`, checks closed-surface edge incidence and Euler characteristic. The browser test checks local-only rendering, two shell draw calls, opacity and camera controls, removal of path controls, mobile overflow, disposal and no-JavaScript fallback.

The repository Three.js reference renderer, local licensed r128/OrbitControls pair, theme and Vue lifecycle remain. The historical directory/URL is retained so the existing link continues working.

```sh
node scripts/prepare-simplex-step-span.mjs
node --test tests/simplex-step-span.test.mjs
node scripts/serve-simplex-step-span.mjs
```

Open `http://127.0.0.1:8789/index.html`. Source: `examples/simplex-step-span/`; generated copy: `website/public/experiments/simplex-step-span/`.
