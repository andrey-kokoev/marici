# Every fixed-rank scaled-mesh cone is positive at small heat

## Question

Does gamma dominance extend beyond rank one in any nontrivial regime?

## Claim boundary

For every fixed matrix rank `N` and fixed scaled mesh `kappa>0`, the endpoint-free Hankel matrix is positive definite when `t>0` is sufficiently small and `h=kappa*t`. The threshold may depend on `N` and `kappa`; no uniform all-rank conclusion follows.

## Small-heat source asymptotic

The gamma integral gives

\[
H(t)=\frac{\log(1/t)}{8\sqrt{\pi t}}+O(t^{-1/2})
\qquad(t\downarrow0).
\]

The endpoint is `O(1)`, while the prime kernel is exponentially small relative to every power of `t`. For each fixed positive `c`, therefore,

\[
H(ct)=\frac{t^{-1/2}}{8\sqrt\pi}
\left[c^{-1/2}\log(1/t)+O_c(1)\right].
\]

For `h=kappa*t`, define

\[
b_n(t)=H(t+nh)-H(t+(n+1)h).
\]

At every fixed `n`,

\[
b_n(t)=\frac{t^{-1/2}}{8\sqrt\pi}
\left[d_n(\kappa)\log(1/t)+O_{n,\kappa}(1)\right],
\]

where

\[
d_n(\kappa)
=(1+n\kappa)^{-1/2}-(1+(n+1)\kappa)^{-1/2}.
\]

## Strict leading Hankel matrix

The leading sequence has the positive moment representation

\[
d_n(\kappa)=\frac1{\sqrt\pi}
\int_0^\infty
r^{-1/2}e^{-r}
\bigl(1-e^{-\kappa r}\bigr)e^{-n\kappa r}\,dr.
\]

Hence for every nonzero polynomial `p(z)=sum_(j=0)^(N-1)c_j z^j`,

\[
\sum_{i,j=0}^{N-1}\overline{c_i}c_jd_{i+j}(\kappa)
=\frac1{\sqrt\pi}
\int_0^\infty
r^{-1/2}e^{-r}(1-e^{-\kappa r})
|p(e^{-\kappa r})|^2\,dr>0.
\]

Since the measure has positive density on an interval, a nonzero polynomial cannot vanish almost everywhere. Thus the fixed `N` leading Hankel matrix `D_N(kappa)` is positive definite.

## Perturbation argument

For fixed `N,kappa`, let `delta_(N,kappa)>0` be the least eigenvalue of `D_N(kappa)`. Entrywise asymptotics in the finite index range `0<=i+j<=2N-2` imply

\[
B_N(t,\kappa t)
=\frac{t^{-1/2}}{8\sqrt\pi}
\left[\log(1/t)D_N(\kappa)+O_{N,\kappa}(1)\right].
\]

The bounded error matrix has norm `O_(N,kappa)(1)`. Once `log(1/t)` times `delta_(N,kappa)` exceeds that norm, the matrix is positive definite.

## Uniformity on compact scaled-mesh intervals

Fix `N` and `0<kappa_min<=kappa<=kappa_max<infinity`. The entries of `D_N(kappa)` depend continuously on `kappa`, and each matrix is positive definite. Compactness therefore gives

\[
\inf_{\kappa\in[\kappa_{\min},\kappa_{\max}]}
\lambda_{\min}(D_N(\kappa))>0.
\]

The small-heat asymptotic errors are also uniform on this compact interval because every scale `1+n*kappa`, for `0<=n<=2N-1`, remains in one compact subset of `(0,infinity)`. Hence one threshold `t0(N,kappa_min,kappa_max)` proves positivity simultaneously for every scaled mesh in that interval.

## Strongest falsification attempt

The least eigenvalue may decay rapidly with `N`, and the error norm may grow with `N` or degenerate as `kappa` approaches zero or infinity. Therefore the quantifiers cannot be exchanged:

\[
\forall N,\kappa\;\exists t_0(N,\kappa)
\]

is proved, while the all-rank cone would require control uniform enough to handle arbitrary rank and independent `t,h`. This theorem does not supply it.

## Disposition

Gamma dominance controls every fixed rank along every fixed scaled mesh near the small-heat boundary. Any counterexample to the all-rank cone must escape this regime by rank growth, mesh degeneration, or non-small heat.