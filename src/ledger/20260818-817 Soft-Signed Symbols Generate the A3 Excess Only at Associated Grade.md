---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 817 — Soft-Signed Symbols Generate the A3 Excess Only at Associated Grade

## Question

Entry 813 finds, at one source-labelled soft--signed double-coordinate
corner,

\[
f=w^2+b^2+a^4.
\]

Its vanishing lattice has rank three, whereas the generic Kato line has
rank one. The finite question is whether the support-sensitive iterated
nearby-cycle object supplies the missing two directions.

Use the representative collision \((g_1,g_2)\), the corner
\(P_3=0,\ E=+P_1\), and the ordered orientation \(da\wedge db\), followed
by the soft and signed normal directions.

## Source-derived associated-grade complex

The Jacobian algebra is

\[
\operatorname{Jac}(f)=\mathbb Q\langle[1],[a],[a^2]\rangle.
\]

The local source family derives three graded symbols:

\[
\begin{aligned}
\text{generic Kato line}&\longmapsto[1],\\
\text{coordinate conormal}&\longmapsto[a],\\
\text{signed Kodaira--Spencer class}&\longmapsto[a^2].
\end{aligned}
\]

Thus

\[
\mathcal C_{\rm ss}^{\rm gr}:
\quad
\mathbb Q\langle K,c_a,\kappa_{\rm sign}\rangle
\xrightarrow{D_{\rm ss}^{\rm gr}}
\operatorname{Jac}(f),
\]

with

\[
\boxed{
D_{\rm ss}^{\rm gr}=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
}
\]

Therefore

\[
\operatorname{rank}D_{\rm ss}^{\rm gr}=3,\qquad
\operatorname{rank}(c_a,\kappa_{\rm sign})=2.
\]

The predeclared support calculus generates exactly the two directions
missing from the generic Kato line at associated grade.

## Betti monodromy and the missing comparison

Abstractly, the \(A_3\) vanishing lattice has Coxeter polynomial

\[
\chi_T(\lambda)=(\lambda+1)(\lambda^2+1).
\]

It therefore has an abstract \((-1)\)-line and an abstract
\((T^2+1)\)-plane. But the frozen source has not supplied vanishing paths
or an integral comparison identifying \([1],[a],[a^2]\) with a labelled
Betti basis. In a standard Coxeter basis the two primary lattices have
index two, but promoting that index to a source extension class would be a
basis-dependent inference.

Hence the full Betti differential and integral extension class are

\[
\boxed{\text{undefined, not zero and not yet }\mathbb Z/2.}
\]

## Independent support census

Exactly

\[
(g_1,g_2),\qquad(g_1,g_3),\qquad(g_2,g_3)
\]

have two movable marked coordinates. In each other representative, one
coordinate is exactly \(-E\); its double boundary forces \(E=0\), placing
it on the deeper nonisolated soft--triangle corner.

Therefore

\[
3\ {\rm orbits}\times3\ {\rm occurrences}\times4\ {\rm signs}=36
\]

generic labelled germs, and

\[
\boxed{
\dim V_{A_3}=108,\qquad
\dim K_{\rm generic}=36,\qquad
\dim V_{\rm exc}=72.
}
\]

The free cyclic action gives \(\chi_{\rm exc}=(72,0,0)\). This independently
reproduces Entry 815's support count.

## Result for H2

The rank-two excess is generated on the existing carrier at de Rham
associated grade. A full nearby-cycle theorem is not yet established.
H2 now requires a source-normalized Betti comparison carrying these
symbols into the integral \(A_3\) thimble lattice.

## Verification

- checker:
  research/benincasa/marici-gm/src/bin/a3_soft_signed_nearby_complex.rs;
- packet:
  research/benincasa/a3-soft-signed-nearby-complex.json;
- allocator claim seqclaim-8fabc25d335bb9bd4cbb603e.

## Next falsifier

Derive labelled vanishing paths from the original \(i\epsilon\) prescription
and compute the comparison from \(([1],[a],[a^2])\) to the integral
\(A_3\) thimble lattice. Only then compute monodromy intertwinement and the
integral extension class.
