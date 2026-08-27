# 3326 — The e6 Torsor Is an A2 Boundary Cocycle Not a Trivial-Line Intertwiner

## Purpose

Entry 3323 identifies the primitive (e_6) logarithmic form with one edge of
the cyclic Leray-frame cocycle. The Clifford reformulation suggested a possible
shortcut: perhaps cyclic equivariance uniquely forces an intertwiner from the
energy-shape plane into the (e_6) line.

The exact representation audit falsifies that shortcut and gives the correct
typing.

## Clifford and root-space form

Let

\[
H=\sum_{i=1}^3(\log X_i)e_i
\]

and let

\[
n=\frac{e_1+e_2+e_3}{\sqrt3}.
\]

Common scaling lies along (n). The cyclic transition forms lie in the
orthogonal shape plane, whose integral boundary lattice is

\[
A_2=\ker\left(\mathbb Z^3\xrightarrow{(1,1,1)}\mathbb Z\right).
\]

The Entry 3323 edge is the primitive root

\[
\alpha_{32}=e_3-e_2=(0,-1,1),
\]

with logarithmic form

\[
\alpha_{32}\cdot dH=d\log\frac{X_3}{X_2}.
\]

Its cyclic orbit spans (A_2\) and sums to zero.

In a two-root basis, the cyclic action is

\[
R=
\begin{pmatrix}
0&-1\\
1&-1
\end{pmatrix},
\qquad R^3=1.
\]

## No ordinary intertwiner

Let (h:A_2\otimes\mathbb Q\to\mathbb Q_{m triv}) be a candidate map to a
cyclic-trivial (e_6) line. Equivariance requires

\[
hR=h.
\]

Exact solution gives

\[
h=0.
\]

Therefore

\[
\operatorname{Hom}_{C_3}(A_2,\mathbb Q_{m triv})=0.
\]

Cyclic symmetry cannot force the desired lower-left extension coordinate as a
multiplicity-one ordinary intertwiner.

## Correct object

The class is instead a logarithmic Čech cocycle between occurrence frames.
On the generic energy torus, (d\log(X_3/X_2)) is a rational change of frame.
On the compactified carrier its divisor is

\[
(0,-1,1),
\]

which cannot be removed by a gauge required to remain regular at the labelled
soft boundary.

Thus the class is:

- generically presentation-trivial;
- nontrivial in the boundary-preserving logarithmic lattice;
- supported on existing soft divisors;
- an (A_2) occurrence cocycle rather than a map from (A_2) to one trivial
  line.

## Consequence

The rank-twelve gate must be formulated as logarithmic lattice descent across
the three occurrence charts. A fixed-chart equivariant-Hom calculation is
mistyped and cannot establish the ((e_6,q_0)) entry.

The required comparison must transport the full rank-twelve extension between
occurrence charts, retain the boundary lattices, and ask whether its triangular
gauge transition has (C_2d\log(X_3/X_2)) in the specified coordinate.

## Verification

The exact checker is
`research/benincasa/checkers/audit_clifford_a2_torsor_typing.py`; its packet is
`research/benincasa/results/clifford_a2_torsor_typing.json`.

Allocator claim: `seqclaim-257a0c60b6ef2323e88da7c9`.
