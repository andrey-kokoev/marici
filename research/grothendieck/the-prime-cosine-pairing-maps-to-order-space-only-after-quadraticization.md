# The prime cosine pairing maps to order space only after quadraticization

## Question

Can the exact prime Hankel form supply the missing map from Hankel polynomials into the source-positive order completion?

## Exact finite packet

For a polynomial `p`, set

\[
f_{t,h,p}(u)=e^{-tu^2}(1-e^{-hu^2})|p(e^{-hu^2})|^2
\]

and, for each prime-power label `lambda_n=log n`,

\[
\beta_n(t,h,p)=\frac{\Lambda(n)n^{-1/2}}{2\pi}
\int_{\mathbb R}f_{t,h,p}(u)\cos(\lambda_nu)du.
\]

The exact prime quadratic is

\[
Q_P(t,h;p)=-\sum_{n\ge2}\beta_n(t,h,p).
\]

At a finite cutoff `N`, adjoin the label `lambda_0=0` and define

\[
c_0^{(N)}=-\sum_{2\le n\le N}\beta_n,
\qquad
c_n^{(N)}=\beta_n.
\]

Then the packet has zero total sum and belongs to the finite order space. Since no positive label lies below `log 2`, its cumulative-sum image is constant on `(0,log 2)`:

\[
Jc^{(N)}(u)=\sqrt2\sum_{2\le n\le N}\beta_n
=-\sqrt2 Q_{P,N}
\qquad(0<u<\log2).
\]

Therefore

\[
\|c^{(N)}\|_{\mathrm{ord}}^2
\ge2\log2\,|Q_{P,N}(t,h;p)|^2.
\]

This realizes the truncated prime value as a bounded boundary coordinate of an explicit zero-sum order packet.

## Convergence

The Fourier transform of `f_(t,h,p)` is a finite linear combination of Gaussians because `|p(e^{-hu^2})|^2` is a finite linear combination of factors `e^{-khu^2}`. Hence `beta_n` decays faster than every exponential in `log n`, up to the factor `Lambda(n)n^(-1/2)`. The sum of `|beta_n|` converges for every fixed `t,h>0` and polynomial `p`. Thus the zero-sum packets have a well-defined infinite coefficient sequence.

Order-norm convergence is a separate condition; absolute coefficient summability alone does not control the logarithmic-gap energy.

## Fatal linearity mismatch

The construction is not a linear map of `p`. It depends on

\[
|p(e^{-hu^2})|^2,
\]

so

\[
p\longmapsto c_{t,h,p}
\]

is quadratic. Consequently `||c_(t,h,p)||_ord` is homogeneous of degree two in `p`, and its squared norm is quartic. It cannot define the required closable quadratic form or a linear GNS intertwiner on the polynomial Hilbert space.

Polarizing `|p|^2` produces a sesquilinear packet `c_(p,q)`, but converting that packet into a Gram norm would square the already sesquilinear target and introduce cross-prime terms absent from the von Mangoldt cosine pairing. That is not a factorization of the original form.

## Relation to bounded heat probes

Heat and fixed Mellin-jet evaluations are bounded linear functionals on the order completion. This confirms that the Fourier-Gaussian coefficients are analytically compatible with the order topology. It does not repair the quadraticization mismatch: the arithmetic packet itself still depends on the quadratic observable `|p|^2`.

## Disposition

The exact prime pairing admits a canonical order-space encoding only after the Hankel polynomial has already been quadraticized. This is a useful bound and convergence representation, but not the missing linear source map. A successful factorization must act linearly on `p` before forming its norm and reproduce the single-prime sum without generating cross-prime terms.