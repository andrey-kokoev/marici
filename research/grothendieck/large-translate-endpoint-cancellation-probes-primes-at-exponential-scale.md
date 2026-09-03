# Large-translate endpoint cancellation probes primes at exponential scale

## Moving prime window

For fixed Gaussian width `sigma`, the source-translation prime channel contains weights of the form

\[
\frac{\Lambda(n)}{\sqrt n}
rac12\left[
 e^{-(\log n-d)^2/(8\sigma)}
+e^{-(\log n+d)^2/(8\sigma)}
\right].
\]

For positive large separation `d`, the first Gaussian localizes `log n` to a window of fixed width around `d`, while the second is negligible. Thus the relevant prime powers satisfy

\[
n\asymp e^d.
\]

Every increase in translate separation moves the arithmetic cutoff exponentially outward.

## Endpoint scale

The endpoint channel grows as

\[
K_{\rm end}(d)
=e^{\sigma/2}\cosh(d/2)
\sim\frac12e^{\sigma/2+d/2}.
\]

Under the prime number theorem heuristic made into a Stieltjes integral, write `L=log n`. The von Mangoldt density contributes `dn`, and the factor `n^{-1/2}` changes this to the scale `e^{L/2}dL`. Hence the moving prime window has leading integral

\[
\int e^{L/2}e^{-(L-d)^2/(8\sigma)}\,dL
=\sqrt{8\pi\sigma}
 e^{d/2+\sigma/2}.
\]

It has exactly the endpoint exponential scale. The fixed Fourier constants determine the cancellation coefficient.

## Consequences

The endpoint's forbidden hyperbolic growth can only be canceled by arithmetic data from primes near `e^d`; a fixed prime cutoff cannot control the difference kernel uniformly in `d`. This is the spatial counterpart of the moving saddle in the large-time scalar heat formula.

A rigorous far-separation theorem requires a Gaussian-window prime number theorem with an error strong enough, after combination with the gamma term and exact constants, to establish the rank-two bound

\[
|K_\sigma(d)|\le K_\sigma(0).
\]

The ordinary prime number theorem supplies the leading cancellation scale but not automatically the bounded residual or its sign. Those demands approach zero-free-region strength and must be stated explicitly.

## Disposition

Reject finite-prime and fixed-cutoff evidence for global translate PSD. Separate the large-`d` branch into exact leading endpoint--prime cancellation and a signed residual estimate. The first missing quantitative object is a directed error bound for the von Mangoldt sum in the moving log-Gaussian window centered at `d`.
