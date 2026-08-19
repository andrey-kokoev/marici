# 891 — The Canonical Five-Point Parke–Taylor Period Has a Source-Normalized Hypergeometric Form

## Frozen source object

Use the source five-point loading on the canonical bounded chamber

\[
0<z_2<z_3<1,
\qquad
(z_1,z_4,z_5)=(0,1,\infty),
\]

with

\[
u=z_2^a(1-z_2)^b z_3^c(1-z_3)^d(z_3-z_2)^e
\]

and the source-labelled Parke–Taylor cocycle

\[
\operatorname{PT}(12345)
=
\frac{dz_2\wedge dz_3}
{(-z_2)(z_2-z_3)(z_3-1)}.
\]

No analytic continuation, chamber transition, or circuit coefficient is inserted.

## Exact reduction

Set

\[
z_3=y,
\qquad
z_2=xy,
\qquad
0<x,y<1.
\]

The ordered source orientation gives

\[
\operatorname{PT}(12345)
=-rac{dx\wedge dy}{xy(1-x)(1-y)}.
\]

Therefore

\[
Z_{12345}
=-
\int_0^1\!\int_0^1
x^{a-1}(1-x)^{e-1}
y^{a+c+e-1}(1-y)^{d-1}
(1-xy)^b,dx,dy,
\]

and Euler reduction gives

\[
\boxed{
Z_{12345}
=-B(a,e)B(a+c+e,d)
{}_3F_2\!\left(
\begin{matrix}
-b,a,a+c+e\\
a+e,a+c+e+d
\end{matrix};1
\right).
}
\]

This normalization, including its minus sign, is fixed before any circuit test.

## Independent finite-\(\alpha'\) calibration

Choose the convergent nonintegral loading

\[
(a,b,c,d,e)=\left(2,\frac12,1,2,2\right).
\]

Then

\[
B(2,2)B(5,2)=\frac1{180},
\]

and the period is

\[
-\frac1{180}
{}_3F_2\!\left(
\begin{matrix}-\frac12,2,5\\4,7\end{matrix};1
\right).
\]

The durable checker evaluates this expression by its hypergeometric recurrence and independently evaluates the original two-dimensional Euler integral by nested midpoint quadrature with Richardson extrapolation. The two values agree within the predeclared numerical tolerance recorded in

`research/benincasa/string-five-point-finite-pt-period.json`.

## Narrow result

The canonical five-point Parke–Taylor period now has a source-normalized finite-\(\alpha'\) realization whose Euler-integral and hypergeometric descriptions agree independently.

This does **not** yet establish the finite-\(\alpha'\) circuit identity of Entry 888. In particular, it does not perform analytic continuation to the other source chambers or fix their half-monodromy phases.

No new carrier structure appears: the finite string correction is carried by the Koba–Nielsen coefficient object over the same bounded incidence chamber.

## Next falsifier

Analytically continue this fixed period normalization to one circuit-adjacent chamber, retain the source branch phases, and test whether the continued column obeys Entry 888's exact sine-coefficient circuit. A mismatch cannot be repaired by changing the normalization established here.
