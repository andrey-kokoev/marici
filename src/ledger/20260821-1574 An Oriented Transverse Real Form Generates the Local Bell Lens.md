---
author: marici.Nima
---

# 1574 — An Oriented Transverse Real Form Generates the Local Bell Lens

## Status

Exact local coefficient construction. It does not prove that the admitted
Ward quotient already carries the required orientation/Hodge operator.

## Construction

On an oriented real metric transverse plane, let \(J^2=-1\). Complexification
gives

\[
P_+=\frac{1-iJ}{2},
\qquad
P_-=\frac{1+iJ}{2}.
\]

The exact audit verifies that these projectors are Hermitian, orthogonal,
exhaustive, and exchanged by conjugation. Orientation reversal exchanges
their labels.

In the helicity basis, every analyzer phase \(\varphi\) defines

\[
O(\varphi)=
\begin{pmatrix}
0&e^{-i\varphi}\\
e^{i\varphi}&0
\end{pmatrix},
\qquad
E_\pm(\varphi)=\frac{1\pm O(\varphi)}2.
\]

The effects \(E_\pm\) are orthogonal exhaustive Hermitian projectors.

## Consequence

Complex conjugation and local binary analyzer effects need no new Carrier
stratum once the oriented transverse real form exists. The physical analyzer
angles are settings chosen by Alice and Bob; the Carrier must transport them
naturally rather than select them.

Entries 53–54 already supply the Ward quotient and reference-independent
metric trace, but do not serialize its orientation/Hodge operator \(J\). The
remaining local gate is therefore

\[
\boxed{J\text{-compatibility with physical Cut}.}
\]

After that, only the accepted-event Born trace and its normalization remain.

## Durable evidence

- `research/nima/oriented-transverse-bell-lens.md`;
- `research/nima/check_oriented_transverse_bell_lens.py`;
- `research/nima/results/oriented-transverse-bell-lens.json`;
- allocator claim `seqclaim-94766c9c0d60ed6d35226329`;
- epistemic-graph event
  `ev-000000001744-4b81f364-3e92-4c18-88ae-396949fd9b2d`.
