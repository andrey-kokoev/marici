# Isotope Wiring — retained requirements

This is the replacement Vue application, not a wrapper around the legacy HTML. Later operator scope corrections supersede the earlier speculative project/workspace architecture.

## Scope

Keep authored diagram identities/connectivity/directions/layout, basic isotope facts and source citations, rendering, selection, labels, inspection and strict checking. Subsequent operator instruction authorizes us to create the Ne-20 model/labels and implement alternating left/right with 10 → 3. Do not demand an existing labeled diagram from the operator. Unresolved models still retain an explicit unresolved marker.

Removed from scope: project-file import/export/recovery, project containers, saving/storage machinery, editing/mutation protocols, duplicate workspace/session models, unused catalog/preferences/camera/playback command scaffolding, scientific attestation operations/digests/timestamps, Turtle attachments, application tool-version records and speculative PWA worker/update protocols. These are not deferred tasks to recreate under new names. Later explicit exception: colored-edge clicks alternate color change and direction reversal per edge, and those edits plus the next operation persist across reloads in this browser. This authorizes narrow per-diagram overrides, not general project files or a storage framework. The later UI carry-over instruction authorizes the existing Zoom/Fit/Move controls; these are implemented as presentation-only camera state, not editing or a general camera-command framework.

PWA delivery and the requested traversal/display behavior below remain requirements. The minimal alternating-route implementation is described in `README.md`; removing premature protocols does not waive remaining delivery requirements.

## Tooling and typing

- Vue 3 SFCs, `<script setup lang="ts">`, Composition API, focused composables, Pinia, Vite and Zod. Oxlint/Oxfmt only; no ESLint/Prettier.
- Verify stable releases when selecting dependencies, pin exact versions and maintain lockfiles. No prereleases, floating updates, silent compatibility overrides or unapproved dependencies.
- Explicit exceptions authorize the separate TypeScript 6 Vue checker while retaining TypeScript 7 for existing checks, and Vite 8.3.5 instead of age-blocked 8.3.6. Neither permits weakened checking. The removed JSON decoder is no longer a dependency.
- No CI, hosted checks, workflows or legacy-test repair.
- No explicit or inferred application-level `any` or `unknown`, unsafe data flows, suppressions, unsafe assertions/non-null assertions, unchecked JavaScript rewrites or ambient declarations pretending to validate data. Literal `as const` narrowing is permitted.
- Zod defines application data structures; infer types from it rather than maintaining parallel interfaces. Actual framework/browser types and behavioral function signatures need not be duplicated as schemas.
- No unconstrained `z.any`, `z.unknown`, `z.custom`, aliases or generated declarations that conceal unsafe values.
- Third-party declaration internals are not application data. Consuming unsafe member/call results is still prohibited.
- Check all owned sources: domain, components/templates, stores/composables, configuration, adapters/workers if ever approved, declarations and verification helpers. Independent coverage must catch excluded files. Vite transpilation is not type checking.

All checking projects retain:

```json
{
  "strict": true,
  "allowJs": false,
  "noUncheckedIndexedAccess": true,
  "exactOptionalPropertyTypes": true,
  "noImplicitOverride": true,
  "noFallthroughCasesInSwitch": true,
  "noImplicitReturns": true,
  "noPropertyAccessFromIndexSignature": true
}
```

Maintain positive and negative local probes for unsafe inferred values, callbacks/catches, generic results, Vue scripts/templates, suppression attempts and coverage escapes. Local type checks, lint, formatting and production build must be separately runnable and fail nonzero. No checker may silently skip an unsupported source or failed type lookup.

## Pre-Ne-20 catalog diagrams

The operator requests editable wiring models for all 17 catalog entries before Neon-20 and rejects preserving the first four green-only drafts. Use the old page's named drawings as the visual reference. Author identities and incidence explicitly; do not extract connectivity from SVG or generate geometry from nuclear counts. Where that reference supplies no colored arrows (H/He), new arrow assignments are implementation choices, not recovered facts. Preserve Ne-20, its existing edits and named versions. Apply the current generic editing/traversal controls, but do not silently recolor the legacy-derived models to force completed routes.

Latest He-3 correction supersedes the legacy side triangles: retain the four colored diamond edges and replace both outer green triangles with one horizontal undirected green bar between left and right. Remove the outer vertices; do not create a center junction.

## Ownership and model integrity

- Components render records and emit identity-based intent; they do not reconstruct adjacency, choose routes or own competing document copies.
- Composables coordinate one behavior and clean up any effects they create. No hidden global state or renamed monolith.
- Pinia owns the in-memory active diagram and shared UI state; explicitly pinned reference diagrams are read-only snapshots. Validate data and selection boundaries before assignment; store no DOM-derived graph or DOM nodes.
- Domain/model validation is independent of Vue, SVG, browser storage and screen measurements.
- Red and blue segment counts must be equal for a valid traversal result. Count distinct model edges, not repeated route steps. Unbalanced drafts remain editable and diagnostic playback is allowed, but display counts immediately and never mark an unbalanced traversal `completed`, even if it closes. No automatic recoloring.
- Vertex/edge identities, endpoint incidence, directions, roles and any junction ordering are authored facts. Never infer them by coordinate matching, DOM order, path segmentation, CSS, marker proximity or hit-test position.
- Crossing/coincident drawings do not merge identities. Resolve obscured-record selection explicitly without silently merging edges.
- Layout endpoints derive from endpoint identities. Do not maintain a separately editable pair of endpoint coordinates.
- The active diagram viewport is the drawing surface, not a dashboard content panel. The title and route readouts overlay it without reserving rows or reducing SVG dimensions. All toolbar controls belong in the appbar, not in the diagram viewport. Use one playback button: `|>` starts/resumes (or restarts after completion), `||` pauses. Add `<` and `>` steppers with exact HTML titles `step back` / `step forward`; stepping pauses and moves to adjacent segment boundaries, clamped to route bounds. Keep Clear path. Empty overlay space passes pointer input through to the drawing.
- Direction arrow marks belong at segment midpoints, not endpoints. For polylines, use the half arc-length position and local tangent. Preserve authored directions; undirected/unresolved edges remain arrowless in active and reference views.
- Rendering, label visibility, DOM order, theme, viewport, zoom and device scale must not change semantic graph data or an eventual route.
- Rational authored coordinates remain exact in the model; floating-point projection is presentation only.
- Basic isotope consistency is not scientific authentication. Unknown electron/charge values must not be fabricated. Synthetic geometry must not pretend to be a reviewed isotope model.

## Concrete UI and domain requirements

The operator subsequently requested carrying over the real application UI: panels, docking pins, graph reference pins and selectors. These are actual in-memory controls, not permission to restore file/storage/editing machinery or the removed records dump. The implemented subset and remaining parity gaps are listed in `README.md`.

- One label per edge at its model-defined midpoint, not grouped IDs.
- **Show edge labels** remains. Later operator instruction removes the records panel, its Inspect control, demo controls and disclaimer/explanatory copy from the app.
- Eventually provide **Path taken**, distinct from animation frames, with unambiguous aliases. Preserve it after stopping; reset for a new run or Clear. Do not invent a successful continuation for unresolved decisions.
- Trace results must identify the document/policy snapshot. Presentation changes must not change route decisions. Playback presents a computed route; it never computes the next edge from animation geometry.

The following label requirements must be implemented in the new authored model (the operator clarified that we create its identities and labels):

- **17 and 22 vertical**.
- Add undirected vertical green **27**, joining **upper-tip → top-junction**. Its crossing with horizontal 12 is not a junction. Retain all existing IDs, endpoints, colors, directions and saved edits; do not reuse retired 5.
- Shell 2 contains both diagonals of all four diamonds. Append the four missing undirected green diagonals as **23–26**, retaining labels 1–22 and the existing endpoint vertices; diagonal crossings are not new junctions.
- Latest shell-2 rule: every NW–SE side is **red pointing SE**, and every SW–NE side is **blue pointing NE**. This supersedes earlier individual assignments (including 4 blue and 18 red). Shell 1 and horizontal/vertical undirected green segments remain unchanged. Preserve edge identities and labels. Later explicit correction: remove duplicate 5 and retain 18, including its saved color/direction and click phase. Do not renumber remaining edges.
- Approved two-pair color swap: **13 and 14 blue; 16 and 20 red**, preserving arrows and other saved edits. Apply once to existing v1 overrides, then respect subsequent UI edits (v2). Under policy v11 this yielded a 30-traversal closed path for the operator's reported configuration, but its 9-red/7-blue imbalance is invalid under the subsequently required balance check. Later routing corrections may change that historical trace. Closure alone does not validate it; do not replace their other directions with bundled defaults. Base directions: **14 bottom-left → bottom-tip; 13 bottom-right → bottom-tip** (14 reversed again).
- The later three-pair optimization was rejected. Restore the verified 28-step operator configuration: **4/13/19 red; 16/18/20 blue**, preserving its other colors and all arrows. Existing v2 saves are untouched; trial v3 saves roll back these six colors to v2 once. The verified configuration has 8 red and 8 blue edges.
- Latest overrides: **2 blue and reversed: center → middle-right**; **4 red, center → bottom-right**; **15 red, bottom-left → left-tip** (latest reversals of 4/15). Preserve IDs; this supersedes the preceding colors/directions for 2/4.
- Reverse **red 19** to **right tip → middle-right**, permitting **26 → 19**, without changing its color or identity.
- Starting from red **8**, the disputed junction must continue **10 → 3 → 7**, not **10 → 1** or **3 → 2**. The later operator correction makes green segments undirected: they admit traversal from either endpoint and have no arrow marks.
- **Same-color arrows first:** the latest explicit operator confirmation supersedes the removal of own-color priority. Unless continuing straight after green, an eligible, unvisited active-color arrow must be taken ahead of green regardless of left/right preference, but never against its arrowhead. Multiple same-color exits use angular ranking. Thus **3 → 19** takes precedence over green 7 when edited red 19 is direction-eligible.
- **Straight green continuation:** after arriving on green, take an available straight green continuation before any colored exit or turning green exit, preserving the pending turn. This applies generally, including **26 → 25** rather than 24 and **24 → 23**. This outranks same-color preference: **26 → 25 → 15**, when 15 is eligible, rather than **26 → 21**. Eligibility guards remain in force.
- **Keep left / keep right** selects the leftmost/rightmost available non-reversing exit, not an arbitrary exit in that half-plane. After straight-green priority and then same-color preference, compare the remaining exits in one signed angular order. Rightmost can be a left turn, and leftmost can be a right turn. There is no opposite-side fallback that reverses the requested comparison. The previous global opposite-extreme rule was an assistant-added interpretation and is withdrawn. Different angles are not an ambiguity. Implement the rule generally, without per-edge continuation exceptions.
- The earlier operator continuation **15 → 6** is superseded by the latest reversal of 15, which now ends at left-tip. The earlier **22 → 2** discrepancy remains in the audit history, but the latest reversal/color change of 2 now supersedes that continuation: 2 is blue and directed into middle-right. This model change does not establish that the underlying alternation interpretation was corrected. Do not claim full traversal conformance.
- **Red and blue edges are strictly visit-once per run.** The other color is unavailable until all edges of the active color have been visited. Upon exhaustion, switch own color and flip the pending left/right preference together, exactly once for that transition, immediately before choosing the next exit. Do not flip it again while entering that exit, even if it turns. The reported balanced configuration must preserve **13 → 14 → 6** (the right preference at 13 survives onto 14). Thereafter ordinary non-straight moves alternate again: after the final red, blue becomes own color immediately and has own-color priority at that same junction. The assistant-added handoff exception is removed: eligible blue 14 must follow last-red 13 instead of green 24. This is a turn-preference change, not an arrow reversal; at last-red 14, green 6 is selected only if own-color blue 18 is ineligible; it cannot outrank an eligible blue arrow. Preserve this phase across green travel; straight-green priority remains first. Green connectors may be reused; the first colored edge establishes the active color. Filter eligibility before applying the pending left/right preference. An unreachable remaining segment does not permit an early switch or a colored revisit. Preserve immediate-reversal restrictions; stop explicitly if these constraints block continuation. Completion means all red and blue edges visited once, not merely reaching a dead end. Loop detection includes active color and visited colored IDs.
- The old sequence `8 → 12 → 10 → 3 → 2 → 13 → 14` is not an approved general traversal specification.

No automatic extraction of identity/aliases from the old DOM or approximate SVG-routing algorithm is permitted. Legacy output and screenshots may inform manual review, not establish authority.

### Persistent edge editing

- First click on each directed red/blue edge changes red ↔ blue; the next reverses its direction, then repeat independently per edge. Labels use the same click action. The start-edge selector selects without editing; Move mode must not edit during drags.
- Persist final color, direction, next operation, edge identity and original endpoint identities in browser-local storage. Validate decoded values and their compatibility before application. No endpoint rewiring, vertex movement, label reassignment, green conversion or edits to pinned snapshots.
- Successful saves advance the document revision and stop/clear the old route. Preserve camera framing. Failed saves do not apply edits or advance the click cycle. Corrupt/incompatible saved data must be reported and retained, not silently discarded or overwritten.
- Persistence is specific to this browser/origin; it is not repository mutation or cross-device synchronization.

### Named versions

- Keep the toolbar limited to the Versions button: no version-status or empty-state text. Keep useful comparison information inside the dialog only when versions exist; avoid duplicate explanatory copy and use the short isotope name for context.
- The Versions dialog must focus its name field on opening, support Escape/Close/outside dismissal without passing that click to the graph, and return focus to its opener. Successful Load closes it and focuses the graph; Save/Delete must not strand focus on a disabled control. Show an explicit empty state and distinguish it from an unreadable library. Separate transient operation feedback from a current content-comparison indicator that includes click phases and start/turn settings, retains its meaning after reload, and is not truncated by long names. Name the diagram inside the dialog; use neutral saved-version selection wording for both Load and Delete. Refresh the library on open and storage events. Block Save with an explanation when the library is unreadable or full; re-enable it after recovery. Clear obsolete feedback on reopening, new input or working-state changes. Verify empty and populated compact layouts separately, requiring all expected controls rather than skipping missing ones. Keep dialog bounds and scrollable controls reachable on narrow/short viewports.

The operator additionally authorizes browser-local named snapshots of diagram edits, not a general project-file/workspace framework.

- Save complete colored-edge state (colors, arrows, next operation), start edge and first turn, scoped per diagram. Preserve existing geometry/identities; no graph is reconstructed from storage.
- Persist names and snapshots across reloads. Reject duplicate names rather than silently overwriting. Loading and deleting require explicit confirmation.
- Loading restores the whole snapshot, advances the document reference, clears stale route/playback and persists restored active edits and start/turn settings together before assigning them. Refresh must retain that working state without another Load action; do not show an arbitrarily selected saved name as though it were the active version. Preserve camera framing and pinned references. Deleting a saved version leaves active edits unchanged.
- Saved versions are immutable snapshots. Later edge edits must not mutate saved copies, and automatic live-edit migrations must not recolor named snapshots. Current routing rules apply when loading.
- Validate name, document, complete edge coverage and topology/geometry compatibility. Retain corrupt/incompatible saved data and report failures. Failed writes must not change active or saved state. Unbalanced drafts remain saveable but never acquire validity from being named.

### Unresolved before traversal

Diamond semantics; distinct/shared/invalid coincident sides; physical meaning of colors (traversal eligibility is now specified above); traversable directions; starting direction and turn preference; definition of left/right at multi-exit junctions; straight-through alternation; ambiguity/reversal/repetition/termination; whether ordering is authored or follows an approved exact-model rule; and which semantic changes invalidate a route.

Alternating left/right and the required 10 → 3 junction are confirmed. The new model and other concrete implementation choices are proposals documented in `README.md`, not silently inferred operator approval. Ambiguous/missing continuations stop explicitly; no drawing-order tie-break is allowed. The later keep-left/keep-right correction supersedes the earlier missing-side stop proposal.

## PWA requirement — implementation not selected

- Localhost development; secure-context deployment, not `file://` or runtime CDN dependencies for core functionality.
- Offline readiness must correspond to a complete installed application and declared bundled catalog/diagram feature set, verified by real offline exercises—not merely schema-shaped claims.
- Missing optional data must be explicit. Interrupted installation must not advertise a partial version as ready.
- Updates must be visible and deferrable, with no incompatible application/data mix or forced reload during active playback.
- No PWA plugin or hand-designed message protocol is automatically authorized. Verify compatibility and use the minimal mechanism needed when this feature is implemented.

## Acceptance and remaining decisions

The local checking and browser-smoke commands are in `README.md`. Preserve core graph, layout, isotope and selection regressions; remove tests of removed speculative features rather than keeping those features alive for their tests.

Still required: review of the newly authored Ne-20 model and explicit corner-case conventions, PWA mechanism/offline acceptance, comprehensive rendering/accessibility/performance/browser checks. A synthetic smoke test or successful build is not full application acceptance. Do not add new functionality merely because it appears in an assistant-generated plan.
