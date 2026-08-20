---
title: "Four Nodal Roots Contract E7 Primitively to A1 Cubed"
date: 2026-08-20
entry: 1184
status: active
sector: cosmology
---

# 1184 — Four Nodal Roots Contract E7 Primitively to A1 Cubed

Sequence claim: `seqclaim-a4cf1f8ef9a1d023c2e4c1f4`.

## Exceptional root subsystem

Resolve one of Entry 1183's two-conic marked sections. Its four conic
intersections give four disjoint \((-2)\)-curves. Inside Entry 1182's
primitive \(E_7\) Gysin lattice, choose the explicit orthogonal roots

\[
E_1-E_2,
\quad
E_3-E_4,
\quad
E_5-E_6,
\quad
H-E_1-E_2-E_7.
\]

Their Gram matrix is

\[
\boxed{-2I_4,}
\]

so they form \(A_1^4\).

## Integral embedding

In a standard simple-root basis of \(E_7\), the gcd of all maximal minors of
the \(7\times4\) embedding matrix is one. Therefore

\[
\boxed{A_1^4\hookrightarrow E_7\text{ is primitive}.}
\]

In particular,

\[
E_7/A_1^4
\]

is torsion-free. Contracting the four nodal roots introduces no hidden
integral index in the quotient.

## Orthogonal intersection-cohomology lattice

The integral orthogonal complement has rank three and discriminant eight.
An explicit unimodular basis change puts its Gram matrix into

\[
\boxed{-2I_3.}
\]

Hence

\[
\boxed{(A_1^4)^\perp_{E_7}\simeq A_1^3.}
\]

The direct sum \(A_1^4\oplus A_1^3\) has index eight in \(E_7\). This is
the intrinsic discriminant gluing of the resolved lattice; it is not torsion
in the contraction quotient.

## Gysin consequence

For a four-node boundary-sum section, the primitive intersection-
cohomological Gysin kernel has rank three:

\[
\boxed{
\ker(\mathrm{Gys})_{\rm IH}
\simeq A_1^3(-1).
}
\]

Thus the source terms have two distinct marked coefficient blocks:

\[
\begin{array}{c|c}
\text{zero-node smooth mark}&E_7(-1),\ \operatorname{rank}=7\\
\text{four-node boundary-sum mark}&A_1^3(-1),\ \operatorname{rank}=3.
\end{array}
\]

Both are Tate lattices derived from the same degree-two del Pezzo geometry.

## Next falsifier

Verify the excision square: map the four local exceptional roots to the four
corresponding node occurrence complexes of Entry 1181 and check that the
primitive contraction agrees with its signed local homotopy. Then assemble
the six or seven \(A_1^3\) blocks and the optional \(E_7\) block using the
actual pair/triple intersections of each source term.

## Evidence

- `research/benincasa/checkers/four_site_qg_a1four_e7_embedding.py`
- `research/benincasa/results/four-site-qg-a1four-e7-embedding.json`
- Entries 1181--1183.
