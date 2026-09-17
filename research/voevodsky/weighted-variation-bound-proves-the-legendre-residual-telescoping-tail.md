# Weighted variation proves the Legendre residual telescoping tail

Let `g:[-L,L]->C^m` be piecewise absolutely continuous and put `h(t)=g(Lt)`.
For the normalized Legendre coefficient row vector

\[
r_n=\sqrt{\frac{L(2n+1)}2}\int_{-1}^1h(t)P_n(t)dt,
\]

use

\[
(2n+1)P_n=(P_{n+1}-P_{n-1})'.
\]

The endpoint boundary term vanishes because
`P_{n+1}(+/-1)=P_{n-1}(+/-1)`. Stieltjes integration by parts therefore gives

\[
r_n=-\frac{\sqrt{L(2n+1)/2}}{2n+1}
 \int_{(-1,1)}(P_{n+1}-P_{n-1})dh.
\]

The Bernstein bound

\[
|P_k(t)|\le
\sqrt{\frac{2}{\pi(k+1/2)}}(1-t^2)^{-1/4}
\]

implies, for `n>=2`,

\[
\|r_n\|
\le \frac{2\sqrt{L/\pi}}{n}
 \mathcal V_{1/4}(h),
\]

where

\[
\mathcal V_{1/4}(h)=
\int_{-1}^1(1-t^2)^{-1/4}\|h'(t)\|dt
+
\sum_j(1-t_j^2)^{-1/4}\|[h]_{t_j}\|.
\]

Consequently

\[
\sum_{n=N}^{M-1}r_n^*r_n
\preceq
\frac{4L}{\pi}\mathcal V_{1/4}(h)^2
\sum_{n=N}^{M-1}\frac1{n^2},I,
\]

and

\[
\sum_{n=N}^\infty\frac1{n^2}\le\frac1{N-1}.
\]

For blocks `N=1000k`, `M=1000(k+1)`, the difference of reciprocal tails is
of order `1/[k(k+1)]`. This proves the telescoping law observed in the
residual scouts.

## Matrix-oriented version

A scalar norm bound discards the favorable orientation of the residual Gram.
To retain it, dominate the vector Stieltjes measure `dh` by a positive scalar
measure `dnu`, write `dh=v dnu`, and define the weighted variation Gram

\[
G_{1/4}=
\left(\int w\,d\nu\right)
\int w(t)v(t)^*v(t)d\nu(t),
\qquad w(t)=(1-t^2)^{-1/4}.
\]

Cauchy--Schwarz in `L2(dnu)` gives the PSD bound

\[
r_n^*r_n\preceq\frac{4L}{\pi n^2}G_{1/4}.
\]

Hence the complete tail is bounded as a matrix by

\[
\sum_{n=N}^\infty r_n^*r_n
\preceq\frac{4L}{\pi(N-1)}G_{1/4}.
\]

For the regularized polynomial residual, `dh` consists of finitely many
polynomial derivative densities and translation-boundary jump rows, plus the
smooth band-multiplier output. Its `G_{1/4}` is therefore a finite collection
of directed one-dimensional integrals and jump outer products. This is the
correct analytic replacement for extrapolating the three floating residual
blocks.
