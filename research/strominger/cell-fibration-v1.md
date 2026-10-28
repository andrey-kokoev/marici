# Cell-level fibration

The old step 3 is removed, together with its dependent layer-4 and layer-5 additions. New additions use the rules below; the old colour rules are not restored.

Original steps 0–2 are unchanged. Former steps 6 and 7 remain as steps 3 and 4, filling only layer-1/2 octahedra. Step 5 adds surface octahedra, including edge positions. Layer 2 is not complete: four inverted tetrahedra (tet-60, tet-41, tet-31, tet-27) still have no assigned colour.

## Current steps

| Step | Construction | P | N | E | Cells |
| --- | --- | ---: | ---: | ---: | ---: |
| 0 | Four corner seeds | 1 | 2 | 1 | 4 |
| 1 | Twelve target-coloured layer-1 tetrahedra | 4 | 8 | 4 | 16 |
| 2 | Twelve source-coloured edge extensions and twelve opposite-coloured face cells in layer 2 | 10 | 20 | 10 | 40 |
| 3 | Four vertex-coloured layer-1 octahedra (former step 6) | 11 | 22 | 11 | 44 |
| 4 | Twelve layer-2 octahedra (former step 7) | 11 | 34 | 11 | 56 |
| 5 | Twenty-four surface octahedra | 17 | 46 | 17 | 80 |
| 6 | Four central tetrahedra: two N, two non-N | 19 | 48 | 17 | 84 |
| 7 | Remaining layer-3 cells, including edges: N | 19 | 90 | 17 | 126 |
| 8 | Copy four quartets to opposite faces | 24 | 98 | 20 | 142 |
| 9 | Paired interior copies | 27 | 101 | 20 | 148 |
| 10 | Remaining interior copies | 27 | 105 | 20 | 152 |
| 11 | Every pair of non-source simplex directions | 33 | 111 | 20 | 164 |
| 12 | Four-neighbour NEPN → P filler coherence | 39 | 111 | 20 | 170 |
| 13 | Surface-to-filler boundary crossing | 41 | 113 | 20 | 174 |
| 14 | Central NPPN → P coherence | 42 | 113 | 20 | 175 |

The folded k=7 carrier has corner colours V₁=N, V₂=P, V₃=E, V₄=N. Cells are whole native tetrahedra or octahedra; colour labels are not established physical particles.

## Layer-2 octahedron rule

View each vertex complex's layer 2 from inside. Its inward triangular boundary contains a hexagon with three filled tetrahedral triangles and three empty octahedral triangles. Each gap copies the filled cell opposite it across the hexagon centre (`p → 2c − p`). If that colour is E or P, use N instead. Thus all twelve new octahedra are N. Earlier cells retain their colours.

This is an inward-boundary rule, not a rule on exterior carrier faces. No inverted tetrahedron is filled by it. Hover information records the opposite cell, source colour and final assigned colour.

## Surface-triangle rule

Add all surface octahedra of the same orientation adjacent to layer-2 triangles: twelve face-middle and twelve edge positions. Shared edge cells are counted once. The two surface triangles share an edge. Copy the source colour with P → E, E → P, N → N. On F214: 22 ← 9, 72 ← 69, 91 ← 96; all three become P. Also 134 ← 138 and 165 ← 171 become P; 148 ← 153 remains E. Both exposed faces of an edge cell read the same source. The hover panel shows the source cell and colours.

The separate edge-colouring step is removed. Cells 16, 31, 34, 127, 130 and 172 remain empty until the final N fill.

## Central-cell rule

Complete two N and two non-N with the three face-connected cells. Add only N or P: two existing N require P; one existing N requires N. Add 24=P, 74=N, 93=P, 95=N. Cell 95 reads 91=P, 104=N, 150=E. Earlier colours are unchanged.

## Remaining layer-3 cells

Step 7 fills all remaining layer-3 positions with N: twelve per vertex, 42 distinct cells (edge cells are shared). For V₃ this includes 139, 154, 108, 62, 50, 81 and the three interior gaps 159, 97, 143. Existing colours remain unchanged.

## Opposite-face quartets

Step 8 translates each central quartet to the opposite carrier face, copying all four colours. For V₁: 72→59=P, 74→63=N, 71→58=N, 125→103=E. All four faces receive a quartet with two N and two non-N: sixteen new cells total. Cell 140 copies 24 as P. Hover shows the source cell.

## Interior pairs

Step 9 copies colours by layer address:

- 5554 and 4554 ← 6444 (N)
- 5545 and 5445 ← 4644 (P)
- 5455 and 5445 ← 4464 (P)
- 4555 and 4554 ← 4446 (N)

Shared targets 4554 and 5445 count once. Six new cells; earlier colours unchanged.

Step 10 adds the specified interior matches: 4455 ← 2466, 5454 ← 6462, and 4545 ← 2646, inheriting each source colour; 5544 ← 6642 is added as N.

The former 5545 colour-extension step is removed. 4646, 6446, 6644, and 5645 remain empty.

Step 11 uses a symbolic rule over all four vertices: source coordinate i is 6, the others 4. For every pair of the three non-source coordinates, increment each once and copy the source colour to the destination only. Each source gives three distinct targets (twelve total): 6444→6455/6545/6554 (N), 4644→4655/5645/5654 (P), 4464→4565/5465/5564 (P), and 4446→4556/5456/5546 (N). Intermediate cells are not filled.

The former nearest-vertex step 12 is removed; its twelve targets remain empty.

## Controls and cuts

Step 12 finds unfilled tetrahedra at permutations of 4466. Decrementing each coordinate identifies four face-neighbours in V₁–V₄ order. Their word must be NEPN; the centre becomes P, preserving exactly two N in the five-cell complex without introducing filler E. The six centres are counted once, not once per view. Existing neighbours remain unchanged.

Step 13 increments the unique 1 to 2 in each permutation of 1666, copying P/N and converting E to P on crossing into filler: 3→10 (P), 163→158 (P), 113→116 (N), 168→162 (N). Existing sources are unchanged.

Step 14 fills the unique central tetrahedron at 5555 with P. Its four face-neighbours (4555, 5455, 5545, 5554) form NPPN; preserving two N and adding no filler E selects P. All 175 cells are now filled.

The endpoint is **Step 14 / 14**. Previous and Restart remove the corresponding additions. Old saved progress beyond 14 clamps to 14; other processes retain their independent progress.

Cuts use geometric layers from the selected vertex, or the union of the four selections with **All vertices**. The range is inclusive. Both bounds use buttons 1–7; button 1 is the corner (internal depth 0). At the endpoint, a single-vertex 3–3 selection contains six tetrahedra and three octahedra; All / 3–3 contains 40 filled cells. A single-vertex geometric layer-3 cut contains 19 filled cells. All / 4–4 contains 70, with no empty geometric layer-3 positions. Corner cells outside a cut remain orientation references, not counted in the visible cut.

**From vertex** uses buttons: All, P (V₂), N1 (V₁), N2 (V₄), E (V₃), coloured to match their cells. Changing the selection moves the new vertex to the previous vertex's screen position and preserves the layer-plane angle and zoom. **All vertices** leaves the view unchanged. Explicit vertex selection is independent of drag locks.

**Show all layers** disables the cut. **Unfilled positions (∅)** explicitly displays same-orientation gaps as wireframes. It does not assign them colours.

## Hover and edges-only view

Cell IDs are 1–175, starting at the proton vertex V₂ and finishing each geometric layer before the next. Within a layer, order follows lattice coordinates V₁,V₃,V₄. IDs include empty cells and do not change with steps or cuts. **Copy ID** copies the integer; **Copy info** also includes the internal geometry key.

Enable **Show cell info on hover** to highlight cells and inspect IDs, shapes, coordinates, vertex-relative layers and construction steps. Unfilled native cells are normally invisible but highlight on hover and are labelled **unfilled**, with no assigned colour or construction step. Cuts restrict them too. They are excluded from filled-cell counts.

Click to pin, **Copy info** to copy the complete record, and Escape to dismiss. In edges-only mode, picking uses edges; at a shared edge an unfilled position takes precedence so it remains reachable. **Show tiling bodies** controls both filled and unfilled picking. Construction or cut changes clear stale hover selections.

**Edges only · thick outlines** omits face rendering without changing construction, counts or saved face opacity. It persists across reload.

## Implementation

- Active model: `../realization-tower/cell-fibration-process.mjs`
- Inner hexagons: `../realization-tower/inner-layer-hex-reflection.mjs`
- Cuts: `../realization-tower/cell-fibration-cut.mjs`
- Current tests: `tests/cell-fibration-process.test.mjs`, `tests/cell-fibration-reflection.test.mjs`, `tests/cell-fibration-empty-hover.test.mjs`
- Browser checks: `scripts/test-cell-fibration-process.mjs`, `scripts/test-cell-hover.mjs`, `scripts/test-cell-edges-only.mjs`

`cell-fibration-history.mjs` preserves the previous construction only for historical structural analysis and geometry test fixtures. The viewer does not import it. The [84-cell structural synthesis](cell-fibration-structural-synthesis-v1.md) describes that historical sector, not the current construction.
