# B/D positive normal cones are individually regular but disjoint at two targets

The entire positive B and D `t=u` face fibres over two fixed target planes have disjoint projected normal-ray families. This result now includes a **local inversion check for each family**. In the common two-dimensional target normal quotient, let `n_i(λ)` be cell i's slope-gap target jet along its exact positive face fibre. The leading normal map is

```
(v,λ) ↦ η = v n_i(λ),                 v=t−u>0,
det ∂η/∂(v,λ) = v det(n_i(λ),n_i'(λ)).
```

For **both B and D**, at **both exact positive target planes**, the rational factor `det(n_i,n_i')` has **no zero anywhere in the full positive fibre interval**; its sign is fixed. Each cell therefore has a locally invertible **two-dimensional leading normal-cone sector**, not just an isolated nonzero Jacobian witness. Meanwhile the previously certified cross-cell wedge `det(n_B(λ_B),n_D(λ_D))` is strictly nonzero for **all positive** `λ_B,λ_D` over each tested target. The positive B and D normal sectors do not overlap in first-order rays there.

This clarifies why cancellation of the **paired source boundary currents** does not imply cancellation of pushed eight-form densities at common nearby targets: their local normal directions separate even though their collapsed face maps and residues match. The conclusion is **first-order and local to two fixed face targets**. It neither excludes other cells/branches nor establishes a surviving global pole, full target form, or complete nine-point triangulation.

Checker: `research/nima/checkers/check_nine_point_positive_normal_cone_local_inversion.py`; result: `research/nima/results/nine-point-positive-normal-cone-local-inversion.json`.
