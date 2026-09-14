# The source Fejér hierarchy is positive through order thirteen

## Computation

Use the source kernel coefficients at

\[
\sigma=0.005,
\qquad h=0.25.
\]

For every order \(2\leq N\leq13\), evaluate

\[
F_N(\theta)
=
K(0)+2\sum_{m=1}^{N-1}
\left(1-\frac mN\right)
K(mh)\cos(m\theta)
\]

on a uniform mesh of 131,072 circle angles.

## Global interpolation bound

The derivative satisfies

\[
|F_N'(\theta)|
\leq
2\sum_{m=1}^{N-1}
\left(1-\frac mN\right)m|K(mh)|.
\]

Multiplying this bound by half the mesh spacing controls every point between adjacent samples.

Coefficient uncertainty is also included, using \(10^{-6}\) for \(K(0)\) and \(2\times10^{-6}\) for each nonzero-separation coefficient.

## Result

Every Fejér polynomial through order thirteen has a positive global lower bound under the inherited coefficient-error model.

The tightest case occurs at order eight, near angle

\[
4.32281.
\]

Its values are:

- mesh minimum: approximately \(0.00185739\);
- mesh interpolation allowance: approximately \(0.00003434\);
- coefficient allowance: \(0.000015\);
- conditional global lower bound: approximately \(0.00180805\).

## Significance

The scalar Fejér hierarchy is much better conditioned here than the highest Cholesky pivots. Orders twelve and thirteen had pivots below \(10^{-6}\), while the tightest Fejér lower bound through the same order remains above \(10^{-3}\).

This validates Fejér regularization as the more stable finite computational projection of circle positivity.

## Scope

The result is conditional on the source coefficient error model and covers only one width, one spacing, and orders through thirteen. The RH-equivalent target still requires all orders along spacings tending to zero.

## Verification

```text
python research/voevodsky/checkers/scout_source_fejer_hierarchy.py
```

Artifacts:

- `research/voevodsky/checkers/scout_source_fejer_hierarchy.py`
- `research/voevodsky/results/source_fejer_hierarchy_scout.json`
