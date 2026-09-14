# One source-side rank-two Weil inequality has a positive error budget

## Target

Consider the antisymmetric two-translate deficit at

\[
\sigma=0.005,
\qquad
d=0.25.
\]

The direct source-side computation gives approximately

\[
K_\sigma(0)-K_\sigma(d)
=0.2668668972.
\]

## Finite-interval error

On the gamma integration interval, the convergent digamma and trigamma series give the coarse bounds

\[
|\operatorname{Re}\psi(1/4+iu/2)|
\leq139.322
\]

and

\[
\left|
\frac{d}{du}\operatorname{Re}\psi(1/4+iu/2)
\right|
\leq10.
\]

These imply a global Lipschitz bound of approximately \(61.20\) for the normalized gamma integrand. The gamma integral was independently recomputed with a composite midpoint rule using 600,000 panels. Its value was approximately

\[
1.5457889100.
\]

The resulting midpoint-centered total deficit was approximately

\[
0.2668668972.
\]

The global Lipschitz estimate bounds the midpoint quadrature error by

\[
0.089249.
\]

This estimate is intentionally much coarser than the observed Simpson convergence. The enclosure is centered on the midpoint computation itself; it does not transfer a midpoint error bound to the separate Simpson approximation.

## Complete budget

After including:

- the midpoint error bound;
- the gamma-tail bound;
- the prime-tail bound;
- a deliberately enlarged \(10^{-6}\) finite-evaluation allowance;

the resulting lower bound is

\[
K_\sigma(0)-K_\sigma(d)
>0.1776.
\]

Thus this individual rank-two inequality is robustly positive under the stated evaluation assumptions.

## Scope

This is an analytic error budget, not yet a publication-grade interval certificate. The finite elementary and special-function values were evaluated with ordinary floating arithmetic rather than a directed-rounding library. The generous allowance makes a sign error implausible at this point, but it is not a formal enclosure theorem.

The result proves neither all separations nor all widths, and it does not imply RH. It demonstrates that source-side interval certification is feasible away from the severe-cancellation regime.

## Verification

```text
python research/voevodsky/checkers/check_coarse_rank_two_positive_enclosure.py
```

Artifacts:

- `research/voevodsky/checkers/check_coarse_rank_two_positive_enclosure.py`
- `research/voevodsky/results/coarse_rank_two_positive_enclosure.json`
