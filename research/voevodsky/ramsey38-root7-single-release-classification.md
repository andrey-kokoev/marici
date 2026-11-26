# Root 7: which single row can move off the shell?

Keep every observed support intact. Release only its requirement to lie on the boundary. Rows 18 and 20 have constructive certificates on the original labels. Twelve other releases leave a forced crossing (single-release checker). The last three exclusions do not require a bound on auxiliary vertices.

For each release take the graph of mandatory boundary edges with the unreleased triangular supports marked as faces. Enumerate cyclic neighbor orders; follow consecutive directed edges to obtain facial walks. For this connected graph, Euler characteristic two selects the rotations on a sphere. Retain rotations realizing the marked faces. Even if auxiliary vertices are present in a mesh, forgetting everything except the required graph induces one of these rotations. Counts include opposite orientations.

Edge {6,21} is still on the boundary. Its link must be a path containing both segments 3–9 and 11–13, from rows 23 and 4. Thus on projecting its order to those four labels there are only eight possibilities: order the two blocks and orient each. In the link disk of endpoint 6 the segments from rim vertex 21 to the other link vertices are ordered as in that path. Restrict to the tips whose spokes from 6 are mandatory boundary edges. They must occur in their rim order starting at 21 (disjoint arcs in a disk). At endpoint 21 take the reverse rotation starting at 6: orientations on the two ends of the same boundary edge are opposite. Auxiliary vertices do not affect the relative orders. In fact the rejections for rows 5 and 17 already fail at a single end: respectively 13 and 11 separate the consecutive pair 3,9.

| Released row | Oriented sphere rotations | Pass fan order | Survive disk separation |
|---|---:|---:|---:|
|5|4|0|0|
|8|4|2|0|
|17|2|0|0|

When releasing row 8, the surviving rotations at 6 have the order 21,11,3,9 or its reversal on the four indicated spokes. The boundary cycle 3–6–21 separates 9 from 11 on the sphere: at vertex 6 their spokes leave on opposite sides. Boundary edge 11–27 puts 27 on the side of 11. The cycle bounds the **actual triangular face** {3,6,21} of tetrahedron 23. Its interior is not on the boundary (both shell sides contain vertices), so it is a properly embedded disk. Such a disk separates a PL ball into sides corresponding to its boundary arcs on the sphere (equivalently, cap it with either boundary disk and apply sphere separation). Row 8, even after release, still demands the intact edge 9–27. It joins opposite sides without any common vertex with the disk. This is impossible.

Consequently 18 and 20 are the only possible one-row releases even allowing extra mesh vertices and non-shellable PL fillings. The assertion concerns the marked root-7 array, not every Ramsey witness. Enumeration: `checkers/ramsey38_root7_fan_order.py`; positive controls and other exclusions: `checkers/ramsey38_root7_single_release.py`.
