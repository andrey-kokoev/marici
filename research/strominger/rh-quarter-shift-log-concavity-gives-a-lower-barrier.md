# Quarter shift log-concavity gives a lower barrier

## Question

Does determinant shift curvature provide a source-derived barrier for the shifted cross ratios?

## Claim boundary

The Newton certificates cover determinant degrees two through eight and every nonnegative integer shift. The resulting barrier has order \(n^{-4}\), so it does not establish inverse-square scaling.

## Disposition

For each tested determinant degree, the polynomial

\[
D_n(a+1)^2-D_n(a)D_n(a+2)
\]

has nonnegative Newton coefficients and a positive constant, proving strict shift log-concavity for every integer shift at those degrees. Consequently

\[
\Theta_{n+1,a}>rac{q_a(0)}{q_a(n)}.
\]

The actual gap degrees are \(3n(n-1)-2\). All five gates pass. The lower barrier is rigorous at bounded determinant degree but asymptotically too weak. The next leaf is `quarter-shift-log-concavity-path-injection`, seeking an all-degree path proof of this simpler curvature inequality; the inverse-square remainder branch remains separately blocked.
