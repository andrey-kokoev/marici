# A fifth adjacent positive eight-cell cancels the `w₇=0` pole locally

At `w₇=0`, physical column **8** vanishes in the sourced four-pair cell. A fifth positive neighboring eight-cell moves that column from the `u` slope to the `t` slope:

```
C_neighbor[:,8] = (−w₇,w₇t).
```

For `w₇>0`, physical columns **(6,7,8)** form a triple-parallel block; cyclic pole `(78)=0` replaces the source cell's `(89)=0`. All ordered two-minors are nonnegative on positive parameters (**23 strictly positive, 13 zero**). On their common positive `w₇=0` boundary, the complete matrices, target maps and full fermionic numerators coincide.

An independent **14-coordinate cyclic-top-form Jacobian** calculation gives the neighbor's oriented sixfold residue exactly **minus** the sourced four-mass eight-form. Their source-to-target Jacobians share seven tangent columns on the common boundary and differ only in the normal `w₇` column. Cramer's cofactor identity makes their pushed simple-pole residues cancel for every fermionic component at any regular transverse target. Three exact positive boundary points, with two transverse directions each, pass the nonzero-Jacobian and cancellation tests.

This screens **seven of eight** basic four-mass source dlog poles by explicit adjacent positive cells. The remaining unscreened factor is **`w₂`**. None of these local facet relations proves a complete global nine-point triangulation or equality to the full positive-image canonical form.

Checker: `research/nima/checkers/check_nine_point_w7_zero_column_neighbor_cancellation.py`; result: `research/nima/results/nine-point-w7-zero-column-neighbor-cancellation.json`.
