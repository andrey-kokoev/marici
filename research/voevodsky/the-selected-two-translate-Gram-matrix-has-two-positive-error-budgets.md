# The selected two-translate Gram matrix has two positive error budgets

## Symmetric channel

At

\[
\sigma=0.005,
\qquad d=0.25,
\]

the symmetric eigenvalue is

\[
K_\sigma(0)+K_\sigma(d).
\]

Its gamma integral has the nonnegative multiplier \(1+\cos(du)\). Therefore the elementary pointwise lower bound for the real digamma function can be integrated directly.

Retaining sixteen positive correction-series terms and bounding the remainder by its decreasing integral gives the lower-center decomposition

\[
2.0128485
-1.9530527
-0.0231993
-0.0051077
=
0.0314887.
\]

A 3,600,000-panel midpoint calculation, together with the global derivative estimate, gives quadrature error at most

\[
0.0156485.
\]

After the tail and floating allowances, the symmetric eigenvalue satisfies

\[
K_\sigma(0)+K_\sigma(d)
>0.0158392.
\]

## Complete rank-two result

The antisymmetric channel was previously bounded below by approximately

\[
0.0194066.
\]

Both eigenvalues of the selected two-translate source Gram matrix therefore have positive analytic error budgets under the stated floating model. Equivalently, that matrix is positive definite with a minimum eigenvalue bounded below by approximately \(0.0158\).

## Scope

This remains conditional on the declared elementary-function rounding allowance. It certifies one parameter pair, not a continuum or higher rank. Its value is methodological: both exchange channels can be handled using source terms and elementary digamma-series inequalities, without zero-location input.

## Verification

```text
python research/voevodsky/checkers/check_elementary_symmetric_eigenvalue_lower_bound.py
```

Artifacts:

- `research/voevodsky/checkers/check_elementary_symmetric_eigenvalue_lower_bound.py`
- `research/voevodsky/results/elementary_symmetric_eigenvalue_lower_bound.json`
