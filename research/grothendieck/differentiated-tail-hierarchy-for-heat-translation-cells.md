# Differentiated tail hierarchy for heat--translation cells

## Question

What tail certificate controls a coherence cell after heat and translation differentiation?

## Derivative weight

Let `L_n=log n`. At fixed heat scale with Gaussian coefficient `c_t>0`, the undifferentiated paired-prime coefficient is bounded by

\[
C_t\Lambda(n)n^{-1/2}e^{-c_tL_n^2}.
\]

Applying `k` heat derivatives contributes `L_n^(2k)`. Applying `m` translation derivatives contributes `L_n^m`. Hence a combined cell of bidegree `(k,m)` has entrywise tail

\[
\varepsilon_N^{(k,m)}
=
2C_t\sum_{n>N}
\Lambda(n)n^{-1/2}
L_n^{2k+m}e^{-c_tL_n^2}.
\]

Using `Lambda(n)<=L_n`, set

\[
s=2k+m+1.
\]

Beyond the monotonicity threshold,

\[
\varepsilon_N^{(k,m)}
\le
2C_t\left[
N^{-1/2}(\log N)^s e^{-c_t(\log N)^2}
+I_s(\log N;c_t)
\right],
\]

where

\[
I_s(L;c)=\int_L^\infty y^s e^{-cy^2+y/2}\,dy.
\]

## Exact recurrence

The base integral is

\[
I_0(L;c)
=
e^{1/(16c)}
\frac{\sqrt\pi}{2\sqrt c}
\operatorname{erfc}\!\left(\sqrt c\left(L-\frac1{4c}\right)\right).
\]

For integers `s>=1`, integration by parts gives

\[
2cI_s(L;c)
=
L^{s-1}e^{-cL^2+L/2}
+(s-1)I_{s-2}(L;c)
+\frac12I_{s-1}(L;c),
\]

with the `I_(s-2)` term omitted at `s=1`. Thus every differentiated tail has a finite recurrence to `erfc` and endpoint exponentials.

## Matrix and curvature bounds

For observer rank `r`, the corresponding differentiated Gram-tail operator satisfies

\[
\|R_{I,N}^{(k,m)}\|_{\rm op}
\le r\varepsilon_N^{(k,m)}.
\]

If a coherence curvature is a signed sum of several differentiated routes, its bound is the sum of their transported tail bounds. Cancellation may sharpen the estimate only when proved at the source level.

## Uniformity boundary

For each fixed `(k,m,t)`, the Gaussian dominates every polynomial and the tail tends to zero. The convergence is not uniform over unbounded derivative order or as `t` approaches a width boundary where `c_t` tends to zero. The meta-observer index must therefore retain derivative bidegree and heat scale.

## Disposition

Attach `epsilon_N^(k,m)` to every heat--translation cell. This makes finite-cutoff curvature claims typed and prevents use of the scalar prime-tail certificate after differentiation.
