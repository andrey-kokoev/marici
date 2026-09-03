# Quarter solid minors through size eight are positive at all starts

## Question

Does the exact Newton certificate persist for the reduced leading-minor families through size eight?

## Claim boundary

The result covers contiguous minors through size eight for arbitrary nonnegative integer starts and shifts. It does not cover larger sizes or noncontiguous minors.

## Disposition

For each leading-minor size one through eight, every Newton coefficient through the polynomial degree bound is nonnegative, the constant is positive, and the next forward difference vanishes exactly. Combined with the positive-weight start reduction, this proves every solid minor through size eight strictly positive for arbitrary nonnegative integer row start, column start, and shift. The positive-coefficient counts follow

\[
1+3\binom{k}{2},
\]

suggesting the sharper exact degree \(3\binom{k}{2}\). The next executable leaf is `quarter-leading-minor-degree-three-binomial`, testing and deriving that cancellation pattern before any further size extension.
