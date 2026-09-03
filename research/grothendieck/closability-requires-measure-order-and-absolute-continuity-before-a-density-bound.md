# Closability requires measure order and absolute continuity before a density bound

## Question

What source properties would make the corrected semibounded-form gate checkable rather than formal?

## Claim boundary

If the coupled gamma-remainder-plus-prime functional is representable by a signed measure on the Bernstein interval, then closability relative to a positive reference measure forces absolute continuity; the lower spectral bound becomes a pointwise lower bound on the Radon–Nikodym density. If the source remains a higher-order distribution, this multiplication-form criterion is unavailable.

## Measure-form theorem

Let `mu0` be a finite positive measure on `[0,1]` with polynomials dense in `L2(mu0)`. Let `nu` be a signed measure, and define on polynomials

\[
\mathfrak q[p]=\int|p(z)|^2\,d\nu(z).
\]

Suppose the positive and negative parts are locally finite. The multiplication form is closable in `L2(mu0)` only if the part of `nu` seen by the form is absolutely continuous with respect to `mu0`. Writing

\[
d\nu=w\,d\mu_0,
\]

the closed form has natural domain

\[
\mathcal D(\overline{\mathfrak q})
=\{f\in L^2(\mu_0): |w|^{1/2}f\in L^2(\mu_0)\}.
\]

It obeys

\[
\overline{\mathfrak q}[f]\ge-\|f\|_{L^2(\mu_0)}^2
\]

exactly when

\[
w(z)\ge-1
\quad\text{for }\mu_0\text{-almost every }z.
\]

The density may be unbounded above.

## Why singular atoms fail

If `nu` has an atom at `z0` while `mu0({z0})=0`, polynomial approximation can produce a sequence concentrated near `z0` with `L2(mu0)` norm tending to zero but fixed value at `z0`. The corresponding point-evaluation quadratic form does not close to zero. Thus singular source pieces cannot be inserted into the GNS completion merely because every finite polynomial evaluation exists.

## Application to the prime functional

The regularized von Mangoldt cosine object is initially a distribution paired with Gaussian–Bernstein envelopes. Before asking for a density lower bound, one must prove one of two typed statements:

1. it combines with the gamma remainder to become an order-zero signed measure in the common Bernstein coordinate and is absolutely continuous with respect to the positive reference measure; or
2. it defines a genuinely differential or nonlocal closed form with an independently specified domain, in which case multiplication-density language must not be used.

Finite moment matrices do not decide this distinction.

## Strongest falsification attempt

Absolute continuity is sufficient for the multiplication model but may be too restrictive for a legitimate nonlocal semibounded operator. Conversely, declaring an abstract nonlocal form without proving closability only renames the target. The first source test is distributional order: determine whether the coupled regularized functional extends continuously to continuous test functions in `z`, rather than only to analytic Gaussian envelopes.

## Disposition

Add a measure-order gate before the relative spectral bound. If order zero and absolute continuity are proved, test the density condition `w>=-1`. Otherwise construct and close the nonlocal form directly; do not invoke Radon–Nikodym or bounded Riesz representation.