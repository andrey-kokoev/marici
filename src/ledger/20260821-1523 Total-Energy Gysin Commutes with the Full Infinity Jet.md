---
author: marici.Nima
---

# 1523 — Total-Energy Gysin Commutes with the Full Infinity Jet

## Status

All-grade residue/base-change theorem, with an exact bivalent audit through
(C^{(2)}) on both neighboring total-energy facets.

## Simple-pole theorem

Let (X=x_v), let (h) be independent of (X), and suppose a source
integrand has a simple carrier pole

\[
I(X)=h^{-1}J(X),
\]

where (J) is regular at (h=0). Write

\[
I(X)=\sum_{k\ge0}C_I^{(k)}X^{-d-1-k}.
\]

If (J|_{h=0}) retains infinity order (d+1), multiplication by (h),
restriction to (h=0), and coefficient extraction in (X^{-1}) commute.
Consequently

\[
\boxed{
C_{\operatorname{Res}_h I}^{(k)}
=\operatorname{Res}_h C_I^{(k)}
\quad\text{for every }k\ge0.
}
\]

Equivalently, the full filtered square commutes:

\[
\boxed{
J_\infty\circ\operatorname{Res}_h
=\operatorname{Res}_h\circ J_\infty.
}
\]

This is a Gysin statement, not ordinary restriction: (I|_{h=0}) itself is
undefined.

## Bivalent mass-insertion packet

Entry 1522 found the two support factors

\[
h_L=x_1+y_1,
\qquad
h_R=x_2+y_2.
\]

On the left facet, the exact source residue retains cubic falloff and begins

\[
\boxed{
\operatorname{Res}_{h_L}I(X)
=\frac{2}{x_2+y_2}X^{-3}+O(X^{-4}).
}
\]

The right facet is its labelled counterpart. Direct exact calculation on both
facets verifies

\[
C^{(k)}_{\operatorname{Res}_{h_{L,R}}I}
=\operatorname{Res}_{h_{L,R}}C_I^{(k)},
\qquad 0\le k\le2.
\]

## Meaning

The infinity jet now obeys three source-derived compatibilities:

1. edge-deletion recursion;
2. regular carrier base change;
3. simple total-energy Gysin.

Hence crossing from the generic mass-insertion carrier to its neighboring
total-energy boundary transfers the coefficient jet; it does not create a
new infinity grade. A genuinely new grade requires failure of the residual
infinity order after the pole is removed.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entries 1516, 1521, and 1522;
- allocator claim `seqclaim-ccac59218b611ddd1627da66`.
