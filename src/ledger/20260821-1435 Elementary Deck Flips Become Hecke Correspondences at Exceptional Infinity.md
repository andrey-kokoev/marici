---
author: marici.Benincasa
---

# 1435 — Elementary Deck Flips Become Hecke Correspondences at Exceptional Infinity

## Status

Exact valuation-shift theorem on all \(32\) sheets of the five-site two-normal
Rees object.

## Raw and normalized sheet generators

Let \(f_S\) denote the raw coefficient on sheet
\(S\in(\mathbb Z/2)^5\), and let

\[
o(S)\in\{2,4,9\}
\]

be its exceptional \(\tau\)-order from Entry 1424. The
valuation-normalized generator is

\[
e_S=\tau^{-o(S)}f_S.
\]

An elementary deck flip \(T_i\) acts regularly on the raw sheet sum by
\(S\mapsto S\mathbin{\rm xor}2^i\). On normalized generators,

\[
T_i(e_S)
=
\tau^{o(S\mathbin{\rm xor}2^i)-o(S)}
e_{S\mathbin{\rm xor}2^i}.
\]

## Exact shift census

Every one of the five elementary flips has the same shift distribution:

\[
\begin{array}{c|ccccc}
\Delta o&-5&-2&0&2&5\\
\hline
\#\text{ sheets}&2&6&16&6&2.
\end{array}
\]

Thus every elementary flip contains both positive and negative exceptional powers.

## Consequence

The raw deck action remains regular before choosing the exceptional lattice, but

\[
\boxed{
T_i\text{ is not a regular degree-zero endomorphism of the normalized Rees lattice.}
}
\]

Negative shifts require \(\tau^{-2}\) or \(\tau^{-5}\). Because each \(T_i\)
is an involution, reversing the correspondence exchanges zeros and poles; no
uniform filtration shift repairs both directions.

The correctly typed continuation is therefore

\[
\boxed{
\text{elementary deck flip}
=
\text{meromorphic/Hecke correspondence supported at exceptional infinity}.
}
\]

No Hecke modification is adjoined in this entry.

## Residual symmetry

Global complement has

\[
o(S\mathbin{\rm xor}31)=o(S)
\]

for all \(S\). It is therefore the unique nontrivial deck translation acting
regularly on the associated grading, exactly as Entry 1430 found by stabilizer
census.

## Architectural meaning

Exceptional specialization does not merely break a symmetry. It retypes most of the unspecialized symmetry as correspondences between differently modified lattices:

\[
\text{regular deck action before specialization}
\longrightarrow
\text{residual graded symmetry plus exceptional Hecke correspondences}.
\]

This supplies the valuation data required by Entry 1430 without adding new
carrier support: all poles lie on the already declared exceptional divisor
\(\tau=0\).

## Scope

This is a valuation theorem. It does not construct the modified lattices, prove a cocycle law for Hecke compositions, or show that the physical positive current pairs with the meromorphic correspondences.

## Next finite falsifier

Compose two elementary flip correspondences on normalized generators. Test
whether their \(\tau\)-shifts telescope exactly to the shift of the composite
deck mask and whether the required lattice modifications satisfy the square
relations without an additional exceptional coherence cell.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_elementary_flip_rees.rs`
- Result: `research/benincasa/results/five-site-elementary-flip-rees.json`
- Source valuation packet: `research/benincasa/results/five-site-two-normal-rees.json`
- Allocator claim: `seqclaim-68d6e958bfbaae3ce538c66f`
- Epistemic graph event: `ev-000000001511-9d1e6714-9fd0-4b59-8fd1-5597f996bef4`
