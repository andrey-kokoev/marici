# The first coupled Loewner scan reaches a conditioning floor

The first genuinely coupled condition is

\[
 D(x,y)=F'(x)F'(y)-\left(\frac{F(y)-F(x)}{y-x}\right)^2\ge0.
\]

A zero-free eta/digamma scan over 29 logarithmic points finds robust positive
values for widely separated pairs. For `y/x>=100`, the smallest sampled
determinant is about `3.0e-10`.

For nearby points close to the origin, raw determinants reach small negative
values around `10^-12`. These are not credible counterexamples: the certified
positive five-node Jacobi model predicts positive determinants at the same
pairs only around `10^-14` to `10^-12`, beneath the complex source evaluator's
transform-depth and differentiation error. The determinant also vanishes
quadratically as `y->x`, making this cancellation unavoidable.

Thus the first coupled scan exposes a numerical conditioning floor rather than
a Pick violation. The next implementation must evaluate `F`, `F'`, and divided
differences together with shared interval correlations or use the source
kernel directly, avoiding subtraction of nearly equal values.

At `x=1/4` the diagonal ambiguity can already be removed analytically. The
quadratic contact coefficient is exactly `16(A_0 A_2-A_1^2)`, and the existing
eta-derived moment intervals certify it strictly positive. See
`quarter-point-loewner-diagonal-curvature.md`.

## Scope

No robust negative counterexample was found, but near-diagonal positivity was
not certified. This remains numerical reconnaissance and does not prove RH.

## Durable verification

- Checker: `checkers/reduced_source_loewner_two_point_scan.py`
- Result: `results/reduced-source-loewner-two-point-scan.json`
