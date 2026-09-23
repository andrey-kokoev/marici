# Structural target-rank collapse on the whole slope face of two positive cells

The rank-seven obstruction at the four-cell corner is **not confined to that corner**. On the entire `t=u>0` face, positive cells **B and D coincide**. For **arbitrary rank-six external data** `Z` with independent image rows, let

```
T = (w₄/u) Z₅ + w₅ Z₆ + w₆ Z₇ + w₇ Z₈ + w₈ Z₉.
```

Their target two-plane is spanned by

```
S = Z₁ + w₂ Z₂ − T,
Q = Z₄ + u(Z₁ + w₂ Z₂) = Y_row1 + u Y_row0.
```

Varying the **five** positive weights `(w₄,w₅,w₆,w₇,w₈)` changes `S` but **does not change `Q`**. Its effect on the two-plane factors through the **four-dimensional quotient** `k⁶/span(S,Q)`. Thus one nonzero source-weight tangent direction is always killed: the full eight-dimensional source-to-target differential has **rank at most seven throughout this face** (where `S,Q` are independent), for arbitrary external `Z`. This is an exact structural rank bound, not a finite-sample extrapolation.

Two additional exact controls with **strictly positive `w₄`** (away from the previous codimension-two corner) show rank exactly seven and five-weight tangent rank exactly four for both B and D, with a **nonzero** left-null × first-Jacobian-variation × right-null pairing when `t−u` is opened. The determinant therefore vanishes **simply in the slope-gap direction on a nonempty algebraic open** for this positive rank-six external configuration, and hence on a nonempty open in joint external/source parameters. It is a tangent-collapse divisor, not an isolated corner rank defect.

This determines why the ordinary inverse-Jacobian cancellation proof breaks down for B/D on their slope face. **It does not evaluate their singular target pushforward**, establish multiplicities or provide the complete nine-point image form.

Checker: `research/nima/checkers/check_nine_point_slope_face_structural_blowdown.py`; result: `research/nima/results/nine-point-slope-face-structural-blowdown.json`.
