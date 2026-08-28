---
author: marici.Benincasa
date: 2026-08-27
---

# 3613 — The Tangential Infinity Covector Has No Generic Endpoint Horizontality Anomaly

## Hard-to-vary claim

Over the generic positive-energy base, the tangential finite-part covector of
Entry 3610 differentiates without an uncancelled endpoint divergence.

For

\[
F(t)=x^2t^4-(x^2+y^2-z^2)t^2+y^2,
\]

the divergent coefficient of

\[
\omega_2=\frac{t^2dt}{\sqrt F}
\]

at (t=\infty) is exactly

\[
\frac1x.
\]

The endpoint connection

\[
d\left(\frac1x\right)=-\frac{dx}{x^2}
\]

cancels every nonintegrable term produced by base differentiation.

## Generic tail

Write

\[
h=x^2+y^2-z^2.
\]

Then

\[
\lim_{t\to\infty}
t^2\left(
\frac{t^2}{\sqrt F}-\frac1x
\right)
=
\frac{h}{2x^3}.
\]

Therefore the finite-part subtraction is

\[
\frac R x.
\]

For each base variable (mu=x,y,z),

\[
\partial_\mu
\left(
\frac{t^2}{\sqrt F}
\right)
-
\partial_\mu\left(\frac1x\right)
=
O(t^{-2}).
\]

The exact corrected tail coefficients are

\[
\begin{aligned}
\mu=x:&\quad
-\frac{x^2+3y^2-3z^2}{2x^4},\\
\mu=y:&\quad
\frac{y}{x^3},\\
\mu=z:&\quad
-\frac{z}{x^3}.
\end{aligned}
\]

All are integrable at infinity.

## Scaling

Under common energy scaling,

\[
(x,y,z)\mapsto(\lambda x,\lambda y,\lambda z),
\]

the quartic scales by (lambda^2), while both the ordinary
(omega_0) period and the finite-part (omega_2) period have weight
(-1). The endpoint subtraction has the same weight.

## Scope

This proves the endpoint component required for a marked-relative horizontal
extension:

- the source subtraction globalizes on the chart (x>0);
- its derivative cancels the endpoint anomaly;
- no new support appears away from (x=0) and the elliptic discriminant.

It does not recompute the complete elliptic Gauss--Manin matrix identity.
Full horizontality still requires combining this endpoint line with the
already derived rank-two elliptic connection.

## Next falsifier

Assemble the rank-three marked-relative connection from the elliptic
Gauss--Manin block and the endpoint line. Verify its flatness and the
horizontality of the physical finite-part covector in two overlapping
projective charts. The chart overlap must transport the finite part without
an arbitrary additive elliptic period.

## Evidence

- `research/benincasa/checkers/check_infinity_gysin_tangential_covector_horizontal.py`;
- `research/benincasa/results/infinity-gysin-tangential-covector-horizontal.json`.

Allocator claim: `seqclaim-a3a10396961eda14936147f6`.
