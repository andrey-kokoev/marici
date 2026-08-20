---
title: "Boundary-Sum Marks Are Four-Node Two-Conic Sections"
date: 2026-08-20
entry: 1183
status: active
sector: cosmology
---

# 1183 — Boundary-Sum Marks Are Four-Node Two-Conic Sections

Sequence claim: `seqclaim-8a6035531d909274eb452c6f`.

## Two source-derived section types

Entry 1182's smooth \(E_7\) benchmark cannot be applied uniformly to the
seven marks of a source OFPT term. Their infinity normals have two types.

### Single-edge normal

A spanning-path denominator has leading mark

\[
y_e=0.
\]

It misses all eight sign nodes. Generically its plane quartic branch is
smooth, so Entry 1182 applies.

### Boundary-sum normal

Every connected proper-subgraph denominator has a two-edge boundary normal.
For the representative

\[
y_1+y_2=0,
\]

one difference coordinate vanishes identically:

\[
\Delta_1=y_2^2-y_1^2=0.
\]

Set

\[
A=y_3^2-y_1^2,
\qquad
B=y_4^2-y_3^2.
\]

The restricted branch quartic is a binary quadratic in \(A,B\):

\[
aA^2+2bAB+cB^2.
\]

At generic Gram kinematics it factors over its quadratic splitting field
into two distinct diagonal conics. Their four intersections are precisely
the four sign nodes satisfying \(\epsilon_2=-1\).

Thus

\[
\boxed{
\text{boundary-sum mark}
=
\text{degree-two del Pezzo section with four }A_1\text{ points}
}
\]

before resolution.

## Complete term census

Among the 28 source terms:

\[
\begin{array}{c|c|c}
\text{zero-node marks}&\text{four-node marks}&\text{term count}\\
\hline
0&7&4\\
1&6&24.
\end{array}
\]

Hence most terms contain one smooth-benchmark mark, while four terms contain
only four-node two-conic sections.

## Consequence

The actual global Gysin packet is not seven independent copies of the smooth
\(E_7\) kernel. Each boundary-sum section carries an \(A_1^4\) contraction
inside its resolved del Pezzo lattice, and Entry 1181 supplies the local
threefold-node contraction with which it must be glued.

This is still existing carrier geometry:

\[
\boxed{
\text{source marked plane}
+
\text{existing sign-node support}
+
\text{quadratic splitting field}.
}
\]

No new divisor was introduced.

## Next falsifier

For one boundary-sum section, identify the four exceptional \((-2)\)-roots
inside the resolved \(E_7\) lattice and compute the contraction quotient and
its discriminant form. Then compare its local \(A_1^4\) boundary map with
Entry 1181's occurrence contraction. This determines whether the global
Gysin kernel descends primitively or acquires an index.

## Evidence

- `research/benincasa/checkers/four_site_qg_mark_section_types.py`
- `research/benincasa/results/four-site-qg-mark-section-types.json`
- Entries 1178, 1181, and 1182.
