# Interval certificate contract for the unchanged Evans Hilbert residual

The current checker evaluates

$$
H(t)=\int_0^\infty
|\xi(\tfrac12+ix)|^2
\frac{2t}{x^2-t^2}\,dx
$$

at the first zero ordinate. High-precision values stabilize near

$$
H(t_1)=-0.1508512190587392007,
$$

but the installed environment has no Arb, python-flint, Sage, or other interval backend. This value is therefore not yet a certificate.

A rigorous checker must produce the following objects.

## 1. Root enclosure

An interval `T=[t_-,t_+]` containing exactly one zero of `xi(1/2+it)`, certified by an argument-principle or validated Hardy-Z sign change plus zero count. A decimal returned by `zetazero` is insufficient.

## 2. Removable-singularity enclosure

Near `x in T`, direct interval evaluation of

$$
|\xi(x)|^2/(x^2-t^2)
$$

causes division by an interval containing zero. Factor the certified simple zero:

$$
\xi(\tfrac12+ix)=(x-t)\,g_t(x),
$$

where

$$
g_t(x)=\int_0^1
\partial_x\xi\bigl(\tfrac12+i(t+s(x-t))\bigr)\,ds.
$$

Then the integrand becomes

$$
2t\,\frac{x-t}{x+t}|g_t(x)|^2,
$$

which is interval-regular across `x=t`.

## 3. Finite validated quadrature

Partition `[0,X]` so that `T` lies in one dedicated regularized cell. Use ball quadrature for `xi`, its derivative, and each integral cell. The output must be one interval `I_X` enclosing the complete finite integral uniformly for `t in T`.

## 4. Analytic tail bound

Provide an explicit bound

$$
|\xi(\tfrac12+ix)|
\le C(1+x)^A e^{-\pi x/4}
$$

for `x>=X`, using Stirling with remainder and an explicit critical-line zeta bound. Then

$$
\left|\int_X^\infty
|\xi|^2\frac{2t}{x^2-t^2}\,dx\right|
\le
\int_X^\infty
C^2(1+x)^{2A}e^{-\pi x/2}
\frac{2t_+}{x^2-t_+^2}\,dx
=:E_X.
$$

## Acceptance criterion

The unchanged-Evans membership is rigorously rejected if

$$
\sup I_X+E_X<0.
$$

A comfortable target is an enclosure contained in `[-0.151,-0.150]`, leaving orders of magnitude more margin than required for tail and quadrature errors.

Status: certificate algorithm fixed; execution blocked only by the absence of a validated complex-ball backend and explicit zeta-tail implementation.
