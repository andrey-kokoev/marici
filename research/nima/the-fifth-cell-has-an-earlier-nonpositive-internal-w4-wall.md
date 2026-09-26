# F_B positivity begins at one wall, but its nonpositive branch has an earlier internal w₄ pole

For the exact positive E target ray `w₂(E)=e>0`, with other E weights `(1,1,1,1,1,3,2)` and fixed positive moment-curve data, the **unique rational F_B inverse** has

```
w₂(F_B) = (445e−44)/259,
w₄(F_B) = 895(21913e−1691)/[37(3488e+58879)].
```

Its six remaining strict positivity factors are positive **for every `e>0`**. Consequently F_B has a strictly positive source preimage **if and only if `e>44/445`**—exactly the lower E_B support wall. E_B is positive only until `e=11531/250`, whereas F_B remains positive beyond that endpoint along this ray.

There is a **separate earlier algebraic wall** at `e=1691/21913 < 44/445`: F_B's `w₄` vanishes there, but its `w₂` is **negative**, so this is **not a positive F_B support transition**. Both the E and F_B 8×8 target Jacobians are nonzero at this target, and E is strictly positive; F_B's other source factors are finite. Since its `χ₁⁴χ₃⁴` minor is `w₂≠0`, the full meromorphic F_B trace has a candidate **genuine component-specific simple pole on an interior E-image target**. Its cancellation by other cells—plausibly a vertical label-3 neighbor without the B shift—must be checked; the earlier two E_B walls being resolved does not close the entire five-cell pole census.

Checker: `research/nima/checkers/check_nine_point_FB_positive_overlap_chamber.py`; result: `research/nima/results/nine-point-FB-positive-overlap-chamber.json`.
