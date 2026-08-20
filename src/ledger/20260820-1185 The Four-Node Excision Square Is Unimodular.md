---
title: "The Four-Node Excision Square Is Unimodular"
date: 2026-08-20
entry: 1185
status: active
sector: cosmology
---

# 1185 — The Four-Node Excision Square Is Unimodular

Sequence claim: `seqclaim-f2aad43b8b179edbd6e1e1f4`.

## Source-oriented local coordinates

Use the representative boundary-sum mark

\[
y_1+y_2=0.
\]

Its four node occurrences are

\[
p_{\epsilon_3,\epsilon_4}
=[1:-1:\epsilon_3:\epsilon_4].
\]

On the marked plane set

\[
A=y_3^2-y_1^2,
\qquad
B=y_4^2-y_3^2.
\]

At a node, in the chart \(y_1=1\),

\[
\boxed{
\det\frac{\partial(A,B)}{\partial(y_3,y_4)}
=4\epsilon_3\epsilon_4.
}
\]

This fixes the Poincaré-residue orientation of each conic intersection
without choosing root signs afterward.

## Excision matrix

Order the four nodes by

\[
(\epsilon_3,\epsilon_4)
=(-,-),(-,+),(+,-),(+,+).
\]

In the corresponding exceptional-root and node-occurrence bases, the local
excision map is

\[
\boxed{
R_{\rm exc}
=
\operatorname{diag}(1,-1,-1,1).
}
\]

Hence

\[
\boxed{\det R_{\rm exc}=1.}
\]

The map is unimodular. It identifies Entry 1184's \(A_1^4\) exceptional
root lattice with the four local node augmentations in Entry 1181, including
their source orientations.

On this sheet \(\epsilon_2=-1\), so the total-parity coefficient is

\[
\epsilon_2\epsilon_3\epsilon_4
=-\epsilon_3\epsilon_4.
\]

Thus the excision orientation equals minus the total-parity orientation by
one common sign. This is exactly compatible with the global relation and
does not vary among the four nodes.

## Consequence

The local Čech contraction and the global del Pezzo root contraction glue
integrally:

\[
\boxed{
\text{no local torsion}
+
\text{no excision index}
+
\text{surviving }A_1^3\text{ lattice}.
}
\]

Cyclic relabelling transports the same determinant-one square to every
boundary-sum mark.

## Next frontier

The single-mark problem is closed. Assemble the seven marked coefficient
blocks termwise:

- six or seven \(A_1^3\) nodal blocks;
- zero or one \(E_7\) smooth block;
- their source-derived pair and triple incidence maps.

Compute the first inclusion--exclusion rank and identify whether any
nontrivial extension survives beyond Tate lattice gluing. Do not add generic
position assumptions: use Entry 1160's exact concurrency packet.

## Evidence

- `research/benincasa/checkers/four_site_qg_a1four_excision_square.py`
- `research/benincasa/results/four-site-qg-a1four-excision-square.json`
- Entries 1181 and 1184.
