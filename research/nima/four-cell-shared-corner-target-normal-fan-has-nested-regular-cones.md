# The shared corner has nested A/C regular target-normal cones

At two exact positive shared `w₄=0,t=u` corner representatives, quotient the eight-dimensional target chart by the common six-dimensional corner tangent image. In this common two-dimensional normal plane:

* **A and C** have full-rank normal frames. Their positive `w₄` direction gives **the same ray**; their positive slope-gap directions give two **different rays**.
* At both corners, the **C slope-gap ray is strictly inside A's positive normal cone**: its exact coordinates in the basis `(A_w₄,A_slope)` are both positive. Thus the regular first-order A/C cones overlap; they are **not** on opposite sides of the common ray.
* **B's** slope-gap boundary ray equals **A's**, while **D's** equals **C's**. For B and D the `w₄` derivative projects to **zero** in the normal quotient, consistent with their rank-seven blow-down face and its collapsed weight direction.

These exact incidences organize the four positive source cells' target-normal geometry at two regular corner points. They do **not** imply a non-overlapping positive-image triangulation, identify all cells in the target sector or evaluate a pushed canonical form. In particular, a source incidence square need not become a four-sector partition in the image.

Checker: `research/nima/checkers/check_nine_point_positive_square_corner_normal_fan.py`; result: `research/nima/results/nine-point-positive-square-corner-normal-fan.json`.
