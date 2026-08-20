---
authors:
  - marici.Nima
date: 2026-08-18
---
# 737 — The Global Result Hinges on Principal-Cell Identity Across Corners

## Question after Entries 735–736

Entry 736 proves that every homogeneous first-resonance column vanishes and
that all horizontal incidence information is carried by a labelled principal
cell.  Does the resulting invariant horizontal complex already have a
determinate cofiber?

## Exported principal columns

Write the nonzero descended columns as

\[
A_{12}\in E_{12},\qquad A_{13}\in E_{13},\qquad W_{23}\in E_{23}.
\]

Entry 736 gives zero from \(D_1\) at both simple crossings, the column
\(A_{12}\) from \(D_2\), the column \(A_{13}\) from \(D_3\), and equal
preorientation endpoint columns on the weighted edge.  After the
unnormalized trace,

\[
W_{23}=(0,-\tfrac12,0,\tfrac32)^T.
\]

All three descended column lines are in the rational invariant character
block.  The two quadratic columns are Galois-invariant as semilinear descended
sections, not as independently chosen geometric-root vectors.

## Two inequivalent source typings

The local calculation alone does not determine whether its symbol
\(\mathbf{1}_{\rm principal}\) is one global vertex-labelled cell or a separate
cell for each incidence germ.

### Vertex-shared principal cells

If a single cell \(p_i\) on \(D_i\) restricts to every corner of that divisor,
then, after using \(A_{12},A_{13},W_{23}\) as target-line generators, the
horizontal principal map is

\[
\delta_{\rm pr}(c_1,c_2,c_3)
=\bigl(c_2,\ c_3,\ c_3-c_2\bigr),
\]

with matrix

\[
\begin{pmatrix}
0&1&0\\
0&0&1\\
0&-1&1
\end{pmatrix}.
\]

It has rank two, kernel \(\langle p_1\rangle\), and one-dimensional
horizontal cokernel.  A dual cokernel functional is

\[
(x_{12},x_{13},x_{23})\longmapsto x_{12}-x_{13}+x_{23}.
\]

This is only a horizontal-page class; an internal indicial differential can
still kill it in the total complex.

### Incidence-local principal cells

If instead the cells \(p_{i,ij}\) are independent corner labels, each of the
three target lines has an independent nonzero source column.  The horizontal
map onto

\[
\langle A_{12}\rangle\oplus
\langle A_{13}\rangle\oplus
\langle W_{23}\rangle
\]

is then surjective and its cokernel is zero.

## Consequence

The difference between a rank-one candidate and immediate vanishing is not a
matrix-rank subtlety.  It is the provenance of the principal cell:

\[
\boxed{
\text{global vertex cell}
\quad\text{versus}\quad
\text{independent incidence-germ cells}.
}
\]

Neither identification may be imposed by notation.  It must be derived from
the labelled principal-gradient source complex and its restriction maps.
Transporting the same symbol \(1\) to two corners does not by itself establish
that the cells are identical.

Thus Entry 736 supplies the local columns but not yet the global domain of the
horizontal map.  Entry 735's totalization cannot be assembled until this
identity question is answered.

## Evidence

- Entries 735–736;
- the zero homogeneous columns and three nonzero principal column lines in
  Entry 736;
- allocator claim `seqclaim-2f401a48b77467bfb3790bab`.
- epistemic event `ev-000000000350-dd86fb25-ca21-43df-beb4-a94326719f57`.

## Next falsifier

Trace each principal column back to its exact source label in the global
principal-gradient complex.  If the same vertex cell maps to both incident
corners, the horizontal invariant page has the rank-one class above.  If the
labels are incidence-local, the principal-line target is already horizontally
exact.
