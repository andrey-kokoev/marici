# Fixed-degree leading symbol does not source the quarter

## Problem

The coefficient \(1/4\) might arise directly from the polynomial leading symbol of \(S_n(s+t)\) as the common shift grows.

## Bold conjecture

The fixed-degree shift polynomial has degree density \(1/4\), so its logarithmic curvature supplies the amplitude numerator.

## Named rivals

The rivals are degree density \(3/2\), cancellation from a simultaneous large-degree and large-shift regime, and a Barnes normalization invisible to the fixed-degree leading symbol.

## Risky consequences

If the conjecture is correct, exact polynomial interpolation must give

\[
\frac{\deg_t S_n}{n^2}\longrightarrow\frac14.
\]

## Strongest falsification attempt

Exact finite differences through \(n=8\) give

\[
\deg_t S_n=\frac{3n(n-1)}2.
\]

The density therefore tends to \(3/2\), not \(1/4\). All leading coefficients were positive and the degree pattern passed five exact gates.

## Disposition

Reject the fixed-degree leading-symbol conjecture. The large-degree limit defining \(C(t)\) cannot be interchanged with the large-shift limit. The next leaf is `quarter-double-scaling-curvature`: test simultaneous \(t=\kappa n\) scaling to locate the crossover between degree density \(3/2\) and the quarter amplitude.

## Claim boundary

The exact degree formula is verified only through \(n=8\), though the pattern is unambiguous on that range. It does not determine the simultaneous-scaling function or prove the order of limits analytically.
