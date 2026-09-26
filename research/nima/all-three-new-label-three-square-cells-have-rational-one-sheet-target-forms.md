# All three new label-3 square cells have rational one-sheet target forms

The three additional positive label-3-sensitive cells **`E_B,E_C,E_D`** each admit an **arbitrary-Y rational one-sheet pushed form on a nonempty regular image open**. Their five mandatory zero-minor sets (zero-based indexing on the eight retained physical columns `(1,3,4,5,6,7,8,9)`) are respectively

```
E_B: (01),(34),(45),(35),(67)
E_C: (01),(23),(56),(67),(57)
E_D: (01),(34),(56),(67),(57).
```

For each cell, the five equations on a rank-two Grassmannian kernel shift `C₀+T K` become linear in the four entries of `T` and `q=det(T)`. At **two exact positive moment-curve targets per cell** the 5×4 linear matrix has rank four and its single left-null equation forces `q=0` for the known source. Therefore on a nonempty regular open the inverse is **unique and rational**: for any target in that cell's image, solve the left-null relation for `q`, then the rank-four equations for `T`, and impose `q=det(T)`. All six positive source-to-target 8×8 Jacobians are nonzero.

For arbitrary first-pivot `Y=[I₂|B]`, each cell has an exact oriented one-sheet coefficient of the familiar form

```
σ · det(C h)^4 /
 [w₂w₄w₅w₆w₇w₈u(t−u) · det(d(C z)/dv)],
```

with `z=Z_ret,last4−Z_ret,first2 B`, `h=Z_ret,first2` and calibrated source signs **`σ(E_B)=−`, `σ(E_C)=−`, `σ(E_D)=+` relative to E**. Their complete fermionic numerators remain distinct target-dependent `(Cχ_ret)^8`. This makes a full four-cell arbitrary-Y label-3 trace comparison tractable but **does not itself show its cancellation, choose contour weights, or determine the nine-point form**.

Checker: `research/nima/checkers/check_nine_point_label3_square_three_new_cells_birational_fibres.py`; result: `research/nima/results/nine-point-label3-square-three-new-cells-birational-fibres.json`.
