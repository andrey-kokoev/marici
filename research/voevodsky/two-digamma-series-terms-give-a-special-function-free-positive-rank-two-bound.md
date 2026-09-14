# Two digamma-series terms give a special-function-free positive rank-two bound

## Pointwise lower bound

Write the real digamma function as its value at \(1/4\) plus the positive correction series

\[
\operatorname{Re}\psi(1/4+iu/2)
=
\psi(1/4)
+
\sum_{k\geq0}
\frac{(u/2)^2}
{(k+1/4)((k+1/4)^2+(u/2)^2)}.
\]

The summand is decreasing in \(k\). Retain the terms \(k=0,1\) exactly and bound the remaining sum from below by its integral. This gives an elementary lower function involving only rational operations and \(\log(1+x)\).

No finite digamma evaluation or asymptotic expansion is then needed.

## Enclosure at one point

At

\[
\sigma=0.005,
\qquad
d=0.25,
\]

the 1,200,000-panel midpoint evaluation of the elementary gamma lower function is approximately

\[
1.3452750157.
\]

After adjoining the endpoint, gamma-constant, and finite prime terms, the center of the lower estimate is

\[
0.0663530029.
\]

A coarse global derivative estimate bounds midpoint quadrature error by

\[
0.0469453746.
\]

After gamma-tail and finite-evaluation allowances, the final lower bound is

\[
K_\sigma(0)-K_\sigma(d)
>0.0194066.
\]

## Improvement

This result no longer depends on numerical evaluation of \(\psi\). The only remaining machine-level assumption is ordinary floating evaluation of elementary functions and the finite arithmetic sum. Replacing those operations with directed rounding would turn this computation into an interval certificate without changing its analytic structure.

## Scope

This proves one robust rank-two sample under the stated rounding assumption. It does not establish a neighborhood, all separations, all widths, higher Gram ranks, or RH.

## Verification

```text
python research/voevodsky/checkers/check_elementary_digamma_lower_bound_deficit.py
```

Artifacts:

- `research/voevodsky/checkers/check_elementary_digamma_lower_bound_deficit.py`
- `research/voevodsky/results/elementary_digamma_lower_bound_deficit.json`
