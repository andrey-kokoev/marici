# Fixed-rank small-heat positivity survives the confluent mesh limit

## Question

Can the fixed-rank small-heat theorem be made uniform as the mesh ratio `kappa=h/t` tends to zero?

## Claim boundary

For every fixed rank `N`, there exist `t0>0` and `kappa0>0` such that the endpoint-free Hankel matrix is positive definite whenever

\[
0<t<t_0,
\qquad 0<h/t<\kappa_0.
\]

The constants depend on `N`. This removes the fixed-rank `kappa->0` escape but gives no rank-uniform statement.

## Differentiated small-heat asymptotics

Let

\[
f(t)=\frac{1}{8\sqrt\pi}t^{-1/2}\log(1/t).
\]

For every fixed derivative order `k`, differentiation gives

\[
(-1)^k f^{(k)}(t)
=\frac{t^{-k-1/2}}{8\sqrt\pi}
\left[(1/2)_k\log(1/t)+O_k(1)\right].
\]

The gamma integral may be differentiated to every fixed order by the same split used for the first derivative. The endpoint derivatives are bounded, and every fixed prime derivative is exponentially small. Hence, for each fixed `M`, the completed heat kernel satisfies these asymptotics uniformly for `0<=k<=M`.

## Strict confluent moment matrix

The coefficients `(1/2)_k` are moments of the positive gamma density:

\[
(1/2)_k=\frac1{\sqrt\pi}
\int_0^\infty r^{k-1/2}e^{-r}\,dr.
\]

Therefore every finite Hankel matrix

\[
\bigl((1/2)_{i+j+1}\bigr)_{0\le i,j<N}
\]

is positive definite. The shift by one appears because each endpoint-free difference contributes one directed derivative.

## Confluent finite-difference reduction

Set `h=kappa*t`. Apply the invertible lower-triangular Newton difference transform to the polynomial basis `1,z,...,z^(N-1)`. After positive diagonal rescaling by the appropriate powers of `h`, the transformed Hankel matrix has entries given by divided differences of `-H'` at the nodes

\[
t,t+h,\ldots,t+(2N-1)h.
\]

As `kappa` tends to zero these divided differences converge to the derivative Hankel matrix built from

\[
(-1)^{i+j+1}H^{(i+j+1)}(t).
\]

Using the differentiated asymptotics and then scaling row and column `j` by `t^j`, the normalized matrix converges, uniformly as `t` tends to zero, to a positive multiple of

\[
\bigl((1/2)_{i+j+1}\bigr)_{0\le i,j<N}.
\]

Its least eigenvalue is positive. Continuity of fixed-order divided differences, uniform in sufficiently small `t`, therefore gives one `kappa0(N)` and `t0(N)` for which all principal minors remain positive.

## Falsification boundary

The Newton congruence becomes increasingly ill-conditioned with `N`, and the least eigenvalue of the gamma moment matrix decreases with rank. The proof supplies no uniform lower bound as `N` grows. It also does not treat `kappa->infinity` or non-small heat.

## Disposition

For fixed rank, the small-heat cone is now covered for mesh ratios in `(0,kappa0)` and on every compact subinterval of `(0,infinity)`. The remaining fixed-rank small-heat singular regime is `h/t->infinity`; the all-rank escape remains rank growth.