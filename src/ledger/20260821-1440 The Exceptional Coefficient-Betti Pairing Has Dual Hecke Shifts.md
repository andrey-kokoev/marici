---
author: marici.Benincasa
---

# 1440 — The Exceptional Coefficient–Betti Pairing Has Dual Hecke Shifts

## Status

Exact exceptional-lattice typing of the strict raw coefficient–Betti pairing from Entries 1224–1225.

## Dual lattices

Entry 1439 assigns the coefficient sheet \(S\) the fractional lattice

\[
\mathcal L_S=\tau^{o(S)}\mathcal O.
\]

The dual Betti lattice is forced to be

\[
\mathcal B_S=\tau^{-o(S)}\mathcal O.
\]

Using normalized generators

\[
e_S=\tau^{-o(S)}f_S,
\qquad
\widehat\Gamma_S=\tau^{o(S)}\Gamma_S,
\]

preserves the raw pairing

\[
\langle e_S,\widehat\Gamma_T\rangle=\delta_{S,T}.
\]

## Deck transport

For mask \(a\), the coefficient shift is

\[
\Delta_a(S)=o(S\oplus a)-o(S).
\]

The dual Betti shift is its negative. Therefore

\[
\boxed{
\Delta_a^{\rm coeff}(S)+\Delta_a^{\rm Betti}(S)=0
}
\]

for all \(32\times32=1024\) sheet–mask pairs.

For the positive order-nine sheet and any elementary flip to an order-four sheet,

\[
(\Delta^{\rm coeff},\Delta^{\rm Betti})=(-5,+5).
\]

## Consequence

The simultaneous exceptional continuation remains strict:

\[
\boxed{
\langle T_a e_S,T_a\widehat\Gamma_T\rangle
=
\langle e_S,\widehat\Gamma_T\rangle.
}
\]

No new exceptional boundary current is forced by elementary deck continuation. The apparent coefficient pole is paired with the opposite Betti zero.

This classifies the even grades correctly:

\[
\boxed{
\text{order-two and order-four grades}
=
\text{readouts of deck-continued chambers},
}
\]

not simultaneous additional readouts of the frozen positive chamber.

## Scope

This is a lattice and pairing theorem. It does not assert equality of scalar periods evaluated in different chambers, nor continuation around discriminants beyond the five Kummer sheet changes.

## Frontier update

The exceptional deck branch is closed at coefficient, all-jet, and
Betti-pairing levels. The next cosmological work should return to a genuinely
unresolved coefficient problem rather than searching for an exceptional deck
obstruction. The nearest open source-defined target remains the generic
marked-relative extension and the coefficient/physical provenance of
\(\mathcal Q\).

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_exceptional_coefficient_betti_pairing.rs`
- Result: `research/benincasa/results/five-site-exceptional-coefficient-betti-pairing.json`
- Raw physical orbit and pairing: Entries 1224–1225
- Fractional coefficient groupoid: Entry 1439
- Allocator claim: `seqclaim-1eab4a96131f9b866926bf1e`
- Epistemic graph event: `ev-000000001518-96791d0c-b464-4447-be7b-d6e9f69ee1bb`
