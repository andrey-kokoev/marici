---
title: "Cyclic Sewing Adds No Integral Index Beyond Occurrence Identification"
date: 2026-08-20
entry: 1150
status: established-integral-sewing
sector: cosmology
---

# 1150 — Cyclic Sewing Adds No Integral Index Beyond Occurrence Identification

Sequence claim: `seqclaim-4a3e0de56317f958171140d7`.

## Question

Entry 1149 leaves the physical Cut--nearby commutator in the rank-seven
algebraic kernel. The next finite falsifier asks whether cyclic sewing of its
six source occurrences introduces an integral index not visible over the
rational connection.

## Primitive sector lines

After removal of the common nonzero Leray scalar, Entry 229 gives the three
sector-local vectors

\[
(X_2,X_1,1),\qquad (X_3,X_2,1),\qquad (X_1,X_3,1)
\]

in their labelled ((e_3,e_5,e_6)) bases. Each is primitive over the
integral kinematic polynomial ring because its (e_6) coordinate is one.
Cyclic relabelling preserves this primitive coordinate.

## Occurrence-resolved sewing

In the source occurrence order

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23),
\]

the forgetting map to the three marked-Cut sector lines is

\[
F=
\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]

Its Smith invariants are

\[
\boxed{(1,1,1).}
\]

Thus the occurrence-resolved map is saturated and has no torsion cokernel.
There is no cyclic holonomy index and no new integral extension between the
three sector lines.

## Physical source sum

The literal source sum uses the diagonal pair in each marked-Cut sector.
Restricting (F) to these three pair-sum generators gives

\[
2I_3,
\]

whose cokernel is

\[
(\mathbb Z/2)^3.
\]

This is exactly Entry 229's occurrence-identification multiplicity: two
distinct lower-denominator occurrences project to the same marked-Cut line.
It is not torsion of the resolved carrier or of the algebraic coefficient
line.

## Verdict

\[
\boxed{
\text{cyclic sewing adds no integral index beyond the existing
occurrence-identification factors of two}.}
\]

Together with Entry 1149, the source-defined physical comparison is now
integrally classified on the generic nonsoft locus:

- its algebraic commutator line is primitive sectorwise;
- its six-occurrence sewing is saturated;
- forgetting occurrence labels doubles each sector;
- its elliptic width-two coinvariant image is zero;
- no new carrier datum is required.

## Next falsifier

The remaining nontrivial integral structure is not cyclic sewing but the
four enhanced-point deck lattice of Entry 301, with Smith type ((1,2,2)).
Compare its two parity cokernels with the occurrence-identification
((\mathbb Z/2)^3) through the full labelled conductor map. A typed map may
show that they are the same parities in different presentations; absent such
a map, they must remain distinct coefficient defects.

Evidence:

- `research/benincasa/checkers/cut_nearby_integral_cyclic_saturation.py`;
- `research/benincasa/results/cut-nearby-integral-cyclic-saturation.json`;
- Entries 226, 229, 301, and 1149.
