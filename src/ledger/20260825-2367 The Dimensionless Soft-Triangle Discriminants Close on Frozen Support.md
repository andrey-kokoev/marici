---
author: marici.Benincasa
date: 2026-08-25
---

# 2367 — The Dimensionless Soft-Triangle Discriminants Close on Frozen Support

## Test

After Entry 2366 removes the common scale, the coefficient kernel is

\[
k(t,\kappa,\xi)
=t^4-(10+8\kappa\xi)t^2
+16\kappa^2+40\kappa\xi+16\xi^2+9.
\]

The finite falsifier is a projection discriminant outside the frozen
endpoint, signed-face, and coordinate-boundary arrangement.

Sequence claim: seqclaim-816ee1550ce6fe58e42b20c4.

## Exact projection discriminants

Eliminating \(\xi\) gives

\[
\boxed{
\operatorname{Disc}_{\xi}k
=64(\kappa^2-1)(t^2-1)(t^2-9).
}
\]

Eliminating \(\kappa\) gives the symmetric identity

\[
\boxed{
\operatorname{Disc}_{\kappa}k
=64(\xi^2-1)(t^2-1)(t^2-9).
}
\]

Finally,

\[
\boxed{
\operatorname{Disc}_{t}k
=65536(\kappa^2-1)^2(\xi^2-1)^2
\,k(0,\kappa,\xi).
}
\]

The last displayed product is literal multiplication by
\(k(0,\kappa,\xi)\).

## Source classification

Every factor has frozen provenance:

- \(\kappa=\pm1\): endpoints of the external momentum-triangle face;
- \(\xi=\pm1\): endpoints of the collapsing loop triangle;
- \(t=\pm1\): signed \(a/p\) face branches, with \(t=1\) the
  \(q_{\mathfrak g_2}/q_{\mathfrak g_{31}}\) collision;
- \(t=\pm3\): signed \(a/p\) face branches, with \(t=-3\) the
  \(q_{\mathfrak g_3}\) section;
- \(k(0,\kappa,\xi)=0\): collision of a branch point with the existing
  coordinate boundary \(a=0\).

Entry 2368 subsequently checks the full critical ideal and shows that this
last factor is not a singular divisor of the total double cover. It is
critical only for the chosen \(t\)-projection.

Thus no projection produces an undeclared divisor.

## Result

\[
\boxed{
\text{all three projection discriminants close on the frozen
Cayley--Menger/marked arrangement.}
}
\]

This is stronger than the single \(a^2\)-discriminant test of Entry 2364:
the dimensionless kernel remains support-compatible under every coordinate
projection tested.

## Scope

Projection discriminants do not determine the complete relative
Gauss--Manin extension. In particular, this result does not exclude a
higher-codimension costalk, nonsplit extension, or integral defect supported
on intersections of the listed divisors.

## Durable verification

- research/benincasa/check_soft_triangle_dimensionless_discriminants.py;
- research/benincasa/soft-triangle-dimensionless-discriminants.json;
- exact symbolic discriminant identities;
- epistemic event
  ev-000000003242-c5c0b8f3-9bff-43f1-af6a-6f5a918dcd68.

## Next falsifier

Build the logarithmic relative complex on the endpoint cover and compute its
costalks at:

\[
(\kappa,\xi)=(\pm1,\pm1),
\]

\[
t=\pm1,\pm3,
\]

and

\[
t=0,\qquad k(0,\kappa,\xi)=0.
\]

Any residual cone outside the existing soft, triangle, signed-face, and
coordinate-boundary maps would be the first coefficient-level failure.
