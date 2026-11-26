# Three Excel rows cannot share a boundary, at any filling size

Question: Can rows 6, 10 and 17 all lie on the boundary of a simplicial 3-ball that keeps the observed tetrahedra and label identifications?

Answer: No. This is a disk obstruction at label 15. It does not require shellability, a bound on the number of tetrahedra, or even a fixed number of additional vertices.

Take the link of 15: a tetrahedron containing 15 gives a triangle in the link; a boundary triangle containing 15 gives a boundary edge; a boundary edge containing 15 gives a boundary vertex. In a triangulated PL 3-ball the link of a boundary vertex is a disk.

- Exposing row 6, `{5,15,23}`, and row 10, `{15,23,27}`, requires the consecutive boundary path `5—23—27` in this disk. Vertex 23 has no third boundary neighbor.
- Exposing row 17, `{14,15}`, puts 14 on the other boundary arc from 27 back to 5. Thus 5,23,27,14 occur in that cyclic order, possibly with other vertices on the return arc.
- The observed tetrahedron `{5,14,15,27}` forces link edge `5—27`. The observed tetrahedron `{14,15,20,23}` forces link edge `23—14`.

These two edges join alternating boundary vertices of a disk. They must intersect, but their endpoint sets are disjoint, and a simplicial embedding forbids an intersection in their interiors. Contradiction. Adding more cells cannot change the boundary order or remove a forced edge. The argument does not cover rules that split labels or subdivide an observed face so that it no longer occurs as the specified simplex.

The forbidden triple is minimal: minimum filling B exposes 6 and 10; C exposes 10 and 17; a six-addition filling exposes 6 and 17. The ball need not contain the third observed tetrahedron for the impossibility proof. Thus one can predict a boundary restriction from two observed four-red rows without constructing a filling.

Evidence for pairwise attainability: `checkers/ramsey38_filling_row_visibility.py` and `checkers/ramsey38_joint_boundary_budget.py`. The local obstruction is the alternating-chords lemma for a disk, not a failed enumeration at a chosen budget.
