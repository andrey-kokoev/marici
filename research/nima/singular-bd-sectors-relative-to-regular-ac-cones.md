# Singular B/D sectors sit differently relative to regular A/C cones

At two exact positive shared target planes, all four cells' normal rays are expressed in the **same** two-dimensional target quotient. The B and D positive face fibres start at the `w₄=0` corner, where B's slope-gap ray equals A's and D's equals C's. For **every point of each complete positive fibre**:

* **B's** normal ray moves strictly **outside A's regular positive normal cone** as soon as the fibre leaves the shared endpoint. The A-basis coefficient of its common `w₄` ray becomes strictly negative.
* **D's** normal ray moves **inside C's regular positive normal cone**. Both C-basis coefficients remain strictly positive along the positive fibre. At the first target D's opposite fibre endpoint meets the A/C common `w₄` ray; the second positive fibre is unbounded and does not reach that ray at a finite endpoint.

These are exact linearized sector-incidence statements for two target planes, not finite sampling along the fibres. They refine the earlier fact that B and D sectors are disjoint: **D can overlap C even though B separates from A**. Overlapping sectors still require oriented density comparison, other image sheets and remaining cells; the local fan does not prove an exhaustive nine-point form.

Checker: `research/nima/checkers/check_nine_point_bd_regular_cone_sector_incidence.py`; result: `research/nima/results/nine-point-bd-regular-cone-sector-incidence.json`.
