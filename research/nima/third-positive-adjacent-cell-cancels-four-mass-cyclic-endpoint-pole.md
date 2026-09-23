# A third positive adjacent cell cancels the four-mass cyclic endpoint pole locally

The sourced four-pair form has a pole at `u=0`. This is the point where its last source pair reaches the cyclic endpoint ray, so a cyclic top-cell pole is involved; it cannot be classified as a full image boundary from that fact alone.

There is an explicit positive eight-dimensional neighbor: hold physical column **9** at `(-w₈,0)` while physical column **8** remains `(-w₇,w₇u)`. In the sourced cyclic `G(2,9)` top measure, the neighbor uses pole **`(91)=0`** in place of the four-pair cell's **`(89)=0`**. Physical cyclic labels `(9,1,2)` form a parallel block. On the positive parameter region, **23 ordered source minors are positive and 13 vanish**. At `u=0` the neighbor and original matrices, targets and full SU(4) fermionic numerators agree.

Write the original top-chart normal `(89)=w₇w₈ f` and the neighbor normal `(91)=g=−w₈(u−f)`. Because `∂f/∂g=1/w₈`, exact sixfold residues of the same top measure give **opposite intrinsic eight-form densities**. Along the shared positive `u=0` boundary the source-to-target Jacobians have the same seven tangent columns and differ only in the transverse `u` column. Cramer's cofactor identity then cancels the local pushed-form pole for **every scalar and fermionic component** wherever both charts are regular. Three distinct exact positive boundary points, with two target directions each, meet those regularity conditions. The checker selects a nonsingular `Gr(2,6)` target chart at each point rather than presuming a fixed chart remains valid.

This is a third local oriented adjacency relation, alongside the `w₄=0` and `t−u=0` cancellations. Neither the list of these three neighbors nor the involvement of a cyclic source pole proves a complete nine-point triangulation, full canonical form, or global image-boundary classification.

Checker: `research/nima/checkers/check_nine_point_cyclic_endpoint_adjacent_cell_cancellation.py`; result: `research/nima/results/nine-point-cyclic-endpoint-adjacent-cell-cancellation.json`.
