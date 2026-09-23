# The arbitrary-Y nine-point zero-column four-pair trace equals the eight-point trace

The four-pair positive source cell embedded in `G₊(2,9)` has **physical column 3 identically zero**. This gives an exact **arbitrary-Y sourced-form statement**, stronger than a finite-target sample. In the first-pivot target chart `Y=[I₂|B]`, recenter all nine external rank-six rows with the same `SL(6)` matrix as in the independent global four-pair trace. Write `z₉=Z₉,last4−Z₉,first2 B` and `h₉=Z₉,first2`. Deleting physical row 3 gives `z₈,h₈`. For **every B and every external row 3**, the following are identical before any trace is taken:

```
C₉(v) z₉ = C₈(v) z₈,
C₉(v) h₉ = C₈(v) h₈,
∂[C₉(v) z₉]/∂v = ∂[C₈(v) z₈]/∂v.
```

Consequently the exact **two-sheet rational field trace** of the sourced target eight-form,

```
Tr_{C₉(v)z₉=0} [−det(C₉(v)h₉)⁴ /
 (w₂w₄w₅w₆w₇w₈u(t−u) det ∂[C₉(v)z₉]/∂v)],
```

is **identically the eight-point sourced four-pair trace**, independent of ninth data `Z₃`, throughout its nondegenerate simple-fibre open set. The full fermionic numerator is likewise `C₉χ₉=C₈χ₈`, independent of `χ₃`. Six exact target/inserted-row controls (three distinct targets, two row-3 choices each) verify target maps and all eight differential columns.

This is a rational form for **one sourced zero-column contribution**, not the full nine-point NNMHV image canonical form: other positive cells and sheets, pole divisors, source-history support and image coverage remain open. It provides a concrete interface for the higher-priority independent arbitrary-Y form branch.

Checker: `research/nima/checkers/check_nine_point_arbitrary_y_zero_column_form_trace.py`; result: `research/nima/results/nine-point-arbitrary-y-zero-column-form-trace.json`.
