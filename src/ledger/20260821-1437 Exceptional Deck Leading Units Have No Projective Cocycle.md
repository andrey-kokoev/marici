---
author: marici.Benincasa
---

# 1437 — Exceptional Deck Leading Units Have No Projective Cocycle

## Status

Strict source-frame theorem with replicated exact modular leading-coefficient audits.

## Source frame

Entry 1221 freezes the labelled chamber-relative deck package and proves that
every elementary sheet flip preserves section labels, residue order, and
ambient \(d^3\ell\) orientation. Entry 1223 proves strict compatibility with
the intrinsic Kummer connection.

Therefore the raw deck action has unit coefficient:

\[
T_a(f_S)=f_{S\mathbin{\rm xor}a}.
\]

Entry 1435 adds only the exceptional power \(\tau^{\Delta_a(S)}\) after
valuation normalization.

## Optional unit-leading normalization

Let \(c_S\) be the source-derived leading coefficient of sheet \(S\), and
define

\[
\widehat e_S=c_S^{-1}\tau^{-o(S)}f_S
\]

where \(c_S\ne0\). Then

\[
T_a(\widehat e_S)
=
\tau^{\Delta_a(S)}u_a(S)\widehat e_{S\mathbin{\rm xor}a},
\]

with

\[
u_a(S)=\frac{c_{S\mathbin{\rm xor}a}}{c_S}.
\]

This unit system is an exact coboundary. In particular,

\[
u_a(S)u_b(S\mathbin{\rm xor}a)
=
u_{a\mathbin{\rm xor}b}(S),
\]

and every elementary square and commuting flip diagram closes identically.

## Finite replication

All \(32\) leading coefficients are nonzero at each of two independent exact
finite-field radial points. The checker verifies per point

\[
160\text{ square identities}
\]

and

\[
800\text{ ordered commutation identities}.
\]

No projective defect appears.

## Consequence

Combining Entries 1435–1437, the exceptional deck correspondence is completely typed at leading Rees order:

\[
\boxed{
T_a:
e_S\longmapsto
\tau^{\Delta_a(S)}e_{S\oplus a},
}
\]

with strict valuation composition and no intrinsic unit or orientation cocycle.

The divisor \(c_S=0\) appears only if one insists on the optional unit-leading
normalization. It is not support of the raw source correspondence and must not
be promoted to a carrier stratum.

## Scope

The theorem concerns the leading exceptional lattice. It does not prove that
the full subleading \(\tau\)-jets form finite Hecke modifications or that the
physical positive current extends meromorphically across every correspondence.

## Next finite falsifier

Compute the first subleading \(\tau\)-jet under one elementary flip between an
order-nine and order-four sheet. Test whether the valuation-shifted transport
remains regular to first jet or requires an additional extension supported on
the exceptional divisor.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_flip_leading_unit_cocycle.rs`
- Result: `research/benincasa/results/five-site-flip-leading-unit-cocycle.json`
- Strict source transport: Entries 1221 and 1223
- Allocator claim: `seqclaim-deeac1ee79472b6515e1e49e`
- Epistemic graph event: `ev-000000001515-d177620c-6601-4684-bb7c-dc5ffc6050b0`
