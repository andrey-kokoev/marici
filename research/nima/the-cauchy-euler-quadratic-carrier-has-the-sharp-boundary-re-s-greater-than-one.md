# The Cauchy Euler quadratic carrier has the sharp boundary \(\Re s>1\)

Introduce an off-seam displacement \(\sigma>0\) and define

\[
Y_\sigma(T)
=
\sum_{n\ge1}n^{-1/2-\sigma}X_{\log n}(T).
\]

Its Cauchy mean is

\[
A_\sigma
=
\mathbb E Y_\sigma
=
\sum_{n\ge1}n^{-1-\sigma}
=
\zeta(1+\sigma).
\]

For the normalized state \(Z_\sigma=Y_\sigma/A_\sigma\), the second moment is

\[
\mathbb E|Z_\sigma|^2
=
\frac1{\zeta(1+\sigma)^2}
\sum_{n,m\ge1}
\frac{
e^{-\frac12|\log(n/m)|}
}{
n^{1/2+\sigma}m^{1/2+\sigma}
}.
\]

If \(n\ge m\), the summand becomes

\[
n^{-1-\sigma}m^{-\sigma}.
\]

Equivalently, if \(N,M\) are independent with

\[
\Pr(N=n)=\frac{n^{-1-\sigma}}{\zeta(1+\sigma)},
\]

then

\[
\mathbb E|Z_\sigma|^2
=
\mathbb E\min(N,M).
\]

The convergence threshold is exact. For \(0<\sigma<1\),

\[
\sum_{m\le n}m^{-\sigma}
\asymp n^{1-\sigma},
\]

so the ordered half of the double sum is comparable to

\[
\sum_{n\ge1}n^{-1-\sigma}n^{1-\sigma}
=
\sum_{n\ge1}n^{-2\sigma}.
\]

Therefore

\[
Z_\sigma\in L^2(\mu_C)
\quad\Longleftrightarrow\quad
\sigma>\frac12.
\]

At \(\sigma=1/2\) the divergence is logarithmic; below it the divergence is
power-like. Since \(s=1/2+\sigma+it\), the quadratic Cauchy carrier exists
exactly in

\[
\Re s>1.
\]

This is the Euler convergence chamber, not the full off-seam half-plane. The
Cauchy covariance does not analytically bridge the critical strip as a
Hilbert state, even though the first moment exists for every \(\sigma>0\).

The result aligns two previously separate thresholds:

- the raw Mellin observer becomes Hilbert-continuous only past the half-offset;
- the normalized nonlinear Euler state becomes square-integrable at the same
  half-offset.

Thus the half-offset is a genuine quadratic boundary of the arithmetic
carrier, not an artifact of linearization.

The completed theta Green form must change representation at \(\Re s=1\).
Analytic continuation of the scalar mean does not continue the Cauchy Hilbert
vector. Any claimed single Hilbert family extending \(Z_\sigma\) through
\(0<\sigma\le1/2\) must exhibit an additional source channel whose Schur
return cancels the max-kernel tail before the norm is formed.

The sharp hostile keeps the scalar identity
\(\mathbb E Z_\sigma=1\) for all \(\sigma>0\) and analytically continues it,
while treating \(Z_\sigma\) as an \(L^2\) vector in the critical strip. The
displayed \(p\)-series excludes that move.
