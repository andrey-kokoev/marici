---
title: "The Global Quarter-Class Has a Two-by-Two Saturation Filtration"
date: 2026-08-20
entry: 1138
status: established-integral-frame-gate
sector: cosmology
---

# 1138 — The Global Quarter-Class Has a Two-by-Two Saturation Filtration

Sequence claim: `seqclaim-33ae41264ecee09218c1618f`.

## Frozen source line

The six-occurrence source vector

\[
c_1=(1,1,1,1,1,1)
\]

is primitive in \(\mathbb Z^6\). Entry 1137's rational physical vector is

\[
g=\frac14c_1.
\]

On their common rational diagonal line, the source and saturated-frame
lattices are

\[
\mathbb Zc_1=4\mathbb Zg
\subset
\mathbb Zg.
\]

Therefore the frozen rational-frame saturation defect is

\[
\boxed{
\mathbb Zg/\mathbb Zc_1\simeq\mathbb Z/4.
}
\]

## Two-stage structure

There is a unique index-two intermediate line \(2\mathbb Zg\) on this
rank-one rational line. The resulting
indices are

\[
4\mathbb Zg\subset2\mathbb Zg\subset\mathbb Zg,
\qquad [2,2].
\]

This \([2,2]\) filtration aligns with two independently derived factor-two
mechanisms:

1. Entries 1130--1131: the normalization sheet-difference generator maps
   to twice the primitive odd coinvariant;
2. Entries 356 and 1137: forgetting the two lower-denominator occurrences
   in each marked-Cut sector sends the all-positive pair to multiplicity two.

Thus the denominator four has a source-motivated two-stage candidate
provenance, rather than being an unexplained fitted scale. A typed
composition of the sheet-parity and occurrence-forgetting maps is still
required to identify those two mechanisms with the two lattice inclusions.

## Qualification

This does **not** prove physical \(\mathbb Z/4\) torsion. The calculation
compares the primitive source occurrence lattice with the lattice generated
by the rational-frame vector \(g\). To interpret the quotient as physical
torsion, one must independently prove that \(g\) is integral in the Betti
realization of the \(e_6\) line.

The established statement is therefore:

\[
\boxed{
\text{order-four denominator defect in the frozen source frame}
\quad\text{with a unique rank-one }2\times2\text{ filtration}.}
\]

This is coefficient-lattice information; it introduces no carrier datum.

## Next falsifier

First construct the typed composition of the sheet-parity and
occurrence-forgetting maps and test whether its Smith map is multiplication
by four. Then test the two stages separately against the physical Betti comparison. If
the source chain realizes only the intermediate lattice, the surviving
defect is \(\mathbb Z/2\); if it realizes \(g\) primitively, the full
\(\mathbb Z/4\) survives; if it realizes only \(c_1\), no torsion survives.

Evidence:

- `research/benincasa/checkers/rank12_e6_global_integral_saturation.py`;
- `research/benincasa/results/rank12-e6-global-integral-saturation.json`;
- Entries 356, 1130--1131, and 1137.
