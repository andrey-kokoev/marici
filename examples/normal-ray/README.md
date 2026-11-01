# Normal-ray viewer — reference-architecture migration

## Retained expansion

Select **Sulfur-32 → View → Retained expansion**. Twenty Previous/Next steps:

1. A white dot appears at the center.
2. One white arrow grows to the right from the dot.
3. Two white triangles open in opposite directions from the X-axis edge,
   forming a square with corners (0,0), (1.5,1.5), (3,0), (1.5,-1.5), all at z=0.
   Both moving apex dots disappear when opening finishes. Only the outer
   boundary is outlined; there is no white line along the shared diagonal.
4. Color the upper triangle red and the lower triangle blue on the front
   (upper blue, lower red on the back). Keep both full-size and touching,
   with no white line between them. Label: **Hydrogen-1**.
5. Add the white line along their shared X-axis diagonal, from (0,0,0) to
   (3,0,0), without changing either face's geometry or color. Label:
   **Hydrogen-2**, protons: 1, neutrons: 1, electrons — shell 1: 1/2.
   These are procedure labels, not a physical derivation.
   **Steps 3–8 now use the square. Steps 9–20 deliberately retain their
   earlier triangular construction; they have not yet been remapped.**

6. Divide both colored halves along the square's vertical center diagonal,
   parallel to Y at x=1.5. This is a color-only split into four full-size
   triangular regions: no shrinking, whitening or new white line yet.
   Front upper left/right: red/blue; lower left/right: blue/red. Reverse
   colors swap. Retain the white X-axis diagonal and the outer boundary.
   The label lists **Helium-3**, protons: 2, neutrons: 1, electrons — shell 1: 2/2.
7. Retain the exact four faces from step 6 and draw a white line from
   (1.5,-1.5,0) to (1.5,1.5,0), along their vertical shared edges. The existing
   horizontal white diagonal remains. No face changes size or color.
   Label: **Helium-4**, protons: 2, neutrons: 2, electrons — shell 1: 2/2.

8. Split the square's upper-right (positive-x, positive-y) blue triangle
   along local x=y, measured from the square center (1.5,0,0). In construction
   coordinates the dividing segment runs from (1.5,0,0) to (2.25,0.75,0).
   The region below this segment stays blue; the region above becomes red
   (reverse colors swap). Retain the other three quadrants and both white
   diagonals. Add a white neutron line along the new x=y division in this
   same step. Both triangles still exactly fill the original face without
   shrinking or whitening; the line overlays their shared edge.
   The label lists **Lithium-6**, neutrons: 3,
   protons: 3, and electrons — shell 1: 2/2, shell 2: 1/8.

9. Keep the exact full-size geometry and colors from step 8 and draw a white
   line along the new pair's shared edge. Do not shrink or move either triangle.
   The new line runs from the central base vertex to the midpoint of the
   right outer sloping edge. Preserve the left pair and its step 7 separator.
   The label lists **Lithium-7**, neutrons: 4, protons: 3, and electrons —
   shell 1: 2/2, shell 2: 1/8.

10. Split the left-center blue face into full-size blue/red triangles
    (red/blue on the reverse), adding a white line along their shared edge.
    Carry forward the right-hand split and separator from steps 8–9.
    This completes the two branches used by steps 11–20, without shrinking,
    erasing or re-splitting the right half. The white line denotes a neutron
    in the procedure, not a physical derivation.
    Keep all earlier splits and separators. The label lists **Beryllium-9**,
    neutrons: 5, protons: 4, electrons — shell 1: 2/2, shell 2: 2/8.

11. Split the upper-right red face into red and blue triangles that touch
    along their shared edge, with no new white separator. Reverse readings
    swap colors. This is a full-size color-only split: preserve the original
    boundary and area, without shrinking, whitening or adding a border.
    Retain all three existing separators and the other faces. The label lists
    **Boron-10**, neutrons: 5, protons: 5, electrons: 5 — shell 1: 2/2,
    shell 2: 3/8.

12. Retain step 11 and add a white separator along the shared edge of its
    small upper-right red/blue pair. The label lists **Boron-11**, neutrons: 6,
    protons: 5, electrons: 5 — shell 1: 2/2, shell 2: 3/8.

13. **Carbon-12**: subdivide the uppermost blue child of the step 11
    upper-right pair, not its inner red child, into touching blue/red
    triangles (red/blue on the reverse). Each new
    triangle has half that small parent's area. This color-only split preserves
    its exact boundary: no shrink, whitening, border or new line.
    Retain every other face and separator. Label: neutrons 6, protons 6,
    electrons 6 — shell 1: 2/2, shell 2: 4/8.
14. **Carbon-13**: keep the exact step 13 geometry and add a white neutron line
    along the new pair's shared edge. Label: neutrons 7; proton, electron and
    shell counts unchanged.

The top-left isotope card also shows natural abundance (%) and nuclear
stability for each labeled step. These are NIST representative abundances
and IAEA/ENSDF reference classifications, matching
`research/kitaev/isotope-electron-shells.html`, not predictions of the geometry.
Abundance varies by sample; “Stable” means no radioactive decay is observed.

15. **Nitrogen-14**: split the opposite, larger upper-left red triangle into
    touching blue/red triangles: the upper child becomes blue, while the
    lower child remains red (reverse colors swap). Do not subdivide
    the smallest Carbon child. Keep the full parent area and boundary,
    changing color only, with no new line or white gap.
    Label: neutrons 7, protons 7, electrons 7 — shell 1: 2/2, shell 2: 5/8.
16. **Nitrogen-15**: retain the exact step 15 geometry and add a white neutron
    line between the new pair. Label: neutrons 8; proton, electron and shell
    counts unchanged. Steps 13 and 15 split opposite upper faces, each of
    area 0.28125, into children of area 0.140625. Steps 12, 14 and 16 only add
    separators; outer faces remain intact. Later steps retain both branches.

17. **Oxygen-16**: subdivide the topmost blue child of step 15's upper-left
    pair (the one containing the apex) into touching blue/red triangles
    (red/blue on the reverse). Leave its lower sibling unchanged, retaining
    the parent's exact area and boundary. Color
    change only: no shrink, white gap or added line. Label: neutrons 8,
    protons 8, electrons 8 — shell 1: 2/2, shell 2: 6/8.
18. **Oxygen-17**: retain step 17 geometry and add only a white neutron line
    along the new pair's shared edge. Label: neutrons 9; proton, electron and
    shell counts unchanged. All earlier faces and separators are retained.

19. **Fluorine-19**: split the topmost red child of the right-hand Carbon
    pair, containing the apex, into touching red/blue triangles (blue/red on
    the reverse). Add a white neutron line along their shared edge without
    shrinking or whitening either face. Retain the lower sibling, all other
    branches and earlier separators. Label: neutrons 10, protons 9,
    electrons 9 — shell 1: 2/2, shell 2: 7/8. This step now places the additional
    neutron separator as well as the PE split; `unplacedAdditionalNeutrons`
    is 0. This is procedural bookkeeping, not a physical derivation.

20. **Neon-20**: split the left-center blue face into touching blue/red
    triangles (red/blue on the reverse). Keep the original area and boundary;
    no shrinking, whitening or new neutron line. All earlier geometry remains.
    Label: neutrons 10, protons 10, electrons 10 — shell 1: 2/2, shell 2: 8/8.
    The neutron separator added in step 19 remains visible and unchanged.

Isotope labels use a compact card with a 14px heading, 12px aligned count
rows and indented shell occupancies. Electron totals are derived from the
shell occupancies: hydrogen 1, helium 2, lithium 3, beryllium 4, boron 5, carbon 6, nitrogen 7, oxygen 8, fluorine 9, neon 10. Step 4 also
uses this format for Hydrogen-1. These are neutral-atom procedure labels.

The lines introduced in steps 2 and 5 have no arrowhead direction marks,
including in later steps; their growth animations are unchanged.
The plane expands from the base edge, not from an enclosing rectangle. The
Animate expansion toggle controls the new layer's transition (0.9 seconds for
steps 1–4; 1.2 seconds of arrow growth then 0.6 seconds of face fill for step 5;
1.2 seconds of color change for steps 6, 8, 11, 13, 15, 17, 19 and 20; 1.2 seconds of white-line growth for steps 7, 9, 10, 12, 14, 16 and 18).
The selected view and step survive reload. This is a separate planar procedure,
not a replacement for Cellulation or a particle-count assignment.
Tests: `node --test tests/retained-expansion.test.mjs` and
`node scripts/test-retained-expansion.mjs`.

## Geometry-only cellulation

The Cellulation **Scene** panel shows grid opacity, face opacity, edges-only,
construction visibility, camera presets/rotation/zoom/reset/recenter, and optional view
auto-rotation (speed appears only when enabled). Unrelated hover/tube inspection,
earlier-plane outlines, ray alignment, particle-axis rotation and numeric camera
angle sliders are omitted here. Other views retain their existing controls.

Select **Sulfur-32 → View → Cellulation**. **Previous / Next** buttons navigate
the steps, starting at **Step 1 · Single unit tetrahedron**: one regular tetrahedron, four triangular
faces and six edges. Every elementary edge has fixed unit length. The tetrahedron
belongs to the same FCC lattice. **Step 2 · Mark top vertex** adds a white dot
at the seed's upward vertex, without changing the tetrahedron or background grid.
**Step 3 · Grow red arrow** adds a red directed edge from that white dot to the
lower-right vertex in the default upright view. A hollow white circle is already
present at the destination in this step. The arrow is fixed to the 3D edge and
scales on screen with the view, not by changing its world coordinates. All direction markers are half-sized and
centered on their segments rather than placed at their endpoints.

**Step 4 · Witness the vertex** keeps that destination circle hollow throughout,
including after the return completes. Two white edges grow in order, turning
right around the front triangular face and returning to the original white dot.
The original dot remains solid white. **No dot fills and no face turns red in Step 4.**
The proposed circle is a continuous, camera-facing ring with a truly empty centre.
At the turn into the second white arrow, a hollow **red** circle appears on that
turning vertex. It remains hollow throughout Step 4.

**Step 5 · Close the adjacent faces** keeps the original white dot, hollow
destination circle and first return path. Two new white arrows grow from the starting white vertex through the
remaining tetrahedron vertex to the white dot at the red arrow's tip. Only after
this second path closes does the destination circle fill white and do **both
triangular faces incident to the red edge** fade red together. The other two faces remain unchanged.
The first red turning-vertex outline is retained. A second red outline appears
on Step 5's turning vertex when its second white arrow starts. Both red markers
remain hollow through the end of Step 5, even though the adjacent faces are red.
Visible red markers support the same click-to-lock normal interaction as white dots.

**Step 6 · Connect the red candidates** retains the five existing directed edges,
the two red faces and both hollow red candidates. A white arrow grows along the
missing tetrahedron edge from the first candidate to the second. Only after it
arrives do both candidates fill red (0.35 s), then the other two faces fill white
(0.65 s). The initial hold is 0.9 s and arrow growth takes 1.6 s. Thus the final
cell has six directed edges, two red faces and two white faces. Switching Animate
on keeps the previously completed red faces but restarts this new arrow, red-dot
fills and white face fills. No camera movement is introduced.

**Step 7 · Repeat from the witnessed white dot** keeps the first tetrahedron in
its completed Step 6 state. It translates the unit tetrahedron along the red
edge so its new starting vertex is the white destination witnessed in Step 5.
The continuation uses the same FCC coordinates and red-arrow direction, sharing
that vertex with the original tetrahedron. It animates steps **2–6** in sequence:
start from that white dot, grow the next red edge, witness the next white vertex,
close its two adjoining red faces, connect its red candidates, fill them red,
and fill its remaining two faces white. Switching Animate on restarts only the
new construction. Existing geometry, camera and still-valid dot locks are
retained; shared vertices have one click target.
Check `node --test tests/cellulation-repeat.test.mjs`.

**Step 8 · Complete the octahedron** retains both completed tetrahedra and adds
the whole FCC octahedron between their facing triangular faces. Four white
arrows run from the four red vertices to the new opposite vertex. With Animate
on they grow in cyclic order (0.6 s hold, 1 s each), then the new white vertex
and the octahedron's faces fill white (0.35 s). No new face fill appears before
all four arrows arrive. The two shared faces are already white; only the six
remaining faces receive the new white overlay, avoiding duplicate shared-face
painting. Face opacity and Edges only are respected. The octahedron has six vertices, twelve elementary edges and
eight triangular faces, with no internal diagonals. The two shared tetrahedral
faces and six existing edges are not redrawn; the two new equatorial edges are
neutral scaffold, not extra arrows. The opposite vertex supports normal locking.
Animate off shows the complete octahedron immediately. Camera and prior geometry
are preserved. Check `node --test tests/cellulation-octahedron.test.mjs`.

**Step 9 · Continue the red-arrow line** adds exactly **one new tetrahedron
and one new red arrow** at the white endpoint of the existing red-arrow chain,
not the octahedron's opposite vertex. The three red arrows are consecutive,
collinear, and point in the same direction. After the new tetrahedron completes
steps 2–6, four white arrows close an octahedron **between the previous last
tetrahedron and the new tetrahedron**. It shares one full triangular face with
each; its faces become white when it closes. The result has three tetrahedra
and two octahedra. No additional tetrahedron pair is introduced. Existing cells
stay complete throughout playback.
Shared vertices have one click target; new markers support normal locking.
Animate off (including reload) shows the completed result; switching it on
restarts only the new assembly. Neither changes the camera.
Check `node --test tests/cellulation-cycle.test.mjs`.

**Step 10 · Continue five more times** repeats Step 9 five times sequentially,
always starting at the current red-arrow endpoint in the same direction. Each
repetition adds exactly one tetrahedron/red arrow and an octahedron between the
preceding tetrahedron and the new one. Four white arrows close each octahedron;
its faces then become white before the next repetition starts. Step 9's assembly
stays complete. The final result has eight collinear red arrows, eight tetrahedra,
and seven octahedra. Animate off shows all five additions immediately; toggling it
on restarts only those additions. Reload keeps Animate off. Camera position,
orientation and zoom are retained; use manual pan/zoom to view the longer chain.
Check `node --test tests/cellulation-extensions.test.mjs` and
`node scripts/test-cellulation-extensions.mjs`.

**Reference-based coordinates:** Steps 11–18 are now defined by local FCC offsets
from the actual terminal red turn in Step 10, not absolute positions. Shortening
Step 10 moves that origin from `(9, 1, 8)` to `(8, 1, 7)` and moves all subsequent
geometry by `(-1, 0, -1)`. Candidate IDs and the camera stay unchanged. The
coordinate triples in the step descriptions below retain the original operator
specification; subtract `(1, 0, 1)` for the current live coordinates. The final
Step 18 endpoint is now `(8, 8, 0)` after five repetitions. Reference continuity is checked by
`node --test tests/cellulation-references.test.mjs`.

**Step 11 · Arrow from (9, 1, 8)** retains the completed Step 10 assembly and
adds one white unit arrow with XYZ Euler direction `(-45°, -45°, 90°)` from +X.
Its FCC endpoints are `(9, 1, 8) → (9, 2, 7)`. An unfilled white candidate
marker appears at the endpoint when the arrow completes, with ID
`step11:candidate`. It supports coordinate hover, grid highlighting and ID copy;
its rotation-lock normal follows the incoming arrow. No cells are added.
Animate plays only this arrow over one second; camera and existing dot IDs stay
unchanged. Recenter includes the new endpoint. Check
`node --test tests/cellulation-step11.test.mjs` and
`node scripts/test-cellulation-step11.mjs`.

**Step 12 · Close the white tetrahedron** first adds the white unit arrow
`(9, 2, 7) → (8, 2, 8)` and fills triangle `918–927–828` white. It then draws
white arrow `(9, 2, 7) → (8, 1, 7)`, fills the existing candidate at `927`
solid white, and fills both newly closed faces `918–927–817` and `927–828–817`
white. The first filled face and all previous work remain visible. The new
completed tetrahedron is included in the two-layer lattice neighborhood (16
construction cells; 180 background cells). The candidate retains its ID.
Animate uses 1 s per arrow, 0.35 s for the dot fill and 0.65 s per face-fill
phase. The faces respect Edges only and Cell face opacity. Check `node --test tests/cellulation-step12.test.mjs`
and `node scripts/test-cellulation-step12.mjs`.

**Step 13 · White arrow from (9, 2, 7)** draws a white unit arrow with XYZ
Euler direction `(-45°, 45°, 90°)` from +X, ending at `(9, 3, 6)`. A hollow
white candidate (`step13:candidate`) appears at its end. Step 12 remains fully
filled, including the solid white dot at `927`. Only the new arrow animates
(over one second); camera and previous dot IDs remain unchanged. Check
`node --test tests/cellulation-step13.test.mjs` and
`node scripts/test-cellulation-step13.mjs`.

**Step 14 · Close face 927–936–837** draws white arrow `936 → 837` with
XYZ Euler direction `(180°, -45°, 180°)` from +X, then white arrow `837 → 927`,
and finally fills the resulting triangle white. Each arrow takes one second;
the face fill takes 0.65 seconds. A hollow white candidate appears at `837`
(`step14:candidate`) when the first arrow reaches it. The hollow candidate at
`936` remains; no extra cells are added.
Check `node --test tests/cellulation-step14.test.mjs` and
`node scripts/test-cellulation-step14.mjs`.

**Step 15 · Close face 927–936–826** draws white arrows `936 → 826` and
`826 → 927`, then fills triangle `927–936–826` white. Step 14's face remains
white. The two arrows take one second each, followed by a 0.65 s face fill;
a hollow white candidate appears at `826` (`step15:candidate`) when the first
arrow reaches it. The candidate at `837` remains, so both are present at Step 15.
Both support coordinate hover, grid highlighting, rotation lock and ID copying.
No extra cells are added. Camera and existing IDs remain unchanged.
Check `node --test tests/cellulation-step15.test.mjs` and
`node scripts/test-cellulation-step15.mjs`.

**Step 16 · Close two side faces** draws white arrow `828 → 837`, fills
triangle `927–828–837` white, then draws white arrow `826 → 817` and fills
triangle `927–826–817` white. Each arrow takes 1 s and each face fill 0.65 s,
strictly in that order. Earlier faces and hollow candidates remain unchanged;
no additional cells or dots are created. Check
`node --test tests/cellulation-step16.test.mjs` and
`node scripts/test-cellulation-step16.mjs`.

**Step 17 · Close the candidate tetrahedron** draws white arrow `837 → 826`
(1 s), fills the existing dots `837`, `826`, `936` solid white (0.35 s), then
fills **both** triangles `936–826–837` and `927–826–837`, plus rectangle
`817–828–837–826`, white (0.65 s). The rectangle's opposite corners are `817`
and `837`; it is rendered as two triangles without a drawn diagonal.
Previous faces remain white and all three candidate IDs are retained. The
completed tetrahedron is included in the bounded background neighborhood;
there are now 17 construction cells. Check
`node --test tests/cellulation-step17.test.mjs` and
`node scripts/test-cellulation-step17.mjs`.

**Step 18 · Repeat steps 12–17 five times** continues in XYZ Euler direction
`(-45°, 45°, 90°)`, i.e. FCC displacement `(0, +1, -1)` per repetition.
The translated Step 12 tetrahedron is exactly the preceding completed Step 17
tetrahedron: that shared join is retained, not duplicated or replayed. Each
repetition then animates its new Steps 13–17, preserving white arrows, face
fills, candidate-to-solid dot fills, and the white rectangle. Five repetitions
advance the live white endpoint from `(8, 3, 5)` to `(8, 8, 0)`, adding five unique
tetrahedra (22 total cells) and 15 uniquely identified dots. Step 17 remains
complete throughout replay. Each repetition takes 11.6 s; Animate off shows
all five immediately. Camera is unchanged; Recenter fits the extended shape.
Check `node --test tests/cellulation-step18.test.mjs` and
`node scripts/test-cellulation-step18.mjs`.

**Step 19 · Attach the mirrored blue assembly** references the actual Step 10
red assembly and the actual Step 18 endpoint. The corrected first blue edge is
`(8, 8, 0) → (7, 8, 1)`. The mirrored copy is then rolled **180° about its
longitudinal axis**, through `(8, 8, 0)` and `(0, 8, 8)`. Both endpoints and all
long-axis arrows stay fixed. The final transform is
`attachment + (-dz, -dy, dx)`, with `d = p - sourceStart`, preserving reflection
handedness, FCC vertices and unit lengths. The four-side path is nonplanar.
Red arrows/faces/markers in the copy become blue; white decorations stay white.
The original assembly stays in place. The shared attachment tetrahedron is
reused rather than duplicated; its prior face meshes are masked at completion
so the blue copy does not double-render those faces. Shared dots retain their existing
IDs/colors; other copied dots have `blue:`-prefixed IDs and transformed normals.
Animate rolls only the reflected copy around its long axis (1.8 s); off/reload shows it complete.
Off-lattice intermediate geometry is not registered as placed cells or pickable
dots until the turn completes. There are 36 completed cells, with one shared tetrahedron counted only once. Camera is retained and Recenter includes the copy. Check
`node --test tests/cellulation-step19.test.mjs` and
`node scripts/test-cellulation-step19.mjs`.

**Step 20 · Close the loop with a reflected white bar** copies only the white
additions from Steps 11–18, not their underlying red assembly. It references the
blue endpoint `(0, 8, 8)` and red start `(0, 0, 0)`. Point reflection through the
midpoint of the source start and attachment is followed by a +90° X rotation
about the attachment; the final map is `attachment + (-dx, dz, -dy)`, where
`d = p - sourceStart`. This closes the fourth equal-length side exactly.
Previous red/blue geometry remains complete. The shared red-start tetrahedron
is reused: duplicate copied faces, arrows and dots are hidden there to preserve
its original colors and IDs. Other copied dots use `closing-white:` IDs.
There are 42 unique completed cells. Animate turns only the new white copy
(1.8 s), with temporary off-lattice geometry excluded from placed-cell picking.
Camera is preserved; Recenter includes the closing bar. Check
`node --test tests/cellulation-step20.test.mjs` and
`node scripts/test-cellulation-step20.mjs`; screenshot:
`test-results/cellulation-step20.png`.

**Step 21 · Build the full white coherence bar · 718 → 178** references the
existing red terminal first turn and reflected blue terminal second turn.
The path is `718 → 628 → 538 → 448 → 358 → 268 → 178`; the existing white
`808 → 718` and `178 → 088` arrows complete the eight-unit connection.
This replaces the earlier edge-only implementation with six complete tetrahedra
and five adjoining complete octahedra, including faces, internal construction
arrows and filled dots. It reuses a six-unit portion of the whole-cell red-bar
construction, recolored white and mapped by `(dx,dy,dz) → (-dx,dz,-dy)` at 718.
There are 53 unique cells at completion. Shared join faces/arrows/dots are
suppressed in the new copy, preserving the existing endpoint IDs and colors.
The five intermediate axial IDs retain the `cross-edge:` prefix; other new
IDs use `cross-complex:`. Animate builds one unit per second, keeping Step 20
complete; replay removes only the new bar. Grid context extends around the
active edge without counting background cells as placed construction.
Check `node --test tests/cellulation-step21.test.mjs` and
`node scripts/test-cellulation-step21.mjs`; screenshot:
`test-results/cellulation-step21.png`.

**Step 22 · Connect the remaining corners · white bar 110 → 770** uses the
same full-complex construction as Step 21. It references the original seed's
second turn and the blue copy's first turn, following
`110 → 220 → 330 → 440 → 550 → 660 → 770`. Existing `000 → 110` and
`770 → 880` segments complete the connection between the remaining corners.
Six white tetrahedra and five complete octahedra are added, bringing the total
to 64 unique FCC cells. The map is `(dx,dy,dz) → (dx,dz,dy)` at 110, with
new IDs prefixed `remaining-edge:` or `remaining-complex:`. All preceding
geometry and join IDs/colors remain intact; only this bar animates or replays.
The two crossbars cross in the +Z projection, not in 3D: their axes lie at
FCC z=8 and z=0 respectively.
Check `node --test tests/cellulation-step22.test.mjs` and
`node scripts/test-cellulation-step22.mjs`; screenshot:
`test-results/cellulation-step22.png`.

**Steps 23–26 · Fill the four faces** build the shell one face at a time:
`000–808–880`, `000–088–808`, `000–880–088`, then `808–088–880`.
Each large face consists of 64 unit FCC triangles, supported by whole tetrahedra
and octahedra on its inward side. Only cells with a complete face on that shell
plane are selected. Existing cells, colored faces, arrows and dot IDs are reused;
new exposed tetrahedral triangles inherit red or blue by matching the actual
colored face planes of the Step 6 seed or its Step 19 blue transform. Exposed
octahedral triangles remain white. Thus Steps 23–24 continue red–white patterns,
and Steps 25–26 blue–white patterns, without repainting the existing white bars.
This replaces the earlier all-white shell fill. Every new boundary reading
retains its owning cell and source seed-face ID (or white-octahedral-filler rule).
New supporting cells can also expose a white triangle on the next shell plane;
it is drawn once and reused later. Internal faces remain neutral scaffold, not
new color/particle assignments.

The bulk fade has been removed. Every new cell now has a deterministic action
trace using the existing local construction protocols:

- Tetrahedron: witnessed source → hollow target → primary arrow → first return
  path → first witness → second return path → second witness → target-dot fill
  → two primary faces → candidate-connecting arrow → candidate-dot fills →
  remaining two faces → whole-cell commitment.
- Octahedron: two completed support tetrahedra and witnessed ring vertices →
  opposite candidate → four incoming arrows → four-arrival witness → opposite
  dot fill → face fills → whole-cell commitment. The two neutral equatorial
  scaffold edges are the existing Step 8 exception, revealed after closure;
  they are not presented as extra directed arrows.

Every action records prerequisite IDs. Face meshes, dots, arrows and placed-cell
membership follow their own certified intervals; a cell is committed only after
all its face witnesses. Candidate dots are interactable while hollow, with the
local centroid-to-vertex normal; new IDs retain `shell:`. Existing dots retain
their colors, normals and IDs. Missing starting/support witnesses block a plan;
no fallback bulk fill is available. Exact directed/color matches are reused.
A reverse arrow is **not** reused as the requested direction: it is retained and
the required opposite arrow is explicitly drawn as a separate recorded addition.
The four patches currently add 31, 31, 22 and 32 such opposite-direction arrows.

**Inspect from start / Previous action / Next action** allows precise inspection
without waiting for playback. **Show complete** evaluates the same validated
trace at its endpoint; it does not bypass construction prerequisites. Normal
playback takes approximately 237, 237, 196 and 212 seconds respectively.
Earlier steps remain complete throughout replay and inspection. Manual inspection
resets on reload, changing steps or enabling Animate.

**Order dependence is now reproduced**, not merely untested. Swapping the two
permitted cell constructions `shell:t:3,1,2` and `shell:t:3,2,1` changes dot
`422` from red to white and changes its normal. Reordering the macro-faces can
also change the final directed arrows. The viewer warns about this; its selected
construction order is unchanged. See
[`cellulation-shell-order-audit.md`](../../research/realization-tower/cellulation-shell-order-audit.md)
for the exact two-cell counterexample, bounded coverage and unresolved rule.
Run `node scripts/check-cellulation-shell-confluence.mjs`; exit 2 means a
reproduced conflict. The JSON report is
`test-results/cellulation-shell-confluence.json`.

The [source-role audit](../../research/strominger/cellulation-dot-422-compatibility.md)
finds that **neither conflicting translated cell preserves its retained boundary
roles**: the red-producing copy requires white 312, already red; the
white-producing copy requires red 332, already white. The viewer retains both
claims and labels 422 unresolved. Opt-in `requireSourceRoles:true` rejects
incompatible copies before emitting their events; the tested Step 23 then admits
0/30 cells. This is a blockage, not a fix by choosing white or red.

The [exhaustive event-model follow-up](../../research/realization-tower/cellulation-shell-exhaustive-verification.md)
checks every permitted action interleaving of the known two-cell fork:
406 states, 155,117,520 schedules, two different outcomes. The full-shell
search is explicitly incomplete at its resource limit. Run
`node scripts/check-cellulation-shell-exhaustive.mjs`; specifications and
replayable counterexamples are written under `test-results/`.

Scope: forward realization of the retained geometric construction protocols,
not a new mathematical coherence theorem, physical flow law or particle-role
assignment. Tests reject omitted returns, early face fills, reversed witness
paths, missing source dots and incomplete face certificates, and check actual
mesh/arrow/dot visibility at every action boundary.
Completed cell counts are 94, 124, 149 and 174. The outer surface has 256 unit
triangles, two triangles per surface edge and Euler characteristic 2; all 86
strictly interior cells are excluded. This is a supported shell, not a solid fill.
Checks: `node --test tests/cellulation-shell*.test.mjs` and
`node scripts/test-cellulation-shell.mjs`. Screenshots:
`test-results/cellulation-step23.png` through `cellulation-step26.png`, and
`test-results/cellulation-shell.png`.

**Validate loop** (Appearance, Steps 20 onward) is a saved, opt-in diagnostic overlay.
It computes once for the completed geometry and reuses the report during camera
movement; off skips validation and animation pauses it. J1–J4 mark the joins,
and numbered amber edges identify findings. The Process panel reports endpoint
closure, equal bar lengths, a 32-edge perimeter traversal, rendered arrow colors
and directions, unique join IDs, and whole FCC cell validity/duplication/face
ownership. Arrows are collected from the visible scene with clone transforms and
actual material colors, not merely copied from model declarations.

The current loop has four closed joins, four sides of eight cell lengths, and
42 valid unique FCC cells. Two findings remain on White A relative to the chosen
red → white A → blue → white B traversal: reversed `808 → 817` and opposing
arrows on `871 ↔ 880`. These may represent intentional counterflow and are not
automatically changed. N–N–P–E roles remain **unassigned**. This does not certify
particle roles or decorative surface overlap/face-role consistency. Orthogonal
review snapshots: `test-results/cellulation-loop-validation-{x,y,z}.png`.
Check `node --test tests/cellulation-loop-validation.test.mjs` and
`node scripts/test-cellulation-loop-validation.mjs`.

The bottom-left **orientation compass** shows signed XYZ directions and shaded
XY/XZ/YZ planes. It follows camera rotation/roll, remains screen-sized through
zoom, and never intercepts pointer input. Check
`node --test tests/orientation-compass.test.mjs` and
`node scripts/test-orientation-compass.mjs`.

Timing: 0.9 s initial hold, 1.6 s per return edge; Step 5 adds a 0.65 s face fill.
**Animate** is an on/off checkbox. Off shows the completed step immediately;
switching it on plays the current sequence from its beginning. While on, step
navigation plays the newly selected sequence. Cell-scale changes do not restart it. Turning it
off stops playback and shows the final state. **Every page load starts with
Animate off**, even if it was on when the session was saved; reloading never
starts playback. Camera/grid/opacity changes do not restart the sequence.
The animation stops scheduling frames when complete and limits time advancement
after stalls.
This is a visualization of the specified witness rule, not an independently
established particle interpretation. No later construction steps are assumed.
Numbered steps show a faint background of whole lattice cells within **two
face-adjacency layers of the currently placed elements**, using the same fixed
unit cells and coordinates. There is no viewport-wide lattice in these steps.
The neighborhood is cached across rotation, pan and zoom, and grows only as
construction cells appear (27 background cells at Step 1; 169 after Step 10).
**Grid opacity** adjusts it independently of the construction.
Enable **Highlight grid edges on dot hover** under Appearance to brighten only
the grid edges incident to an existing construction dot. The option is saved;
it defaults off. The separate saved **Show grid vertex candidates on hover**
option also defaults off. When disabled it skips vertex-cache construction,
projection and hover picking. When enabled, bare grid vertices show a temporary
hollow white candidate and their FCC position when hovered, but do not trigger edge highlighting or become
placed construction dots. Their fixed-pixel hit radius and cached vertex list
avoid rebuilding the grid. The marker clears on leave or drag, and existing dots
take precedence. This also works in the full-reference view. Highlighted edges have camera-facing labels at their midpoints (with
leader lines and collision avoidance), showing XYZ Euler angles in degrees.
Because a direction does not determine roll, these use the shortest rotation
from +X toward the edge pointing **away from the hovered dot**. The hovered dot
shows its integer FCC `(x, y, z)` position. These values are lattice-relative,
not camera-relative, and the labels never intercept pointer events.
Leaving the dot or disabling the option removes the highlight and labels without
rebuilding the lattice. Check `node scripts/test-cellulation-grid-hover.mjs`. The step selection persists. Unit check: `node --test tests/cellulation-steps.test.mjs`.

The construction is translated **eight unit cell lengths screen-up**, capturing
screen-up from the current/restored camera the first time the updated cellulation
view renders. The camera does not move. That world-space offset is saved and
applied to every step and its lattice, including click targets; it neither follows
later camera rotations nor accumulates on reload. The moved start can be outside
a close-up viewport. Explicit **Reset view** reframes the translated seed centroid
28% across and 28% down the viewport; it is never invoked by this translation.
Check `node scripts/test-cellulation-placement.mjs`.

The frame-cross **Recenter** icon sits directly below the reset icon on the
viewport and also below **Reset view** in the Scene panel. The viewport button
remains visible with the panels closed. It fits the currently
placed construction to the viewport with a 15% margin, excluding the surrounding
lattice. It preserves the current viewing direction/roll rather than restoring
the default orientation. It pauses auto-rotation and releases a dot lock so it can
center the whole shape. It does not move cells or restart construction animation.
Check `node scripts/test-cellulation-recenter.mjs` and
`node --test tests/cellulation-neighborhood.test.mjs`.

Step navigation and the Animate toggle never reset the camera. Position, orientation and
zoom are retained across steps and reference-view changes, restored on reload,
and remembered when returning to Cellulation during the session. The upright
default is used only when no prior cellulation view is available, or when the
operator explicitly presses Reset view. Check:
`node scripts/test-cellulation-view-retention.mjs`.

Hover any dot to see its stable ID, integer FCC lattice coordinates `(x, y, z)`,
and translated world coordinates. **Double-click a dot to copy its exact ID**
to the clipboard using VueUse `useClipboard`. A brief confirmation appears;
unavailable/denied clipboard access reports the ID for manual copying instead.
A double-click leaves the dot's final pin state unchanged.
Lattice coordinates do not change with view
scale, pan or rotation and can be quoted alongside the ID to identify a vertex.

Click a white dot (including the proposed outline) to fix that vertex and its
outward centroid-to-vertex normal. Drag, rotation buttons, view presets and
spin are constrained to rotation about the normal through that dot. The dot's
screen position and normal stay fixed; panning is disabled and zoom is anchored
to it. A short bar above the dot marks the lock (no surrounding ring). Click again to release, or click another dot
to replace it; keyboard Enter/Space works too. Reset releases the lock. The lock
survives step and cell-scale changes while its dot remains available, but clears
on hiding/removing the dot, switching views or reloading. No lock is
silently restored from a saved session. Browser check:
`node scripts/test-cellulation-dot-lock.mjs`.

Choose **View → Full cellulation · reference** for the repeating FCC tetrahedral–
octahedral honeycomb. It is no longer bounded by the sulfur carrier. **Cell scale**
changes the view scale (0.5–2), not the geometry: smaller values show more unit
cells across the screen; larger values show fewer, larger-looking cells. The
visible world span changes inversely to this setting. Camera orientation is
unchanged. All construction and lattice coordinates remain fixed, and animation
is not restarted. There are no particle labels, wire overlays, composition
glyphs or particle inventory. View scale and the camera persist.

In the separate full-reference view, the mathematical lattice is unbounded;
the renderer materializes a moving
window around the camera target, snapping to even lattice translations so
panning does not change the lattice phase. A camera-aligned slab covers the
entire viewport, including its corners, with extra cells outside the frame.
Its width and height follow zoom, pan, rotation and aspect ratio without the old
12-unit viewport cap or perimeter fade. A camera-oriented depth fade keeps
distant layers from obscuring nearby cells; column clipping avoids allocating
a large cubic volume when zoomed out. The legacy bounded helper remains for
non-view fixtures, but the live viewer always uses the viewport slab. No extra faces, cuts or
octahedral diagonals are inserted. Source: `repeating-cellulation.mjs` and
`cellulation-renderer.js`. Check with `node --test tests/repeating-cellulation.test.mjs`
and `node scripts/test-sulfur-cellulation.mjs`.

Separately, **12×12 fibration → Tetrahedral–octahedral cellulation** opens the
larger reference carrier. That minimal Three.js entry point reuses its geometry:
119 tetrahedra and 56 unsplit octahedra in the existing finite tetrahedral carrier.
It is not an infinite lattice or a particle model. No role labels, polarity
sheets, flow arrows, central markers or composition glyphs are displayed.
Shared faces and edges are drawn once; octahedral internal diagonals are absent.

Controls: tetrahedron/octahedron visibility, edges, face opacity, reset;
Trackball rotation/zoom/pan and focused-canvas arrow-key rotation / +/- zoom.

- Sources: `cellulation.html`, `cellulation.js`, and
  `research/realization-tower/cellulation-geometry.mjs`.
- Local research route: `/research/realization-tower/cellulation.html`.
- Website route: `/experiments/native-belt/cellulation.html`.
- Build: `node scripts/prepare-normal-ray.mjs`; website copy:
  `node scripts/prepare-native-belt-viewer.mjs`.
- Checks: `node --test tests/cellulation-geometry.test.mjs` and
  `node scripts/test-cellulation-view.mjs` (local server on port 8777).


Authoritative UI and renderer source now lives here, following
`examples/threejs-reference/` and `docs/threejs-pages.md`. This is an actual
compiled Vue SFC migration, not a styling-only change.

- `App.vue`: separate closable process/scene panels, accessible controls,
  imperative handle lifetime, reduced-motion preference, cancellation during
  lazy renderer loading.
- `useViewerModel.js`: reactive inputs and pure computed render packets.
- `scene.js`: owned Three.js/TrackballControls renderer. Objects stay outside
  Vue reactivity; static views render on demand, motion uses bounded elapsed
  time, and offscreen/hidden views suspend frames. Resources, textures, controls,
  observers and event listeners are disposed on teardown/failure.
- `index.html`: meaningful static SVG/text outside the Vue mount, surviving
  missing JavaScript, missing bundles or unavailable WebGL.
- `style.css`: responsive layout with no floating panels over the model on
  narrow screens; visible keyboard focus and independent panel closure.

The matched Three.js **0.180.0** module and TrackballControls addon come from
this repository's pinned package dependency, as in the migrated tetrahedral
planes viewer. No CDN or older global r128 control is loaded. The build copies
Three.js and Vue license files into its generated directory.

## Published native N-cut belt

Public guide: `/experiments/native-belt-guide`. Launch:
`/experiments/native-belt/index.html?preset=native-belt`.
`node scripts/prepare-native-belt-viewer.mjs` rebuilds this viewer and publishes
local assets and licenses; the website build invokes it automatically.
`node scripts/test-native-belt-publication.mjs` checks the published route,
preset, navigation, geometry/wiring switch and reload persistence.

Geometry removes one displayed unit N tip per parent and rigidly docks the
exposed triangle to the central belt-face triangle. Removed records remain in
`parentCutAudit`. Wiring is an expanded diagram, not the metric embedding.
Opaque P/E faces follow the native tetrahedral-orientation color convention;
thick white borders mark the declared inside-N sector. V-labels use screen-space
layout, with V1/V2 suppressed in both belt views. Geometric attachment is checked;
native field transport and physical interpretation remain open.

## From center cell — interface expansion

Select **From center cell — interface expansion** in the process menu at
`research/realization-tower/normal-ray.html`. Previous/Next traverses the dot,
central P, revised P/E/N/N boundary, relocation through native octahedral
wedges, bidirectional meeting guides, and eight typed arrow cells (steps 0–5).
The removed candidate trial is not restored: Step 5 builds the operator's
P [N N] E, P [P P] P, P [N E] N, and P [N P] N assignments.
Existing processes are unchanged.
Progress is saved independently.

Source: `research/realization-tower/center-interface-process.mjs`.
Every displayed cell is selected by exact vertices from the existing esd7
census. The central regular tetrahedron has four neighboring octahedral wedges;
these are not reflected regular tetrahedra. Each boundary identity relocates to
the opposite congruent wedge in its own native octahedron. The source's cyclic
component order supplies the displayed two intervening cells. All consecutive
cells share complete triangular faces, including the middle pair. Source ring
orientation is a display convention, not uniquely forced by P/N/E types.
The remaining fourth wedge in each octahedron is not filled. Geometry membership
is verified; the assigned types do not constitute a native species-law proof.
The incorrect cap dilation and compressed 3/5/9/17 collar display have been
removed. Those earlier screenshots/probes are historical, not this construction.
The native k=7 envelope is a reference only; guides are not certified paths.

Build and check:

```sh
node scripts/prepare-normal-ray.mjs
node --test tests/center-interface-process.test.mjs
node scripts/test-center-interface-process.mjs
```

See [the working approach](../../research/strominger/recursive-interface-realization-approach.md).

## Be-9 → Central-sleeve trial

**Be-9** is a separate Construction process entry cloned from Be-8. Its
White-rooted hex simplex View stays at depth four, with the same eight layers.
With **Show Be-9 reference** enabled, **Central neutron sleeve (trial)** routes
the four mixed strands (output slots 7, 2, 1 and 8) through a common central
region in all three reference/component assemblies. It preserves their
identities and output matching; the other four native guides remain unchanged.
Two incoming pairs become two outgoing pairs through explicit retained passages.

The trial is enabled by default. Uncheck it to restore **Be-9 reference (Be-8
clone)**. The translucent central region encloses four separated display lanes,
not an identity-merging crossing. Each rerouted strand now has four segments
and four midpoint polarity markers. See the
[connection rule](../../research/realization-tower/beryllium-9-reference.md).

Be-8 remains unchanged. Process selection/progress persist separately; seed
display settings are shared, as in the other seed views. The trial switch is
persisted but applies only to the Be-9 reference, not its layer construction.

Checks: `node --test tests/beryllium-9.test.mjs tests/beryllium-9-sleeve.test.mjs`,
`node scripts/test-beryllium-9-viewer.mjs` and
`node scripts/test-beryllium-9-sleeve.mjs`.

## Be-8 → White-rooted hex simplex

Construction process **Be-8** has exactly one View: **White-rooted hex simplex**.
It uses **depth four**: four white-plus-branch steps, eight edge bands, four
side pairs per layer and six-unit pair height. All eight retained layer copies
remain. Each layer has 25 nodes and 30 edges; its reflection centre is at Y=-3.5.
The layer selectors, gap, camera presets and comparison controls are shared with
the Su-32 view, which stays at depth eight.

**Show Be-8 reference** displays an independent eight-route candidate on a unit
octahedral carrier. Four (p,e) entry ports each have two retained turn choices t:
clockwise/counterclockwise to the adjacent rim port, then to the opposite pole.
All twelve native edges are used, with two retained strands on each. The eight
output slots form a reversible permutation; no selected Su-32 or layer paths are
used to construct this reference. Labels are (t,p,e), not Su-32's (a,b,p,e).
See `research/realization-tower/beryllium-8-reference.md` for the routing rule.
Two full copies appear below the Be-8 reference: component selection in fixed
clockwise and counterclockwise directions. The four mixed strands resolve to two
white and two red; the opposite direction swaps those selections. The original
reference remains white–red. Pure white and pure blue stay unchanged.
Only the selected component colour changes: all eight identities, columns,
guides, edge order and input/output slots remain fixed. There are no reversed
paths, swapped slot labels or additional reading arrows. The three white polarity
markers per mixed strand stay at the same straight-segment midpoints and retain
the same orientations. Bottom numbers remain the original output slots.
The Be-8 comparison panel widens to show a 3D traced octahedron to the right of
each of its three reference/component graphs. Assemblies use the same eight
native routes, row-specific colours and white polarity arrows; shared edges
have slightly separated display lanes with exact native endpoints. Drag to
rotate, use arrow keys when the canvas is focused, or Home/Reset to restore the
view. Hover a strand on the left to highlight it in all three assemblies; others stay visible at 20% opacity. Small
screens stack the assemblies below their graphs. Check with
`node scripts/test-be-octahedral-assemblies.mjs`.

Reference and Combined use eight aligned comparison positions. Combined traces
the selected depth-four layers under the explicitly selected candidate rule;
no native/source identity correspondence is assigned by column position.

No sulfur inventory, fibration or other sulfur views are exposed under Be-8,
and selecting Be-8 does not change the saved Su-32 View selection.
Seed display settings are shared; process selection persists independently.

Checks: `node --test tests/beryllium-8.test.mjs` and
`node scripts/test-beryllium-8-viewer.mjs`.

## Sulfur-32 → White-rooted hex simplex

A planar honeycomb simplex rooted at a vertical white edge, with an independent
point-reflected copy in a lower parallel plane. Depth 8 uses the hex experiment
convention: eight white-plus-branch steps, or sixteen edge layers. Each layer has
81 vertices, 108 edges and 256 root-to-boundary paths ending at nine vertices.
Colours identify undirected edge families, clockwise from upward vertical:
white 0°, blue 120°, red 240°. White segments have midpoint direction arrows.

The original is at z=0 and the copy at z=−gap (default gap 2). With c at the
midpoint of the white edge immediately below the original central vertex in XY,
and halfway between planes in Z, the exact copy map is
p′=2c−p. Colours, route histories and endpoint order are carried through that
map, so copied white arrows reverse. The gold dot marks c. Gap is adjustable;
oblique and face-on view buttons aid inspection.

The complete pair is retained and cloned again: the new pair is mirrored through
the plane perpendicular to the central white arrow at its midpoint, then moved
by −2gap in Z. Here the mirror is y=−6.5, so (x,y,z) maps to (x,−13−y,z−2gap).
This replaces the previous 120° rotation. There are four layers at Z=0, −gap,
−2gap, −3gap, with colours retained and directed endpoints and route histories
transported by the reflection.

All four are then retained and copied four gaps lower. Each copied layer is
point-reflected in its own plane about the same XY center: (x,y,z) maps to
(−x,−13−y,z−4gap). Layer order is preserved. The eight resulting layers lie at
Z=0 through −7gap; selectors 1–8 independently toggle their visibility. New gold
markers indicate each lower layer's center. No inter-layer joins are added.

Eight separate parallel blue/red pairs are drawn to the right of each visible
layer, in its plane. The first pair remains in place; seven copies are spaced
0.45 units apart. They are planar projections of twisted pairs, not replacements
for simplex paths. Each axis spans the simplex's actual height (12 units): eight
1-unit white sleeves alternate with eight exposed half-unit bands, the projection
of the coloured edges onto the white direction. Sleeve arrows inherit that
layer's direction. Each exposed conductor follows the signed lateral direction
of its same-colour simplex edges; the return half-turn is inside the preceding
white sleeve. The two conductors stay continuous; projected crossings do not
join them. Existing layer buttons also hide that layer's eight pairs.

**Show twisted pairs** has independent, persistent checkboxes:
- **By layer**: the existing right-hand bank in each selected layer's plane.
- **Combined**: complete retained layer routes in a separate comparison panel,
  to the right of Process—not the former left-hand bank of display-pair segments.
- **Show Su-32 reference**: the existing native reference above Combined in that
  panel. Its sixteen identities, full native guides and output permutation remain
  unchanged when layer selection or the continuation rule changes.

Both diagrams use sixteen aligned column positions, each containing a miniature
projection of one complete route. Reference labels are (a,b,p,e); Combined labels
are bottom-sleeve number and terminal conductor colour. Alignment is ordinal,
not a claimed native identity correspondence. Gold dots mark route starts.

The continuation rule defaults to **Not determined**, which leaves Combined
empty rather than fabricating paths. Two explicitly labelled candidates can be
inspected: same-colour or crossed interior sleeves, both continuing through the
sole existing boundary trunk. Each traces sixteen complete root-connected paths
from actual layer edges. Selected-layer copies are grouped by retained template
identity; identical directed full projections are deduplicated only within that
identity. Different identities are never merged for looking alike. No visible
layers gives an empty Combined diagram while the reference remains available.
The native correspondence and inter-layer sewing rule remain unestablished.

Process sidebar controls follow the enabled views: layer selection is shown for
By layer or Combined (labelled Combined source layers when only Combined needs
it). Gap, geometry notes and camera presets are shown only for By layer.
Reference-only mode hides all of those controls without resetting their settings.
Check all toggle combinations with `node scripts/test-seed-control-visibility.mjs`.

Toggles and the candidate rule persist. The panel does not change the 3D camera
or graph; closing it turns off Combined and the reference, not By layer.

Checks: `node --test tests/sulfur-route-comparison.test.mjs tests/branching-seed.test.mjs`
and `node scripts/test-branching-seed-viewer.mjs`.

## Sulfur-32 → Hex strands · 3D

The Sulfur-32 View menu includes the hex-grid experiment in Three.js. The sixteen
calculated seed paths occupy separate depth layers, with adjustable spacing,
strand isolation, stages 0–7, and individual transformed-copy selection. Set
spacing to zero to recover the planar layout. Show shape adds the planar context.
These controls persist; existing Geometry and Wiring views are unchanged.

Depth separation is display-only, not an octahedral folding. Copy histories are
retained even where their edges coincide; seam continuations remain unassigned.
The viewer model is generated directly from `public/experiments/hex-edge-grid.html`
and `hex-edge-strands.js` by the normal viewer build, not a separate construction.

Checks: `node --test tests/hex-strands-view.test.mjs` and
`node scripts/test-hex-strands-viewer.mjs` (viewer served on port 8777).

## Sulfur-32 reflection

Select **Sulfur-32 reflection** beside **Sulfur-32** in the process menu. It opens
at the completed assembly; Stage or Previous/Next traverses all five construction
stages. The view reads the exact regular-4-simplex construction certificate at
`research/strominger/results/regular-simplex-reflection-v1/verification.json`.

- **Wiring** (default) uses the same continuous, spiral-striped tube renderer as
  Sulfur-32: one retained strand per copy history, with an incoming and outgoing
  bundle. The final assembly has sixteen distinct strands, including coincident
  histories, in white, blue-white, red-white and blue. Opacity is adjustable.
  Internal guides follow actual simplex edges and visit all five labelled vertices
  of each history's successive copies. Shared edges connect the copy visits.
  These are explicit display routes: four native-edge circuits and deterministic
  shortest contact walks, with external bundle leads. They do not establish an
  identification of reflection histories with the original native (a,b,p,e) channels.
- **Geometry** shows all five vertices and ten edges, with a slider rotating the
  fourth coordinate into the visible projection.
- **Copy history** highlights any of the sixteen retained histories, including
  coincident copies. Geometry has fourteen distinct full cells in the final stage.
- In Geometry, the central six-cell circuit is turquoise; its cells are blue.
  Pink and gold distinguish the two vertices outside the working face.
- Stage and view settings persist independently of the original Sulfur-32 process.

```sh
node --test tests/sulfur-reflection-process.test.mjs tests/sulfur-reflection-bundle.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-sulfur-reflection-viewer.mjs
```

The browser test uses the local viewer on port 8777 (override `NORMAL_RAY_URL`),
checks stage navigation, projections, copy selection, reload persistence, and
switches back to the original Sulfur-32 Wiring view to verify its sixteen strands.

## Preserved behavior

The source geometry remains in `research/realization-tower/normal-ray-model.mjs`
and `normal-ray-procedure.mjs`. The viewer does not replace the construction.

- k=1..7, independent procedure stages; changing k recomputes immediately.
- The procedure now follows adjacent surface triangles on the outer face opposite V2; k counts surface-edge crossings, not inward plane depth.
- At k=1, the start and end are distinct primitive cells sharing exactly one edge. Step 2 assigns whole-cell P/E roles again.
- `surface-path-model.mjs` selects a reproducible surface path (first edge-only continuation, then a longest shortest path with cell-ID tie breaks). This is an explicit display-path choice, not an isotope-selection law.
- Orthographic projection, initial/reset azimuth 67°, elevation −68°.
- Envelope barycenter at 62.5% of viewport height.
- Free trackball orbit without pole stops, scroll/pinch zoom and pan.
- Clickable V1–V4 labels toggle fixed rotation anchors without snapping. One anchor allows rotation about its barycenter-to-vertex axis; two stop rotation.
- Both closable panels, appearance controls and optional auto-rotation; the world-orientation overlay has been removed.
- Keyboard orbit/roll/zoom alternatives added; automatic motion starts off.

The role assignments remain trial procedure data, not isotope predictions.

## Isotope-constructor settings

All scene preferences use one app-qualified, versioned localStorage key:
`marici:isotope-constructor:v1:scene-settings` (`settings.js`). It stores k,
appearance and P/N/E label visibility, motion preferences, vertex locks, panel
and section visibility, and camera orientation/roll, pan and zoom. Its `process`
namespace stores the selected construction, k, step, branch, and independent
progress for each construction. Reload resumes the saved selection; older records
without this namespace start at step zero. Camera writes are throttled; unload flushes
pending changes. Reduced-motion safety stops do not erase the saved spin preference.

Legacy `normal-ray:k`, `normal-ray:labels`, and `normal-ray:face-opacity` values
are imported only when the namespaced record is absent. No other application's
keys are changed. Values are validated and clamped; malformed or unavailable
storage falls back safely to defaults. Removing the namespaced key resets the
record (legacy values, if present, will be imported again).

## Process 3

Select **Process 3 — diamond rules** to start the independent clean reconstruction.
The current foundation implements steps 0–4 (seed, three initial rays, atomic
corner diamonds) for every k. Step 5 locates the actual k-envelope centroid:
k=3,5,7 have a unique central P. Step 6 uses a unique four-vertex mapping to add
three P neighbors, leaving the V1-side neighbor unresolved, with dashed geometric
path guides. E is surface-only; the interior E trial has been removed. At k=5 there are nine tied mappings, so the center is shown but shell
orientation remains unresolved. Even k needs an octahedral center rule.
Run `node scripts/inspect-process3.mjs --k 5,7 --step 6` for reproducible overview,
core and axis screenshots plus JSON audits; the tool prints its artifact directory.
It deliberately stops before edge-front filling and N closure; Process 2 remains unchanged. See
[the rule contract and next stages](../../research/realization-tower/process3.md).

## Particle counts

The bottom-right **Counts** panel collapses with its header (mouse or keyboard).
It opens in a compact view: native inventories show their primary whole-cell or
assembly counts; **Breakdown & notes** reveals the retained location, face, void
and trial-channel rows and their scope notes. This is a presentation change only:
no counts, geometry or physical identifications change. The expanded panel scrolls
within the viewport on small screens.

The bottom-right viewport table counts assigned cells, not visible labels or
rendered faces. Surface cells expose a triangular face on the current k-tetrahedron;
all other assigned cells count as interior filler (including edge-/vertex-only
boundary contacts). Each cell is counted once, with P/N/E columns, location
subtotals, and combined totals. Display opacity and visibility do not affect counts.

## Build and test

```sh
pnpm normal-ray:prepare
pnpm normal-ray:test
```

Publisher: `scripts/prepare-normal-ray.mjs`. Only the dedicated generated
`research/realization-tower/normal-ray-viewer/` directory is emptied by builds.
It publishes the compatibility HTML at the **unchanged** URL:

http://127.0.0.1:8777/research/realization-tower/normal-ray.html

The generated directory's own `index.html` is also usable. Serve the repository
root over HTTP; opening files directly is unsupported. Do not hand-edit the
published HTML or hashed assets. The superseded standalone renderer and its
legacy local TrackballControls copy are removed.

## Verification scope

Node checks cover geometry, normality, seven stops, endpoint roles and reactive
state propagation. Browser checks rebuild locally and block external requests.
They cover desktop/mobile Chromium, default view, procedure changes, locks,
keyboard camera controls, opacity without geometry rebuilding, idle scheduling,
independent panels, reduced-motion changes, explicit spin opt-in, offscreen
pause/resume, unmount disposal, pending-start cancellation, unavailable WebGL,
missing application bundle, JavaScript-disabled fallback and the context-loss
handler. A desktop screenshot was inspected during migration.

Not a cross-browser/mobile-hardware certification or real GPU-loss recovery
test. Rendering failure asks for reload, rather than claiming context restoration.
Vite reports a large Three.js renderer chunk; no performance benchmark is
claimed. Broad website publication is separate from this local-viewer build.
