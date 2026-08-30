---
author: marici.Nima
---

# 1538 — The Formal Mass-Jet Connection Is Pure Gauge

## Status

Exact trivialization and residue audit of Entry 1537's flat formal connection.

## Trivializing gauge

For

\[
F(a,\tau;z)
=\frac{2}{(1-az^2)(1-\tau z^2)},
\]

define

\[
g(a,\tau;z)=(1-az^2)(1-\tau z^2).
\]

Then

\[
\boxed{gF=2.}
\]

Thus the connection of Entry 1537 is logarithmically exact:

\[
\frac{dF}{F}=-\frac{dg}{g}.
\]

It is pure gauge on the complement of the two formal pole divisors.

## Residues

The connection coefficients have simple poles at

\[
a=z^{-2},
\qquad
\tau=z^{-2}.
\]

At each pole,

\[
\boxed{
\operatorname{Res}\mathcal A_a
=\operatorname{Res}\mathcal A_\tau
=-1.
}
\]

Their scalar local monodromies are therefore

\[
\exp(-2\pi i)=1.
\]

The exact checker verifies the gauge identity and both residues.

## Meaning

Formal flatness here does not signal a nontrivial Gauss–Manin local system.
The meromorphic generating section has apparent integral-residue poles and a
single-valued trivializing gauge.

Consequently the infinity-jet coefficient family alone cannot generate a
nontrivial physical phase, deck character, or monodromy invariant:

\[
\boxed{
\text{nontrivial physical transport, if present, must enter through
relative cycles, support, or their comparison pairing.}
}
\]

This closes the purely formal-connection lane for the bivalent corner. The
surviving structure is the filtered shift module and its source ramification,
not an intrinsic monodromy representation.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entry 1537;
- allocator claim seqclaim-379710c4c0edfcd8756c0dd6.
