---
id: 417
date: 2026-08-17
title: The Gysin-Collapsed Atlas Is a Four-Term Filtered PC Module
---

# The Gysin-Collapsed Atlas Is a Four-Term Filtered PC Module

Entry 416 derived the unique regrading \(\deg_G(p,q)=p\). This determines an
explicit algebraic object, not merely a rank profile.

Let
\[
C_{\rm Tate}=
[\mathbb Z_{\rm or}\xrightarrow N P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}\xrightarrow\epsilon\mathbb Z]
\]
and let \(E=\Lambda^\bullet\mathbb Z^3\), retained as a four-step Cartier
filtration rather than added to chain degree. Define
\[
\boxed{\mathcal P_{\rm fil}=C_{\rm Tate}\otimes E,}
\]
with:

- chain degree inherited only from \(C_{\rm Tate}\);
- filtration degree inherited from exterior degree in \(E\);
- chain differential \(d=d_{\rm Tate}\otimes1\);
- degree-zero Cartier operator
  \[
  B=1\otimes\iota_{(1,1,1)}.
  \]

The chain-degree ranks are
\[
\boxed{(8,24,24,8)}.
\]
Their Cartier filtration profiles are respectively
\[
(1,3,3,1),\quad(3,9,9,3),\quad
(3,9,9,3),\quad(1,3,3,1).
\]

## Exact identities

The executable basis audit proves integrally
\[
d^2=0,\qquad B^2=0,\qquad dB=Bd.
\]
Thus \(B\) is a filtered chain endomorphism, exactly as required after the
Gysin transfer. It is no longer mis-typed as a second cellular boundary.

Both directions have explicit unit contractions. A spanning-tree
contraction of the Tate window uses
\[
h(z)=r_0,\quad h(r_1)=-t_0,\quad
h(r_2)=-t_0-t_1,\quad h(t_2)=o,
\]
with the other basis values zero, and satisfies
\[
dh+hd=\operatorname{id}.
\]
Exterior multiplication by the first positive Cartier basis vector
contracts the filtration complex:
\[
B(e_1\wedge-)+e_1\wedge B=\operatorname{id}.
\]
No denominator occurs in either contraction.

## Meaning

This is the first object in the sequence that has simultaneously:

1. the correct four-degree PC amplitude;
2. all eight Cartier states over every Tate carrier generator;
3. the integral \(N/(1-r)/\epsilon\) carrier differential; and
4. the three-normal Cartier operator as degree-zero filtered structure.

It is the canonical algebraic source normal form for the transferred loaded
map. It is not yet identified with a subquotient of Entry 143's
occurrence/Čech target. That remaining realization must map \(d\) to the
facewise support differential and \(B\) to the graph-Cartier can--var
operator while preserving the generic roof and endpoint residues.

The executable audit is
\`research/voevodsky/check_collapsed_filtered_pc_module.py\`.
