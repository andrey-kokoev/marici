# Eight positive label-3 cells form an oriented source-incidence cube

The previously found horizontal-column-3 square `(E,E_B,E_C,E_D)` extends to a **full eight-cell positive source cube** by verticalizing physical column 3, yielding `(F,F_B,F_C,F_D)`. The three independent source choices are **horizontal versus vertical physical column 3**, the `w₄` cyclic-pole shift, and the `t−u` slope-pole shift. Every ordered 2×2 source minor of both new F_C and F_D is nonnegative. All twelve expected square/vertical face-source identities hold; the calibrated orientation signs relative to E are

```
E, E_B, E_C, E_D : +, −, −, +
F, F_B, F_C, F_D : −, +, +, −.
```

The four horizontal/vertical pairs share their complete `w₂=0` boundary source matrices with opposite orientations. At one exact positive moment-curve control **all eight full 8×8 target Jacobians are nonzero**, with seven common target tangent columns per vertical pair. This establishes **regular local target adjacency candidates**, not full pushed-pole cancellation at every edge or an eight-cell triangulation.

The `χ₃⁴χ₅⁴` source minor is **`w₂w₄` for all four E cells**, **zero for F and F_C** (parallel columns), and **`w₂w₄/t` for F_B and F_D** (their shifted column 5). Thus the cube contains six cells capable of carrying that component. Its equal-source-parameter orientation sum vanishes, but distinct target maps and inverse sheets prevent a conclusion about the complete arbitrary-Y image form.

Checker: `research/nima/checkers/check_nine_point_label3_oriented_eight_cell_cube.py`; result: `research/nima/results/nine-point-label3-oriented-eight-cell-cube.json`.
