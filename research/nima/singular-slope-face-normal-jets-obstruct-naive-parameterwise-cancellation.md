# Different normal target jets obstruct naive parameterwise cancellation on the singular slope face

The two positive cells **B** and **D** in the source incidence square have opposite intrinsic residue signs and coincide at `t=u`. Nevertheless their maps differ already at **first order transverse to that face**. For arbitrary external rank-six data, put

```
T = (w₄/t)Z₅ + w₅Z₆ + w₆Z₇ + w₇Z₈ + w₈Z₉.
```

One generator of each target two-plane is `S=Z₁+w₂Z₂−T`. Taking `Q=Y_row1+t Y_row0`, the other generators are

```
Q_B = Z₄+t(Z₁+w₂Z₂)−(t−u)(w₇Z₈+w₈Z₉),
Q_D = Z₄+t(Z₁+w₂Z₂)−(t−u)(w₆Z₇+w₇Z₈+w₈Z₉).
```

Hence `D−B` has physical-column-7 lower entry `−w₆(t−u)`; the **boundary images agree, but transverse target jets need not**. This explains why equal-and-opposite source residues cannot be divided by the *same* target Jacobian on this collapsed face.

For two exact strictly positive interior points of the slope face, both `8×8` Jacobians have rank seven and simple transverse determinant zeros. Their determinant-linear-coefficient ratios (`B/D`, in a common target chart and a fixed `t=u+ε` source path) are **`−16072/4169`** and **`−94367/23446`**, respectively—not 1. Thus **the naive same-source-parameter leading push coefficients do not cancel** at either control.

**Crucial limitation:** these ratios compare different target points as soon as `ε≠0`; they are **not** coefficients of image forms evaluated at the same target. They do not prove a surviving target pole or disprove cancellation after correct inverse branches, contour multiplicities and other cells are included. A singular target pushforward remains necessary for the global form.

Checker: `research/nima/checkers/check_nine_point_singular_slope_face_normal_jets.py`; result: `research/nima/results/nine-point-singular-slope-face-normal-jets.json`.
