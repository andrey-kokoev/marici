# UI review and regression ledger

## Current contract: Neutron-only

The operator subsequently removed EP wiring as a view/mechanism. This supersedes
all EP-view switching/editing criteria in the historical ledger below. There is no
view selector or EP renderer; old flags cannot reactivate it. Old references migrate
to Neutron-only, or show an explicit undefined-drawing placeholder. Definitions and
inventory validation remain data features. Undo/Redo and record comparisons belong
only to Definition, never to the read-only canvas.

Current acceptance commands:

- `node scripts/test-isotope-wiring-neutron-only.mjs`
- `node scripts/test-isotope-wiring-green-v.mjs temp/isotope-green-v`
- `node scripts/test-isotope-wiring-catalog-filters.mjs`
- `node scripts/test-isotope-wiring-catalog-scroll.mjs`

These cover removal of EP controls, legacy preference/reference migration, renderer
API refusal to restore EP paths, supported drawings, undefined/edited placeholders,
reference pinning/scale, definition-only undo, SVG/project exports and persistence.

## Historical review before the single-mechanism change

This tracks the numbered gaps discussed with the operator. It records concrete
acceptance checks, not a claim that all possible usability problems are eliminated.
The drawings, record inventories and physical interpretations are not redefined here.

## Evidence

All commands run from the repository root:

- **Boundaries:** `node scripts/test-isotope-wiring-ui-boundaries.mjs`
- **Failure paths:** `node scripts/test-isotope-wiring-ui-failure-paths.mjs temp/isotope-green-v`
- **References:** `node scripts/test-isotope-wiring-references.mjs temp/isotope-green-v`
- **Catalog:** `node scripts/test-isotope-wiring-catalog-filters.mjs`
- **Scrolling:** `node scripts/test-isotope-wiring-catalog-scroll.mjs`
- **Recovery:** `node scripts/test-isotope-wiring-ui-state.mjs`
- **Drawings:** `node scripts/test-isotope-wiring-green-v.mjs temp/isotope-green-v`

Failure-path checks include missing and throwing runtime methods, runtime recovery,
IndexedDB read failure followed by a successful save, stale/programmatic mutation
controls, keyboard Undo/Redo, full pin capacity, long imported names/distributions,
and header/help/comparison bounds at narrow widths. Screenshots supplement DOM
assertions; a long-name header overflow was found visually and then added to tests.

## Original gaps

| IDs | Closure / acceptance criterion | Evidence |
| --- | --- | --- |
| 1–2 | Footer is application storage status only. Declared item inventory is in the catalog; actual counts are explicitly labelled in validation details. | Boundaries |
| 3 | No repeated Neutron-only caption/legend. Side-by-side captions identify isotopes. | Drawings, Boundaries |
| 4–5 | Restore-built-in belongs to Definition; local theme belongs to Settings. Settings is absent when the host owns the theme. | Boundaries; markup inspection |
| 6 | Validation contains record checks, issues and collapsed inventory/serialization details, not comparison results or grammar. | Failure paths |
| 7 | Comparison source and Change details are beside Changes. Legend directs users there, not to the removed Counts location. | Failure paths |
| 8 | Graph / Definition are workspace modes; EP wiring / Neutron-only are visualizations; complete / changes-from-base are source formats. | Boundaries, Recovery |
| 9 | Search × clears text only; Clear all filters is a separate action. | Catalog |
| 10 | Record-editing labels use plain-language pair/line/boundary terms; Help defines EP, witnesses, cells, shells and source formats. | Failure paths; markup inspection |
| 11 | Inspection starts read-only, including in EP wiring. Edit records / Finish editing explicitly controls mutations and placement experiments. | Failure paths |
| 12 | Panel docking uses a panel-layout icon; reference pins use the pin icon. | Recovery; markup inspection |
| 13 | At most one saved reference per isotope ID, regardless of view changes. | Boundaries |
| 14 | Pinned items toggle off even at capacity. Full-capacity pin is focusable, has an accessible explanation, and gives visible feedback on activation without adding a reference. | Failure paths |
| 15 | Result reads “Record checks: Passed” under an explicitly non-physical scope. No redundant positive basic-check headline or “0 errors” apply toast. Runtime failure visibly reports unavailable. | Failure paths |
| 16 | Mass filter is labelled Mass, not A. | Markup inspection |
| 17 | Mouse/keyboard selection and navigation do not recenter an open list. | Scrolling |
| 18 | Catalog captions contain P/N/E and shell data, not repeated IDs. | Catalog |
| 19 | Captions wrap without clipping. Imported long names/distributions fit; header titles cannot overlap controls and retain a full-name tooltip. | Catalog, Failure paths; screenshots |
| 20 | Pagination is hidden for one page. | Catalog |
| 21 | Pin action is an icon on the active isotope row, not the toolbar. | References |
| 22 | References are beside the active drawing on the same background, with equal drawing areas and shared scale/camera. | References; screenshots |
| 23–24 | Saved list position is restored; initial fallback finds the selected item. Ordinary selection does not reset that position. | Scrolling |
| 25 | Tests assert layout bounds, including imported data, instead of checking only text presence. | Catalog, Failure paths |
| 26 | Tests assert reference alignment, dimensions, common scale and shared zoom/pan, not only their presence. | References |
| 27–28 | Functional checks are supplemented by failure injection, visual inspection and this scope/ownership ledger. These are ongoing verification practices, not guarantees against future UX mistakes. | Evidence above |

## Deeper gaps

| ID | Closure / acceptance criterion | Evidence |
| --- | --- | --- |
| D1 | Named sketches are only available for matching built-in records/targets. Edited definitions show actual EP wiring. Sketch-mode Undo/Redo and stale record controls cannot mutate data. | Failure paths |
| D2 | Help distinguishes EP record grammar from illustrative sketch shapes. | Failure paths; Help text |
| D3 | View selector reports the actual rendered view; unsupported sketches are disabled. | Boundaries, Recovery, Failure paths |
| D4 | Source format does not relabel the complete canvas drawing as a delta. | Boundaries; render inspection |
| D5 | Reference identity is the isotope, with its pinned record/view snapshot retained until unpinned. No duplicate isotope pins. | Boundaries, References |
| D6 | Project export/import includes workspace and references; restored references survive reload. Unapplied text drafts remain explicitly separate exports. | Boundaries |
| D7 | File distinguishes active graph SVG and canvas-with-references SVG. Canvas export contains all drawings under a common camera. | Boundaries |
| D8 | Active and reference drawings have isotope-name captions in comparison layouts. | Boundaries; screenshots |
| D9–D10 | Fit remains an action; a separate × fit readout describes relative magnification, not an absolute physical scale. | Boundaries |
| D11 | Unavailable or failed comparison runtime clears checked state and disables the control; recovery does not revive a stale overlay. | Failure paths |
| D12 | Pinning leaves keyboard focus in the active catalog row. | References, Boundaries |
| D13 | Application persistence, definition application, structural checks and serialization checks have separate scopes. Load errors are sticky across initialization and subsequent saves. | Boundaries, Failure paths |
| D14 | Obsolete footer inventory/validation control, handler and styles are removed. | Failure paths; source inspection |

## Verification limits

The listed scenarios are targeted regression coverage. They do not certify physical
models, replace user evaluation, or establish compatibility with every historical
suite whose expectations predate the new explicit editing and UI organization.
