# Nonreal E sheets produce a real label-3 trace on a V-only positive sector

At the exact strictly positive regular V target with `w₂=1/20`, **neither A nor E has any positive source preimage**. A nevertheless has a nonzero two-real-nonpositive-sheet meromorphic continuation. E's **entire** quadratic fibre has **negative discriminant**—there is **no real E source sheet at all**.

Tracing E's full oriented `χ₃⁴χ₅⁴` coefficient over its **two complex-conjugate inverse sheets**, including the `8×8` target Jacobian and first-pivot `det(C h)^4`, produces the **nonzero exact real rational**

```
574262600221040549082343531638386685475363999744770369704222989857701083407642584204794237
/164066435423468368612538130115983921349415597737770956275518917774599411910183469243618337751040.
```

This establishes a sharper distinction between **positive-source support** and **algebraic meromorphic trace**: a positive real target can have no *real* E inverse whatsoever while E's complete rational supertrace is nonzero there. Both A and V are identically `χ₃`-blind, so the `χ₃⁴χ₅⁴` coordinate of a naive three-cell *meromorphic* combination `A+E+V` at this target equals this nonzero E value, even though the *positive-supported* A and E pushes vanish. That is **not** a verdict on the full nine-point amplitude; further positive cells, sheets and contour coefficients could cancel the component.

Checker: `research/nima/checkers/check_nine_point_complex_E_trace_over_positive_V_target.py`; result: `research/nima/results/nine-point-complex-E-trace-over-positive-V-target.json`.
