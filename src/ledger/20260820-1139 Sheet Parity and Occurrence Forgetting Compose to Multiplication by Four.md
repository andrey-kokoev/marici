---
title: "Sheet Parity and Occurrence Forgetting Compose to Multiplication by Four"
date: 2026-08-20
entry: 1139
status: established-integral-composition
sector: cosmology
---

# 1139 — Sheet Parity and Occurrence Forgetting Compose to Multiplication by Four

Sequence claim: `seqclaim-8d679abfbe454ee3a680c6f3`.

## Frozen labelled maps

Use the six source occurrences in the order

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
\]

For each occurrence, Entry 1131's oriented physical boundary is

\[
e_- - e_+.
\]

Entry 1130's integral sheet comparison sends this boundary to minus twice
the primitive odd coinvariant.  On the six occurrence lines the first map is

\[
S=-2I_6.
\]

Entry 356's occurrence-forgetting map is

\[
F=
\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]

Both maps preserve the source occurrence labels, so their composition is
typed without inserting a new comparison:

\[
C=FS=-2F.
\]

## Smith and invariant-line calculations

The full map \(C:\mathbb Z^6\to\mathbb Z^3\) has nonzero Smith invariants

\[
(2,2,2).
\]

Let

\[
x=(1,1,1,1,1,1),\qquad y=(1,1,1).
\]

Then

\[
Sx=-2x,
\qquad Fx=2y,
\qquad Cx=-4y.
\]

Consequently, on the cyclically invariant rank-one source line, the two
independently derived index-two operations genuinely compose to

\[
\boxed{\mathbb Z\xrightarrow{-4}\mathbb Z.}
\]

Its cokernel is \(\mathbb Z/4\).  This supplies the typed source-side
provenance that Entry 1138 deliberately left open.

## Qualification

The result proves that normalization-sheet parity followed by
lower-denominator occurrence forgetting produces multiplication by four on
the invariant source line.  It still does **not** prove physical
\(\mathbb Z/4\) torsion in the \(e_6\) period lattice.  That would additionally
require an integral Betti comparison showing that Entry 1137's rational
quarter-vector is primitive on the \(e_6\) side.

Thus the narrow conclusion is

\[
\boxed{
\text{the denominator four has a typed source-side composition,}
\quad
\text{while its physical Betti survival remains open}.}
\]

No new carrier datum is introduced.

## Next falsifier

Construct the integral Betti realization of the first-Rees \(e_6\) line and
the comparison square from the physical Cayley--Menger boundary.  Compute
whether the image is primitive, index two, or index four.  Only this square
can distinguish no physical torsion, \(\mathbb Z/2\), and \(\mathbb Z/4\).

Evidence:

- `research/benincasa/checkers/rank12_e6_parity_occurrence_composition.py`;
- `research/benincasa/results/rank12-e6-parity-occurrence-composition.json`;
- Entries 356, 1130--1131, and 1137--1138.
