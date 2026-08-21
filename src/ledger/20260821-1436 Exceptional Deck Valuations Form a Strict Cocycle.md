---
author: marici.Benincasa
---

# 1436 — Exceptional Deck Valuations Form a Strict Cocycle

## Status

Complete valuation-level composition theorem for all \(32\) sheets and all
pairs of deck masks.

## Shift function

For sheet \(S\) and deck mask \(a\), define

\[
\Delta_a(S)=o(S\mathbin{\rm xor}a)-o(S),
\]

where \(o(S)\in\{2,4,9\}\) is the exceptional Cartier order.

Entry 1435 shows that \(\tau^{\Delta_a(S)}\) is the lattice modification
carried by the deck correspondence.

## Exact composition identities

Across all \(32^3=32768\) triples \((S,a,b)\),

\[
\boxed{
\Delta_a(S)+\Delta_b(S\mathbin{\rm xor}a)
=
\Delta_{a\mathbin{\rm xor}b}(S).
}
\]

The two orders of composition also agree:

\[
\boxed{
\Delta_a(S)+\Delta_b(S\mathbin{\rm xor}a)
=
\Delta_b(S)+\Delta_a(S\mathbin{\rm xor}b).
}
\]

For every elementary generator \(i\),

\[
\Delta_i(S)+\Delta_i(S\mathbin{\rm xor}2^i)=0.
\]

## Consequence

The meromorphic powers required by Entry 1435 compose strictly. No additional exceptional coherence cell is required by the valuation data:

\[
\boxed{
\tau^{\Delta_b(S\oplus a)}\tau^{\Delta_a(S)}
=
\tau^{\Delta_{a\oplus b}(S)}.
}
\]

Thus the full deck group survives exceptional specialization as a strict group of valuation-shifted correspondences, while only the subgroup

\[
\{0,31\}
\]

acts without lattice modification on the associated grading.

## Remaining coherence gate

This theorem controls only powers of the exceptional parameter. It does not yet control the leading units or orientation signs of the transported coefficient forms. A nontrivial unit-valued two-cocycle could still require a coherence cell even though the valuation cocycle is exact.

## Scope

No Hecke lattice is adjoined, and no physical-current pairing is asserted. The result is the complete exponent-level acceptance test for such a construction.

## Next finite falsifier

Retain the source leading coefficients \(c_S\), transport them under two
elementary flips, and compute the unit ratio around every commuting square.
Test whether it is identically \(1\), a removable sheet rephasing, or a
genuine exceptional unit cocycle.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_flip_rees_coherence.rs`
- Result: `research/benincasa/results/five-site-flip-rees-coherence.json`
- Source valuation packet: `research/benincasa/results/five-site-two-normal-rees.json`
- Allocator claim: `seqclaim-53b0a2535012ab51396f5bfa`
- Epistemic graph event: `ev-000000001514-1b1f4234-d08c-4c1f-bc19-9c211e492a2d`
