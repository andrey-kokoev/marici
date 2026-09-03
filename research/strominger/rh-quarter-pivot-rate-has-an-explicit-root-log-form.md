# Quarter pivot rate has an explicit root-log form

## Problem

The boundary-normalized rate remained an improper quadrature.

## Bold conjecture

Let \(r_i\) be the roots of \(8r^3+17r^2+14r+4\). Then

\[
f(\kappa)=H(\kappa)-1+(\kappa+2)
\left[
\log\frac{\kappa+2}{\kappa+1}
+
\sum_i\frac{
\log\bigl((\kappa+2)/(\kappa-r_i)\bigr)}{r_i+2}
\right].
\]

## Named rivals

The rivals are an omitted endpoint term, an unavoidable imaginary branch contribution, and a residual improper integral.

## Risky consequences

The conjugate-root terms must combine to a real rate, the formula must solve the first-order equation, and it must match an independently transformed tail quadrature.

## Strongest falsification attempt

At five positive ratios, the imaginary residual is zero, the maximum quadrature discrepancy is \(3.47\times10^{-6}\), and the maximum differential-equation residual is \(4.84\times10^{-9}\). The large-ratio residual relative to \(3\log\kappa+\log4-1\) decreases across the tested tail. Omitting the endpoint term \(-1\) fails deliberately. All five gates passed.

## Disposition

Resolve the conditional rate to the explicit root-log expression. The next leaf is `quarter-explicit-rate-vs-exact-pivots`: test this zero-parameter rate directly against nested exact-pivot windows.

## Claim boundary

The formula is conditional on the rational defect and uniform rate ansatz. It does not prove either input.
