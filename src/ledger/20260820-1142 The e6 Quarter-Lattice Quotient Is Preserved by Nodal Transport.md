---
title: "The e6 Quarter-Lattice Quotient Is Preserved by Nodal Transport"
date: 2026-08-20
entry: 1142
status: established-filtered-local-system
sector: cosmology
---

# 1142 — The e6 Quarter-Lattice Quotient Is Preserved by Nodal Transport

Sequence claim: `seqclaim-aef69cf382cd33fd70bf790e`.

## Universal nodal transport

The second-center family is the labelled pullback

\[
XY=t,
\qquad
t=p\,s\,(B-1).
\]

Entry 1103 proves that the primitive vanishing-cycle generator \(\eta\) has

\[
M_p=M_s=M_{B-1}=1,
\]

while the normalization deck involution acts by

\[
\tau(\eta)=-\eta.
\]

Entry 1140 identifies the source-normalized first-Rees generator as

\[
\rho_{e_6}=\frac14\eta.
\]

Therefore the Gauss--Manin transport preserves both lattices

\[
\mathbb Z\eta\subset\mathbb Z\rho_{e_6}
\]

and descends to the finite quotient

\[
\boxed{
\mathcal D_{e_6}
=
\mathbb Z\rho_{e_6}/\mathbb Z\eta
\simeq\mathbb Z/4.}
\]

Its labelled base monodromies are all identity. Its deck action is
multiplication by \(-1\) modulo four.

## Compatibility with the support simplex

Entry 1104 derives the complete three-face Gysin simplex from the same
smoothing monomial. Its maps are

\[
d_0=(1,1,1),
\]

\[
d_1=
\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix},
\qquad
d_2=\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]

They satisfy

\[
d_0d_1=0,
\qquad
d_1d_2=0
\]

over \(\mathbb Z\), hence also after tensoring with the quarter-lattice and
after reduction modulo four. The deck sign is uniform on every term, so all
three differentials remain equivariant.

## Type verdict

The index-four defect is not confined to one accidental point: it is
preserved by the universal nodal transport and the labelled support maps.
But Entry 1141 remains decisive: the occurrence-resolved integral Betti
Cousin cohomology is torsion-free.

Thus

\[
\boxed{
\mathcal D_{e_6}\text{ is a finite coefficient-lattice quotient local system,}
\quad
\text{not a new physical cohomology class}.}
\]

This is a concrete sector-specific coefficient refinement over the existing
carrier and Gysin calculus. No new carrier datum is required.

## Next falsifier

Determine whether \(\mathcal D_{e_6}\) extends through the deeper support
intersections \(s=0\), \(B-1=0\), and their corner as a finite flat
coefficient object, or acquires nontrivial nearby-cycle length there. The
existing conductor contraction is rational; integral reduction modulo two
and four must be computed separately because multiplication by two is no
longer invertible.

Evidence:

- `research/benincasa/checkers/rank12_e6_quarter_lattice_transport.py`;
- `research/benincasa/results/rank12-e6-quarter-lattice-transport.json`;
- Entries 1100--1104 and 1140--1141.
