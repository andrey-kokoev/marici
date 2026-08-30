---
author: marici.Nima
---

# 1537 — Mean-Mass and Unequal-Mass Jet Transport Is Formally Flat

## Status

Exact formal-connection calculation on the double-Gysin infinity-jet
generating section.

## Coordinates and section

Write

\[
a=4\bar y^2,\qquad
\tau=(y_1-y_2)^2,\qquad
z=X^{-1}.
\]

The normalized corner section is

\[
F(a,\tau;z)
=\frac{2}{(1-az^2)(1-\tau z^2)}.
\]

Its parameter derivatives close on the same line:

\[
\boxed{
\partial_aF
=\frac{z^2}{1-az^2}F,
\qquad
\partial_\tau F
=\frac{z^2}{1-\tau z^2}F.
}
\]

## Mixed curvature

Define the scalar formal connection coefficients

\[
\mathcal A_a=\frac{z^2}{1-az^2},
\qquad
\mathcal A_\tau=\frac{z^2}{1-\tau z^2}.
\]

They have no cross-dependence and commute. Therefore

\[
\boxed{
\partial_a\mathcal A_\tau
-\partial_\tau\mathcal A_a
+[\mathcal A_a,\mathcal A_\tau]
=0.
}
\]

Equivalently,

\[
\boxed{\partial_a\partial_\tau F
=\partial_\tau\partial_aF.}
\]

The exact checker verifies both the first-order equations and the mixed
identity.

## Physical fiber

At \(\tau=0\),

\[
\mathcal A_\tau=z^2,
\]

recovering Entry 1534's even-grade shift. Mean-mass transport remains

\[
\mathcal A_a=\frac{z^2}{1-az^2},
\]

which generates the one-channel recurrence along the physical locus.

## Meaning

The source-derived coefficient family has no mixed coherence defect between
tangential mean-mass transport and invariant transverse transport. Its formal
two-parameter totalization is already flat; no additional homotopy cell is
required at this level.

This is a formal coefficient-connection statement. It is not yet an
identification with a physical Gauss–Manin connection on relative cycles.
That stronger claim would require a source pairing or comparison morphism.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1534–1535;
- allocator claim seqclaim-aec0bb2819733f798caf5211.
