# Many-many labelled detector Gaussian majorant

The source-supported target estimate is a compact-local bound of the form

$$
\|h_{j,k,n,m}\|\,\|w_{j,k,n,m}\|
\le
A_K(1+\log p_j)^M
\exp\{-c_K e^{2a_j}\}
\,b_{k,n,m},
$$

where, on shells with lower endpoint `a_j >= a_0 > 0`, one may take

$$
 b_{k,n,m}\lesssim e^{-\pi(n^2+m^2)a_0^2}
$$

up to the declared grade factor. This is summable against the declared source weights. Under

$$
\sum_{j,k,n,m}(1+\log p_j)^{2M}e^{-2c_K e^{2a_j}}b_{k,n,m}^2<\infty,
$$

then

$$
\sum_{j,k,n,m}
\|h_{j,k,n,m}\|^2\|w_{j,k,n,m}\|^2<\infty.
$$

Hence the labelled mode-to-wall detector extends continuously from finite packets to the full direct-sum carrier. The attenuation factors `t^j u^k`, with `0<t,u<1`, only improve the bound.

This is the analytic condition needed to pass the synthetic shell-mode model to an infinite labelled detector. The Gaussian shell factor is source-supported; the grade/pair summability and selected wall weights still require verification from the explicit response formulas.

Status: interior detector continuity closed under the pair Gaussian bound; endpoint-uniform continuity remains conditional.
