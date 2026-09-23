# Endpoint logarithms expose the regulator in singular-face current cancellation

The B/D `t=u` boundary seven-forms cancel exactly **before** the collapsed one-dimensional fibre is integrated. That shared regulator is not optional if the contributions are integrated separately. In coordinates following the exact affine positive fibre `p+λr`, contracting B's nonzero seven-form gives

```
F_B(λ) = −r₄ / [w₂ u ∏_{i=4}^{8}(wᵢ+rᵢλ)],       F_D(λ)=−F_B(λ).
```

At two exact positive target planes, the **lower** fibre endpoint is the shared `w₄=0` source corner and has a nonzero simple-pole coefficient; the individual integrals diverge logarithmically. The exact coefficients of `1/(λ−L)` are `−196625/112504` and `−427350125/4398371712`. At the first target the finite **upper** endpoint is `w₅=0` and has coefficient `−1573/20286` in `1/(U−λ)`; at the second, the upper interval is unbounded but `F_B=O(λ⁻⁵)`, so its upper tail converges.

Using **identical** interior cutoffs gives an exactly zero paired integral for every cutoff value. If only D's lower cutoff is changed from `ε` to `cε`, the paired result instead approaches the nonzero finite shift `lower_coefficient·log(c)`. Thus separately assigning unregulated B/D face pushforwards would be unjustified: the paired regulated source-current identity is real, but it does **not** supply a regulator-independent singular target-form residue or a global nine-point canonical form.

Checker: `research/nima/checkers/check_nine_point_slope_face_fibre_endpoint_logs.py`; certificate: `research/nima/results/nine-point-slope-face-fibre-endpoint-logs.json`.
