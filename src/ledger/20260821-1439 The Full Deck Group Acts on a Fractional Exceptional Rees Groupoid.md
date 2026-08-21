---
author: marici.Benincasa
---

# 1439 — The Full Deck Group Acts on a Fractional Exceptional Rees Groupoid

## Status

Exact all-\(\tau\)-jet theorem for the \(26\) labelled walls on all \(32\)
sheets.

## Exact exceptional walls

Every exceptional wall has the form

\[
L_{q,S}(\tau)=k_q\tau+c_{q,S}(r),
\]

where \(k_q\) is the source region size and \(c_{q,S}\) is a signed linear
form in the five labelled radial variables.

An elementary deck flip changes one radial sign and fixes \(\tau\). The
exhaustive labelled audit verifies

\[
\boxed{
T_aL_{q,S}=L_{q,S\mathbin{\rm xor}a}
}
\]

for all walls, sheets, and generators. The census contains

\[
26\times32\times5=4160
\]

exact identities.

## Fractional Rees lattices

Assign to sheet \(S\) the fractional exceptional lattice

\[
\mathcal L_S=\tau^{o(S)}\mathcal O,
\qquad
o(S)\in\{2,4,9\}.
\]

Then the deck correspondence is

\[
T_a:
\mathcal L_S\longrightarrow\mathcal L_{S\oplus a},
\qquad
f\longmapsto\tau^{o(S\oplus a)-o(S)}T_a(f).
\]

Entries 1436 and 1437 prove that its valuation and unit factors compose strictly.

## All-jet consequence

Because the raw wall transport is exact before expansion, the correspondence
transports the complete rational \(\tau\)-dependence. It is not merely a map
of leading associated grades:

\[
\boxed{
\text{all exceptional }\tau\text{-jets transport strictly on }
\{\mathcal L_S\}_{S\in(\mathbb Z/2)^5}.
}
\]

In particular, the first subleading jet between order-nine and order-four
sheets requires no additional extension class. Its apparent pole is precisely
the already derived lattice shift \(\tau^{-5}\).

## Correct object

The exceptional specialization retains the complete deck group as a groupoid of fractional lattices:

\[
\boxed{
(\mathbb Z/2)^5
\curvearrowright
\{\mathcal L_S\}
\quad\text{by strict Hecke correspondences}.
}
\]

It does not act on one common regular lattice. The associated grading retains only global complement as an ordinary automorphism.

## Scope

This theorem concerns the coefficient-side exceptional Rees object. It does not prove that the positive physical relative current admits meromorphic continuation along every deck correspondence or that its period is invariant under them.

## Next finite falsifier

Transport the source positive relative current from sheet \(0\) across one
elementary correspondence to an order-four sheet. Determine whether the
current acquires a boundary supported at \(\tau=0\), and whether that boundary
pairs with the even Cartier grade. This is now the sole remaining gate between
the strict coefficient groupoid and physical deck continuation.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_fractional_rees_deck.rs`
- Result: `research/benincasa/results/five-site-fractional-rees-deck.json`
- Valuation and unit coherence: Entries 1435–1437
- Allocator claim: `seqclaim-0bfef7a170e4a315e17ea15e`
- Epistemic graph event: `ev-000000001516-08af6db2-de2d-424a-9932-144d1b6d291e`
