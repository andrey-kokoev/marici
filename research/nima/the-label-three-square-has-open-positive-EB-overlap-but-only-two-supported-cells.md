# The label-3 square has an open positive E/E_B overlap, not four-cell support

At **two distinct exact positive rank-six moment-curve target controls**, reconstruct **every** inverse sheet of the four-cell label-3 square `(E,E_B,E_C,E_D)` and test all eight strict source inequalities exactly (`w₂,w₄,w₅,w₆,w₇,w₈,u,t−u>0`). Both targets have the **same positive-sheet multiplicities**:

```
E: 1 positive + 1 nonpositive algebraic sheet;
E_B: 1 positive sheet;
E_C: 0 positive sheets;
E_D: 0 positive sheets.
```

All contributing E and E_B target Jacobians are nonzero. By the inverse function theorem their positive target images overlap on a **nonempty open neighborhood** of each control. The oriented **positive-source-supported** `χ₃⁴χ₅⁴` contribution is the sum of only the E-positive and E_B-positive branches; it is **nonzero at both targets** and differs exactly from the **complete meromorphic four-cell field trace**, which additionally includes E's nonpositive sheet and nonpositive E_C/E_D inverses. Exact coefficients and all inverse-sheet positivity signs are in the certificate.

This is a concrete **multiplicity and contour distinction**: four positive source-cell parameterizations do not imply that all four are supported at a given positive target; meromorphic continuation counts still other algebraic sheets. The two overlapping positive cells do not cancel their complete component pointwise. These two neighborhoods do **not** determine global four-cell coverage, correct contour weights or the full nine-point form.

Checker: `research/nima/checkers/check_nine_point_label3_square_positive_supported_vs_trace_multiplicity.py`; result: `research/nima/results/nine-point-label3-square-positive-supported-vs-trace-multiplicity.json`.
