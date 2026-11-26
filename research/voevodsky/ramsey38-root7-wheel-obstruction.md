# Root 7 cannot be repaired by changing the boundary triangulation

Assumptions: all short supports lie on the boundary sphere of a simplicial PL 3-ball and the two observed tetrahedra occur as intact cells. Auxiliary boundary and interior vertices are allowed.

The boundary contains the simple cycle 3–11–27–9–21–3 (edges supplied in order by rows 2,1,8,17,20). Vertex 6 is off the cycle. Its four boundary spokes to 3,11,9,21 are rows 15,19,5,18. By the Jordan curve theorem the cycle separates the sphere. All four spokes run on the side containing their hub. Removing a small disk about the hub gives four disjoint arcs in an annulus. Their cyclic endpoint orders agree up to reversal, so 3,11,9,21 occur in this order around 6 in every admissible boundary sphere. Other vertices between them do not change that order.

The link of 6 inside the ball is a disk with that order on its rim. Tetrahedron 23 supplies the link edge 3–9, and tetrahedron 4 supplies 11–21. These edges join alternating endpoints. They must cross, which is impossible for disjoint simplicial edges in a disk. This excludes every boundary repair preserving the stated data, not only the two known seven-label spheres. The distinction from the earlier rim scan is that the cyclic order is forced by a boundary cycle **away from** the link center. The boundary by itself exists; the prescribed pair of interior cells is incompatible with every such boundary.

Replay the row-to-edge certificate with `python research/voevodsky/checkers/ramsey38_root7_boundary_repair.py`.
