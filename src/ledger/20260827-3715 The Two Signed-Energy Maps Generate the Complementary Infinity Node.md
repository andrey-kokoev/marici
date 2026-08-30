---
author: marici.Benincasa
date: 2026-08-27
---

# 3715 — The Two Signed-Energy Maps Generate the Complementary Infinity Node

## Source-labelled normals

Entry 3710 identifies the complementary all-soft germ as the ordinary node

\[
\Omega^2-r^2-uv=0,
\]

where the two labelled normal coordinates are

\[
u=\lambda-2\mu=\frac{z-(x+y)}d,
\qquad
v=\lambda+2\mu=\frac{z+(x+y)}d.
\]

Their Jacobian in the ordered coordinates \((\lambda,\mu)\) is

\[
\det\frac{\partial(u,v)}{\partial(\lambda,\mu)}=4.
\]

Thus \((u,v)\) is an étale normal-coordinate system at the generic node.
No fitted coordinate or additional divisor is used.

## Ordered-residue incidence

Let \(e_u\) and \(e_v\) denote the two existing labelled signed-energy
nearby-cycle generators. Let

\[
e_{uv}=d\log u\wedge d\log v
\]

denote the ordered rank-one node generator. The Čech/Koszul incidence map is

\[
\mathbb Q\langle e_u,e_v\rangle
\longrightarrow
\mathbb Q\langle e_{uv}\rangle,
\qquad
(a,b)\longmapsto a-b.
\]

Its matrix is

\[
\begin{pmatrix}1&-1\end{pmatrix}.
\]

The map has rank one and is surjective. Its kernel is

\[
\mathbb Q\langle e_u+e_v\rangle,
\]

the ordinary diagonal overlap relation between the two branch generators.

## Reflection covariance

The source reflection exchanges \(u\) and \(v\). It therefore exchanges
\(e_u,e_v\) and reverses the ordered target orientation:

\[
e_{uv}\longmapsto-e_{uv}.
\]

Writing \(S\) for the source swap, the exact covariance identity is

\[
\begin{pmatrix}1&-1\end{pmatrix}S
=
-\begin{pmatrix}1&-1\end{pmatrix}.
\]

The Kummer deck character remains anti-invariant on all three residue
objects and is distinct from this occurrence reflection.

## Result

The two already declared signed-energy maps generate the complete rank-one
node coefficient. Their supported comparison cokernel vanishes. Therefore
the complementary infinity chart contributes:

- no ungenerated node class;
- no new coefficient object;
- no new carrier support;
- only the standard labelled overlap relation.

Together with Entries 3705, 3708, and 3710, this closes the all-soft gluing
of the physically activated infinity line at the local de Rham/Kato level.
Integral physical-chain normalization remains a separate question and is
not inferred from this incidence calculation.

## Evidence

- `research/benincasa/checkers/check_infinity_signed_node_incidence_map.py`;
- `research/benincasa/results/infinity-signed-node-incidence-map.json`;
- Entries 3705, 3708, and 3710.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007977-99a33406-e526-43fb-be5f-8ec38bdf21a1`.

Allocator claim: `seqclaim-737c7a68b8eef472cb8ffd6b`.
