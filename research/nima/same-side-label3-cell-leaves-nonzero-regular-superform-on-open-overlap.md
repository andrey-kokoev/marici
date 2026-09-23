# Same-side A/E pole cancellation leaves a regular label-3 superform on an open overlap

A and the label-3-sensitive positive cell E have identical `w₂=0` source matrices and opposite oriented local simple-pole residues. At **three exact positive boundary points**, both full `8×8` target Jacobians are invertible and their target-normal directions have the **same sign**. The inverse function theorem therefore gives a **nonempty open overlap of their strictly positive target images** near each point, not merely a shared boundary ray.

On that overlap, their leading `1/w₂` pole cancels. But their **complete local supersymmetric pushed forms do not cancel identically**. A has physical column 3 zero and hence no `χ₃` dependence. E has `det(C₃,C₅)=w₂w₄`, so its `χ₃⁴χ₅⁴` sourced coefficient is exactly

```
w₂³ w₄³ / [w₅ w₆ w₇ w₈ u(t−u)].
```

It is **regular and vanishes cubically** at `w₂=0`, explaining why it does not disturb the simple-pole cancellation, but is **nonzero at every strictly positive source interior point** on E's regular branch. Two additional exact positive interior controls confirm nonzero locally pushed coefficients after division by E's `8×8` Jacobian. Thus E supplies a genuine **regular label-3-sensitive remainder** in the A/E local overlap.

This compares **local inverse branches**, not the complete global two-sheet trace of E; additional E sheets or other positive cells may cancel that component. It does not give a full nine-point amplitude or image canonical form.

Checker: `research/nima/checkers/check_nine_point_same_side_overlap_label3_regular_remainder.py`; result: `research/nima/results/nine-point-same-side-overlap-label3-regular-remainder.json`.
