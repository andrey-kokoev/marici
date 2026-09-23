# Total positivity makes the entire B/D slope-face fibre a single line

For **arbitrary strictly totally positive rank-six external data**, not just the moment-curve example, every positive `t=u` face target of cells B and D has a **one-dimensional affine weight fibre**, with no further B/D face-preimage branch at different `u` or `w₂`.

Set `P=span(Z₁,Z₂,Z₄)`, `W=span(Z₅,Z₆,Z₇,Z₈,Z₉)`, and

```
T=(w₄/u)Z₅+w₅Z₆+w₆Z₇+w₇Z₈+w₈Z₉,
S=Z₁+w₂Z₂−T,          Q=Z₄+u(Z₁+w₂Z₂).
```

The target plane is `Y=span(S,Q)`. Positive `T` lies **outside P**: a four-coordinate determinant `det(Z₁,Z₂,Z₄,T)` is a positive sum of strictly positive ordered four-minors. Hence `Y∩P=span(Q)`. For any other B/D face preimage of the same plane, `Q'` lies in this intersection. Its `Z₄` coefficient is fixed to one, so `Q'=Q`, forcing **`u'=u`, `w₂'=w₂`**. Moreover `Q` lies outside W because `det(Q,Z₅,…,Z₉)` is a positive sum of ordered six-minors. The five weight directions therefore project with rank four to `k⁶/Y`; their full preimage is **one affine line**, whose positive locus is an interval (possibly unbounded).

For the two previously checked strictly positive moment-curve target planes, the **entire positive B/D face fibres**, in the same λ normalization, are

```
point 1:  −14/55 < λ < 7/11;
point 2:  −1213/645 < λ < +∞.
```

The unique D normal-jet matches to B are `−7098/4169` and `−57011/13291`, respectively, **outside these complete positive intervals**. Thus no *positive B/D slope-face preimage of either tested target plane* matches its selected B normal jet to first order. This strengthens the former *one-fibre-branch* limit; it still does **not** exclude other positive cells, prove target pole survival, solve nonlinear off-face image matching or establish the full nine-point form.

Checker: `research/nima/checkers/check_nine_point_slope_face_full_positive_fibre.py`; result: `research/nima/results/nine-point-slope-face-full-positive-fibre.json`.
