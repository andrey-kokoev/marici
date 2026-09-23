# First-order common-target normal quotient for the singular positive slope face

Cells B and D coincide on `t=u`; their seven-dimensional source face maps with rank six. To compare their off-face behaviour at **common target coordinates**, quotient the eight-dimensional target tangent chart by the **same rank-six face image**. The resulting normal space is two-dimensional. For each cell, project (1) its slope-gap normal target jet `n` and (2) the first-order unfolding `m` of the **same collapsed weight-kernel direction**. Both exact `2×2` normal frames `(n,m)` are invertible at two positive face points.

In those shared target normal coordinates, B's `n` decomposes in D's `(n,m)` frame as

```
point 1: (1, −7098/4169)
point 2: (225947/46892, −969187/46892).
```

The slope-gap scaling coefficient is **positive** in both exact controls, while a **nonzero collapsed-fibre shift** is required to match the normal direction. This comparison is more appropriate than equating Jacobians at matched source parameters, but it remains only a **first-order tangent-space calculation**. The required fibre shifts are finite in the chosen normalization: their positivity and the nonlinear common-target inverse branches have **not** been solved. No singular pushed-form cancellation, image overlap or global nine-point canonical form is claimed.

Checker: `research/nima/checkers/check_nine_point_singular_face_normal_quotient_overlap.py`; certificate: `research/nima/results/nine-point-singular-face-normal-quotient-overlap.json`.
