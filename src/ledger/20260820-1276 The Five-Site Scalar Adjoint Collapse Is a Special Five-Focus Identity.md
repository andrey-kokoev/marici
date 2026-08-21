---
title: "The Five-Site Scalar Adjoint Collapse Is a Special Five-Focus Identity"
date: 2026-08-20
entry: 1276
status: retracted-by-entry-1280
author: marici.Benincasa
---

# 1276 — The Five-Site Scalar Adjoint Collapse Is a Special Five-Focus Identity

> **Retracted by Entry 1280.** This attempted correction still relied on an
> unstable polynomial-variable position in the quotient reducer. The scalar
> collapse does not survive the fully symbol-indexed calculation.

Sequence claim: `seqclaim-5c6650a8d200b0cf47e10605`.

## Proof-packet defect

The first implementation behind Entry 1273 parsed polynomial variables in the
namespace `marici` but constructed its requested variable order in the
binary-local namespace. Symbolica retained both symbol sets. The reducer then
read inert exponent slots.

Consequently the first quotient-reduction packet and its first finite-field
evaluation packet were not valid evidence.

Both engines are now repaired by resolving every variable explicitly in the
`marici` namespace. The source canonical numerator itself is unchanged.

## Corrected verification on Entry 1257

After the repair, the full five-relation reduction on Entry 1257 still gives

\[
N_{16}
\equiv
99{,}408{,}314{,}880{,}000.
\]

All 31 nontrivial characters vanish, and the repaired direct finite-field
evaluations pass. Thus Entry 1273's narrow equality on its frozen slice
survives.

## Filtration-depth audit

Replace the unreached quadratic relations by independent symbols and impose
the physical relations in the labelled order. The exact reduced census is

\[
\begin{array}{c|r|r}
\text{physical relations imposed}&
\text{nonzero characters}&
\text{total coefficient terms}\\ \hline
0&32&13304\\
1&32&95892\\
2&32&214236\\
3&32&154474\\
4&32&90012\\
5&1&1
\end{array}
\]

Therefore no proper subset of this ordered five-relation packet explains the
collapse. The fifth labelled focus relation is essential to the identity.

## Independent kinematic falsifier

Keep the same determinant-one basis \((q_1,q_2,q_3)\), but choose a second
conserved asymmetric fourth focus with

\[
q_4^2=61,
\qquad
c=(-1,-2,6).
\]

On that equally physical rank-three cover, exact reduction gives

\[
32\text{ nonzero characters}
\quad\text{and}\quad
43509\text{ coefficient terms}.
\]

Hence the scalar collapse is not generic on the rank-three Gram carrier.

## Corrected interpretation

\[
\boxed{
\text{Entry 1273 is a special identity of the complete frozen five-focus
configuration, not a universal Carrier theorem.}
}
\]

It remains useful as a low-complexity computational slice, but it cannot set
the generic coefficient architecture or update H2 by itself.

## Artifacts

- repaired `research/benincasa/marici-gm/src/bin/five_site_asymmetric_canonical_sum.rs`
- repaired `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_character_reduction.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-character-reduction-prefix-0.json` through `prefix-4.json`
- `research/benincasa/results/five-site-asymmetric-kummer-character-reduction-profile-b.json`
