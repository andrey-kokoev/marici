---
title: "The Occurrence-Resolved Four-Site Node Cech Cone Is Acyclic"
date: 2026-08-20
entry: 1181
status: active
sector: cosmology
---

# 1181 — The Occurrence-Resolved Four-Site Node Cech Cone Is Acyclic

Sequence claim: `seqclaim-7016ab124882ebefd1041a49`.

## Frozen complex

For each of the 28 source OFPT terms, take its seven supported sign nodes.
At each node retain every vanishing denominator label as a distinct Čech
vertex, including labels whose geometric hyperplanes coincide.

Order vertices lexicographically by source label. For an oriented subset
\((i_0,\ldots,i_j)\), use the standard boundary

\[
\partial(i_0,\ldots,i_j)
=
\sum_{a=0}^j(-1)^a
(i_0,\ldots,\widehat{i_a},\ldots,i_j).
\]

Augment each local occurrence simplex to its node class, then map the seven
node classes into Entry 1179's basis of

\[
V_{\rm van}=\mathbf Q^8/\langle r_{\chi_{234}}\rangle.
\]

This fixes residue-orientation signs before taking ranks.

## Exact result

For every term:

1. consecutive differentials compose to zero;
2. every local occurrence simplex is exact after augmentation;
3. the seven augmentations map isomorphically onto \(V_{\rm van}\);
4. the complete cone has zero homology in every degree.

The deepest source profile reaches Čech degree five. Nevertheless,

\[
\boxed{
H^\bullet(\mathcal K_{\rm node}^{(a)})=0
\qquad(a=1,\ldots,28).
}
\]

Repeated labels increase chain dimensions but generate no residual class.
Changing the source-label order only conjugates the complex by orientation
signs and does not alter this conclusion.

## Closure theorem

Entries 1171--1181 now give the complete algebraic node packet:

\[
\boxed{
\begin{aligned}
&8\text{ local }A_1\text{ nodes},\\
&1\text{ total-parity relation},\\
&7\text{ supported deck occurrences},\\
&\text{mixed-Tate local arrangements},\\
&\text{acyclic occurrence-resolved localization cone}.
\end{aligned}
}
\]

Hence the four-site total-energy nodes contribute no residual marked-relative
algebraic coefficient class. They require neither a new carrier stratum nor
a new coefficient type.

The positive physical node remains meaningful as a labelled occurrence, but
its class is absorbed by the supported total-parity relation. A physical
effect would require additional source-derived relative-chain data and
cannot be inferred from this algebraic packet.

## Next frontier

Retire the node branch. Return to the smooth part of the quartic-double-solid
marked complement, where the generic coefficient object has non-Tate
threefold cohomology. The next source-defined test is the Gysin image of one
marked hyperplane section into the smooth rank-twenty middle system, followed
by the seven-hyperplane localization sequence. This is distinct from the
now-closed nodal support complex.

## Evidence

- `research/benincasa/checkers/four_site_qg_node_cech_cone.py`
- `research/benincasa/results/four-site-qg-node-cech-cone.json`
- Entries 1178--1180.
