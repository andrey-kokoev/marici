# Two positive face targets have disjoint B/D first-order normal-ray families

The complete positive fibres of B and D over each of two fixed `t=u` target planes are known exactly. Their transverse slope-gap target jets can now be compared **for every pair of positive preimages**, not only at selected source points. In the same two-dimensional target-normal quotient, write their affine fibre parameters as `λ_B,λ_D` and their projected normal jets as `n_B(λ_B),n_D(λ_D)`.

At the first strictly positive moment-curve target, both λ lie in `(-14/55,7/11)`. The normal-jet wedge has numerator

```
−16072 λ_B − 4169 λ_D − 7098.
```

Writing `λ_B=−14/55+x`, `λ_D=−14/55+y` with `x,y>0`, its negative is **`16072x+4169y+107016/55>0`** everywhere in the full positive rectangle.

At the second target, both λ lie in `(-1213/645,+∞)`. Its wedge numerator is `−7(92929545 λ_B λ_D+446128057 λ_B+274073711 λ_D+1175623831)`. After the same lower-bound shift, **every coefficient of the negative numerator is strictly positive**, including the constant and the `xy` term (exact polynomial in the checker). The chart denominators are nonzero along these fixed target-plane fibres.

Therefore **no positive B-face normal ray is parallel to a positive D-face normal ray** above either tested target plane. This is an exact *uniform-on-the-two-positive-fibres* first-order obstruction. It does **not** prove a global separation theorem for all targets, rule out other positive cells or compute a singular image form; first-order target cones alone do not decide full image-boundary coverage.

Checker: `research/nima/checkers/check_nine_point_positive_slope_face_normal_cones.py`; result: `research/nima/results/nine-point-positive-slope-face-normal-cones.json`.
