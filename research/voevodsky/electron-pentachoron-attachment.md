# Electron pentachoron attached in hydrogen-1 and hydrogen-2

Date: 2026-10-09
Status: Visual geometric hypothesis; five-cell spinor dynamics not derived

## Change requested

The operator requested the electron itself be represented by a pentachoron in both isotope assemblies. This is distinct from the earlier `pentachoron-direction-trial.md`, which constructed a parent of the entire face-sharing pair.

## Geometry

Retain the electron's tetrahedral boundary cell ABCD, with the existing vertices (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1), now all at w=0. Add E=(0,0,0,√5).

All six edges of ABCD have squared length 8. Each edge from E has squared length 3+5=8. The resulting 4-simplex is regular and nondegenerate: ABCD spans its three-dimensional affine hyperplane, while E has nonzero fourth coordinate.

The boundary cells are ABCD, ABCE, ABDE, ACDE, BCDE. The viewer shows the original four triangles and six edges of ABCD, plus the six triangles and four edges involving E. This is a projection of the boundary, not five disjoint three-dimensional solids.

The declared projection is πλ(x,y,z,w)=(x,y,z)+λw D/‖D‖ in the electron's local frame. Its default λ is zero: E projects to the interior of ABCD, yielding a Schlegel-style view with five marked vertices and all ten edges. The earlier default 0.9 put E beyond D and visually hid the distinction from a taller tetrahedron; it was replaced after operator feedback. Projection is a display choice, not a derived parameter. Changing λ moves the fifth projected vertex while fixing ABCD pointwise. The full pentachoron remains nondegenerate even when its projection overlaps existing geometry.

## Attachments preserved

- **¹H:** proton ABC is identified with the ABC triangle of the electron's boundary cell, using the existing face-match permutation. The proton and the electron's ABCD cell have their fourth vertices on opposite sides.
- **²H:** the proton ABC face meets the belt's lower rim. The ABC triangle of the electron's ABCD cell meets its upper rim. All six matched rim vertices coincide. The belt's uniform display-scale conversion √(8/3) is retained.

The attachment uses a triangular face *within* the tetrahedral boundary cell; it does not identify the entire proton tetrahedron with an entire electron boundary cell.

## Retained calculation versus new hypothesis

The existing four-face spinor calculation, 144-transfer count and two-component return remain attached to ABCD. They are not promoted to a derived operator on the pentachoron's five tetrahedral boundary cells. Neither the extra vertex nor the projection supplies electric charge or a mass law.

The same electron geometry is used in both isotope modes and the separate-constructions view. The previous whole-pair parent experiment remains separately labelled.

## Verification

`node research/voevodsky/checkers/check_unified_assembly_page.mjs`

Browser tests check all ten 4D squared edge lengths, five boundary cells, both isotope attachments, and pointwise invariance of ABCD when the projection slider changes. Existing spinor, rotation, isotope replay and mobile checks remain in place.
