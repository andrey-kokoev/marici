# The singular-face endpoint log coefficient descends to a regular corner six-form

For a positive B/D `t=u` face fibre that reaches `w₄=0` with all other weights positive, the **lower endpoint logarithm** has a universal source coefficient. Contract the B boundary seven-form along any fibre direction with `r₄>0` and use `w₄=r₄(λ−L)` near the endpoint. The coefficient of `dλ/(λ−L)` is

```
−1/(w₂ w₅ w₆ w₇ w₈ u) evaluated at the shared source corner;
```

D has its opposite. The fibre-direction normalization cancels out. At the corner all four full source matrices and every fermionic numerator coincide.

At **two exact positive corner representatives**, the map from the six corner parameters `(w₂,w₅,w₆,w₇,w₈,u)` to a selected six-dimensional target chart has a **nonzero exact `6×6` Jacobian minor**. Dividing the universal source coefficient by that minor gives a **nonzero local target-corner six-form coefficient** for each individual log; B and D's coefficients are opposite in the same chart. Thus the endpoint ambiguity is anchored to a concrete regular six-dimensional image stratum and cancels under the **same** cutoff.

This is **not** a residue of the singularly pushed eight-forms: source-fibre endpoint logarithms and target-space form residues are different operations. The separate unregulated logarithms still diverge, and no full nine-point image canonical form or triangulation is established.

Checker: `research/nima/checkers/check_nine_point_corner_log_to_target_sixform.py`; certificate: `research/nima/results/nine-point-corner-log-to-target-sixform.json`.
