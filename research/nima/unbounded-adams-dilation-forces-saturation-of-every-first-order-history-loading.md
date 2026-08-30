# Unbounded Adams dilation forces saturation of every first-order history loading

## Dilation calculation

Let

\[
(U_rf)(x)=r^{1/2}f(rx),\qquad r>0,
\]

on \(L^2(\mathbb R)\). For the closed derivative
\(\mathsf D=\partial_x\),

\[
\mathsf D U_r=rU_r\mathsf D.
\]

Hence, for nonconstant \(f\in H^1(\mathbb R)\),

\[
\|U_rf\|_2=\|f\|_2,\qquad
\|\mathsf D U_rf\|_2=r\|\mathsf Df\|_2.
\]

For the first-order graph metric

\[
G=I+\mathsf D^*\mathsf D,
\]

the normalized derivative loading is

\[
\frac{\|\mathsf D U_rf\|_2^2}
{\|U_rf\|_2^2+\|\mathsf D U_rf\|_2^2}
=
\frac{r^2\|\mathsf Df\|_2^2}
{\|f\|_2^2+r^2\|\mathsf Df\|_2^2}
\longrightarrow1.
\]

Thus any source space containing a nonconstant vector and its unbounded
dilation orbit satisfies

\[
\|\mathsf D G^{-1/2}\|=1.
\]

## Adams consequence

Unweighted first-order history loading has no strict completion margin along an
unbounded Adams scale ray. This remains true when each finite grade is strict,
prime fibers are diagonal, scale transport is unitary, and the seed is rapidly
decaying.

A strict margin requires at least one source-native repair:

1. higher-order energy;
2. a damped incidence coefficient;
3. a bounded physical scale or separately typed Adams-end object.

## Weighted criterion

If grade \(r\) carries scalar weight \(\rho(r)\), then

\[
R_r(f)
=
\frac{|\rho(r)|^2r^2\|\mathsf Df\|_2^2}
{\|f\|_2^2+r^2\|\mathsf Df\|_2^2}.
\]

A strict high-grade margin follows when
\(\limsup_{r\to\infty}|\rho(r)|<1\). If
\(|\rho(r)|\to1\), saturation remains.

## Verdict

The Adams-native no-go is

\[
\text{nonconstant unbounded dilation orbit}
+
\text{first-order graph}
\Longrightarrow
\text{zero strict unweighted margin}.
\]

The decisive source calculation is therefore the placement and covariance of
the Euler half-density weight before completion.
