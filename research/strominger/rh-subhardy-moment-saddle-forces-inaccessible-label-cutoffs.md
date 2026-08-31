# Sub-Hardy moment saddle forces inaccessible label cutoffs

## Question

How must the arithmetic label cutoff grow with the number of cancelled moments before a finite Gram calculation resolves the relevant tail?

## Moment saddle

For the weight exponent \(0<\beta<1/2\), the order-\(K\) squared moment norm is controlled by

\[
M_{2K}=\sum_{n\ge2}
\frac{(\log n)^{2K}}{n e^{2a(\log n)^\beta}}.
\]

With \(x=\log n\), its integral comparator has exponent

\[
\Psi_K(x)=2K\log x-2ax^\beta.
\]

The unique critical point satisfies

\[
\Psi_K'(x)=\frac{2K}{x}-2a\beta x^{\beta-1}=0,
\]

hence

\[
x_K=\left(\frac{K}{a\beta}\right)^{1/\beta}.
\]

The derivative is positive below \(x_K\) and negative above it. Therefore a cutoff with \(\log N<x_K\) truncates the comparator while its integrand is still increasing and cannot resolve its dominant region.

## Discrete transfer

The logarithmic cell widths obey

\[
\frac1{n+1}<\log\!\left(1+\frac1n\right)<\frac1n.
\]

Thus the factor \(1/n\) in the discrete mass is the source-derived cell scale for \(x=\log n\). On either monotone side of the saddle, ordinary upper and lower Riemann-sum bounds compare the atomic sum to its integral plus at most endpoint terms. This transfers the location of the dominant logarithmic range without identifying the atomic and continuous polynomial closures.

A necessary scale for a direct label enumeration is consequently

\[
N_K\gtrsim
\exp\!\left[
\left(\frac{K}{a\beta}\right)^{1/\beta}
\right].
\]

## Numerical consequence

For \(a=1\), \(\beta=1/4\), and \(K=6\),

\[
x_6=24^4=331776.
\]

The adaptive computation stopped at \(N=100000\), for which \(\log N\) is only about \(11.51\). It did not approach the dominant logarithmic range.

## Disposition

Fixed or ordinary exponential-in-\(K\) label grids cannot decide boundedness of the anchored minimum norms in the sub-Hardy regime. The observed norm growth is cutoff-contaminated. Further direct enumeration is rejected; the next test must bound the infinite atomic Gram matrix analytically, using sum-integral error estimates rather than reaching the saddle by enumeration.

## Claim boundary

The saddle law is a necessary resolution scale, not a proof that the anchored norms are bounded or divergent. It does not transfer continuous moment indeterminacy to the atomic measure.
