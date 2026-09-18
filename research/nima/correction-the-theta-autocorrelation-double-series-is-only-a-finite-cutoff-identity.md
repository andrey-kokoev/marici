# Correction: the theta autocorrelation double series is only a finite-cutoff identity

For a finite theta-label cutoff `N`, termwise Gaussian integration is valid and gives

$$
A_{\Phi,N}(t)
=\frac{3e^{t/2}}2
\sum_{1\le n,m\le N}\frac1n
\frac{r^2(-6+23r^2-6r^4)}{(1+r^2)^{9/2}},
\qquad r=\frac{me^t}{n}.
$$

It is not valid to pass directly to the unrestricted double series by absolute convergence. Along a fixed coprime ray

$$
(n,m)=(da,db),
$$

the ratio `r=(b/a)e^t` is independent of `d`, while the summand is proportional to

$$
\frac1d.
$$

Unless the ratio profile vanishes at that particular `r`, the ray contributes a harmonic divergence. Therefore

$$
\sum_{n,m}\int|\phi_n(u)\phi_m(u+t)|\,du
$$

diverges, and Fubini/Tonelli does not authorize the infinite termwise formula.

The completed theta autocorrelation itself remains finite because the original theta sum has Poisson/completion cancellations before squaring and integration. Those cancellations are destroyed by naively separating every labelled pair.

Consequently the double ratio kernel is a finite-cutoff diagnostic, not a completed identity. Passing to completion requires one of:

1. Poisson resummation before integration;
2. subtraction of the common scaling-ray divergence;
3. a relative/projective limit retaining the divergent primitive line;
4. determinant/anomaly-line renormalization compatible with the common carrier.

This scaling-ray divergence is precisely the kind of primitive normalization that the seam and archimedean currents must absorb. It cannot be discarded termwise.

Status: finite-cutoff kernel formula retained; unrestricted double-series claim retracted; completion-compatible renormalization is required.
