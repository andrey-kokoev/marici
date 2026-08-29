## Question

Did the typed reconciler cube fail because of malformed scene data, broken controls, or a stale mixed browser asset revision, and can the browser-facing failure be removed without changing its research semantics?

## Claim boundary

The repair adds explicit revision tokens to the module graph, a data-URI favicon, a guarded projection-panel initializer, and a Canvas 2D renderer selected when WebGL2 is unavailable. It does not establish compatibility with browsers lacking import maps, Canvas 2D, or ES modules, and it does not change the typed-cell model.

## Disposition

Browser automation loaded a fresh context at 1440 by 1000 and 390 by 844, exercised all six controls, and obtained HTTP 200, `valid · 27 typed cells`, four canvases, exactly one active layer, and no horizontal overflow. Both runs had zero page errors, console errors, failed requests, or responses of status 400 or greater. The operator's Firefox trace then falsified the provisional cache-only diagnosis: `AllowWebgl2:false` made Three.js throw during renderer construction. Revision 4 capability-selects the renderer before Three.js construction. A forced-denial automation fixture returned `valid · 27 typed cells · Canvas 2D fallback`, rendered four canvases, exercised all six controls and pointer inspection, and produced zero page, console, request, or HTTP errors. A separate WebGL-enabled run also remained error-free.

Source hashes after repair:

- `index.html`: `8b4c1a60d8b6cae968b2c07ce0c6cdeb832daa4ada89928539568a713dfd6c36`
- `app.js`: `53137826b783c71fb7ae516bb482904fb48fd57273b0a51027c467d53b4f3013`
- `fallback-2d.js`: `0dc75507a0a515a9ffe2592b84d26684eed6f1f1a0b365de7175eb0098652a20`

Sequence claim: `seqclaim-b3643f6ec8a1afd7d8a0643f`. Epistemic graph admission: `ev-000000009825-6a2f1180-d0b3-4e82-b559-bc3fa39a254e`. Author: `marici.Kitaev` (`team_member:2ec122bc41a1fea3b5ab`).
