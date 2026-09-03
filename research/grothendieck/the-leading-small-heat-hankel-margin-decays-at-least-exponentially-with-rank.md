# The leading small-heat Hankel margin decays at least exponentially with rank

## Question

Can the fixed-rank small-heat perturbation argument plausibly yield a rank-uniform heat threshold from its leading gamma moment matrix alone?

## Claim boundary

No. For every fixed scaled mesh `kappa>0`, the least eigenvalue of the leading `N` by `N` Hankel matrix has an explicit exponential upper bound. This does not disprove the full cone; it shows that a rank-uniform proof cannot use an unstructured operator-norm error against the smallest leading eigenvalue.

## Leading measure

The leading moments are

\[
d_n(\kappa)=\int_0^1 y^n\,d\mu_\kappa(y),
\]

where the change of variables `y=e^(-kappa*r)` in the gamma representation gives a finite positive measure on `(0,1)`. Its total mass is

\[
\mu_\kappa((0,1))=d_0(\kappa)
=1-(1+\kappa)^{-1/2}.
\]

Let `D_N(kappa)=(d_(i+j)(kappa))`.

## Exponentially small Rayleigh quotient

Set `m=N-1` and take

\[
p_m(y)=(1-y)^m.
\]

Its coefficient vector has squared Euclidean norm

\[
\sum_{j=0}^m\binom mj^2=\binom{2m}{m}.
\]

The corresponding Hankel quadratic form is

\[
\int_0^1(1-y)^{2m}\,d\mu_\kappa(y)
\le d_0(\kappa).
\]

Therefore

\[
\lambda_{\min}(D_N(\kappa))
\le
\frac{d_0(\kappa)}{\binom{2N-2}{N-1}}.
\]

Using the central-binomial asymptotic,

\[
\lambda_{\min}(D_N(\kappa))
=O_\kappa\!\left(\frac{\sqrt N}{4^N}\right).
\]

The bound is uniform for `kappa` in a compact subinterval of `(0,infinity)` because `d0(kappa)` is then uniformly bounded.

## Consequence for the perturbation proof

The fixed-rank asymptotic has the form

\[
B_N(t,\kappa t)
=\frac{t^{-1/2}}{8\sqrt\pi}
\left[\log(1/t)D_N(\kappa)+E_N(t,\kappa)\right].
\]

A certificate using only

\[
\log(1/t)\lambda_{\min}(D_N)>\|E_N\|
\]

must confront a leading margin no larger than order `4^(-N)sqrt(N)`. Unless the error has matching structure or an equally strong rank-decaying bound, this method drives the sufficient heat threshold rapidly toward zero as rank grows.

This is a limitation of the norm-perturbation proof, not evidence of a negative Hankel minor. The exact error may align favorably with the near-null polynomials.

## Strongest next test

Project the first gamma correction and the prime kernel onto the explicit near-null family `(1-y)^(N-1)`. The relevant comparison is directional:

\[
\frac{\langle c_N,E_Nc_N\rangle}
     {\langle c_N,D_Nc_N\rangle},
\]

not the full operator norm. A sign or asymptotic formula for this quotient could distinguish genuine rank instability from a poorly conditioned proof basis.

## Disposition

Rank-uniform small-heat positivity cannot be obtained from the leading least-eigenvalue margin plus a coarse error norm. Continue only with structured error estimates on near-null polynomial directions or a source factorization preserving the moment measure.