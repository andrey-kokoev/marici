# A specified complex sixfold n=9 fibre contour recovers the full two-sheet four-mass invariant locally

An explicit **complex** fibre-contour prescription—not a canonical positive-image contour—is now available near the sourced four-mass target. At fixed regular rank-six nine-point target `Y₀`, take a small oriented six-torus about each isolated intersection of the six-dimensional full source fibre with the six cyclic divisors

```
(12)=(23)=(34)=(45)=(67)=(89)=0.
```

Use transverse normal order `(a,b,c,h,e,f)` and **sum both local six-tori**. The prior symbolic sixfold residue of the cyclic `G(2,9)` source form equals the complete intrinsically oriented four-mass eight-form, and the exact transverse `14×14` chart Jacobian is `diag(J₈,M₆)` with both blocks invertible. After fixing the eight-dimensional target, the residue on sheet `i` is consequently `source_density(s_i)/J₈(s_i)` times the **full** fermionic numerator `δ⁴(C_i χ)δ⁴(C'_i χ)`. The symbolic zero-column identity makes this numerator independent of inserted physical `χ₃` for every SU(4) flavor.

At **two independent strictly positive rank-six external targets**, the checker finds precisely two isolated local fibre intersections each, recomputes both target-chart Jacobians, and verifies that their residue sum matches the independently tested sourced `Y₀` two-sheet coefficient EXACTLY. Five flavor-selected quartic moments have a rank-two Hankel matrix with distinct sheet ratios, consistent with the complete source invariant. On each target one boundary sheet is positive and one is only a rationally continued nonpositive sheet: the **full two-sheet trace differs from the single positive local residue**. Thus a contour retaining only the real positive source intersection cannot be silently substituted for this specified algebraic two-torus sum.

This construction identifies a concrete local n=9 **cyclic top-measure fibre residue** producing the embedded n=8 four-mass invariant. It does NOT prove that this complex contour is the full n=9 positive-image canonical integration cycle, that all other poles cancel, or that the full nine-point amplitude contains this invariant as a term. Arbitrary-`Y` continuation and global residue/orientation analysis remain open.

Checker: `research/nima/checkers/check_nine_point_sixfold_fibre_contour_two_sheet_trace.py`; result: `research/nima/results/nine-point-sixfold-fibre-contour-two-sheet-trace.json`.
