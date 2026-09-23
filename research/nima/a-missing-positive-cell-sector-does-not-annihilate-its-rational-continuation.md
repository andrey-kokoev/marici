# Missing positive-source support does not annihilate a rational two-sheet continuation

The exact positive V target at `w₂=1/20` has **no positive A inverse source**; its two complete A algebraic sheets violate strict positivity. Nevertheless, tracing A's **oriented meromorphic coefficient over both nonpositive algebraic sheets** gives a **nonzero exact rational number**:

```
A rational two-sheet continuation:
115119579069212764953302490780133575960562854344321909
/347693057538216533589287914395684764225399842406400000000  > 0.
```

The V one-sheet oriented scalar form at the **same target and same first-pivot chart** is also nonzero but **negative** (see the exact coefficient in `research/nima/results/nine-point-supported-vs-meromorphic-trace-vertical-target.json`). Thus the two locally sourced rational forms are distinct at this target.

This enforces a crucial distinction in the active form branch:

* The **positive-source-supported push** from A has zero weight at the V target, so A does **not** give a positive-cell cover of the full nine-point image.
* A's **algebraic two-sheet rational continuation** need not vanish there; it is explicitly nonzero. Therefore **missing positive-cell coverage alone cannot prove that A's rational function differs from an as-yet unconstructed full canonical form**. Conversely, the distinct A/V coefficients cannot identify that form without all other cells and contour weights.

This corrects the overly strong inference from the previous coverage-only steps, without weakening their certified open positive-image omissions.

Checker: `research/nima/checkers/check_nine_point_supported_vs_meromorphic_trace_vertical_target.py`; result: `research/nima/results/nine-point-supported-vs-meromorphic-trace-vertical-target.json`.
