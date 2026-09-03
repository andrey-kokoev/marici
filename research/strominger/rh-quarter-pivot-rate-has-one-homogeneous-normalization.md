# Quarter pivot rate has one homogeneous normalization

## Problem

The first-order pivot equation must be solved and its undetermined data isolated.

## Bold conjecture

Writing

\[
H(\kappa)=\log A(\kappa)+4\log(\kappa+1)-4,
\]

the rate function is

\[
f(\kappa)=(\kappa+2)
\left[C-\int_0^\kappa\frac{H(u)}{(u+2)^2}\,du\right].
\]

## Named rivals

The rivals are an additional functional ambiguity, loss of positivity in \(A\), and a missing homogeneous mode caused by an incorrect integrating factor.

## Risky consequences

The quadrature must solve

\[
f-(\kappa+2)f'=H,
\]

and adding \(C(\kappa+2)\) must leave the equation invariant while an ordinary constant shift must not.

## Strongest falsification attempt

Numerical differentiation of high-resolution Simpson quadrature at four ratios gives maximum residual \(4.85\times10^{-9}\). Adding \(7(\kappa+2)\) preserves those residuals; adding an ordinary constant fails deliberately. The candidate pivot limit stays positive. All five gates passed.

## Disposition

Resolve the rate equation to a one-parameter family. The normalized pivot curvature cannot determine \(C\). The next leaf is `quarter-pivot-rate-boundary-normalization`: extract one boundary value from exact pivot asymptotics and test consistency across \(\kappa\).

## Claim boundary

The quadrature solves the equation conditional on the candidate \(A\). It does not prove the determinant rate ansatz or supply the boundary normalization.
