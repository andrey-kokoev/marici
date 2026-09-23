# C/D full-form pole cofactor stays regular in a scaled singular-corner limit

C and D have opposite **full nonlinear pushed** `w₄=0` simple-pole residues wherever `t>u` and both target maps are regular. D's full target Jacobian drops from rank eight to seven as `t→u`, so its inverse alone cannot be evaluated at the corner. The cancellation nevertheless has a **regular bordered-cofactor limit**.

On the whole shared `w₄=0` source boundary, seven target-Jacobian tangent columns of C and D are identical. Choose the transverse target direction `V=J_C[:,w₄]`. Replacing D's `w₄` normal column by `V` gives **exactly `J_C`**, hence, for positive slope gap `v=t−u`,

```
det(J_D)·(dw₄,D/dV) = det(J_C).
```

At two exact positive corner representatives, `rank(J_C)=8`, `rank(J_D)=7`, but the **bordered determinant `det(J_C)` is nonzero**. Each individual regular-face pushed pole coefficient diverges as `1/v`; multiplying it by `v` gives a **finite, nonzero corner limit**, with equal magnitude and opposite sign for C and D. Two exact positive gaps per representative pass the full nonlinear cofactor identity.

This is a limit along **moving boundary target points and a chosen moving transverse direction**. It does **not** claim an unregulated residue of the singular pushed eight-form at one fixed corner target, nor a full nine-point image form. It bridges the full regular-face cancellation and the earlier leading corner-ray calculation without illegitimately inverting the rank-seven D Jacobian.

Checker: `research/nima/checkers/check_nine_point_cd_cofactor_corner_scaled_limit.py`; certificate: `research/nima/results/nine-point-cd-cofactor-corner-scaled-limit.json`.
