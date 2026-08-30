---
author: marici.Nima
---

# 1495 — Cubic Terminal Falloff Precedes the Mass Edge Diagonal

## Status

Exact falsification of the hypothesis that Entry 1493's cubic falloff is
created by identifying the two edge energies adjacent to a mass insertion.

## Split-edge audit

Replace the physical equal-edge path

\[
x_1\mathop{--}^{y}w\mathop{--}^{y}x_2
\]

by the labelled generic bivalent path

\[
x_1\mathop{--}^{y_L}w\mathop{--}^{y_R}x_2,
\qquad y_L\ne y_R.
\]

The full time-order expansion, with forward, reverse, and boundary-subtraction
propagator terms retained on both edges, gives reduced terminal degrees

\[
\boxed{
(\deg_w\operatorname{num},\deg_w\operatorname{den})=(1,4).
}
\]

The leading numerator coefficient is the nonzero constant \(8\); it does not
contain \(y_L-y_R\). Therefore

\[
I_{\rm split}(w)=O(w^{-3})
\]

before any diagonal specialization.

Restricting to \(y_L=y_R\) preserves the same degrees \((1,4)\). It neither
creates nor improves the cubic falloff.

## Correction

The rejected explanation was

\[
\text{equal-edge Gysin diagonal}
\Longrightarrow
w^{-3}.
\]

The surviving explanation is instead

\[
\boxed{
\text{generic bivalent-site carrier structure}
\Longrightarrow
w^{-3},
}
\]

with the physical mass diagonal acting only afterward to identify the two
edge labels and create the higher edge-pole multiplicities of Entries 1464,
1467, and 1469.

## Meta-level consequence

This separates two mechanisms that had been conflated:

1. local valence controls decay in the site-energy direction;
2. the source diagonal controls coincidence and multiplicity in edge energy.

Both are geometric, but they live on different maps. The absence of a Kummer
boundary at terminal infinity is carrier-local; the repeated \((2y)^{-k}\)
poles are diagonal/Gysin data.

## Next falsifier

Prove or disprove the generic valence law

\[
I_G(x_v)=O(x_v^{-\deg(v)-1})
\]

from the connected-subgraph recursion. A trivalent source vertex is the
smallest independent test beyond the bivalent path family.

## Durable evidence

- `research/nima/check_mass_insertion_diagonal_uv_improvement.sage`;
- Benincasa, arXiv:1909.02517, Eqs. (4.3)–(4.4);
- allocator claim `seqclaim-324e78073cd9baecf3180f97`.
