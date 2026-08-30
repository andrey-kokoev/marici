# A finite Euler certificate for the eta jet

Set `f_j(x)=(log x)^j/x`. After `m` derivatives,

\[
 (-1)^m f_j^{(m)}(x)=m!x^{-m-1}P_{m,j}(\log x),
\]

where, if `prod_(k=1)^m(1+z/k)=sum q_r z^r`,

\[
 P_{m,j}(y)=\sum_{r=0}^j {j\choose r}(-1)^r r!q_r y^{j-r}.
\]

Exact rational evaluation proves `P_(m,j)(9)>0` for `m=60,61` and every
`0<=j<=4`. Since `dP_(m,j)/dy=j P_(m,j-1)`, all these polynomials remain
positive and increasing for `y>=9`. Integral representations of forward
differences therefore make `Delta^60 f_j(n)` positive and decreasing for
`n>=10000`.

Sixty Euler transformations give a remainder bounded by

\[
 \frac{\Delta^{60}f_j(10000)}{2^{60}}
 \le \frac{60!P_{60,j}(10)}{2^{60}10000^{61}},
\]

because `9<log(10000)<10`. Every bound is below `10^-100`; the checker uses
exact rational arithmetic throughout. Hence the earlier `3.31e18` raw cutoff
collapses to a prefix of 9,999 terms and 60 tail differences.

This proves the tail architecture. The remaining implementation obligation is
directed-rounding enclosure of `log n` in the finite prefix and difference
table, plus `log 2`; no long or restart-sensitive computation is required.

## Scope

This theorem certifies the accelerated remainder, not yet the transcendental
finite sum. It proves no infinite Hausdorff hierarchy and no RH statement.

## Durable verification

- Checker: `checkers/eta_euler_tail_bound.py`
- Result: `results/eta-euler-tail-bound.json`
