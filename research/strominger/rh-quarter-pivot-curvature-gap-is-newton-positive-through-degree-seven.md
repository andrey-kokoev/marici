# Quarter pivot-curvature gap is Newton-positive through degree seven

## Question

Can the all-shift pivot-curvature inequality be certified exactly after clearing its positive denominators?

## Claim boundary

The certificates cover determinant degrees two through seven and every nonnegative integer shift. They do not prove the gap positive at arbitrary determinant degree.

## Disposition

The cleared gap is

\[
q_a(n)D_n(a)D_n(a+2)D_{n-1}(a+1)^2
-q_a(n-1)D_n(a+1)^2D_{n-1}(a)D_{n-1}(a+2).
\]

For each degree two through seven, every Newton coefficient is nonnegative, the constant is positive, and the polynomial tail vanishes exactly. The actual degrees are \(9,27,57,99,153,219\), following \(6(n-1)^2+3\), and every coefficient through the degree is positive. This proves cross-ratio degree monotonicity for all integer shifts at determinant degrees through seven. The next leaf is `quarter-pivot-gap-planar-network`, seeking an all-degree positive path or minor representation of this gap rather than extending degree sampling.
