# Weighted variation controls the infinite Legendre prime residual

Let `g` be piecewise absolutely continuous on `(-L,L)` and put `h(t)=g(Lt)`.
For normalized Legendre functions `phi_n`, integration by parts using

\[
(2n+1)P_n=P_{n+1}'-P_{n-1}'
\]

and the Bernstein bound

\[
|P_m(t)|\le \sqrt{\frac2\pi}
(m+1/2)^{-1/2}(1-t^2)^{-1/4}
\]

gives, for `n>=2`,

\[
|\langle g,\phi_n\rangle|
\le \sqrt{\frac{2L}{\pi}}\frac{J(g)}n,
\]

where

\[
J(g)=\int_{-1}^1|h'(t)|(1-t^2)^{-1/4}dt
+\sum_{t_j}|[h]_{t_j}|(1-t_j^2)^{-1/4}.
\]

Consequently

\[
\|Q_Ng\|_2
\le \sqrt{\frac{2L}{\pi(N-1)}}J(g).
\]

For a dangerous finite eigenvector `v`, take `g=P_{prime}v`. It is a finite
piecewise polynomial, so `J(g)` is a finite collection of weighted polynomial
integrals and jump values, directly amenable to Arb quadrature. This turns the
infinite residual tail into finitely many scalar enclosures.
