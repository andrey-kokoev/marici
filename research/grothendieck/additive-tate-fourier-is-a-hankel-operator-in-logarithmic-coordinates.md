# Additive Tate Fourier Is a Hankel Operator in Logarithmic Coordinates

## Unitary logarithmic pullback

On the positive real ray define

\[
(Uf)(q)=e^{q/2}f(e^q).
\]

This identifies additive (L^2(dx)\) on the ray with (L^2(dq)\). For a
logarithmic state (g\), the inverse is

\[
f(x)=x^{-1/2}g(\log x).
\]

Choose either the even or odd additive extension of (f\) to the real line.

## Exact conjugated kernels

With additive Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx,
\]

the even extension gives

\[
(K_+g)(r)
=2\int_{\mathbb R}
e^{(r+q)/2}\cos(2\pi e^{r+q})g(q)\,dq.
\]

The odd extension gives

\[
(K_-g)(r)
=-2i\int_{\mathbb R}
e^{(r+q)/2}\sin(2\pi e^{r+q})g(q)\,dq.
\]

Thus logarithmic Tate Fourier is a Hankel operator: its kernel depends on the
sum (r+q\). Ordinary Fourier transform in (q\) is a convolution operator
whose kernel depends on the difference. The two transforms are structurally
distinct before any asymptotic or numerical test.

## Exact Hermite falsifier

Take

\[
g(q)=h_1(q)=q e^{-\pi q^2}.
\]

For the even additive lift, as (r\to-\infty\), dominated expansion of the
cosine gives

\[
(K_+h_1)(r)
=2e^{r/2}\int_{\mathbb R}e^{q/2}h_1(q)\,dq
+O(e^{5r/2}).
\]

The leading coefficient is nonzero:

\[
\int_{\mathbb R}q e^{-\pi q^2+q/2}\,dq
=\frac{1}{4\pi}e^{1/(16\pi)}.
\]

Hence

\[
(K_+h_1)(r)
=\frac{1}{2\pi}e^{1/(16\pi)}e^{r/2}
+O(e^{5r/2}).
\]

But (h_1(r)=r e^{-\pi r^2}\) decays super-exponentially as
(r\to-\infty\). Therefore (K_+h_1\) is not a scalar multiple of (h_1\).
The Hermite phase (-i\) cannot be the even Tate sheet phase.

The odd additive lift is a different source port, governed by (K_-\). Its
existence does not restore the prior inference: reciprocal oddness in (q\)
does not choose additive parity in (x\).

## Consequence

The actual sheet operator has now been derived rather than named. It couples
the two logarithmic ends through a sum kernel and naturally implements
reciprocal reflection. Endpoint pointing and sheet transport are therefore
two distinct rungs:

1. evaluation separates translations in the Mellin chart;
2. the Hankel operator transports that chart through additive Tate Fourier.

Any orientation law must be extracted from the spectrum, quadratic form, or
boundary current of (K_+\) and (K_-\), not from ordinary Hermite phases.
