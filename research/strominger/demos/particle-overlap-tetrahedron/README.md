# Particle windows: Cartesian, tetrahedral and pentachoron

Owner: `marici.Strominger`. Published route: `/experiments/particle-overlap-tetrahedron/` in both public roots. Local Three.js + OrbitControls follow the existing paw-cycle/minimal-data-packet viewers; the MIT license is preserved. No CDN or package installation is required.

## Dual-incidence space — current view

`vacuum.html` has only **Previous item** and **Next item** action buttons.
Selections open fully assembled. The buttons remove/re-add displayed carriers
and wrap between the first and last item instead of stopping at the ends. The same
controls assemble the legacy layouts. Orbit/zoom remains available directly
on the canvas. There are no transport, circuit, electron-reader, reset-camera,
or tube controls.

The default **Deuterium · native window assembly** passes the necessary local
P/N/E occurrence and shared-interface checks. This does not derive the earlier
inter-realization gluing hypotheses.

**He-3, He-4 and Li-6 now use corrected phase-reference assemblies.** Native
readers and their combinations have explicit consecutive C/M phase witnesses.
A neutron advances `M0 C1 M1 [C2] -> M1 C2 M2 [C3]`; its old C2 coefficient
enters the active window. All five coefficients and all three face-character
components survive. Absolute phase and command history are not reset when
coefficient permutations close.

Labels cover all four witnessed occurrences of **every visible item**, not
just the last item. Shared vertices list all distinct C/M names (for example, `C1 / C3`);
no earlier occurrence is overwritten. Carrier and realization provenance stays
in the model data, not in the visible vertex labels. They
are not permanent geometric vertex names. Neutral `vertex-*` IDs remain
separate from those phase labels.

**Shape 1 / Shape 2** select two independent assemblies for desktop comparison.
Both are shown side by side at a common scale. Previous/Next use one shared
item index; a shorter assembly remains complete until that index falls below
its length. The shared index wraps at both ends, and both selections initially
show complete assemblies. Label visibility and face transparency apply to both. The second
shape can be set to None. Comparison translations affect the drawing only,
not the checked geometry or phase histories. There is no mobile-specific
rearrangement. Outside-context
coefficient retention is still an explicit reference law, not derived physical
binding or stability.

See `../../phase-first-assembly-v2.md` for the corrected construction and
`../../phase-discipline-audit-v1.md` for the withdrawn models' failure witnesses.
`phase-advance-model.mjs` validates the next-realization comparisons;
`phase-assembly-model.mjs` checks native readers and history-bearing whole
assembly certificates before display admission. `assembly-display-model.mjs`
handles prefixes independently of any between-element growth law.

Legacy H/He/Pb loadouts remain geometric comparisons, not phase evidence.
The base 343 cells and existing Pb mesh pool are retained. All face materials
share the horizontal **Face transparency** slider (0–100%, initially opaque).
Proton, neutron, and electron faces use the same opacity and depth-write rules;
electron edges remain dotted while nuclear edges are solid. Edges are black,
2-CSS-pixel `LineSegments2` / `LineMaterial` strokes, using unmodified official
r128 addons matched to the existing renderer (provenance and hashes in
`vendor/lines/UPSTREAM.json`). Edges remain opaque, depth-tested and depth-writing;
transparent faces composite over edges behind them, attenuating them continuously.
Opaque faces hide rear edges completely. A small face polygon offset avoids
coplanar edge/face fighting. **Show vertex labels** toggles the current labels. Both settings persist across loadout and
item changes. No extra tube geometry is constructed.

With two shapes selected, **Rotate both around own centers** makes left-drag
apply the same rotation to both assemblies about their respective full-assembly
bounding-box centers. These anchors stay fixed when stepping through prefixes;
labels and edges follow the rotated geometry. Unchecking restores scene orbit.
Zoom and pan remain available. The option is disabled in single-shape mode.

Active verification: `node research/strominger/checkers/check_fiber_space.mjs`.
Current phase construction: `node research/strominger/checkers/check_phase_assembly.mjs`.
Li-7 adds one neutron while retaining the selected Li-6 geometry, roles and
readers; see `../../lithium7-phase-reference-v1.md` and
`node research/strominger/checkers/check_lithium7_assembly.mjs`.
Be-9 (4P/5N/4e) retains the selected Li-7 assembly and adds one P/N/e using
the existing interfaces; see `../../beryllium9-phase-reference-v1.md` and
`node research/strominger/checkers/check_beryllium9_assembly.mjs`.
B-10 (5P/5N/5e) uses a separate whole-assembly reference: extension of the
selected Be-9 is blocked in the bounded search. B-11 (5P/6N/5e) retains that
B-10 and adds one neutron. See `../../boron-phase-references-v1.md` and
`node research/strominger/checkers/check_boron_assemblies.mjs`.
C-12 (6P/6N/6e) and C-13 (6P/7N/6e) are separate retained-B-11 extensions.
Direct neutron addition to the selected C-12 is blocked by occupied PN ports.
See `../../carbon-phase-references-v1.md` and
`node research/strominger/checkers/check_carbon_assemblies.mjs`.
All phase references now enforce coverage of every physical contact as well
as every carrier; B/C/N selections were regenerated. See
`../../assembly-contact-coverage-repair-v1.md` and
`node research/strominger/checkers/check_assembly_contact_coverage.mjs`.
N-15 (7P/8N/7e) retains C-13 and is available in the viewer. N-14 is physically
stable but has no complete candidate in the current bounded isotope ansatz and
is not displayed. See `../../nitrogen-phase-audit-v1.md` and
`node research/strominger/checkers/check_nitrogen_assemblies.mjs`.
These remain phase references, not physical stability derivations. Only stable
isotopes are added to the viewer; unstable isotopes remain test controls.
Withdrawn-model negative controls: `node research/strominger/checkers/check_phase_discipline.mjs`.

## Previous cell-only lattice view (replaced)

Open `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/vacuum.html`.
The UI contains the lattice, independent P/N/E cell-highlight checkboxes,
layer-ordered item navigation, coordinate-direction flippers, and view controls. No coordinate form or explanatory
panels remain. Each lattice cell has one permanent mesh; the checkboxes change
which existing cell meshes are highlighted, without adding particle geometry.
Coordinates remain available on node hover.

The Atom selector offers neutral hydrogen-1 (1P/1e), deuterium (1P/1N/1e),
and helium-4 (2P/2N/2e). `atom-model.mjs` selects distinct existing cells:
a face-connected nucleus, with electron display sites two face hops away.
This deterministic placement is a visualization rule, not a nuclear binding,
orbital, or energy model. P/N/E checkboxes filter the displayed species.
Atom presets suppress the unrelated neon inspector so it cannot obscure an
occupant. Every occupant reuses the corresponding permanent lattice mesh.

`simplex-components.mjs` constructs layers directly, starting at `layer0-item1`.
It does not build the full space first and then relabel it. The placement recipe is:

| Layer | Items | Composition |
|---|---:|---|
| 0 | 1 | upright unit-simplex seed, origin (0,0,0,0) |
| 1 | 4 | four face-attached octahedral groups |
| 2 | 44 | regular tetrahedra |
| 3 | 126 | 74 regular tetrahedra + 52 octahedral groups |

Each octahedral item contains four non-regular primitive tetrahedra. Item IDs
are `layerN-itemK`, with K starting at 1 independently in each layer. Navigation
visits all 175 items in construction order and highlights every constituent
cell of the selected item. Groups are not additional enclosing solids.

The seed is upright. The enclosing tetrahedron has the opposite orientation;
this relation is retained explicitly rather than concealed by arbitrary caps.
The rejected nonconvex cap replacements have been removed. The envelope has
four flat faces, subdivided into 196 boundary triangles. Tests verify every
boundary triangle lies on an envelope face, as well as closure, non-overlap,
and equality of the seed and total-volume centroids. Coordinates are signed
affine structural coordinates summing to one; the four envelope corners are
permutations of (-5,2,2,2). No camera-only orientation workaround is used.

The assembly uses two primitive
shapes, with 120 shared nodes and 343 cells: 119 regular
tetrahedra and 224 non-regular tetrahedra grouped into 56 octahedral
subassemblies. The unrequested expansion to fifteen intervals has been
reverted. Primitive edge length is 6/7. Groups carry no extra volume or mesh.
Tests check all 58,653 cell pairs (with bounding-box separation before the
exact separating-axis test), component congruence, group membership,
uniqueness, and total volume.

`simplex-model.mjs` binds P/N/E to three actual adjacent lattice cells.
Coordinates and rendered points reference the same node table as the lattice;
hover shows node coordinates. P/N share M0/C1/M1; N/E share M1/C1/C2.
No independent placement, rescaling, or reflected off-lattice vertices remain.
The initial cell is the upright layer-zero seed. Surface peeling is retained
as an independent check: reversed depths agree with construction layers,
and the seed is the unique deepest item. Coordinate slabs shown by the four
λ controls are distinct from the four assembly layers. No barycenter
marker or Center panel is displayed. P/N/E labels are not physical identifications.

Verify with `node research/strominger/checkers/check_simplex_space.mjs`.
The earlier three-axis checker describes the superseded view, not this tab.

## Previous planar comparison

Open `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/planes.html`,
or choose **Previous planar comparison** in the current view. This separate
view has no occupants or particle paths: discrete R (realization) levels carry
triangular lattice patches with concrete M+, M-, C+, C- axis labels and one
signed pair repeated. Every R step exchanges M/C roles as well as rotating the
frame: default rotation is 60 degrees; with MMC at R=0, odd levels (including
negative ones) use CCM. The reference selector inverts this alternating
sequence. Click an R label or its node to toggle full plane / faint traces,
independently of selection. R=-1,0,+1 start full. Keyboard and touch toggles
are supported; orbit drags do not toggle. Controls also expose initial
orientation, extent, spacing, frame guides and single-frame isolation. See
`../../vacuum-space-plane-controls-v5.md` for controls and 58-check verification,
and `../../vacuum-space-alternating-R-v4.md` for the typed transition rule.

Carrier selectors add Empty, Lone proton, Lone neutron, Lone electron and All
three. Every vertex now directly references an actual lattice node. The three
cells triangulate one elementary prism between adjacent R planes, retaining the
P/N/E incidence chain and shared faces. These are non-regular lattice cells,
not the earlier centered/scaled tetrahedra. Expand **Lattice node addresses**
to inspect all bindings; **Focus cells** changes the camera only. Non-lattice
rotation steps are blocked rather than snapped. See
`../../vacuum-space-lattice-cells-v7.md` and the current 80-check receipt.

## Representations

- `?view=lattice` now defaults to **volumetric tetrahedral carriers**, also selectable with the Tetrahedral carriers button or `&geometry=carrier`. The proposed proton is C0/M0/C1[M1]; the proposed neutron is M0/C1/M1[C2]. These are consecutive four-vertex carriers, not two active faces assigned to one common carrier. They share the entire M0/C1/M1 face. In particular the neutron continuation vertex is C2, NOT C0. Selecting P/N highlights its respective body. This default is P/N ONLY: no electron MCC face/arrows/control/identity-anchor leg. The old three-window trace and electron selection are available only in the separate legacy chart views; C2 here is N's fourth vertex, not an electron assignment. Both rendered meshes have four triangular faces, squared edge length8 and volume8/3. The second selected pentachoron facet is unfolded across the shared face: C2 becomes(-5/3,-5/3,-5/3) in this3D display, while its original4D identity/coordinates remain retained. This is an isometry on each selected facet, not a global isometry/projection of the full4-simplex. C0-C2 is not an edge of either displayed carrier. The bodies are geometric carriers with marked windows, not a derived assignment of two separate physical species or a completed C/M lattice assembly. Body surfaces remain visible when triangle-window fills are hidden.
- `?view=lattice&geometry=chart` (Flat lattice chart): x is the realization coordinate; z is the operator-assigned C/M codimension layer, with Cs at0 and Ms at1. Coordinates: C0=(-1,0,0), M0=(-1,0,1), C1=(0,0,0), M1=(0,0,1), C2=(1,0,0). The C spine advances along x and the shared M1 excursion leaves and returns to C1 without reversing x. All five carriers lie in the xz plane, with y=0. M1 is directly above C1 along z; y remains unassigned and unused. Solid primitive transitions may be grid diagonals; dashed edges record composites. Camera orbit is unrestricted across the normal0–180degree polar range, including views from below. The initial camera uses z-up and shows Ms above Cs; world-coordinate codimension remains unchanged while orbiting. Switching to the4D views restores their y-up camera. The lattice grid has no negative codimension layer.
- `?view=hex`: one tetrahedral lattice, bounded to Euclidean radius4 about C1=(0,0,0). Only complete tetrahedra whose vertices lie inside that sphere are retained; unused vertices are removed and edges deduplicated. A single Three.js LineSegments geometry draws all lattice edges. There is no separate CMC-plane grid, prism grid or overlapping volume grid. The boundary is stepped along complete-cell faces rather than cutting cells at a smooth sphere. Axial `[q,h,r]` maps to `(q+r/2,h,sqrt(3)r/2)`; a Freudenthal triangulation in basis `(a,-b,c)` preserves the equilateral CMC faces. Three axes have opposite rays labelled a₁/a₂, b₁/b₂ and c₁/c₂; the c-ray labels are lowercase and distinct from carriers C₁/C₂. M0=(-1/2,0,sqrt(3)/2), M1=(1/2,0,sqrt(3)/2), and the C spine is unchanged. Each window remains a shared face of two tetrahedra. Cells have volume sqrt(3)/12 and are non-regular; regular tetrahedra alone cannot tile Euclidean3D space. Per-edge color fades off-plane edges within the same geometry. Orthographic rendering, free orbit, selections, shared/reversed arrows, trace and context/fill controls remain available. These are declared display coordinates, not a physical crystal identification.

- `?view=pentachoron`: C0/M0/C1/M1/C2 are the five original vertices of a regular4-simplex. All three particle triangles are original2-faces. No sixth point is introduced. The4D angle rotates the y-w plane, then orthogonally drops w. C2 remains the original fifth vertex rather than the barycenter. The initial4D angle is0°, placing the projected fifth vertex at the outer tetrahedron's center. The control is limited to±20°: its facet barycentric weights are (1+u)/4,(1-u)/4,(1+u)/4,(1-u)/4 with u=-sqrt(5)tan(angle), so all remain strictly positive. Thus C2 stays inside the projected3D tetrahedron throughout the allowed range, without changing its source4D vertex coordinates or using perspective. All five tetrahedral boundary cells can be highlighted; their orthogonal images can overlap.
- `?view=barycenter`: the earlier hypothesis remains selectable. Four carriers occupy one facet and C2 is the intrinsic barycenter, while V4 is the distinct fifth outer vertex. The electron triangle is radial rather than an original face.

Every mode uses a Three.js OrthographicCamera for3D-to-screen projection, with aspect-correct responsive frustum sizing and bounded wheel/pinch zoom. No perspective or Schlegel mode remains. The4D-to-3D maps also have orthonormal rows; retained3D lattice coordinates pass through unchanged. All modes preserve the route labels and selected walk occurrence across switching. Two C1 occurrences are one geometric point, and neutron/electron arrows use separate display lanes to expose their opposite traversals. Progress is display traversal, not physical time. Regular4-simplex coordinates follow `research/voevodsky/checkers/check_pentachoron_spin_interfaces.py`; the labels and physical interpretation are proposed, not native-carrier identifications.

## Volumetric correction and verification

The earlier identity overlay on the flat chart did NOT display tetrahedral
volumes; it must not be presented as completing that objective. The corrected
default visibly renders the two noncoplanar source carriers. Wireframes,
individual body labels, the shared MCM face and all five node identities are
explicit. The old planar chart is an intentionally separate button/view.

    python research/aspect/scc/scc.py check particle-tetrahedral-carrier-viewer-v1 --verbose

The live requested URL passes18 carrier checks, including tetrahedral volumes
computed from the ACTUAL rendered mesh buffers, desktop/mobile output, original
identity retention and explicit chart switching. Screenshots/receipt are under
`research/strominger/results/particle-carrier-viewer/`. All154 original chart
regressions and39 identity-overlay checks still pass; those chart-specific tests
now explicitly select `geometry=chart` rather than pretending a planar chart is
a volumetric body. The core `model.mjs` remains unchanged.

## Optional electron [M₂] trial

Choose **Try electron [M₂]**, or open
`?view=lattice&geometry=carrier&electron=m2`. This adds the complete candidate
`E = M1 C1 C2 [M2]`, not merely the old MCC face. M2 is a new geometric source
extension, not M0 renamed or an original pentachoron vertex. The original P/N
vertices and bodies remain unchanged. Returning to P/N carriers removes the
trial body and hides M2.

M2 is the reflection of M0 through the N/E shared face M1/C1/C2. In the unfolded
coordinates it is `(-31/9,-1/9,-1/9)`. All three tetrahedra have squared edge
length8 and absolute volume8/3, with disjoint interiors. The trial retains the
old electron window's order M1→C1→C2 and its declared spectral adapter, but that
five-label proof DOES NOT include M2 or prove native electron equivalence.

See `../../electron-M2-carrier-trial-v1.md` for construction and scope. Trial
screenshots are `electron-M2-trial-*.png` in the carrier-viewer results directory.

## Identity-development layer

All four views now include an **Identity through the walk** panel. Its P/CMC,
N/MCM and E/MCC buttons use the same retained window selection as the scene;
Follow walk tracks the original trace. Positive, negative and common modes are
available. A phase probe changes the displayed real/imaginary axes but not the
underlying eigenline projector. It is a diagnostic, not physical time.

The mint marker is the active window barycenter; the gray marker/trail is the
first-seen assembly mean. Repeated C1 retains a new occurrence but does not insert
a sixth vertex into that geometric mean. The inspector separately shows the
occurrence-weighted mean, source root/occurrences, eigenvalue, original source
anchor/displacement and explicit additional closing edge.

Transport uses the verified original five-role source: positive P maps to
positive N with120degree phase, then to negative E with cumulative phase0.
The N/E comparison requires the inverse cycle, retained as TWO forward cycles.
Other seeds transport through the complete retained mode family. Common mode
retains its homogeneous identity coordinate and is not misdrawn as a missing
identity merely because its centered directional ellipse vanishes.

`identity-data.mjs` is generated, not hand-maintained. The targeted publisher
validates every input hash of
`research/strominger/results/cmc-mcm-identity-attachment/verification.json` before
exporting its53-check result. The original `model.mjs` was not changed, preserving
its existing mathematical source bindings. If mathematical inputs change, rerun
`cmc-mcm-identity-attachment-v1`, then prepare the viewer again.

Cartesian/hexagonal/barycenter views are coordinate presentations, not silent
isometries of the verified pentachoron metric. The panel labels source and chart
values separately. Geometric closure adapters are not claimed native particle
commands, and no physical C/M, charge, spin or time assignment is derived.

Additional browser verification:

    python research/aspect/scc/scc.py check particle-overlap-identity-viewer-v1 --verbose

Set `PARTICLE_IDENTITY_BASE_URL=http://127.0.0.1:8766` to test the live server;
otherwise the checker creates an ephemeral local server. The completed live test
passes39 groups with no script errors, alongside154 original regression groups.
Desktop/mobile screenshots and source-bound receipt are under
`research/strominger/results/particle-overlap-identity-viewer/`. The owned local
server's PID and requested URL are recorded in its `server-info.json`.

## Prepare, verify, serve

```text
node research/strominger/checkers/prepare_particle_overlap_viewer.mjs
python research/aspect/scc/scc.py check particle-overlap-viewer-v1
node public/experiments/eight-node-coherence-pyramid/dev-server.mjs
```

Open a representation:

- `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/?view=lattice`
- `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/?view=hex`
- `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/?view=pentachoron`

The targeted publisher only refreshes this experiment in `public/experiments/particle-overlap-tetrahedron/` and `website/public/experiments/particle-overlap-tetrahedron/`; ownership sentinels guard both destinations. Site preparation, build and deployment scripts are untouched.

The SCC checker covers the retained barycenter tests plus hexagonal basis/inverse placement, six nearest neighbors, equilateral triangles, elementary-cell membership for each window, actual rendered grid-edge alignment, tetrahedron volumes and interior-face pairing, exact CMC section preservation, a four-unit Euclidean cutoff and exactly one rendered lattice object with no plane overlay, and tetrahedral desktop/mobile interactions; integer Cartesian lattice coordinates, codimension layers, realization direction, unused y and xz planarity, M1 directly above C1 along z, projected C2 interior containment and unrestricted lattice orbit, proper simplex incidence/metric, orthonormal projection rows and barycentric-average preservation, live orthographic WebGL, depth-independent segment scale, wheel zoom/reset, all particle selections,4D rotation and all five cells, traversal endpoints, state-preserving mode switching, deep links, mobile sizing and label separation. Numerical geometric assertions test this display implementation; they are not source-identification proofs. Results and desktop/mobile screenshots are under `research/strominger/results/particle-overlap-viewer/`. Earlier receipts are archived as `verification-barycenter-v1.json` (21 groups) and `verification-lattice-pentachoron-v2.json` (65 groups). The preceding orthographic-only implementation passed80 groups; that receipt is archived as `verification-orthographic-v3.json`. Current checks additionally enforce the requested lattice-axis meanings.
