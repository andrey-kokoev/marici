# Euler ratios supercontract along every doubling Adams ray

## Exact edge ratio

The source coefficient at prime \(p\) and grade \(k\) is

\[
a_{p,k}
=
\frac1k p^{-k/2}.
\]

For the doubling Adams edge \(k\to2k\), the coefficient ratio is

\[
\rho_{p,k}
=
\frac{a_{p,2k}}{a_{p,k}}
=
\frac12p^{-k/2}.
\]

After \(n\) doubling steps,

\[
k\to2k\to\cdots\to2^nk,
\]

the ratios telescope:

\[
\prod_{j=0}^{n-1}\rho_{p,2^jk}
=
\frac{a_{p,2^nk}}{a_{p,k}}
=
2^{-n}p^{-(2^n-1)k/2}.
\]

This is superexponential contraction in the constructor depth.

## Domination of type-fiber growth

Let \(A_{p,k}:F_{p,k}\to F_{p,2k}\) be the normalized type-fiber edge. If

\[
\|A_{p,2^jk}\|\le M
\]

uniformly, then the weighted word satisfies

\[
\left\|
\prod_{j=0}^{n-1}
\rho_{p,2^jk}A_{p,2^jk}
\right\|
\le
M^n2^{-n}p^{-(2^n-1)k/2}.
\]

For every fixed \(M<\infty\), the right side is uniformly bounded in \(n,p,k\) and tends to zero along every infinite ray.

More generally, Euler contraction dominates grade-dependent growth whenever

\[
\log\|A_{p,k}\|
\le
\theta k\log p+o(k\log p)
\]

with

\[
\theta<\frac12.
\]

The remaining exponent budget is exactly the earlier endpoint-lift threshold.

## Seam and Fourier cells

Moving-seam transport and Fourier-orbit permutation are source-isometric in the transported saturated topology. They contribute no ray growth.

Uniformly bounded associators or endpoint comparison cells contribute at most ordinary exponential growth in \(n\), which is still dominated by the double-exponential Euler factor. This statement requires their bounds to be independent of grade and prime.

## Source normalization

The raw weighted map has no lower bound as \(k\to\infty\). That is expected. Observability must compare it to the arithmetic source norm carrying the same coefficient \(a_{p,k}\).

After source normalization, the relevant type-fiber comparison is \(A_{p,k}\), not the vanishing scalar ratio. Upper semigroup stability and lower observability are therefore different statements.

## Failure modes

Euler contraction does not repair:

- a type-fiber edge undefined on the completed domain;
- cross-prime leakage;
- growth with exponent \(\theta\ge1/2\);
- comparison-cell norms depending superexponentially on grade;
- loss of the weighted source normalization.

It does repair any fixed generatorwise or ordinary exponential composite bound along the doubling ray.

## Consequence

The infinite-ray norm problem is no longer an independent gate under the sub-half-density growth budget. The concrete unresolved questions are:

1. exact preservation of prime-label idempotents;
2. a uniform sub-half-density bound for the type-fiber and endpoint lifts;
3. source-normalized lower observability;
4. finite coherence of the seam and endpoint cells.

## Frontier

The weighted Adams ray is analytically stable once the type-fiber edge satisfies

\[
\log\|A_{p,k}\|
<
\frac12k\log p
\]

uniformly with positive margin.

The earliest remaining authority gate is prime-label preservation. Without it, coherent off-diagonal prime rows can bypass every one-ray estimate.
