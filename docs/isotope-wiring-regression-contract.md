# Isotope-wiring regression contract review

Review baseline: `3ace86e33`, website currency task T03, iteration 2. This records a software-contract review, not scientific admission or a newly selected nuclear model.

## Why the 28 failures must not be repaired by restoring removed features

The current contract at the baseline already says:

- `examples/isotope-wiring/README.md`, **No routing inferred from rendered geometry**: remove SVG-derived graph extraction, routing, playback and trace downloads. No replacement routing belongs in the legacy editor.
- `examples/isotope-wiring/UI-REVIEW.md`, **Current contract: Neutron-only**: no EP view or renderer; old flags cannot restore them. Undefined/edited drawings stay explicitly undefined. Record comparisons and Undo/Redo belong only to Definition, never to the read-only canvas.
- The legacy source's `DRAWING_RECIPES` and detailed tests in `tests/isotope-wiring-li6-line-colors.test.mjs` define the newer H–Na drawings. Older contour descriptions coexist in the README but are not the current recipe contract. Higher isotope contour checks remain separate.
- `apps/isotope-wiring/README.md` and `src/domain/route.ts` define a separate typed authored-incidence routing policy. Its current active-color/visit-once rules are not the retired legacy drawing-order algorithm.

Those declarations predate this repair. Reintroducing an old API, EP paths, a custom-drawing fallback or canvas comparison overlays would violate them. This review therefore explicitly supersedes the obsolete assertions and replaces their coverage; it does not skip or mark failing cases TODO.

## Failure-to-coverage accounting

| Previous failures | Count | Reviewed resolution and replacement checks |
|---|---:|---|
| Missing legacy `traceAlternatingEdges` | 6 | Test removal of routing exports, animation/trace controls and stale route flags; retain authored arrows and immutable model records. A positive detector control fails on an injected legacy routing export. Check the separate typed route with its own freshly compiled checker, not by claiming these absence tests prove its policy. |
| Old H–Na contour / default EP-view expectations | 16 | Default rendering must stay Neutron-only. Fifteen current recipe cases check identity, inheritance, exact viewports, arrow/brace counts, the retained base diagonal, inventories, model checks and unchanged input definitions in inline/export modes. The existing detailed recipe suite retains exact edge, reflection and arrow-position checks. H/He keeps the actual triangle/square assertions without restoring EP rendering. A malformed SVG is a positive failure control. |
| Earlier Ne20 colors/green-diagonal orientation | 2 | Freeze the current authored overrides and transformed green diagonals, including the fact that historical edge IDs named red/blue do not determine current colors. Keep inherited geometry, arrow counts, exports and Na23 isolation checks. No source colors or geometry are changed by this review. |
| Keyboard entry expected on unsupported V51 | 1 | Verify a supported drawing's requested cell, explicit undefined-drawing behavior for V51 and a visible fallback for absent/hidden cell IDs. Fix the actual renderer defect where a nonvisible requested cell left no keyboard entry. Read-only exports retain labels without interactive controls. |
| Old graphical comparison overlays | 3 | Verify added/removed/changed ownership and retained before/after record values in the comparison data, not fabricated canvas paths. Edited drawings remain undefined even when model predicates pass; duplicate occupancy still fails despite unchanged inventory. Removed shells/cells stay in record differences, viewport calculations remain bounded and stale overlay flags cannot change the authored export. |
| **Total** | **28** | All three affected files retain 83 active test cases. The full combined suite must retain all 371 cases with no skips/TODOs. |

The focus fallback is the only change to the legacy renderer in this review. It selects an actually visible owned cell when a requested focus/selection is absent from the authored template. It neither creates new incidence nor changes drawing recipes, inventory, coordinate geometry or scientific claims.

## Reproduction

```sh
node --test tests/isotope-wiring-alternating-route.test.mjs tests/isotope-wiring-li6-line-colors.test.mjs tests/isotope-wiring-research.test.mjs
node --test tests/isotope-wiring-*.test.mjs tests/isotope-reference-fts.test.mjs tests/simplex-step-span.test.mjs tests/two-attractor-field.test.mjs
node scripts/test-isotope-wiring-no-rendered-routing.mjs
```

For the independent typed routing checker, use that application's installed/pinned toolchain from `apps/isotope-wiring/`:

```sh
node node_modules/typescript/bin/tsc -p tsconfig.verify.json
node .verification/scripts/check-routing.js
```

The typed checker is separate evidence: its policy is not claimed equivalent to the retired source inferred from strokes. Likewise, a passing software predicate does not establish placement, a physical isotope or a native field operation. The old 33-workflow browser report is not refreshed by these checks; the maintained current browser matrix remains task T04.
