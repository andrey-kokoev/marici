# A coarse unit-disk bound closes the quarter-disk tail budget

Let `F'(t)=sum g_n t^n` be analytic on the unit disk and suppose

\[
 \sup_{|t|\le1}|F'(t)|\le20.
\]

Cauchy's coefficient estimate gives `|g_n|<=20`. Therefore on `|t|<=1/4`,

\[
 \left|\sum_{n\ge5}g_nt^n\right|
 \le20\frac{(1/4)^5}{1-1/4}
 =\frac{20}{768}
 \approx0.026041667.
\]

The certified quarter-disk polynomial permits a tail of `0.0298826193`, so
this leaves margin about `0.003840953`. Consequently the two coarse statements

1. `F'` is analytic on `|t|<=1`;
2. `|F'|<=20` there,

imply `|F'|>=1/16` on `|t|<=1/4`. Combined with the one-circle curvature gate,
they certify pointwise reciprocal-slope concavity on the first central cell.

In the centered coordinate, the unit `t` disk corresponds to `|s-1/2|<=1`.
The next attack is therefore a compact completed-source enclosure on this
fixed disk. The constant 20 is intentionally loose; numerical source values
are far smaller.

Neither unit-disk analyticity nor the bound 20 has yet been certified. This is
a sufficient reduction, not continuum concavity or an RH proof.

## Durable verification

- Checker: `checkers/central_F_prime_outer_disk_cauchy_tail.py`
- Result: `results/central-F-prime-outer-disk-cauchy-tail.json`
