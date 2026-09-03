# The quarter four-staircase cross minor is second order

## Question

At what order does the subtractive cross minor enter the quarter-staircase condensation balance?

Exact rational determinants through \(n=12\) give a positive decreasing cross ratio. On \(n=8,\ldots,12\),

\[
n^2\Theta_n
=0.25305,
0.24863,
0.24517,
0.24238,
0.24009,
\]

while \(n\Theta_n\) decreases from \(0.03163\) to \(0.02001\). The relative late-window spread is \(0.0527\) for \(n^2\Theta_n\), compared with \(0.462\) for \(n\Theta_n\). Thus the grid supports

\[
\Theta_n=\frac{\theta_2}{n^2}+o(n^{-2}).
\]

Consequently

\[
\log(1-\Theta_n)
=-\frac{\theta_2}{n^2}+o(n^{-2}).
\]

Unlike the half-Weibull two-staircase, the quarter four-staircase cross minor does not enter at order \(1/n\).

## Disposition

Resolve the finite scaling discrimination in favor of \(n^{-2}\). The next leaf is `quarter-four-staircase-cross-limit`: determine and prove the coefficient \(\theta_2\), then insert it into the full condensation balance for the \(13/48\) logarithmic term.

## Claim boundary

Degree twelve does not prove the order or the limit. The scaling comparison is diagnostic and required correction of an initial absolute-spread test, which incorrectly favored \(n^{-1}\); relative spread gives the dimensionless comparison.
