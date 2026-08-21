---
author: marici.Benincasa
---

# 1434 — The Positive Polygon Chamber Selects Neither Contraction Endpoint

## Status

Exact support theorem for the frozen Euclidean polygon current, replicated at
arities \(4\) through \(8\).

## Frozen physical chamber

The source Euclidean current is supported on

\[
X_i>0,
\qquad
y_i\ge0.
\]

Contract the edge \((n,1)\) by restricting to

\[
y_{\{n,1\}}=0.
\]

The two singleton walls entering Entry 1432 then become

\[
q_{\{1\}}=X_1+y_{\{1,2\}},
\]

\[
q_{\{n\}}=X_n+y_{\{n-1,n\}}.
\]

Both are strictly positive at a generic point of the contraction boundary.

## Endpoint support

The first endpoint residue \(q_{\{1\}}=0\) can meet the nonnegative closure
only if

\[
X_1=y_{\{1,2\}}=0.
\]

The second endpoint residue \(q_{\{n\}}=0\) can meet it only if

\[
X_n=y_{\{n-1,n\}}=0.
\]

Thus each endpoint belongs to a deeper site-soft and adjacent-edge-soft corner, not to the generic edge-contraction divisor.

Therefore

\[
\boxed{
\overline\Gamma_{+}\cap\{y_{\{n,1\}}=0\}
\text{ selects neither singleton endpoint generically.}
}
\]

## Consequence

Entry 1432's one-sided unit residue is algebraically valid but is not selected by the frozen physical current. The positive chamber supplies neither

\[
\operatorname{Res}_{q_{\{1\}}=0}
\quad\text{nor}\quad
\operatorname{Res}_{q_{\{n\}}=0}
\]

on the generic contraction boundary.

Hence the direct physical recursion route closes:

\[
\boxed{
C_n\not\longrightarrow C_{n-1}
\text{ through the generic positive edge-contraction boundary.}
}
\]

A comparison would require an additional pushforward over the site-splitting fiber or an analytically continued relative current on the deeper soft corner. Neither is present in the frozen source.

## Architectural meaning

The three levels are now separated:

\[
\text{graph contraction exists},
\]

\[
\text{local endpoint residues exist},
\]

\[
\text{the physical current selects neither endpoint}.
\]

This is a concrete example of why Carrier functoriality and coefficient-level residue identities do not by themselves imply physical period functoriality.

## Scope

This closes only the generic positive-chamber route. It does not analyze analytically continued cycles on the deeper soft corners or forbid a separately derived contraction trace.

## Next frontier

Retire direct polygon-period recursion. The remaining naturality question is the filtered deck correspondence from Entry 1430: construct one elementary sheet flip on the full two-normal Rees object before associated grading and determine its valuation shift and support.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/polygon_contraction_physical_chamber.rs`
- Result: `research/benincasa/results/polygon-contraction-physical-chamber.json`
- Source chamber: Entries 1217 and 1233
- Allocator claim: `seqclaim-8ee58b2a91bbf0d53f7a76e3`
- Epistemic graph event: `ev-000000001510-3f4d2ec3-610c-44c4-9d64-f9ef6d2e0dad`
