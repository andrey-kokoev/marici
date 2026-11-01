# Be-8: depth-four view and eight-route reference candidate

## Layer construction

The Be-8 view uses four white-plus-branch steps. Per layer this gives 25 vertices,
30 edges (10 of each colour), 16 graph routes, and four bottom white sleeves.
The same-colour/boundary-trunk continuation traces eight retained conductors,
two per bottom sleeve, covering every edge. The three copy operations still
produce eight layers. Side-pair height is six units; the reflection centre is
(0,-3.5), rather than Su-32's (0,-6.5).

## Independent reference

`buildBeryllium8Reference()` uses the twelve edges of a unit native octahedron.
It does not import the source-layer tracer or take a subset of Su-32's wires.

Choose opposite poles as input and output. The four remaining vertices form a
rim square. Their (p,e) labels occur in cyclic Gray order:

    ++ → +- → -- → -+ → ++

For every entry port retain both choices t=+ and t=-. Each complete route is:

    input pole → entry port → adjacent rim port → output pole

- t=+ selects the next rim port in the displayed cyclic order.
- t=- selects the previous rim port.
- The immutable record ID is `be8:wire:tpe`.
- Output addresses retain t and use the new rim port's (p,e).
- Colours follow the incoming (p,e) label: pure white for (++), pure blue for
  (--), and the same white–red palette for both mixed states.
- The mixed-state distinction is carried by a separate polarity arrow:
  q=(p−e)/2 is +1 for (+,-), directed along the original route, and -1 for
  (-,+), directed against it. q is independent of the retained rim turn t.
  This changes the colour encoding, not the routes, IDs or slot permutation.

Four entry ports times two turns gives eight distinct complete routes. Every
native edge carries exactly two retained records. The reference is an explicit
minimal octahedral routing candidate, not an inferred particle inventory.

## Natural matrix

The returned `permutation[j][i]` is one precisely when input i reaches output j.
`matrixBasis` gives the exact row/column ordering. Both row and column sums are
one; transposition gives the inverse.

In sign-labelled input/output coordinates:

    (t,p,e) → (t,p,-e) if t·p·e = +1
    (t,p,e) → (t,-p,e) if t·p·e = -1

Thus two passes flip both p and e while retaining t; four passes restore every
slot. Equivalently, this is a turn-controlled cyclic shift S or its inverse on
the four rim ports. The underlying four-cycle has eigenvalues 1, i, -1, -i.
These are statements about slot routing; the original strand ID is retained
throughout its complete guide.

## Display and checks

The comparison panel shows three aligned eight-strand rows before Combined:

1. The unchanged reference.
2. Components selected in a fixed clockwise direction d=+1.
3. Components selected in the opposite direction d=-1.

Only component colour changes. All original guides, edge sequences, input/output
slots, identities, retained (t,p,e) signs and columns stay unchanged. There is no
path reversal, swapped start/end labelling or additional reading arrow.

For a mixed strand let q=(p−e)/2 be its polarity along the original route, and
t its retained rim turn. The selected component is white if q*t*d=+1 and red
if q*t*d=-1. Thus four mixed strands become two white and two red, swapped in
the opposite-direction row. Pure white and pure blue remain unchanged. The
original reference still shows the white–red mixtures; source palettes are kept
in the component model rather than overwritten.

White polarity markers remain at the midpoint of each of the three straight
segments, with identical positions and orientations in all three rows. Gold
dots retain their original start positions. Bottom numbers remain the original
output slots.

### Traced octahedra

Each of the three reference/component diagrams has a rotatable 3D assembly to
its right. The wider panel adds a second column; small screens stack the views.
The assemblies use an orthonormal projection of the same four-coordinate native
guides, producing six vertices, twelve edges and eight triangular faces.
All eight retained routes are drawn in their row's colours, with the same twelve
white polarity arrows (three per mixed identity). No connections are inferred
from display crossings.

Two strands sharing an edge use separated display lanes, offset by ±0.04 and
tapered back to the exact native endpoints. These offsets do not alter guides,
edge memberships, output slots or the reference permutation. Hover a strand in
any left-hand diagram to highlight that identity in all three assemblies. Drag
an assembly to rotate, wheel to zoom, and right-drag to pan (standard Three.js
OrbitControls). Arrow keys also rotate; Home/Reset restores position and target.
Hover targets cover entire diagram columns, including labels. Other strands
and their arrows remain visible at 20% opacity until the pointer leaves. Each canvas resizes and releases its resources on removal.

Combined follows underneath. All full-reference rows retain the same column positions. The
reference and its component views never change with layer visibility or the candidate
sleeve-continuation rule. Column alignment is not an assigned native/source
identity map.

- `node --test tests/beryllium-8-reference.test.mjs tests/beryllium-8-direction-components.test.mjs tests/beryllium-8.test.mjs`
- `node scripts/test-beryllium-8-viewer.mjs`
- `node --test tests/beryllium-8-assembly.test.mjs`
- `node scripts/test-be-octahedral-assemblies.mjs`

Tests verify actual native edge lengths, complete routes, retained identities,
edge memberships, the bijective eight-by-eight matrix, its four-cycle law, depth
and reflection geometry, comparison alignment, persistence, and unchanged Su-32.
