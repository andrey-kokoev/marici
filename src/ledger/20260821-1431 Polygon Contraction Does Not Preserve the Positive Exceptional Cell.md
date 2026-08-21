---
author: marici.Benincasa
---

# 1431 — Polygon Contraction Does Not Preserve the Positive Exceptional Cell

## Status

Exact labelled-facet typing theorem, replicated at source arities \(4\) through \(8\).

## Proposed operation

Contract the labelled edge \((n,1)\) of \(C_n\). The target \(C_{n-1}\)
has one merged site whose source preimage is \(\{n,1\}\).

The contraction is well defined on partial-energy facets. In particular,

\[
c^*q'_{\{1\}}=q_{\{n,1\}},
\]

while every singleton not incident to the contracted edge pulls back to the corresponding source singleton.

## Common-cell obstruction

The positive exceptional period of \(C_n\) is frozen on the cell containing

\[
q_G,\ q_{\{1\}},\ldots,q_{\{n\}}.
\]

The target period cell pulls back instead to

\[
q_G,\ q_{\{n,1\}},\ q_{\{2\}},\ldots,q_{\{n-1\}}.
\]

Therefore

\[
\boxed{
c^*(\text{target positive cell})
\ne
\text{source positive cell}.
}
\]

The mismatch is not a relabelling artifact: the exact wall identity is

\[
\boxed{
q_{\{1\}}+q_{\{n\}}
=
q_{\{n,1\}}+2y_{\{n,1\}}.
}
\]

Only on the contracted-edge divisor \(y_{\{n,1\}}=0\) does the merged target
wall equal the sum of the two source singleton walls.

## Consequence

Labelled graph contraction exists at Carrier level, but direct period recursion does not:

\[
\boxed{
C_n\not\longrightarrow C_{n-1}
\quad\text{by ordinary pullback of the frozen cells.}
}
\]

A typed comparison would require, in order:

1. restriction to \(y_{\{n,1\}}=0\);
2. a residue/Gysin or counit operation combining the two source singleton poles;
3. compatibility with the exceptional current and its orientation.

No such normalization is inferred from the facet identity.

## Architectural meaning

Entry 1429's alphabet bound is natural at the level of allowed wall sizes, but its individual periods are not automatically functorial under graph contraction. This is another instance of

\[
\text{Carrier map}
\not\Rightarrow
\text{coefficient/current comparison map}.
\]

## Scope

The theorem rejects only strict common-cell pullback. It does not obstruct a derived contraction comparison supplied by an independently normalized residue, Gysin map, or physical counit.

## Next finite falsifier

Apply the source residue at \(y_{\{n,1\}}=0\) to one low-arity pair,
beginning with \(C_5\to C_4\). Determine whether its normal Jacobian and
orientation canonically convert

\[
\frac{1}{q_{\{1\}}q_{\{n\}}}
\quad\text{into}\quad
\frac{1}{q_{\{n,1\}}},
\]

or leave an unavoidable convolution/relative coefficient.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/polygon_contraction_typing.rs`
- Result: `research/benincasa/results/polygon-contraction-typing.json`
- Allocator claim: `seqclaim-19c669990975ff66ff34ee7f`
- Epistemic graph event: `ev-000000001507-f018f193-9a0a-4e66-a9ac-6f763a668b7b`
