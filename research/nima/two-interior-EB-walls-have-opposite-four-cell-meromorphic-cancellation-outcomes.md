# Two interior E_B walls have opposite four-cell meromorphic outcomes

The E_B one-sheet superform has a genuine simple pole at **both** positive-source support endpoints along a target curve lying inside E's regular positive image. The **other algebraic sheets of the full four-cell square** behave differently at the two walls:

* **Lower `e=44/445`, E_B `w₂=0`:** both E inverse sheets and the unique E_C/E_D sheets have finite nonzero source denominators, target pivots and 8×8 Jacobians. They cannot cancel E_B's **`χ₁⁴χ₅⁴` order-`−1` pole**. Hence the **complete meromorphic four-cell sum** has a genuine interior pole in that component. An additional cell or contour exclusion would be required for a global form regular there.
* **Upper `e=11531/250`, E_B `w₄=0`:** E's **second, nonpositive** algebraic inverse sheet lies on the **same complete source matrix and `w₄=0` face** as E_B, whereas E's positive inverse remains regular. Both boundary Jacobians have rank 8, their seven tangent columns agree, and opposite oriented residues cancel in **two transverse target directions**. The upper E/E_B meromorphic pole therefore cancels **in every fermionic component**; E_C/E_D remain regular. A positive-supported-sheet-only sum would **miss this algebraic cancellation**.

This is an exact contrast between **source-supported positive contour** and **complete meromorphic field trace**. It identifies one four-cell pole that survives and one that cancels, not the global nine-point canonical form or a unique physical contour.

Checker: `research/nima/checkers/check_nine_point_label3_square_internal_wall_uncancelled_poles.py`; result: `research/nima/results/nine-point-label3-square-internal-wall-uncancelled-poles.json`.
