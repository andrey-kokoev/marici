---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 767 — The Complete Hom Divisors Form a Typed Cyclic Correspondence

## Exact pullback audit

For the cyclic normalized base map

\[
U=\frac{2u}{u-v},\qquad
V=\frac{2(2-v)}{u-v},
\qquad d=u-v,
\]

each of Entry 762's twelve target-local factors was pulled back exactly.
After clearing the forced power of (d), the numerator was divided by the
complete fixed-(G_{12}) factor family.

Five finite factors map inside the existing list:

\[
u\mapsto u,qquad
v\mapsto v-2,qquad
v-u\mapsto y,
\]

\[
u-2\mapsto v,qquad
v-2\mapsto u-2,
\]

up to units and powers of the normalization denominator.  The target-local
factor (y) pulls back to a unit divided by (d), so its divisor is carried
to the chart boundary rather than to a finite fixed-chart divisor.

## Fixed-polynomial closure fails

The remaining six target-local factors acquire nonunit residual
polynomials not present in the fixed twelve-factor list:

\[
1-y,quad 1+y,quad y-u^2,quad y+u^2,quad P_6,quad u^2+1.
\]

Consequently,

\[
\boxed{
\rho^*\mathcal D_{12}^{\rm fixed}
\not\subseteq
\mathcal D_{12}^{\rm fixed}+\langle d\rangle.
}

This is not a defect in Entry 766.  It proves that its chartwise transported
divisor lattice is necessary: the same twelve abstract labels return after
three charts, but their normalized polynomial representatives are not a
single invariant list on the (G_{12}) affine chart.

## Consequence for stabilization

A local pole-order stabilization proof performed only on the twelve
fixed-(G_{12}) polynomials is not occurrence-global.  It must either:

1. be transported chart by chart through Entry 766's correspondence; or
2. be repeated on the cyclic saturation containing the six residual
   representatives and the normalization boundary.

No new physical carrier divisor is inferred.  These are coefficient-gauge
and chart-boundary representatives produced by occurrence transport.

The sheared resonant grades

\[
15,quad17,quad28,quad30
\]

remain unchanged in the recursively transported filtration.  They should
not be attached to an invariant fixed-polynomial denominator list.

## Evidence

- `research/benincasa/check_cyclic_hom_divisor_orbits.py`;
- `research/benincasa/cyclic-hom-divisor-orbits.json`;
- Entries 762, 765, and 766;
- allocator claim `seqclaim-9c4df307facb69a73540ee0d`.
- epistemic event
  `ev-000000000381-f76d35bf-ac58-498e-bc27-4b8b12d9f488`.

## Next falsifier

Construct the finite cyclic saturation of the twelve divisor labels over all
three charts, including the normalization boundary.  Determine its divisor
orbits and test local indicial pole stabilization on one representative of
each orbit.  If the saturation does not close after three labelled charts,
the present transported pole filtration is incomplete.
