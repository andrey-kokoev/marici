# The prime functional has no termwise finite-variation extension

## Question

Can the regularized prime cosine functional be promoted to an order-zero signed measure by summing the individual prime-power functionals in total variation?

## Claim boundary

No. The von Mangoldt coefficients are not summable after the `n^-1/2` normalization. Convergence on Gaussian–Bernstein polynomials comes from Fourier oscillation and analytic smoothing. Any order-zero measure extension must therefore be constructed from cancellation across prime powers or from the completed gamma–prime combination; it cannot arise by termwise variation bounds.

## Exact prime functional

For a polynomial `p`,

\[
\mathcal Q_P[p]
=-\frac1{2\pi}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\int_{\mathbb R}
W_{t,h,p}(u)\cos(u\log n)\,du,
\]

where

\[
W_{t,h,p}(u)
=e^{-tu^2}(1-e^{-hu^2})|p(1-e^{-hu^2})|^2.
\]

For polynomial `p`, expansion into finitely many Gaussians makes each Fourier transform decay like

\[
\exp\!\left(-\frac{(\log n)^2}{4s}\right)
\]

for suitable positive `s`. This log-Gaussian decay makes the original prime series converge.

## Failure of termwise variation

If the cosine is replaced by its absolute value before integration, then

\[
\int_{\mathbb R}
|W_{t,h,p}(u)\cos(u\log n)|\,du
\]

has no decay in `n` forced by Fourier oscillation. For any nonzero nonnegative envelope, its large-frequency absolute-cosine average remains a positive fraction of its `L1` mass. The resulting coefficient series contains

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n},
\]

which diverges. Already the prime terms give

\[
\sum_p\frac{\log p}{\sqrt p}=\infty.
\]

Thus the series of individual prime-power functionals does not converge in total variation.

## Topology consequence

The polynomial domain carries more structure than a generic continuous or `L2` function of the Bernstein coordinate: its pullback is analytic in `e^{-hu^2}` and preserves Gaussian Fourier decay. Completion only in the leading archimedean `L2` norm may lose this analytic structure. Therefore continuity of the prime form on that completion cannot be inferred from its convergence on every polynomial.

A measure-order promotion requires one of:

1. a source-valid summation that proves cancellation across prime powers and yields a finite signed measure;
2. completion of the gamma and prime pieces together before taking variation;
3. a stronger analytic form domain whose topology controls the required Fourier decay, followed by a separately proved closable embedding into the archimedean Hilbert space.

## Strongest falsification attempt

The divergence of termwise variation does not prove that no finite signed measure represents the summed functional; conditionally convergent distributions can admit order-zero resummations. It proves only that absolute atomwise summation cannot construct that measure and that any claimed extension must exhibit its cancellation mechanism.

## Disposition

Reject termwise total-variation construction of the prime measure. The next source gate is an explicit resummation or analytic-domain closability theorem preserving von Mangoldt cosine cancellation.