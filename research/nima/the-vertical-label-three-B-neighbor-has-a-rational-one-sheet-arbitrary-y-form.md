# The vertical label-3 B-neighbor has a rational one-sheet arbitrary-Y form

The new positive `F_B` cell, which **locally cancels** E_B's lower interior `w₂=0` superpole, is **birational** on a nonempty regular image open. After deleting its identically zero physical column 2, its five mandatory vanishing two-column minors on retained labels `(1,3,4,5,6,7,8,9)` (zero-based indices) are

```
(1,2), (3,4), (4,5), (3,5), (6,7).
```

For a rank-two kernel shift `C₀+T K`, these five equations are linear in the four entries of `T` and `q=det(T)`. At **two exact strictly positive rank-six moment-curve controls**, the linear matrix has rank four, its unique left-null constraint fixes `q=0` at the known source, and the full target 8×8 Jacobian is nonzero. Thus the inverse on a regular image open is **unique and rational**.

For arbitrary first-pivot `Y=[I₂|B]`, write `z=Z_ret,last4−Z_ret,first2 B`, `h=Z_ret,first2`. Its calibrated oriented **one-sheet** target coefficient is

```
+det(C_F_B h)^4 /
 [w₂w₄w₅w₆w₇w₈u(t−u) · det(d(C_F_B z)/dv)],
```

and the complete fermionic numerator is `(C_F_B χ_ret)^8`. Both exact positive controls give a nonzero coefficient. This makes the **full meromorphic common-target comparison** with E_B's lower pole tractable; local incidence alone has not yet certified global cancellation or the complete nine-point form.

Checker: `research/nima/checkers/check_nine_point_vertical_label3_B_cell_birational_form.py`; result: `research/nima/results/nine-point-vertical-label3-B-cell-birational-form.json`.
