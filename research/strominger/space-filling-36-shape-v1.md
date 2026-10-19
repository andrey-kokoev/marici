# Which solid fits 36 = 12+12+12?

## Geometric candidate: truncated octahedron

The exact hull screen gives:

| Solid | Vertices | Geometric edges | Faces |
|---|---:|---:|---:|
| Cube | 8 | 12 | 6 |
| Cuboctahedron | 12 | 24 | 14 |
| Rhombic dodecahedron | 14 | 24 | 12 |
| Truncated octahedron | 24 | 36 | 14 |

The truncated octahedron's vertices are the permutations of (0,+/-1,+/-2).
Its edges split into three families of12 according to the unique zero coordinate
of the edge displacement. This is a geometric coordinate-plane partition, not
a P/N/E species assignment.

It is the body

    |x_i| <= 2,  |x|+|y|+|z| <= 3.

Its14 supporting planes are exactly the relevant Voronoi bisectors of

    Lambda = (4Z)^3 union ((2,2,2)+(4Z)^3).

All other lattice bisectors are redundant by the explicit integer inequalities
in the receipt. Every point has a nearest lattice point; translates of this
Voronoi cell therefore cover R3 with disjoint interiors. Its exact volume32
agrees with the lattice covolume. This is an all-lattice argument, not a finite
patch extrapolation. A bounded bisector regression is retained separately.

## It fails the current native whole-cell gate

The actual constructor exports two regular tetrahedron orientations and four
split-octahedron components. Their faces have only six unoriented normal
classes: four tetrahedral diagonal classes and two coordinate-axis classes.
The truncated octahedron needs seven classes; in the displayed orientation its
third square-face normal (0,1,0) is absent.

An exposed planar facet of a union of complete native cells must be built from
primitive faces of that same orientation. Thus a convex union can have at most
12 facets. Euler's formula and minimum vertex degree3 give

    E <= 3F - 6 <= 30.

So no convex solid with36 geometric edges can be an exact complete-cell union
under this fixed subdivision. Rigid rotation or invertible affine deformation
of the truncated octahedron cannot reduce its seven distinct normal classes
to six. Counting extra subdivisions along a straight edge does not evade the
stated geometric-edge convention.

The obstruction does not cover nonconvex solids, cuts through native cells,
new subdivision rules or interpreting36 as field coordinates rather than solid
edges. Those would be different candidate contracts, not silent repairs.

## Interpretation

The truncated octahedron fits the numerical edge partition and space-filling
requirements, but it is NOT yet a fitting PNE solid: its current native
whole-cell construction is excluded, and no PNE assignment or field sewing
has been supplied. This comparison does not select an element from its atomic
number. The number24 here counts vertices, not protons.

## Replay

    node research/strominger/checkers/export_native_solid_templates.mjs
    python research/strominger/checkers/check_space_filling_36_shape.py

Receipt: `results/space-filling-36-shape/verification.json`.
The actual JS constructor export is source-hash pinned and checked for staleness.
The conjecture net retains the positive geometric result and negative native
result as separate nodes. Production/viewer and native geometry are unchanged.
