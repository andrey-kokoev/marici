# The four-mass inverse discriminant is not a traced-form pole on an exact target slice

Use positive rank-six external moment-curve data in a positive-determinant `GL(6)` chart. Start from the first regular sourced four-pair target and perturb a rational Grassmannian target coordinate by `ε`: `Y[0,4]↦Y[0,4]+ε`. Invert the source map by writing `C=C̄+TK` with `KZ=0`, solving four parallel-pair minor equations linearly in the four entries of `T` and `q=det(T)`. The remaining quadratic `P(q;ε)=A(ε)q²+B(ε)q+C(ε)` has **exact discriminant**

```
Δ(ε) = (81471625 ε² + 27031090 ε + 346921)/(14300 ε + 589)².
```

The numerator has two distinct **negative** real algebraic zeros (approximately `−0.31841215` and `−0.01337318`); there is no branch collision for `ε≥0` on this particular slice. The linear inverse solver determinant is `−98(14300ε+589)/225`, separating its exceptional chart pole from the two discriminant zeros.

At either discriminant zero, put `q*=−B/(2A)`. Exact polynomial-gcd checks show that **every source-form denominator factor** `w₂,w₄,w₅,w₆,w₇,w₈,u,t−u`, the source row-gauge determinant, the quadratic leading coefficient, and the four-pair linear solver determinant are NONZERO at `q*`. These are therefore *regular simple ramification points* of the algebraic source map on this slice, not boundaries where the intrinsic eight-form is singular.

Locally a simple fold has `ε−ε*∼z²`. A regular source differential `f(z)dz` pushed through the two conjugate inverses contributes `(f(z)−f(−z))/(2z)` up to a regular nonzero factor: the apparent individual-sheet `1/√Δ` terms **cancel in the trace**. Thus the discriminant alone does not generate a pole of the two-sheet pushforward on this exact slice. This is a local analyticity statement, not a universal cancellation of other source or chart poles and not an equality to the full nine-point positive-image canonical form.

Checker: `research/nima/checkers/check_nine_point_four_mass_discriminant_slice.py`; result: `research/nima/results/nine-point-four-mass-discriminant-slice.json`.
