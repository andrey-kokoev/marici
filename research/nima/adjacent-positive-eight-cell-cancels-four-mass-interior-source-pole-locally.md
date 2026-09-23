# Adjacent positive eight-cell cancels the four-mass interior source pole locally

At the exact target `ε=485/12278`, the sourced four-pair cell `A` has a nonzero pushed-form residue on its positive `w₄=0` boundary, while the same target is interior to the full nine-point positive image. An **explicit adjacent positive eight-dimensional positroid cell** now provides an exact local cancellation mechanism.

Keep the loop column at physical label 3 and all four-pair source coordinates, but in cell `B` replace physical column 5 by

```
C_B[:,5] = (−w₄/t, w₄).
```

It becomes parallel to physical columns 6 and 7: the cyclic pole `(56)=0` replaces cell `A`'s `(45)=0`. With `w₂,w₄,w₅,w₆,w₇,w₈,u,t−u>0`, all ordered source minors are nonnegative; **23** are strictly positive and **13** identically zero (the triple parallel block introduces one additional dependent vanishing minor). Both eight-cells meet at their common positive seven-dimensional boundary `w₄=0`, where **their full matrices, targets, and fermionic numerators are exactly identical**.

The sourced cyclic `G(2,9)` top form supplies an unambiguous relative orientation. Cell `A` uses six pole normals `(12),(23),(34),(45),(67),(89)`. Cell `B` replaces `(45)` by `(56)`, with `g=(56)=w₅(w₄−ht)` in the same top-chart coordinates. Because `∂h/∂g=−1/(w₅t)`, their oriented intrinsic eight-form densities satisfy **`ρ_B=−ρ_A`** in the same source-coordinate order.

At the common boundary sheet the two exact `8×8` source-to-target Jacobians are nonzero. Differentiating the SAME target slice `Y[0,4]↦Y[0,4]+ε`, with its row-gauge change handled explicitly, gives nonzero transverse `dw₄/dε` in both cell charts. The resulting local pushed-form residues satisfy **`Res_B=−Res_A` exactly**, not just numerically. Since the full `δ⁴×δ⁴` fermionic numerator agrees on the common matrix, **every four-flavor component's shared-boundary pole cancels**; the checker separately verifies the `XXXX` component.

This is a **local cancellation between two specified source-contour contributions**, consistent with the target being image-interior. It neither proves these two cells form a complete triangulation nor sums other sheets and source cells, and does not compute the full nine-point image canonical form.

Checker: `research/nima/checkers/check_nine_point_adjacent_cell_positive_pole_cancellation.py`; certificate: `research/nima/results/nine-point-adjacent-cell-positive-pole-cancellation.json`.
