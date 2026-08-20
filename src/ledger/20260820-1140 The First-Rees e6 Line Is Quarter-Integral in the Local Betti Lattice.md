---
title: "The First-Rees e6 Line Is Quarter-Integral in the Local Betti Lattice"
date: 2026-08-20
entry: 1140
status: established-local-integral-comparison
sector: cosmology
---

# 1140 — The First-Rees e6 Line Is Quarter-Integral in the Local Betti Lattice

Sequence claim: `seqclaim-7c56c28a22411ff22cfe22a8`.

## Integral node pair

Order the normalization sheets as \((e_+,e_-)\). Entry 1131 gives the
primitive physical boundary

\[
d=e_- - e_+=(-1,+1).
\]

The local integral Betti group is the reduced homology of these two points,

\[
\widetilde H_0(\{e_+,e_-\};\mathbb Z)=\mathbb Z\langle d\rangle.
\]

Its primitive integral dual has the symmetric rational representative

\[
\eta=\left(-\frac12,+\frac12\right),
\qquad \eta(d)=1.
\]

The halves here do not make \(\eta\) nonintegral: cochains differing by a
constant represent the same reduced cohomology class, and \(\eta\) is the
symmetric representative of the primitive class represented integrally by
\((0,1)\).

## Comparison with the source-normalized e6 residue

Entry 1133 gives the first-Rees covector

\[
\rho_{e_6}=\left(-\frac18,+\frac18\right).
\]

Therefore

\[
\rho_{e_6}=\frac14\eta,
\qquad
\rho_{e_6}(d)=\frac14.
\]

The integral Betti lattice inside the source-normalized rational \(e_6\)
line is consequently

\[
\mathbb Z\eta=4\mathbb Z\rho_{e_6}.
\]

Hence

\[
\boxed{
\mathbb Z\rho_{e_6}/\mathbb Z\eta\simeq\mathbb Z/4.}
\]

This local Betti calculation supplies the target-side comparison missing
from Entries 1138--1139.

## Interpretation

The node cohomology itself is free; it has no torsion. The \(\mathbb Z/4\)
is an index defect between the source-normalized first-Rees de Rham line and
the primitive integral Betti lattice. Equivalently, the printed \(e_6\)
normalization is quarter-integral at this node.

Thus the correct statement is

\[
\boxed{
\text{physical local Betti comparison has index four,}
\quad
\text{but the topological node group is torsion-free}.}
\]

It is coefficient-lattice information over the existing normalization
carrier, not a new carrier primitive.

## Next falsifier

Transport the primitive local Betti generator through the six occurrence
sectors and the source Cousin differential. Determine whether the local
index-four comparisons assemble into a global integral hypercohomology
class or cancel as the rational class does. No global \(\mathbb Z/4\) claim
is authorized before this integral Cousin calculation.

Evidence:

- `research/benincasa/checkers/rank12_e6_local_betti_lattice.py`;
- `research/benincasa/results/rank12-e6-local-betti-lattice.json`;
- Entries 1131, 1133--1134, and 1138--1139.
