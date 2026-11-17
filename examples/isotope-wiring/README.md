# Isotope Wiring

This is the working app for ongoing isotope-wiring development, promoted from
`research/chatgpt/isotope-wiring.html` at the operator's request. Its canonical
editable source and entrypoint is [`index.html`](index.html), not a generated copy.

### Ca-46 stacked visual trial

Select Ca46 and open **Stacked 3D trial ↗**, or open
[`ca46-stacked-trial.html`](ca46-stacked-trial.html) directly. It shows all sixteen
retained tetrahedral depth embeddings, a real shared shell-1/shell-2 vertex,
oblique/projection/side views, rotation, and an explicitly schematic wrapper
attachment map. The original wrapper projection remains available for comparison.
No physical frame law or wrapper surface is implied.

This companion page is generated from the geometry solver, not edited by hand:

```sh
node scripts/build-ca46-stacked-visual.mjs
node scripts/build-ca46-stacked-visual.mjs --check
node scripts/test-ca46-stacked-visual.mjs
```

The template is `core/render-stacked-visual.mjs`. Website preparation also copies
the companion page to `/experiments/ca46-stacked-trial.html`; the baseline editor
keeps its historical research-fixture geometry available to the audit scripts.

**The Ca46 editor has been restored to the enclosing-diamond presentation from
before the terminal-map and shell-layer redesigns.** The shell-1/shell-2 vertex
contact remains at (0,134), marked in amber. References and exports follow this
restored view. Wrapper placement still does not establish a transport law.
The rejected redesigns remain renderer-only experiments, explicitly selected by
`presentation: 'terminal-map'` or `presentation: 'layers'`; neither is the UI default.
The pure renderer's `stackedContact: true` option selects this editor presentation;
its default retains the historical contour-contact projection so earlier research
checks are not silently reinterpreted. Other isotopes are unchanged.

### No routing inferred from rendered geometry

The SVG-derived graph extraction and routing implementation has been removed.
The editor does not infer connectivity, direction, or traversal from rendered
positions. Its dependent animation, path readout, trace download, and rendered
segment ID labels/hover targets have also been removed. The authored drawing,
arrows, colors, inventory attachment, Inspect control, and pan/zoom remain.
No replacement routing algorithm is installed. The [regression contract review](../../docs/isotope-wiring-regression-contract.md) accounts for superseded routing, contour and canvas-overlay tests separately from the current authored-diagram checks.

`node scripts/test-isotope-wiring-no-rendered-routing.mjs` checks that the removed
pipeline stays absent and that the drawing and ordinary interactions still work.

### Ne-20 validated Turtle inventory

Select **Neon-20**, then **Validation** to see its attached nuclear inventory
(Z=10, N=10, A=20), source/byte digests, Turtle preview and download. The isotope
panel also labels the attachment. The browser checks embedded Turtle byte integrity;
SHACL and source-operation replay run during snapshot preparation, not in the browser.
Electron count and charge are unspecified in this inventory. The existing authored
drawing, shell declarations and electron assumptions remain separate and unchanged.
Edited working Z/N are compared against the snapshot; a mismatch is shown rather
than certifying the edits. Missing, malformed or byte-corrupted snapshots fail closed.

The standalone editor embeds the snapshot for offline/file use. Refresh it after
changing the Turtle artifact, reference resource or validation code:

```sh
uv run --python 3.12 --with pyshacl==0.30.1 --with rdflib==7.1.4 python scripts/prepare-isotope-wiring-turtle.py
node scripts/prepare-isotope-wiring-turtle.mjs
node scripts/prepare-isotope-wiring-public.mjs
node scripts/test-isotope-wiring-turtle.mjs
```

Both preparers support `--check`. The Python step performs actual validation and
writes `core/ne20-inventory.json`; the Node step verifies its input hashes and embeds
it. Website publication refuses stale snapshots or embeddings. The snapshot is local
build evidence, not a physical certificate or a signature authenticating arbitrary HTML.

### Reference labels

Click the grey dotted-underlined **Reference observations** heading beside any
diagram to select nuclear stability (on by default), natural abundance, reference
electron-shell populations, and reference proton/neutron counts. The heading gains
contrast on hover and keyboard focus. A nearby popover holds the controls and
source notes; Escape, an outside click, or its close button dismisses it. The
heading remains available even when all fields are hidden. Preferences are saved
locally and apply to the active diagram, pinned references, and labeled SVG exports.
These are reference observations, not predictions or validation of the drawing.
Missing isotope rows display “not available”; no stability is inferred from a
nearby isotope. Matching uses the definition's declared Z and N, not its name.

The offline editor embeds the Frictionless resource at
`research/matter/isotope-reference.resource.json`. After changing the reference:

```sh
node scripts/extract-isotope-reference.mjs
node scripts/prepare-isotope-wiring-reference.mjs
node scripts/prepare-isotope-wiring-public.mjs
node scripts/test-isotope-wiring-reference-labels.mjs
```

The publisher checks both extraction and embedding freshness. Spin/parity,
binding energies, radii and moments remain unavailable until added to the sourced
dataset; the earlier discussion's rounded example values are not embedded.

The website embeds this same source at `/experiments/isotope-wiring`, linked from
**Matter → Isotope wiring editor** and the construction index. The host component
`website/.vitepress/components/IsotopeWiring.vue` supplies the website's live theme
tokens without reloading the editor on light/dark changes. The app's `website-theme`
style block uses these tokens with standalone light/dark fallbacks. Direct-file
sessions follow the system theme until you choose a theme in **File**; that choice
is retained locally when browser storage is available.

The website page also offers **Open full-window editor** and **Download standalone
HTML**. VitePress configuration runs `scripts/prepare-isotope-wiring-public.mjs`
for both development and production builds: it checks embedded-core freshness and
copies the canonical HTML byte-for-byte to
`website/public/experiments/isotope-wiring-standalone.html`. That generated copy is
ignored by Git; edit this directory's `index.html`, never the public copy.
After `node node_modules/vitepress/bin/vitepress.js build website`, run
`node scripts/test-isotope-wiring-public.mjs` to check the actual production output,
route navigation, live core/survey, full-window launch and exact downloaded bytes.
It supports `ISOTOPE_BROWSER` like the other browser runners. Building and testing
locally do not deploy the site.

Open `index.html` directly in a browser. The standalone HTML contains its styles,
JavaScript, and isotope fixtures; no build step or external assets are required.
Use the File menu to export projects or definitions before moving between browser
locations or making changes, and import them to resume work.

The app provides isotope selection, graph and wiring views, absolute/delta JSON
definitions, cell editing, counts, validation, and import/export. In both hosted
and direct-file sessions, validation runs the structural core. In **Definition** mode,
**Compare stored records** shows added, removed and changed records against the selected
base, retaining before/after values and metadata distinctions. It does not draw canvas
overlays or turn edited records into a new authored sketch. The read-only canvas and its
SVG export retain only the supported authored drawing; undefined drawings remain explicit.
A record difference is not a physical transition or registration of measured structures.
Expand a change or failed check and use **Inspect** to select its record where supported.
The inspector shows exact lattice ports, occupied supports, and neighboring cells
sharing support. Checks update after edits and undo; unresolved placement remains
explicit even when the model checks pass. Both modes run the same embedded runtime,
including placement trials, without external code or assets. An incomplete copy
missing that runtime explicitly marks checks unavailable rather than passing them.
Fixtures and visual conventions
are working research inputs, not evidence of physical adequacy.

**Neutron-only mechanics.** Neutron-only is the sole renderer. There is no view
selector, EP wiring renderer, colored path overlay or EP editing path. Old preferences
and reference snapshots cannot restore those mechanics; references and SVG exports
are normalized to Neutron-only. Stored definitions and validation data are retained.
Named drawings currently support H1, H2, He3, He4, Li6, Li7, Be9, B10, B11, C12, C13, N14, N15, O16, O17, O18, F19, Ne20, Na23, Mg24, Mg25, Mg26, Al27, Si28, Si29, Si30, P31, S32, S33, S34, S36, Cl35, Cl37, Ar36, Ar38, Ar40, K39, K41, Ca40, Ca42, Ca43, Ca44, Ca46 and Sc45,
with records and inventory targets matching their built-in definition. Unsupported
or edited definitions show **Neutron drawing not defined**, never a fallback view.
Existing unsupported references retain their data and show the same placeholder;
new references require a defined drawing.
The current H–Na drawings are the explicit `DRAWING_RECIPES` in `index.html` and the
independent edge/arrow expectations in `tests/isotope-wiring-li6-line-colors.test.mjs`.
Li7 inherits Li6 with vertical braces; successive named recipes retain authored
translations/reflections and added triangle sides. Ne20 uses its declared color overrides
and rotated green diagonals: edge IDs containing `red` or `blue` are historical identifiers,
not a rule deriving current colors. Inventories and physical interpretation remain separate.

<details><summary>Historical H–Na contour description — superseded by the current authored recipes</summary>

H1 is an open triangle (two edges), H2 a closed triangle, He3 a square with two outward Vs closed by vertical outer edges
attached at its left and right vertices, and He4 a square
with both diagonals. Li6 uses that crossed first-shell square plus a closed triangle whose apex directly
shares the first-shell bottom vertex, with no surrounding second-shell sector frame;
its attachment arrangement is a provisional sketch. Li7 retains one upright triangle,
inset inside a second-shell square that meets the first-shell bottom vertex.
Be9 uses that same outer square, replacing the inner triangle with a square
crossed by both diagonals. B10 adds a triangle below, attached at the
bottom vertex of that inner second-shell square, without a shell-2 outer wrapper.
B10's first and second crossed squares share a vertex, with no gap.
B11 adds the expanded shell-2 wrapper around the inset crossed square and triangle,
without a separate empty square below. C12 has three crossed squares joined
vertex-to-vertex, with neither a shell-2 wrapper nor a lower empty square.
C13 adds the shell-2 outer square enclosing the lower two crossed squares,
with a small inset as in B11; there is no separate empty square.
N14 keeps C12's crossed squares in place and adds a closed triangle rotated
90 degrees counterclockwise about the shared vertex of the second and third
squares, filling the right-hand gap between them. There is no wrapper.
N15 adds the shell-2 neutron square around the lower two crossed squares and
rotated triangle, with the same small inset as C13.
O16 keeps N14's three crossed squares and right-hand triangle, adding its mirror
image on the left of the axis. There is no shell-2 wrapper.
O17 adds that wrapper around O16's lower two crossed squares and mirrored
triangles, using the same small inset as N15.
O18 uses C13's wrapped layout with a fully crossed square in the right-hand
shell-2 slot and an uncrossed square in the left-hand slot.
F19 retains O17's wrapper and left-hand triangle, replacing only the right-hand
triangle with a fully crossed square.
Ne20 removes the shell-2 wrapper and expands the left-hand triangle into a fully
crossed square too. All five squares are crossed, with no gap below shell 1.
Na23 adds the shell-2 wrapper around that four-square cluster, with the usual
small inset, and a closed triangle growing downward from the wrapper's bottom
vertex. The triangle represents the visible `s3-00` cell; no shell-3 wrapper is drawn.

</details>

The following higher-isotope contour checks retain their separately scoped fixtures:

Mg24 is a provisional continuation: the Na23 bottom triangle becomes a fully
crossed square, with the shell-2 neutron wrapper removed. All six crossed squares
join without gaps. Under the requested drawing convention, each PE triangle
contains one N, so no additional wrapper is drawn for Mg24. Its fixture has 12 P,
12 N and shell inventory `[2,8,2]`; this is not a claim about nuclear geometry.
Mg25 is the next provisional drawing: the same six crossed squares plus a
shell-2 neutron wrapper, with the bottom crossed square attached to its bottom
vertex. Its fixture has 12 P, 13 N and unchanged shell inventory `[2,8,2]`.
Mg26 provisionally adds a shell-3 neutron wrapper around the bottom crossed
square. The two wrappers meet at a vertex; six crossed squares plus two wrappers
represent 14 N under the requested convention. Its fixture has 12 P, 14 N and
shell inventory `[2,8,2]`.
Al27 provisionally replaces Mg26's shell-3 wrapper with a triangle attached below
the bottom crossed square, retaining the shell-2 wrapper. Six crossed squares,
one PE triangle and one wrapper represent 14 N under the requested convention;
the fixture has 13 P, 14 N and shell inventory `[2,8,3]`.
Si28 provisionally completes Al27's bottom triangle as a crossed square and
removes the remaining shell-2 wrapper. Seven crossed squares join without gaps,
representing 14 PE and 14 N under the requested convention. The fixture retains
14 N and has 14 P with shell inventory `[2,8,4]`.
Si29 provisionally adds a shell-2 neutron wrapper to Si28's seven crossed squares,
leaving shell 3 unwrapped. The fixture has 14 P, 15 N and unchanged shell inventory
`[2,8,4]`; seven crossed squares plus one wrapper represent 15 N under the convention.
Si30 provisionally adds a shell-3 wrapper enclosing both lower crossed squares.
The shell-2 and shell-3 wrappers meet at a vertex. Seven crossed squares plus two
wrappers represent 16 N; the fixture has 14 P, 16 N and shell inventory `[2,8,4]`.
P31 provisionally replaces the shell-3 wrapper with a right-hand triangle between
its two crossed squares, retaining the shell-2 wrapper. Seven crossed squares,
one PE triangle and one wrapper represent 16 N. Its fixture has 15 P, 16 N and
shell inventory `[2,8,5]`.
S32 provisionally adds the mirrored left-hand triangle in shell 3 and removes
the shell-2 wrapper. Seven crossed squares plus two PE triangles represent
16 PE and 16 N under the requested convention, with no wrappers. Its fixture
has shell inventory `[2,8,6]`.
S33 provisionally adds the shell-2 neutron wrapper to S32's geometry, retaining
both shell-3 side triangles without a shell-3 wrapper. Seven crossed squares,
two PE triangles and one wrapper represent 17 N. The fixture has 16 P, 17 N
and unchanged shell inventory `[2,8,6]`.
S34 provisionally adds the shell-3 wrapper around S33's crossed squares and
mirrored triangles. Seven crossed squares, two PE triangles and two wrappers
represent 18 N; its fixture has 16 P, 18 N and shell inventory `[2,8,6]`.
S36 consolidates the two shell-3 PE triangles into one right-hand crossed square
at `s3-01`, moving the `s3-11` PE record there. An uncrossed neutron-only square
occupies the left (`s3-11`), replacing the second shell-2 wrapper. One shell-2
wrapper and two shell-3 wrappers remain. Eight crossed squares, one neutron-only
square and three wrappers represent 16 PE and 20 N under the provisional convention.
Its fixture retains shell inventory `[2,8,6]`; this is not established nuclear
geometry. S35 is radioactive and is skipped.
Cl35 provisionally completes S34's right shell-3 triangle into a fully crossed
square and removes the shell-3 wrapper. The left triangle and shell-2 wrapper
remain: eight crossed squares, one PE triangle and one wrapper represent 18 N.
Its fixture has 17 P, 18 N and shell inventory `[2,8,7]`.
Cl37 provisionally keeps Cl35's PE shapes and adds two shell-3 neutron wrappers;
shell 2 retains its single wrapper. Eight crossed squares, one PE triangle and three contours
represent 20 N. Its fixture has 17 P, 20 N and unchanged shell inventory `[2,8,7]`.
The extra-contour placement is a trial, not established nuclear geometry; Cl36
is radioactive and is skipped.
Ar36 provisionally completes Cl35's left shell-3 triangle into a fully crossed
square and removes the remaining shell-2 wrapper. Nine crossed squares with no
neutron-only contours represent 18 PE and 18 N under the drawing convention.
Its fixture has 18 P, 18 N and shell inventory `[2,8,8]`; the layout is illustrative,
not measured nuclear geometry.
The next five stable-isotope trials retain Ar36's nine crossed-square core:

| Trial | P / N | Shell inventory | Provisional additions |
| --- | --- | --- | --- |
| Ar38 | 18 / 20 | `[2,8,8]` | One neutron wrapper each on shells 2 and 3 |
| Ar40 | 18 / 22 | `[2,8,8]` | Two neutron wrappers each on shells 2 and 3 |
| K39 | 19 / 20 | `[2,8,8,1]` | Shell-4 PE triangle; one shell-3 wrapper |
| K41 | 19 / 22 | `[2,8,8,1]` | Shell-4 PE triangle; one shell-2 wrapper and two shell-3 wrappers |
| Ca40 | 20 / 20 | `[2,8,8,2]` | Shell-4 crossed square; no wrappers |

The following five trials retain the shell-4 crossed square. Wrapper counts below
are listed for shells 2, 3, 4; a dash means unwrapped, excluded from ordering.

| Trial | P / N | Shell inventory | Wrappers (2 / 3 / 4) |
| --- | --- | --- | --- |
| Ca42 | 20 / 22 | `[2,8,8,2]` | 1 / 1 / — |
| Ca43 | 20 / 23 | `[2,8,8,2]` | 1 / 2 / — |
| Ca44 | 20 / 24 | `[2,8,8,2]` | 1 / 2 / 1, using coherence spans below |
| Ca46 | 20 / 26 | `[2,8,8,2]` | 1 / 2 / 3, spanning adjacent shell pairs (see below) |
| Sc45 | 21 / 24 | `[2,8,9,2]` | 1 / 2 / — |

An explicit, non-completing NNPE/NNNN path-reversal audit is available separately:
[contract, checks, and missing native bridge](PATH-REVERSAL.md). Run
`node scripts/check-isotope-path-reversal.mjs`; the current Ca46 fixture correctly
reports `unknown` because its native path topology has not been declared.
Inventory success does not imply path reversibility. In the current path
interpretation, each two-PE crossed square is a tetrahedron viewed from above:
four vertices, six edges. Its diagonals are opposite neutron legs crossing only
in projection, never a central graph junction. The connected-path trial records
this explicitly without assigning a metric depth or frame-transport law.
A separate layered trial now retains PE cycles, local neutron spaces, and wrapper
transport with explicit candidate interfaces; see the layered section of
[PATH-REVERSAL.md](PATH-REVERSAL.md). Run
`node scripts/study-ca46-layered-transport.mjs` to inspect the transfer and its
reverse. It changes no drawing or particle count and does not establish unique
routing or frame return.
Multiple neutron-space paths are now retained as admissible alternatives, with
an optional path-independent frame-coherence audit:
`node scripts/study-ca46-neutron-coherence.mjs`. This compares eight local path
pairs, six wrapper-side pairs, and 53 basis cycles. Actual coherence remains
unknown without transport matrices; synthetic flat/twisted connections are
implementation controls only. See PATH-REVERSAL.md for the scope and limits.

Ca44 now uses the same projected-tetrahedron/coherence-path interpretation:
ten two-PE tetrahedra, with wrappers spanning 1+2, 2+3, 1+2+3, and 3+4.
Its outer contour vertices touch at y=134, 354, and 584. The shared graph trial
finds five components and 34 fundamental cycles under candidate endpoint gluing;
frame return is still conditional on a supplied transport law. Run
`node scripts/study-calcium-connected-paths.mjs Ca44` for the bounded audit.

Ca46 now trials **overlapping coherence wrappers**, rather than separate
shell-local contours: one spans shells 1+2; the two associated with shell 3 span
2+3 (inner) and 1+2+3 (outer); shell 4's wrappers span 3+4, 2+3+4, and
1+2+3+4. Each successive wrapper reaches one shell farther inward, including
all intermediate shells.
The PE shapes and counts are unchanged. Each PE-to-PE junction has 20 units of
space for the wrapper contours. The outer contour tips meet at y=134 (shells
1–2), y=364 (2–3), and y=594 (3–4), without interpenetrating at these junctions.
Contours are refitted around the
vertices of the included PE complexes, with 10-unit initial clearance and
additional clearance for outer contours. The enlarged 1+2+3 contour also encloses
the 1+2 and 2+3 wrappers. The outermost shell-4 wrapper encloses all four PE
complexes and the other wrappers. This is a visual hypothesis, not a demonstrated physical
coherence relation; the 20 PE / 26 N inventory remains unchanged.

Sc45 is Ca43 plus one PE triangle (including one N) at `s3-02` below the shell-3
crossed-square cluster. It retains Ca43's 1 / 2 / — wrapper allocation. One
shell-3 wrapper closely surrounds the inner cluster, like shell 2's wrapper;
the triangle attaches to its bottom vertex. The other shell-3 wrapper encloses
the inner wrapped cluster and the triangle together, with a 10-unit top clearance
above the inner wrapper. Its radius is 170 units; the compact layout raises shell 4
without changing any PE shapes or wrapper counts. Ca46 has no observed
decay; Ca48 is omitted because its double-beta decay is known. These drawings
are provisional and do not predict stability or establish nuclear geometry.
Stored witness slots are bookkeeping; only named shapes are rendered, not extra
diagonals from otherwise unused witness slots.

Latest proposed refinement: fill lower-n shells first, continuing until a shell
has one more wrapper than its preceding (n−1) shell before moving outward.
Ca43 therefore has one wrapper on shell 2 and two on shell 3, with shell 4
unwrapped. Ca44 retains the Ca43-plus-one-N count: 1 / 2 / 1, now drawn as
the coherence spans above rather than shell-local wrappers.
Ca46 retains the resulting 1 / 2 / 3 counts, but now uses the adjacent-shell
coherence-wrapper experiment described above. A newly wrapped
outer shell can therefore have fewer wrappers while it fills; the earlier
nondecreasing-count rule is not a universal constraint on intermediate layouts.
Other existing trials have not been automatically redistributed. In particular,
Ar40's double-wrapped shell 2 requires
review before this can be treated as a universal generator.

User-supplied drawing rule: wrapping starts at shell 2. Ca42 has one wrapper each
on shells 2 and 3, with shell 4 unwrapped. The older K39 trial still has only a
shell-3 wrapper and remains pending review against this newly stated rule.
The earlier ordering proposal compared only wrapped shells; an unwrapped shell
was absent from the comparison, not a zero-wrapper entry. The Ca44 instruction
refines that proposal into a filling sequence rather than a static inequality. K41 therefore has one wrapper on shell 2
and two on shell 3; its unwrapped shell-4 PE triangle does not participate.
This is a drawing constraint, not an experimentally established nuclear law.

Ar37, Ar39 and K40 are radioactive and omitted from this stable-isotope sequence.
Nested-wrapper placement is an explicit trial choice, not inferred from isotope
stability or inventory agreement. Stored witness slots provide bookkeeping, not
measured neutron positions. Shell-3 spacing grows to keep its outermost wrapper
from overlapping shell 2; viewport bounds include every contour.

These named-fixture shapes are visual prototypes, not counts of neutron records.
In He4, opposing green two-leg Vs form a crossed square. Crosses and sector frames
are visual guides, not additional counted neutrons. The canvas and inspector are read-only. Definition changes, Undo/Redo,
and stored-record comparisons belong to the **Definition** editor, not the canvas.
No stored-record comparison paints colored paths onto neutron drawings. This is only a visual prototype: graph records and checks remain
legacy-based, and no new attachment rule or
shell-capacity derivation is claimed. Focused visual regression:
`node scripts/test-isotope-wiring-green-v.mjs`.

**Docked isotope picker.** Find isotope is docked by default: selecting an isotope
keeps the panel open, and on wide screens it docks beside the graph rather than
covering it. Undock to restore auto-close on selection. The preference is remembered
when local storage is available. The panel-layout icon is distinct from reference pins and has an accessible action
label and tooltip. Close/Escape still dismiss the panel. On narrow screens it remains
a dismissible overlay. Opening the panel focuses its search field; the clear button
clears only the search text. **Clear all filters** separately clears search, element,
and mass filters. Active filters are listed
beside the result count; an empty list offers **Show all isotopes** to clear them.

**Isotope navigation.** Previous/Next buttons to the right of the isotope selector
step through the full catalog in element/mass order, independently of search filters.
They work immediately, stop at catalog boundaries, and resume from the restored
selected isotope after reload. Text drafts stay intact.
Focused check: `node scripts/test-isotope-wiring-navigation.mjs`.

**UI recovery.** Local storage restores the selected isotope, Graph/Definition
tab, source format/base, selected cell, inspector/catalog/counts visibility, pin state,
search and filters, list scroll position, grid/occupancy/differences,
move mode and zoom/pan. Without a saved list position, the selected isotope is brought
into view. Changing filters resets the list scroll. Selecting an item does not move the
list. All matching isotopes render in one scrollable list, without pagination controls;
legacy saved page numbers are ignored. Focused scroll checks:
`node scripts/test-isotope-wiring-catalog-scroll.mjs`.

The **pin icon on the active isotope row** in Find isotope keeps read-only graph
snapshots beside the active graph, without a fixed pin-count limit,
on the same canvas, without separate cards or a bottom panel. All drawings use equal
canvas space and a common coordinate scale; zoom and pan move them together.
With pins present, each graph has at least 260 px of panel width. Horizontal
scrolling appears inside the graph panel when needed, rather than shrinking
all graphs or overflowing the page. Active headings scroll with their graph.
References are visible in Graph mode, newest pin first (nearest the active graph).
Canvas SVG exports use the same order. Active and pinned graph headings show
P / N / E counts and shell inventory beneath the isotope name, matching the
catalog captions; pinned captions describe their saved snapshots. They retain the applied definition and
grid/occupancy settings as pinned, independent of subsequent edits, isotope
navigation or reselection. Old EP/overlay reference preferences are discarded.
Each isotope can have at most one reference, independent of view changes. The active
row's pin toggles that reference without moving keyboard focus out of the list;
each canvas reference also has an unpin button. All pins are restored, not just
the first three; exports include off-screen pinned graphs as well.
References are restored on reload and included with workspace
settings in project exports/imports. Older projects without workspace settings still load.
Current reference/migration checks: `node scripts/test-isotope-wiring-neutron-only.mjs`
and `node scripts/test-isotope-wiring-references.mjs` (six pins, desktop/mobile
scrolling, reload, shared scale, full-canvas export and unpinning).

**UI boundaries.** The footer contains application storage status only. Isotope
inventory belongs in the catalog; actual record counts and scoped checks are in
**Validation**, with serialization and inventory details collapsed. Comparison-base
selection and **Change details** belong to **Compare stored records** in the
Definition editor, not to the canvas or validation panel.
Terminology and diagram conventions are in **Help**, separate from validation. Neutron-only has no repeated
canvas mode label or legend; side-by-side drawings carry isotope names. **Fit** is
always an action, with a separate magnification readout relative to the current fit.
**Definition** edits the source representation (complete or changes-from-base), not
a different canvas view. Restore-built-in is in that editor, and theme is in Settings.
The File menu distinguishes active-graph SVG export from canvas-with-references SVG
export; the latter uses the shared camera and preserves reference views.
Missing or throwing structural runtimes clear and disable stored-record comparison
and explicitly mark validation unavailable; recovery re-enables the controls. Storage-load failures remain visible after initialization and later
saves, rather than being overwritten by readiness messages. Successful record checks
are explicitly labelled, not presented as a claim of physical validity.
Current focused checks: `node scripts/test-isotope-wiring-neutron-only.mjs`,
`node scripts/test-isotope-wiring-green-v.mjs`,
`node scripts/test-isotope-wiring-catalog-filters.mjs` and
`node scripts/test-isotope-wiring-catalog-scroll.mjs`. Earlier view-switching and
EP-editing browser scripts describe the retired UI and are not current acceptance tests.
The gap-to-verification ledger is [UI-REVIEW.md](UI-REVIEW.md).
Custom definitions load before restoring selection. Missing definitions and malformed
preferences fall back safely. An open catalog is reopened with search focus. Transient
placement dialogs and undo history are not restored. This is UI state only: applied
graphs still use IndexedDB and unapplied text has its separate draft storage.
Focused recovery checks: `node scripts/test-isotope-wiring-ui-state.mjs`.

**Stable isotopes before oxygen.** The catalog includes H-1/2, He-3/4,
Li-6/7, Be-9, B-10/11, C-12/13 and N-14/15 (13 nuclides). Their Z/N
inventories are established. Their count-matching EP/neutron-line arrangements
and shell assignments are illustrative model seeds, not physical derivations;
placement metadata remains in the source, without on-drawing question markers. Radioactive
H-3, Be-7/10, C-14 and other unstable nuclides are not included in this set.

**Placement questions and trials.** Explicit `placementQuestions` entries contain
an `id`, a `reason`, and `pairIds`, `witnessIds` and/or `cellIds`. These remain
source metadata; drawings and SVG exports do not display question marks, placement
warnings or prototype caveat labels. The catalog has no Draft/Ready workflow UI.
Old imported workflow fields are ignored, not interpreted as validation results.
Actual structural/count failures remain visible. Focused checks:
`node scripts/test-isotope-wiring-clean-display.mjs`.

In the inspector, **Try another placement** previews moving one existing EP
record or neutron line witness into another cell of the same shell. Choose the
record type, record and destination. Witness trials preserve the H/V axis and
reject an occupied destination axis through the shared model checks. Shell boundary
witnesses are excluded: they are shell-owned, not cell-owned. Witness question anchors
follow the record; missing or boundary-witness anchors remain explicitly unlocated. Original and candidate use a matched,
shell-focused viewport. The structural core checks each candidate; failures remain
visible and cannot be kept through this action. The modal first shows configuration;
**Review comparison** opens the drawings before the keep action is available. On narrow
screens the current trial is shown first, with the original below it. **Back to options**
retains the selections, and Escape/Discard returns to the inspector. Background controls
are inactive and keyboard focus stays inside the trial. The **Keep … as alternative** button
names the current preview destination, uses a fresh catalog ID and enables comparison to the original. It preserves record
identity, supplied Z/N and shell targets, and keeps placement unresolved. Discarding
or closing changes nothing; a stale preview cannot be saved after the source changes.
This is a bounded relocation experiment, not automatic selection of nuclear geometry
or a general rewrite interface. Test it with
`node scripts/test-isotope-wiring-placement.mjs`; add `--standalone` to exercise the
same workflows over `file://` with network access disabled.
`node scripts/test-isotope-wiring-witness-placement.mjs` exercises witness trials
offline; add `--hosted` for the website. These checks include duplicate-axis failures,
source isolation, stale previews, project replay and noncolliding witness IDs when
editing the vacated cell.

**Test placement alternatives** in the trial dialog surveys other cells in the
same shell, in deterministic batches of at most eight. It shows coverage, inventory
checks, overall results and failing predicates. **Preview** opens that candidate;
scanning itself neither changes the working definition nor saves or ranks results.
Changing the selected record resets the survey; editing the source invalidates it.
If source and alternatives pass, the supplied checks do not select a unique placement.
A partial survey, no passing relocation, or unknown targets never establishes physical
uniqueness. Only one record moves; routes/axis, shell and targets stay fixed.

For example, moving O16's `s2-01-H` witness to `s2-00` passes, while moving it to
`s2-10` fails duplicate-axis occupancy. Both retain matching inventory: counts alone
do not distinguish them. This is a test of the supplied model, not nuclear evidence.
Run `node scripts/test-isotope-wiring-survey.mjs` offline, or add `--hosted`.

The proposed categorical architecture is [MACHINERY.md](MACHINERY.md). It separates
incidence maps, interface assembly, revision-bound edits, compilation, evidence,
readouts, and persistence; these are implementation obligations, not claims that
the legacy app already satisfies them.

The independent [finite-incidence kernel](core/CLOSURE.md) implements structural
maps, finite limits/colimits, and open-component composition. Both editor modes now
use its checked legacy adapter and model evaluator for live structural inspection;
general composition and rewrite operations are not editor actions. Same-shell EP
and neutron-line placement trials are separate bounded, core-checked actions. Run `node --test tests/isotope-wiring-category.test.mjs`
for its structural and coherence checks. The [attributed adapter](core/ADAPTER.md)
adds model labels, explicit support gluing, and retained-source recovery; test it
with `node --test tests/isotope-wiring-adapter.test.mjs`. The next layer,
[model predicates and policy coherence](core/MODEL.md), is checked with
`node --test tests/isotope-wiring-model.test.mjs`. [Immutable revisions and ground
rewrites](core/REVISIONS.md) add atomic operations, before-image undo, and bundle
replay; test them with `node --test tests/isotope-wiring-revisions.test.mjs`.
[Typed rules and independence witnesses](core/RULES.md) construct both pushout
squares, transport surviving matches, and audit declared derivations; test them
with `node --test tests/isotope-wiring-rules.test.mjs`.
[Supplied overlaps and joins](core/OVERLAPS.md) and
[selective verification](core/SELECTIVE.md) have dedicated suites:
`node --test tests/isotope-wiring-overlaps.test.mjs tests/isotope-wiring-selective.test.mjs`.
The [bounded labelled overlap census](core/CENSUS.md) and
[replayable verification bundles](core/VERIFICATION-BUNDLES.md) are checked with
`node --test tests/isotope-wiring-census.test.mjs tests/isotope-wiring-verification-bundles.test.mjs`.
[Bounded automatic matching](core/MATCHING.md) has a dedicated suite:
`node --test tests/isotope-wiring-matching.test.mjs`.
[Bounded multi-step join search](core/JOIN-SEARCH.md) is checked with
`node --test tests/isotope-wiring-join-search.test.mjs`.
[Supplied isomorphic joins](core/ISOMORPHIC-JOINS.md) have a dedicated suite:
`node --test tests/isotope-wiring-isomorphic-joins.test.mjs`.
[Automatic anchored-isomorphism search](core/ISOMORPHIC-SEARCH.md) is checked with
`node --test tests/isotope-wiring-isomorphic-search.test.mjs`.
[Persistent-occurrence joins](core/PERSISTENT-JOINS.md) are checked with
`node --test tests/isotope-wiring-persistent-joins.test.mjs`.
[Concrete context lifting](core/CONTEXT-LIFTING.md) is checked with
`node --test tests/isotope-wiring-context-lifting.test.mjs`.
[Context-lift composition](core/CONTEXT-COMPOSITION.md) is checked with
`node --test tests/isotope-wiring-context-composition.test.mjs`.

Run `node --test tests/isotope-wiring-core.test.mjs` for legacy-core regression checks.
Identity deltas replay against a supplied snapshot; cycle detection follows actual
definition dependencies rather than rejecting a reused ID. Same-ID application
stores the compiled absolute snapshot, and indirect cyclic updates are rejected
before changing drafts. Generated deltas use `{ "op": "remove-metadata", "key": "…" }`
to delete inherited top-level metadata absent from the target. Older editor versions
do not support this new operation. Generated cell IDs retain existing single-digit
coordinates and delimit larger coordinates to avoid collisions; ambiguous old
files are not migrated automatically.

These repairs do not freeze mutable delta bases, preserve graph-array order, or
establish arbitrary full-document replay. Keep absolute snapshots and the actual
base definitions; `base` and `ops` remain delta protocol fields, not roundtrippable
custom metadata. Editing still uses the repaired legacy engine, not the independent
revision machinery.

Validate the built website with `node scripts/test-isotope-wiring-public.mjs` and
run the current matrix with `node scripts/test-isotope-wiring-browsers.mjs`. These
exercise the actual Neutron-only/Definition contract, production iframe/theme
retention, exact downloads, storage/replay and failure controls. The older
`test-isotope-wiring-website`, `standalone`, `placement`, `witness-placement`,
`survey`, `accessibility` and `ux` scripts include retired UI criteria; they are
historical probes, not the current passing matrix. Headless comparison/placement
coverage remains in `node --test tests/isotope-wiring-research.test.mjs` and the
current browser data-bridge workflow; neither implies that retired dialogs exist.
`vitepress build website` builds the public route but does not deploy it.

**Text drafts and recovery.** Unapplied Wiring text is retained independently of the
applied graph through graph edits, Undo/Redo, reset and imports. It is restored after
reload when browser local storage is available. **Wiring \*** flags pending text;
the source status distinguishes saved text from session-only text. **Compare with
applied JSON** shows the current applied representation without replacing the draft.
Applying text whose graph/base changed requires confirmation; explicitly discarding
a draft also requires confirmation. **Download text draft** preserves the exact text,
including incomplete JSON. **File → Export all text drafts** archives every retained
buffer with its isotope, format and base, including buffers for reset custom definitions.
Project/definition exports contain applied state, not these text buffers. Browser storage is not a durable backup or cross-device sync.

Same-ID Apply and project import now update the visible working definition rather
than reselecting its old in-memory overlay. Save status is scoped to the graph and
only reports completion for the latest write. Add/Remove buttons name their mutations.

**Keyboard and touch.** Tab enters the graph at one cell; Right/Down and Left/Up
move through definition order (not spatial directions), and Home/End jump to the
ends. Enter/Space opens inspection; Escape returns focus to the cell. Zoom shortcuts
retain cell focus. Catalog and Counts dismissal return focus to their controls;
read-only comparison diagrams have no inactive cell buttons. Unresolved cells include
that status in their accessible names. Coarse-pointer toolbar and editor controls
have 44px targets; use **Move** for single-finger panning and **Fit** to reset.
On mobile the inspector occupies a separate lower pane, not an overlay. The graph
focuses on the selected shell and identifies that scope in its caption. Dense SVG
cells can still require zooming.

The historical `test-isotope-wiring-accessibility.mjs` includes removed editing
controls; its earlier touch/editing report is not current acceptance. The current
matrix checks mouse/keyboard interactions and emulated viewport sizes, including
visible keyboard entry/Inspect and camera-state recovery. It does not certify
real devices, screen readers, multi-touch or every pointer gesture.

**Cross-browser regression.** Run `node scripts/test-isotope-wiring-browsers.mjs`
for the complete sequential Chromium/Firefox/WebKit matrix, or append engine names
and `--case=<id>` for an explicitly partial diagnosis. Its current ten-case contract
is in `config/isotope-wiring-browser-matrix.v1.json`; it is not the historical
eleven-case/33-run contract requiring removed EP/placement-dialog controls.

Currency iteration 3 records **30/30 passing runs**, zero failures/unrun cases, on
Chromium 151.0.7922.34, Firefox 153.0 and WebKit 26.5. Base commit `3ace86e33` alone
is insufficient: the tested working tree was dirty and exact source hashes are in
`config/isotope-wiring-browser-evidence.v1.json`. See the [verification record](../../docs/isotope-wiring-browser-verification.md)
for scope, engine versions, failure controls and limits. `node scripts/check-isotope-wiring-browser-evidence.mjs`
checks recorded byte freshness without replaying browsers. A partial or drifted run
cannot be reported as a complete pass. Missing engines fail rather than being skipped;
install them explicitly with `node node_modules/@playwright/test/cli.js install chromium firefox webkit`.
This record does not certify shipping Safari, iOS/Android, real devices or physical adequacy.

WebKit's native offline flag rejects `file://` navigation on this Windows build.
Its file-mode tests instead abort HTTP(S) requests via Playwright routing; a dedicated
check verifies that even a reachable local server receives no request. Chromium and
Firefox additionally use native offline mode. Browser tests wait for completed core
initialization, not just the static initial page title.

`node scripts/test-isotope-wiring-ux.mjs` specifically exercises text recovery,
confirmation/cancellation, storage denial, explicit edit labels, mobile first-screen
access and non-overlapping inspection, and the modal configure/compare workflow.

**Maintaining the embedded core.** The handwritten editor remains in `index.html`.
Its marked inline-core section is generated from `core/browser-entry.mjs` and the
shared core sources. After changing those modules, run
`node scripts/prepare-isotope-wiring-core.mjs`; `--check` verifies freshness without
writing. `node --test tests/isotope-wiring-standalone.test.mjs` checks freshness and
agreement with Node on fixtures, differences and trials. Only maintainers need
this build step: the delivered HTML opens directly and needs no sidecar files.

Keep future app changes here. The separate 3D retained-expansion viewer remains
in [`../normal-ray/`](../normal-ray/); this move does not replace or merge it.
