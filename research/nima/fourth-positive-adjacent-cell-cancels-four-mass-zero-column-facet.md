# A fourth adjacent positive cell cancels the four-mass `w₅=0` facet locally

At `w₅=0` the sourced four-pair matrix acquires a second zero physical column, **6** (in addition to loop column 3). A fourth positive eight-dimensional cell shares this boundary: for `w₅>0` set physical column **6** to `(0,w₅)` instead of the original `(-w₅,w₅t)`. It becomes vertical and parallel to physical columns `(4,5)`; the cyclic pole **`(56)=0`** replaces the original **`(67)=0`**. All ordered minors are nonnegative on the positive parameter region, with **23 strictly positive and 13 identically zero**.

The checker constructs the neighbor in the full gauge-fixed cyclic `G(2,9)` top chart and computes its **complete 14-coordinate measure Jacobian**. Its sixfold residue at `(12),(23),(34),(45),(56),(89)` is exactly **minus** the oriented four-mass residue at `(12),(23),(34),(45),(67),(89)`. On their common `w₅=0` boundary the complete source matrices and all fermionic numerators coincide. The two `8×8` source-to-target Jacobians agree in their seven boundary-tangent columns, and differ only in the `w₅` normal. Cramer's cofactor identity therefore cancels the pushed pole for any regular transverse target direction and **every SU(4) component**.

Three distinct exact positive boundary points and two transverse directions per point satisfy the nonzero Jacobian and cancellation checks. This is the **fourth** local oriented positive-cell adjacency relation established around the sourced four-mass cell; it does not amount to a complete n=9 triangulation or full image canonical form.

Checker: `research/nima/checkers/check_nine_point_zero_column_neighbor_cancellation.py`; certificate: `research/nima/results/nine-point-zero-column-neighbor-cancellation.json`.
