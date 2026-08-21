# Direct source differentiation does not yet resolve Loewner curvature

The local two-point falsifier away from the quarter point is

\[
 C(x)=\frac{F'(x)F'''(x)}6-\frac{F''(x)^2}4.
\]

If `C(x)<0` anywhere on the positive real axis, then the `2 by 2` Loewner
kernel fails for sufficiently close points and the proposed global Pick
explanation is false.

A 33-point logarithmic scan from `10^-2` to `10^2` was attempted by extracting
the first three derivatives from complex source values at three heights. The
baseline discretization was positive at every point. It is not admissible as
evidence: halving the step while changing transform depth produced a negative
control value, and at `x=1/4` the numerical curvature differed from the
independently certified value by about 86 percent.

This failure is expected numerically. `C` combines a third derivative with a
square and is small after cancellation. Double-precision evaluation of the
eta/digamma transform does not preserve the correlations needed for its sign.
Neither the baseline positive scan nor the control negative is a credible
mathematical sign determination.

## Consequence for the attack

The next implementation must not merely shrink finite-difference steps. It
needs one of:

1. directed interval automatic differentiation of the reduced source;
2. a direct integral/kernel formula for `C(x)` that exposes a square or
   covariance; or
3. high-precision ball arithmetic with a certified truncation remainder.

The quarter-point identity remains certified because it evaluates `C(1/4)`
through the eta-derived moment determinant instead of numerical
differentiation. Global diagonal curvature, global Pick positivity, and RH
remain open.

## Durable verification

- Checker: `checkers/reduced_source_loewner_diagonal_curvature_scan.py`
- Result: `results/reduced-source-loewner-diagonal-curvature-scan.json`
