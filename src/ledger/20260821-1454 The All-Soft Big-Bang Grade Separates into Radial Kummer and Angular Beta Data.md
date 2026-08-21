---
author: marici.Benincasa
---

# 1454 — The All-Soft Big-Bang Grade Separates into Radial Kummer and Angular Beta Data

## Status

Exact leading homogeneous grade at Entry 1453's remaining soft corner. This
does not yet prove the full filtered all-soft totalization.

## Frozen corner

At

\[
y=X_1=X_2=0,
\]

the source positive coordinates are

\[
u=x_1\ge0,
\qquad
v=x_2\ge0.
\]

The two singleton denominators and total-energy denominator become

\[
q_1=u,
\qquad
q_2=v,
\qquad
q_T=u+v.
\]

With endpoint Kummer exponents \(\alpha_1,\alpha_2\), the leading source form
is

\[
\frac{u^{\alpha_1}v^{\alpha_2}}
{uv(u+v)}du\,dv.
\]

## Forced radial blowup

Use the positive simplex coordinates

\[
u=rt,
\qquad
v=r(1-t),
\qquad
r\ge0,
\quad
0\le t\le1.
\]

Since

\[
du\,dv=r\,dr\,dt,
\]

the form factors exactly:

\[
\boxed{
\frac{u^{\alpha_1}v^{\alpha_2}}
{uv(u+v)}du\,dv
=
r^{\alpha_1+\alpha_2-2}dr
\;t^{\alpha_1-1}(1-t)^{\alpha_2-1}dt.
}
\]

Equivalently, the radial factor is

\[
\frac{dr}{r}\,r^{\alpha_1+\alpha_2-1},
\]

and the angular positive-chain period is

\[
\int_0^1
t^{\alpha_1-1}(1-t)^{\alpha_2-1}dt
=
B(\alpha_1,\alpha_2)
=
\frac{\Gamma(\alpha_1)\Gamma(\alpha_2)}
{\Gamma(\alpha_1+\alpha_2)}.
\]

## Geometric typing

The radial coordinate \(r\) is the existing simultaneous-soft normal. The
exceptional angular interval has inherited labelled endpoints:

\[
t=0\leftrightarrow u=0,
\qquad
t=1\leftrightarrow v=0.
\]

Thus the leading coefficient object is

\[
\boxed{
\mathcal K_{r^{\alpha_1+\alpha_2-1}}
\otimes
H^1_{\rm rel}
\left(
\mathbb P^1_t,\{0,1,\infty\};
\mathcal K_{t^{\alpha_1-1}(1-t)^{\alpha_2-1}}
\right).
}
\]

Its physical normalization is the source beta period. No angular section or
normalization has been fitted.

## Classification

\[
\boxed{
\text{existing radial soft carrier}
+
\text{two labelled endpoint occurrences}
+
\text{sector-specific beta/Kummer coefficient}.
}
\]

There is no new carrier generator at the leading all-soft grade. The apparent
coupling of the two singleton classes is the canonical beta-function pairing
on the exceptional simplex.

## Scope boundary

The radial integral is scaleless at the strict homogeneous grade and requires
the source analytic regulator or the next nonhomogeneous terms. Therefore this
entry determines the carrier and coefficient type, but not a finite global
number.

Entry 1455 subsequently proves that no nonhomogeneous radial order exists for
the complete two-site primitive; the source family is exactly conical.

## Next falsifier

Superseded by Entry 1455's exact homogeneity test.

## Durable provenance

- Entries 1451 and 1453;
- allocator claim `seqclaim-89474ffd9a6927a8e8470d40`.
- epistemic event `ev-000000001548-45cf5d63-1621-44dc-8e16-10d5f474a05e`.
