# Quarter explicit rate matches exact pivots with a seven-halves logarithmic correction

## Problem

Direct inverse-degree fits appeared to miss the explicit rate by an approximately constant amount.

## Bold conjecture

The discrepancy is finite-window bias caused by an omitted correction

\[
-\frac{7}{2}\frac{\log n}{n}
\]

in the normalized pivot rate.

## Named rivals

The rivals are an incorrect boundary constant, a ratio-dependent logarithmic coefficient, and failure of the explicit rate.

## Risky consequences

Fitting exact pivots with basis

\[
1,\quad\frac{\log n}{n},\quad\frac1n,\quad\frac1{n^2}
\]

must recover the zero-parameter rate and a ratio-independent coefficient near \(-7/2\).

## Strongest falsification attempt

Exact pivots through degree twenty-eight were tested at four ratios. Explicit-rate residuals are at most \(1.66\times10^{-4}\). The fitted logarithmic coefficients are \(-3.49813,-3.49879,-3.49939,-3.49976\), with total spread below \(0.002\). Forcing the coefficient to zero fails deliberately. All five strengthened gates passed.

## Disposition

The explicit rate survives direct pivot testing, and the prior boundary mismatch is explained by the omitted logarithmic correction. The next leaf is `quarter-pivot-log-correction-seven-halves`: derive \(-7/2\) from Stirling expansion and determinant leading symbols.

## Claim boundary

The coefficient is finite recognition from a declared correction model, not a theorem. Agreement does not prove the rational crossover or a uniform remainder.
