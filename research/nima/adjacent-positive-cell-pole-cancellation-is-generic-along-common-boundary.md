# Adjacent positive-cell pole cancellation holds generically along the common boundary

The exact pole cancellation between the sourced four-mass eight-cell `A` and its adjacent eight-cell `B` is **not special to the previously chosen target** `ε=485/12278`. It follows from a cofactor identity on their entire common positive `w₄=0` boundary, wherever the target charts are regular.

The cells coincide as complete matrices when `w₄=0`: `C_A=C_B`. Their full fermionic numerators consequently coincide there. The independently calculated sixfold residues of the SAME sourced cyclic top form give **opposite oriented eight-form densities** in the same eight source-coordinate order. Let `J_A` and `J_B` denote their `8×8` source-to-`Gr(2,6)` target-chart Jacobians. At `w₄=0`, the seven columns tangent to the common boundary are **identical**; only the transverse column associated with `w₄` differs. For any target direction `V` transverse to the common image divisor, Cramer's rule gives

```
det(J_A)·(dw₄/dV)_A = det(J_A with transverse column replaced by V)
                       = det(J_B with transverse column replaced by V)
                       = det(J_B)·(dw₄/dV)_B.
```

Since the source boundary densities have opposite signs, the local target pole residues obey **`Res_A(V)+Res_B(V)=0`** for *every* Grassmann/flavor component wherever both Jacobians and speeds are nonzero. This is an algebraic generic-open statement, not an extrapolation from one numerical target. The checker independently verifies the source-cofactor and oriented-residue equality at **three distinct exact positive boundary points**, using two different transverse target directions at each.

This supplies a robust local internal-boundary cancellation mechanism consistent with the interior status of the earlier target. It does **not** establish cancellation of other divisors, an exhaustive nine-point contour triangulation, or the complete positive-image canonical form.

Checker: `research/nima/checkers/check_nine_point_adjacent_cell_generic_boundary_cancellation.py`; certificate: `research/nima/results/nine-point-adjacent-cell-generic-boundary-cancellation.json`.
