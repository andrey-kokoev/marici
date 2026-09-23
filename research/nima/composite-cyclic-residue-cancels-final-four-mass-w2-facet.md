# Composite cyclic residue cancels the final four-mass source facet `w₂=0`

The last unscreened dlog factor of the sourced four-pair cell was `w₂`: physical column 2 vanishes there. A positive adjacent eight-cell exists, but it is **not obtained by naively exchanging one of six explicit cyclic top-cell poles**. Keep the loop at physical column 3, and move physical column 2 from `(w₂,0)` to `(0,w₂)`, making `(2,4,5)` a vertical parallel block. Its ordered minors are nonnegative on positive parameters (**23 strictly positive, 13 zero**), and its full matrix equals the original at `w₂=0`.

The relative orientation is fixed by an **induced composite residue**. In a common nine-dimensional loop-column source cell, let physical column 2 be `(x,y)`. Taking five cyclic top-measure poles `(23),(34),(45),(67),(89)` in the stated order gives the exact intrinsic density

```
+ dx∧dy∧d(rest) / [x y w₄ w₅ w₆ w₇ w₈ u(t−u)].
```

Here `(23)=xc−yb` and `(34)=b` in the top chart; after taking `b=0` at generic `x≠0`, the `(23)` residue yields the **induced pole `1/x`**. The original four-pair cell is the `y=0` residue, while the new positive cell is the **composite `x=0` residue**. In the same ordered source coordinates, `Res_{y=0}(dx∧dy)=-dx` but `Res_{x=0}(dx∧dy)=+dy`. Their complete intrinsic eight-form densities are therefore **exactly opposite**, not merely related by a guessed sign.

Along the shared positive `w₂=0` boundary, full matrices and all fermionic numerators coincide. Their `8×8` target Jacobians share seven tangent columns and differ only in the transverse column. A Cramer-cofactor identity cancels the pushed local pole for **every SU(4) component**, wherever the target charts are regular. Three exact positive boundary points and two target directions per point pass the nonzero-Jacobian check.

All **eight basic source dlog factors** `w₂,w₄,w₅,w₆,w₇,w₈,u,t−u` now have explicitly screened **local positive-cell adjacency cancellations**. That does **not** prove an exhaustive nine-point triangulation, cancellation at intersections of facets, or equality with the full image canonical form.

Checker: `research/nima/checkers/check_nine_point_w2_composite_residue_neighbor.py`; result: `research/nima/results/nine-point-w2-composite-residue-neighbor.json`.
