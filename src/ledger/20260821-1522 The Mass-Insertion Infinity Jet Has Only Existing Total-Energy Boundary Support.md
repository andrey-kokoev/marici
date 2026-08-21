---
author: marici.Nima
---

# 1522 — The Mass-Insertion Infinity Jet Has Only Existing Total-Energy Boundary Support

## Status

Exact support audit through (C^{(2)}) for the generic bivalent
mass-insertion carrier.

## Result

For

\[
I(X)=\sum_{k\ge0}C^{(k)}X^{-3-k},
\]

the reduced denominators of the first three coefficients differ only by
nonzero rational units. Their common pole divisor is

\[
\boxed{
\Delta_{J_\infty^2}
=(x_1+y_1)(x_2+y_2).
}
\]

Thus the checked infinity-jet block becomes singular only on

\[
x_1+y_1=0
\qquad\text{or}\qquad
x_2+y_2=0,
\]

the two pre-existing neighboring total-energy facets.

## Consequence for the mass diagonal

The physical specialization (y_2=y_1) neither annihilates nor creates a
factor of this divisor generically. It therefore introduces no new infinity
boundary and no independent mass-supported jet coefficient. This realizes
the regular-base-change theorem of Entry 1521 in the first nontrivial packet.

The statement is a support result through (C^{(2)}), not yet an all-grade
factorization theorem for every graph.

## Meaning

At this depth, the supercritical infinity data is new coefficient thickness
on old carrier support. It is not evidence for a new carrier divisor. A new
infinity-supported stratum would require an independently derived
specialization that kills the leading denominator coefficient rather than an
ordinary equal-edge mass diagonal.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1521 (regular-specialization theorem);
- allocator claim `seqclaim-5997f8418966e50cfe543f04`.
