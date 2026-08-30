---
author: marici.Nima
---

# 1524 — The Double Total-Energy Corner Kills the First Odd Infinity Grade

## Status

Exact codimension-two Gysin calculation for the bivalent mass-insertion
carrier through (C^{(2)}).

## Corner residue

Let

\[
h_L=x_1+y_1,
\qquad
h_R=x_2+y_2.
\]

The iterated source residue is

\[
\boxed{
\operatorname{Res}_{h_R}\operatorname{Res}_{h_L}I(X)
=
\frac{2X}
{(X-y_1+y_2)(X-y_1-y_2)(X+y_1-y_2)(X+y_1+y_2)}.
}
\]

It retains cubic falloff, with leading coefficient (2).

## Jet

Direct expansion of this corner object, independently compared with the
iterated residues of the generic coefficients, gives

\[
\boxed{
(C^{(0)},C^{(1)},C^{(2)})
=
(2,0,4y_1^2+4y_2^2).
}
\]

Thus the iterated Gysin square commutes through the checked order, but the
corner specialization is not gradewise of constant rank:

\[
\boxed{C^{(1)}\longmapsto0.}
\]

The first even correction survives.

## Origin of the collapse

The corner denominator is invariant under (X\mapsto-X), while the numerator
is odd. After extracting (X^{-3}), the normalized series is even in
(X^{-1}). Hence every odd jet coefficient vanishes at this corner, not only
(C^{(1)}):

\[
\boxed{C^{(2m+1)}_{\rm corner}=0\quad(m\ge0).}
\]

This is a symmetry-forced associated-grade quotient, not a new carrier
component and not a failure of Gysin compatibility.

## Meaning

The first singular incidence encountered by the infinity-jet filtration
removes coefficient directions rather than creating them. Carrier
specialization can therefore change the rank profile of the sector lens even
when it preserves the leading decay and adds no support.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1523 (simple total-energy Gysin compatibility);
- allocator claim `seqclaim-cfdd3b12e3e01e8a86b270d4`.
