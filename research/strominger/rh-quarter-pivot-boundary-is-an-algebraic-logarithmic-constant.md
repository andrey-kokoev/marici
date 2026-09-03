# Quarter pivot boundary is an algebraic-logarithmic constant

## Problem

The boundary normalization was known only as an improper integral.

## Bold conjecture

The integral reduces to logarithms of the roots of the cubic pivot-defect polynomial, without an additional Barnes constant.

## Named rivals

The rivals are a genuinely Barnes-transcendental constant, a missing endpoint term in integration by parts, and branch ambiguity from the complex roots.

## Risky consequences

If \(r_i\) are the roots of

\[
8r^3+17r^2+14r+4=0,
\]

then

\[
C=\log2-\frac52+
\sum_{i=1}^3\frac{\log(2/(-r_i))}{r_i+2}
\]

must be real and match independent quadrature.

## Strongest falsification attempt

The roots are one negative real root and a complex-conjugate pair. Their polynomial residuals are below \(10^{-12}\); the conjugate contributions cancel in the imaginary part. The closed form gives \(0.469418374\), while endpoint-regularized quadrature differs by \(1.30\times10^{-6}\). Omitting \(\log2\) fails deliberately. All five gates passed after repairing the root solver's omitted leading coefficient.

## Disposition

Resolve the boundary constant to the displayed algebraic-logarithmic form, conditional on the crossover. The next leaf is `quarter-pivot-rate-explicit-form`: insert this normalization into the rate quadrature and derive a boundary-normalized expression for \(f(\kappa)\).

## Claim boundary

The formula closes the integral implied by the candidate pivot defect. It does not prove that defect, the rate ansatz, or the determinant limit.
