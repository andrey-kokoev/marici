# Regular C and singular D cancel their shared leading target-ray pole

The positive **D** blow-down normal sector lies inside regular **C**'s target-normal cone at two exact shared corners. In common A normal coordinates `(X,Y)`, their shared `w₄=0` boundary ray has equation `H=X−cY=0`, `c>0`. With `k=1/(w₂w₅w₆w₇w₈u)` evaluated at their common corner, regular C's leading pushed normal density has residue

```
C:  +k/Y     at H=0.
```

D's normal map is `η=v(R_C+ℓb)`, where `ℓ=0` is its `w₄=0` fibre endpoint. Its normal Jacobian vanishes on the slope-gap face, so an ordinary inverse-Jacobian boundary check at that face would be invalid. Instead, **invert the leading D normal map at `v>0`** and then take its common-target ray residue. At both exact positive controls the result is

```
D:  −k/Y     at H=0.
```

Thus the **leading common-target `w₄=0` pole cancels between C and D**, including every fermionic component: their full matrices and numerators agree on this shared positive boundary. This is a concrete oriented target-form cancellation involving one singular blow-down cell, beyond the prior regulated source-current statement.

The result is restricted to the **leading linearized normal form near two regular corner targets**. It does not establish cancellation of the entire nonlinear pushed eight-forms, other target facets, image coverage or the complete nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_singular_d_regular_c_shared_target_pole.py`; result: `research/nima/results/nine-point-singular-d-regular-c-shared-target-pole.json`.
