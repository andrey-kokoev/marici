---
title: "Complete Source Summation Preserves Every Exceptional Cartier Order"
date: 2026-08-21
entry: 1438
status: active-narrow-result
author: marici.Nima
---

# 1438 — Complete Source Summation Preserves Every Exceptional Cartier Order

Sequence claim: seqclaim-35e51c531be1b4c408db0ea3.

## Question

Entries 1424 and 1435 derive exceptional orders from the minimum denominator
growth among the 180 source terms. On a mixed sheet, the complete sum of all
minimal terms could still cancel and raise the true coefficient valuation.

Does that happen at the coalesced-focus physical boundary?

## Exact characteristic-zero census

The checker expands every source denominator at \(\tau=0\), retains precisely
the terms of minimal order on each of the 32 sheets, and sums their leading
coefficients over \(\mathbb Q\).

Every complete leading sum is nonzero:

\[
\boxed{
c_S\ne0
\qquad
\text{for all }S\in(\mathbb Z/2)^5.
}
\]

Therefore the full source coefficient has exactly the termwise order

\[
\boxed{
10[2]+20[4]+2[9].
}
\]

No sheet moves to a deeper Cartier grade after source summation.

## Exact leading values

At unit coalesced radius, the 32 coefficients take only five signed rational
values:

\[
\boxed{
\left\{
-\frac9{128},
-\frac1{288},
\frac3{640},
\frac7{1440},
\frac9{128}
\right\}.
}
\]

The uniform pair is

\[
c_0=\frac9{128},
\qquad
c_{31}=-\frac9{128}.
\]

Global complement has the exact character predicted by Entry 1425:

\[
c_{S\oplus31}=(-1)^{o(S)}c_S.
\]

## Consequence

The valuation-shifted Hecke correspondence of Entries 1435–1437 is not merely
a termwise model. Its leading Cartier lattice is the actual complete
coalesced-focus source lattice on all 32 sheets.

In particular:

- no cancellation divisor occurs at the coalesced physical point;
- every optional unit-leading normalization is defined there;
- Entry 1437's unit coboundary applies without deleting a sheet;
- the residual \(\mu_2\) character is exact over \(\mathbb Q\).

## Scope

This is a characteristic-zero theorem at unit coalesced radius. Entry 1437
provides generic finite-field nonvanishing at two further radial points. A
global classification of the divisor \(c_S(r)=0\) away from these loci remains
open and must not be promoted to Carrier support without an independent
geometric derivation.

## Verification

- Checker:
  research/nima/check_five_site_coalesced_exceptional_leading_sums.py
- Result:
  research/nima/results/five-site-coalesced-exceptional-leading-sums.json
- Result SHA-256:
  b64a0fceac27319c12b493a757381f8e666d59a960a03bb113b8bde056b4b114
- The checker performs exact rational summation of all 180 source terms on all
  32 sheets.
- Two deterministic reruns produced byte-identical results.

## Next falsifier

Compute the first subleading \(\tau\)-jet for one elementary flip connecting
the uniform order-nine sheet to an order-four sheet. Determine whether the
strict leading correspondence extends to first jet inside a finite Hecke
modification, or leaves an exceptional extension class.
