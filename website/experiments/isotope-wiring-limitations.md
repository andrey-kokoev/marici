# Isotope wiring: validation and export limits

[Return to the editor](/experiments/isotope-wiring) · [Separate 3D workbench](/experiments/construction-workbench)

**[Which editor is hosted? Typed-app and Morse status](/experiments/typed-wiring-development)** — `apps/isotope-wiring/` is a separate development-only application, not the source of this iframe or standalone download. Its Morse dialog describes authored incidence plus a supplied rotation/handle convention; it is not a computed smooth atlas, gradient flow or physical nuclear surface.

The hosted editor embeds the standalone `examples/isotope-wiring/index.html`. Its original counts, delta compiler and File operations belong to the **legacy implementation**. Both hosted and direct-file sessions run the same embedded structural adapter and model evaluator: validation exposes findings, **Definition → Compare stored records** retains before/after record values, and the cell inspector shows lattice ports and shared-support neighbors. The canvas is read-only and Neutron-only: it does not infer routing from SVG, display record-difference overlays or invent a sketch for edited/unsupported definitions. These additions do not replace the editing engine. Direct-file sessions need no network assets or server. An incomplete HTML copy missing the core explicitly marks checks unavailable. A valid definition or matching inventory is not an established nuclear geometry, isotope stability result, or complete equivalence certificate.

## Repaired cases and remaining limits

| Case | Current behavior | Remaining boundary |
|---|---|---|
| Replay an identity delta | `compile(diff(A,A), {A})` replays against the supplied snapshot. Same-ID application saves an absolute draft; stored dependency cycles are rejected before mutation. | This does not supply immutable revision IDs or make a self-referential project a snapshot. |
| Base-only metadata | Generated deltas explicitly delete absent top-level metadata using `remove-metadata` operations. | Older editor versions cannot read this operation. Graph comparison still does not certify arbitrary whole-document replay, graph-array order, or custom fields named `base` or `ops`. |
| Generated cell IDs | Larger coordinates are separated; existing single-digit fixture IDs are unchanged. Uniqueness is checked across shell sizes 1–20. | Ambiguous previously saved files are not automatically migrated. |
| Change a delta base | A mutable base can change the compiled target without changing the delta. | Keep the actual base and its provenance, not just a definition name or delta text. |

Retain original project exports and **absolute definitions** outside the app before editing or moving between browser locations. Inspect metadata as well as graph records when comparing exports. This is a caution, **not a certified persistence or roundtrip guarantee**. Do not rely solely on delta exports, displayed counts or an apparently unchanged drawing as a backup check.

**Verified software checkpoint: `3ace86e33`, rechecked during currency correction iteration 1.** The narrow legacy core suite contains 14 passing checks with no TODOs, including the three repaired regressions, true-cycle rejection, metadata deletion and exhaustive generated-ID uniqueness over the supported coordinate range. At that historical checkpoint the separate broader software baseline was **343/371 passing, with 28 failures and zero TODOs**, in traversal/color/rendering tests; those failures were not the three repaired core cases.

**Currency correction iteration 2:** the reviewed combined suite now has **371/371 passing, with no skips or TODOs**. The [regression contract review](https://github.com/andrey-kokoev/marici/blob/main/docs/isotope-wiring-regression-contract.md) accounts for all 28 earlier failures and their replacement coverage. This is not a claim that an old routing algorithm or obsolete contour picture was proved correct: removed mechanisms stay removed. The renderer also now falls back to a visible keyboard target when the requested cell is absent from the authored template. It also retains counterexamples showing mutable-base dependence and loss of graph-array ordering. The Counts panel says **Graph records replay checked**: that check compares graph records, not the entire definition.

## Applied state and unapplied text

Wiring text drafts are stored separately from applied definitions and retained across
graph edits, Undo/Redo, reset and imports. Where local storage is available they also
survive reload. The editor explicitly reports session-only text if saving fails.
**Compare with applied JSON** lets you inspect current applied state without discarding
a draft. Applying retained text after its graph or delta base changes requires
confirmation; explicit text discard also asks for confirmation.

**Download text draft** saves the exact text, even if it is not valid JSON.
**File → Export all text drafts** archives all retained buffers, identified by isotope,
format and base, including buffers whose custom graph was reset. Project
and definition exports contain applied state, not unapplied buffers. Local browser
storage can be cleared and is not cloud sync or a durable backup. Keep external
exports. Same-ID Apply/import updates the current visible definition, and graph
save messages refer only to completion of the latest graph write.

<details><summary>Historical placement-trial UI — not current read-only canvas controls</summary>

The following two sections describe the earlier interactive placement workflow. Current Definition data operations and headless trial functions are separate from what the hosted canvas exposes; do not treat these historical instructions as current UI acceptance.

## Placement questions and alternatives

Question marks represent explicit `placementQuestions` anchors, not uncertainties
inferred from counts or from prose notes. Missing anchors remain unlocated; passing
model checks never removes a placement question. Markers survive SVG and project
export/import.

The **Try another placement** action, available both hosted and directly from file,
moves one owned EP record or neutron line witness within its existing shell.
Witness trials preserve H/V axis; an occupied destination axis fails the shared
model checks. Shell boundary witnesses are excluded because they are not cell-owned.
Explicit `witnessIds` question anchors follow relocated line witnesses; missing or
boundary anchors remain unlocated. It preserves inventory and supplied targets, checks the candidate
with the structural core, and shows original and trial at a matched shell scale.
A failed candidate remains visible but cannot be kept by this action. Keeping a
passing candidate creates a separate absolute definition with unresolved status;
it neither overwrites the source nor chooses an experimentally established placement.
The same candidate checks and source-isolation rules apply in direct-file sessions.
Trials are modal: background controls are inactive, Tab remains inside the dialog,
and Escape returns to the inspector. Configure first, then **Review comparison**;
the keep action is available only on the comparison step. Mobile shows the current
trial before the original so the candidate is visible before committing.

`node scripts/test-isotope-wiring-placement.mjs` checks preview isolation, rejection
of failed/stale candidates, unique alternatives, mobile/keyboard behavior and
fresh-context project replay. Add `--standalone` to run the same workflows over
`file://` with network disabled. `node scripts/test-isotope-wiring-witness-placement.mjs`
checks witness trials, including duplicate-axis rejection and editing vacated cells
without reusing a relocated record ID; add `--hosted` for the website run.

## Testing placement alternatives

The trial dialog's **Test placement alternatives** surveys same-shell destinations
for the selected record, at most eight per click. Coverage and unchecked destinations
are explicit. Results show inventory checks separately from overall checks and failed
predicates; selecting **Preview** does not save a candidate. Changing the record resets
results, and source edits make them stale.

O16's `s2-01-H` witness can move to `s2-00` and pass all supplied checks, while moving
it to `s2-10` fails duplicate-axis occupancy despite the same inventory. Thus inventory
agreement does not select a placement, and multiple passing definitions demonstrate
underdetermination by these predicates. This is not an experimental nuclear prediction.
Finding no passing alternative in a completed survey establishes neither physical
uniqueness nor uniqueness under other edits: routes/axes, shell, targets and all other records are fixed.
Unknown checks are not passes; partial surveys leave explicit unchecked cases.

`node scripts/test-isotope-wiring-survey.mjs` checks individual-trial agreement,
coverage/pagination, result inspection and source isolation offline; add `--hosted`
for the website. General composition, multi-record transformations and comparison
against physical observations remain outside this action.

</details>

## Core integration boundary

The inspected pending local development includes several headless layers. These source paths are provenance locators, not promises of a stable public API; uncommitted files may be absent from a clean checkout of the published revision.

| Layer | Implemented local scope | Limits that remain |
|---|---|---|
| `core/finite-diagrams.mjs` | Checked finite-incidence diagrams and structural maps; the embedded adapter constructs these diagrams for inspection. Pointwise finite limits/colimits and open-component gluing remain headless operations. | Fixed schema presentation; bounded software tests are not a formal proof of implementation correctness. Closure of extra model constraints does not follow from ambient closure. |
| `core/legacy-adapter.mjs` and attributed adapter | Live absolute-definition import supplies the editor's cell neighborhoods in both modes. Explicit support interfaces, model labels and retained-source recovery are also implemented. | Recovery uses the retained original source, not an inverse of bare incidence. A modified/glued object is not automatically exported back into a current legacy definition. |
| `core/model-predicates.mjs` and shared `model-evaluation.mjs` | The same predicate evaluator runs in Node and both editor modes, with localized verified/refuted/unknown/notApplicable statuses. Browser checks omit archival hashes; they are live findings, not export certificates. | Z/N and shell targets are supplied targets, not derived observables. Model-valid objects are not composition-closed under the tested gluing; typed counterexamples are retained, not deleted to fit counts. |
| `core/revisions.mjs` | In-memory immutable revisions, explicit ground rewrites, before-image undo, branch-head checks and dependency-complete bundle replay. | Undo restores a state while retaining a new history event. Browser autosave and legacy delta compilation do not use this revision engine. Generic rewrite matching, cross-engine migration and selective evidence transport are not supplied. |

The draft `examples/isotope-wiring/MACHINERY.md` and companion `core/CLOSURE.md`, `core/ADAPTER.md`, `core/MODEL.md` and `core/REVISIONS.md` specify these local boundaries. The browser integration is limited to checked structural import, model evaluation, neighborhoods, record differences and same-shell EP and neutron-line placement trials; it does not expose the remaining composition/revision machinery. Imported unknown fields may be retained without being interpreted as structural incidence.

A model predicate can pass while a source fixture still records an **unresolved placement**. Likewise, a typed gluing can fail model predicates even when its inventory matches the supplied targets. Neither passing software coherence checks nor choosing an isotope name derives measured nuclear content or physical adequacy.

## Reproduction and provenance

In a development checkout containing the pending suites, use:

```sh
node --test tests/isotope-wiring-core.test.mjs
node scripts/test-isotope-wiring-browsers.mjs
node scripts/check-isotope-wiring-browser-evidence.mjs
node --test tests/isotope-wiring-category.test.mjs tests/isotope-wiring-adapter.test.mjs tests/isotope-wiring-model.test.mjs tests/isotope-wiring-revisions.test.mjs
```

The first command checks the actual legacy source. The current browser matrix checks the Neutron-only contract, Definition replay, metadata deletion, fresh-context import/reload, rejected cyclic updates, missing-runtime/corrupt-data refusal and built-host/download behavior. Placement and survey functions are tested through isolated data APIs, not a retired placement dialog. The evidence command checks the recorded coverage and matching tested bytes; it does not replay browsers. The final command checks the independent software layers, not physical isotope claims. `node --test tests/isotope-wiring-research.test.mjs` additionally checks agreement between the browser-facing projection and Node evaluation. Test totals are snapshot-specific; inspect TODO, failure and scope fields rather than treating a process exit as a universal certificate.

Earlier scripts such as `test-isotope-wiring-standalone.mjs` contain retired EP-editing/canvas-overlay criteria and are not current acceptance tests. The current matrix replaces them with explicit Neutron-only, Definition, missing-runtime and download checks. `node --test tests/isotope-wiring-standalone.test.mjs`
checks the embedded runtime against maintained source functions. Maintainers regenerate
its marked HTML section with `node scripts/prepare-isotope-wiring-core.mjs` after core
changes; opening the delivered file needs no build step.

`node scripts/test-isotope-wiring-browsers.mjs` runs ten current-contract cases in each of Chromium, Firefox and WebKit, including a reachable-server network-isolation control. Missing engines and failures are recorded; unrun cases never count as passes.

**Historical browser report (first committed in `c1025e302`):** the source reported
33 passing Windows Playwright runs, including hosted/direct-file placement trials,
surveys, exports and fresh-context project replay. The exact tested source revision
and engine versions were not retained with that report; its commit identifies the
record, not an independently established execution checkpoint. That historical result is not current acceptance.

**Current recorded browser matrix (currency iteration 3): 30/30 runs passed**, with zero failures or unrun cases, on Chromium 151.0.7922.34, Firefox 153.0 and WebKit 26.5. Exact source hashes and per-case engine versions are recorded against base commit `3ace86e33` plus the tested dirty working tree. The [verification record and scope](https://github.com/andrey-kokoev/marici/blob/main/docs/isotope-wiring-browser-verification.md) identify the ten cases and explain why they are not the historical eleven-case/33-run matrix. They include direct-file and built-host behavior, storage/replay and data-API placement checks, not retired placement-dialog controls. The separate typed app, live deployment, real devices and screen readers are outside this record.

The same historical report described WebKit's native offline flag rejecting local-file
navigation on that Windows build, with HTTP(S) requests aborted through routing and
a dedicated reachable-server isolation check instead. Chromium and Firefox used native
offline mode. A new run must recheck the engine-specific behavior rather than treating
that workaround as a passing native-offline navigation test.

`node scripts/test-isotope-wiring-accessibility.mjs chromium` additionally exercises
keyboard cell navigation and focus return, panel dismissal, 44px coarse-pointer
controls, and emulated touch editing/panning at 320px. Arrow navigation follows
record order, not spatial proximity. Dense diagram cells may require zoom; pinch
and multi-touch navigation are not implemented. The historical report described keyboard, mouse panning and emulated
touch editing passing in all three engines, with continuous touch-drag injection
checked only in Chromium; this is not a current cross-engine result. Real-device and screen-reader testing remain open. The mobile inspector now sits below the graph,
which focuses on the selected shell rather than being covered by the panel.
`node scripts/test-isotope-wiring-ux.mjs` exercises these layouts, modal focus,
text-draft recovery and confirmation flows.

The [standalone editor source](https://github.com/andrey-kokoev/marici/blob/main/examples/isotope-wiring/index.html) and [embedding component](https://github.com/andrey-kokoev/marici/blob/main/website/.vitepress/components/IsotopeWiring.vue) identify the running implementation. Pending development documents are not linked as though already available in that published revision. This page documents bounded software repairs and residuals; it supplies no formal theorem or physical admission.
