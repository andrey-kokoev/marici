# Fejér regularization turns circle positivity into a scalar hierarchy

## Construction

For fixed width \(\sigma\) and spacing \(h\), let

\[
k_m=K_\sigma(mh).
\]

The order-\(N\) Fejér regularization of the associated circle distribution is

\[
F_N(\theta)
=
k_0
+2\sum_{m=1}^{N-1}
\left(1-\frac mN\right)
k_m\cos(m\theta).
\]

Every coefficient is supplied by the endpoint, gamma, and prime source formula.

## Positivity equivalence

If the circle distribution is positive, convolution with the nonnegative Fejér kernel gives

\[
F_N(\theta)\geq0
\]

for every \(N\) and \(\theta\).

Conversely, if every Fejér regularization is nonnegative, the approximate-identity limit is a positive distribution. Thus

\[
\mu_{\sigma,h}\geq0
\]

if and only if

\[
F_N(\theta)\geq0
\]

for every natural \(N\) and every circle angle.

Combined with Herglotz, this is equivalent to positivity of the complete Toeplitz ladder.

## Computational use

This replaces an unstructured infinite matrix question by a hierarchy of scalar trigonometric-polynomial inequalities. Each finite order can be attacked by:

- interval evaluation on an angle mesh;
- a derivative bound between mesh points;
- exact source enclosures for the finitely many coefficients.

A finite Fejér order is not identical to the same-size Toeplitz PSD condition. The equivalence holds for the complete all-order hierarchy.

## RH gate

For one spacing, this proves only positivity of an aliased circle pushforward. Requiring the full Fejér hierarchy along spacings tending to zero recovers real-line Weil positivity by the de-aliasing theorem and is therefore RH-equivalent under the standard source comparison.

## Verification

```text
python research/voevodsky/checkers/check_fejer_scalarization_of_toeplitz_positivity.py
```

The checker verifies positive atomic examples through order sixteen and retains a signed-circle hostile producing negative Fejér values.

Artifacts:

- `research/voevodsky/checkers/check_fejer_scalarization_of_toeplitz_positivity.py`
- `research/voevodsky/results/fejer_scalarization_of_toeplitz_positivity.json`
