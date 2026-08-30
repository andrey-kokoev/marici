---
title: "The Asymmetric Five-Site Canonical Function Has a Degree-Sixteen 13304-Term Numerator"
date: 2026-08-20
entry: 1270
status: active-exact-coefficient-input
author: marici.Benincasa
---

# 1270 — The Asymmetric Five-Site Canonical Function Has a Degree-Sixteen 13304-Term Numerator

Sequence claim: `seqclaim-c896cc4d5fda96860fc1403f`.

## Source-normalized compilation

Entry 1250 authorizes the 180-term Eq. (33) representation with unit weights.
On Entry 1257's asymmetric physical slice, combine the four-denominator
supplements over their common set of twenty labelled factors while retaining

\[
G,g_1,\ldots,g_5
\]

as the six common factors.

Exact sparse polynomial arithmetic gives

\[
\boxed{
\Omega_{C_5}^{\rm asym}(t,y)
=
\frac{N_{16}(t,y_1,\ldots,y_5)}
{\prod_{a=1}^{26}q_a(t,y)}.
}
\]

The numerator satisfies

\[
\deg N_{16}=16,
\qquad
\#\operatorname{supp}(N_{16})=13304.
\]

Its serialized expanded form has 387020 characters.

## Carrier-factor audit

For every one of the 26 labelled linear carrier factors \(q_a\), perform
exact multivariate polynomial division

\[
N_{16}=q_aQ_a+R_a.
\]

All remainders are nonzero:

\[
\boxed{
q_a\nmid N_{16}
\quad
\text{for all }a=1,\ldots,26.
}
\]

Hence no marked wall disappears when the source triangulation is summed. The
complete frozen pole carrier survives in the canonical coefficient form.

## Interpretation

This is the first exact expanded computational input for the corrected
five-site integrated problem. It establishes neither a period rank nor a
Picard--Fuchs operator. It shows that coefficient reduction cannot begin by
cancelling carrier divisors.

The complexity is structured rather than unbounded:

\[
180\text{ source terms}
\longrightarrow
13304\text{ numerator monomials over 26 labelled walls}.
\]

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_canonical_sum.rs`
- `research/benincasa/results/five-site-asymmetric-canonical-sum.json`

## Next falsifier

Pull this exact rational form to Entry 1257's three-variable Cayley--Menger
cover. Before seeking a scalar Picard--Fuchs equation, compute a finite
twisted de Rham/Jacobian quotient at generic \(t\) and measure the smallest
source-derived Gauss--Manin coefficient rank.
