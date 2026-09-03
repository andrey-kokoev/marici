# A source-typed Fourier–order kernel exists without identifying it with the Hankel kernel

## Question

Can one define a coupled gamma–prime kernel on the source-positive order domain while keeping arithmetic-label and spectral variables distinct?

## Typed source chain

Let `lambda` denote the arithmetic logarithmic-label coordinate. For a finite zero-sum coefficient packet `c`, define

\[
(Jc)(\lambda)=\sqrt2\sum_{\lambda_i>\lambda}c_i.
\]

This is the established isometry from the order norm to the fixed-partition step subspace of `L2(d lambda)`.

Let `u` denote the Fourier-dual spectral coordinate and use the unitary Fourier transform

\[
\mathcal F:L^2(d\lambda)\longrightarrow L^2(du).
\]

For fixed `t,h>0`, define the heat-windowed synthesis

\[
(T_{t,h}c)(u)=
\frac{1}{\sqrt{2\pi}}
e^{-tu^2/2}(1-e^{-hu^2})^{1/2}
(\mathcal FJc)(u).
\]

Every arrow is source-defined: ordered logarithmic labels give `J`, Fourier duality gives `F`, and the completed heat finite difference gives the window. No zero location enters.

## Prime kernel on the finite source core

For finite zero-sum packets `c,d`, define

\[
K_P^{t,h}(c,d)=
-\sum_{n\ge2}\Lambda(n)n^{-1/2}
\int_{\mathbb R}
(T_{t,h}c)(u)\overline{(T_{t,h}d)(u)}
\cos(u\log n)du.
\]

For finite packets, `Jc` and `Jd` are compactly supported step functions. Their Fourier transforms have at most reciprocal decay, while the heat window supplies Gaussian decay in `u`. The Fourier transform in `u` of their windowed product consequently has Gaussian decay in `log n`; the prime series converges absolutely. Equivalently, the Gaussian analytic functional constructed earlier acts on

\[
e^{-tu^2}(1-e^{-hu^2})
(\mathcal FJc)(u)\overline{(\mathcal FJd)(u)}.
\]

Thus `K_P^(t,h)` is a well-defined sesquilinear kernel on the finite order core.

## Completed kernel

Let `G` be the already derived archimedean gamma functional on the same heat-windowed test functions. Define

\[
K_{\Gamma+P}^{t,h}(c,d)
=
G\!\left(
 e^{-tu^2}(1-e^{-hu^2})
 (\mathcal FJc)\overline{(\mathcal FJd)}
\right)
+K_P^{t,h}(c,d).
\]

This is a source-typed coupled kernel on one common core. It adds gamma and prime contributions before closure or semiboundedness is asked.

## What has and has not been constructed

The kernel exists algebraically and analytically on finite zero-sum packets. It does not identify the order-space Riesz vector `r_s`, indexed by arithmetic-label Laplace evaluation, with the Hankel polynomial vector `p(e^{-hu^2})`. In particular, no theorem gives

\[
K_{\Gamma+P}^{t,h}(r_s,r_v)=H(s+v)
\]

or a finite-difference variant. Such a statement would still require a separate typed comparison map.

Nor has boundedness in the order norm been proved. The Gaussian analytic-functional bounds depend on the test decay rate, and Fourier products of an order-norm convergent sequence need not remain in one fixed Gaussian test step. Therefore closability, graph-core density, and semiboundedness remain open properties of this kernel.

## Strongest falsification attempt

The construction could be dismissed as target polarization if `T_(t,h)` were chosen from the desired Hankel value. It is not: `T_(t,h)` is composed solely of the independently established cumulative-sum isometry, ordinary Fourier transform, and exact heat finite-difference window. The remaining possible failure is mathematical rather than circular: the resulting kernel may be nonclosable or unbounded below in the order topology.

## Disposition

A source-typed coupled kernel has been added on the finite order core. It is not the completed Hankel kernel until a source-derived comparison map to Hankel polynomial probes is proved. The next exact test is closability: determine whether `c_k -> 0` in the order norm and `K(c_k-c_l,c_k-c_l) -> 0` forces `K(c_k,c_k) -> 0`, with gamma and prime kept jointly regularized.