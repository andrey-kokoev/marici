# Quarter leading minor has exact three-binomial degree

## Question

Why do the Newton certificates terminate earlier than the entrywise polynomial degree bound?

## Claim boundary

The degree statement holds for every minor size. Strict positivity of every Newton coefficient has only been verified through size eight.

## Disposition

The top homogeneous alternant has column exponents

\[
0,4,8,\ldots,4(k-1).
\]

Its Vandermonde factor removes \(\binom{k}{2}\) degrees from the total \(4\binom{k}{2}\), leaving the exact shift degree

\[
3\binom{k}{2}.
\]

The remaining Schur leading factor is positive on the common positive direction, so the leading coefficient is positive. Exact calculations through size eight match this degree, have positive coefficients at every Newton order through it, and vanish identically above it. The next executable leaf is `quarter-leading-minor-newton-size-twelve`, using the sharp degree to stress-test coefficient positivity at larger sizes.
