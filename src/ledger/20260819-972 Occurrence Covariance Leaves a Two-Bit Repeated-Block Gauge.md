# 972 — Occurrence Covariance Leaves a Two-Bit Repeated-Block Gauge

## Normalization gate after Entry 971

The localized intertwiner is canonical on four factor subquotients, but the
two repeated factors each have rank two.  Entry 909 transports both sparse
and dense occurrence bases by the same swap

\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

An integral internal gauge \(P\) compatible with this transport must satisfy

\[
PJ=JP,
\qquad P\in GL_2(\mathbb Z).
\]

## Exact centralizer

Writing

\[
P=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

the commutation equation forces \(a=d\) and \(b=c\).  Unimodularity then
requires

\[
a^2-b^2=\pm1.
\]

Over the integers this has exactly four solutions:

\[
\boxed{
P\in\{I,-I,J,-J\}.
}
\]

The checker exhausts all entries in \([-4,4]\) and recovers precisely these
four matrices; the displayed Diophantine factorization proves there are no
larger solutions.

Modulo overall residue orientation, each repeated block retains the two
choices

\[
I\quad\text{or}\quad J.
\]

Since the \(ZA_2B_{24}\) and \(A_3B_{34}/Z\) blocks are independent, the
residual unsigned gauge is

\[
\boxed{(\mathbb Z/2)^2.}
\]

## Narrow conclusion

Cyclic and reflection covariance preserve the localized intertwiner but do
not select an internal occurrence ordering.  Every allowed gauge has signed
cyclic composition \(+1\).

Therefore Entry 971 cannot yet be promoted to a uniquely normalized global
matrix.  The remaining ambiguity is finite and coefficient-theoretic; it is
not a carrier defect.

## Next falsifier

Use the actual six component formulas of the mixed-corner exceptional row,
not only their zero supports.  Compare their leading units on both branches
with the source residue orientations of the two labelled corner occurrences.
Test whether those units select \(I\) or \(J\) in each block.  If they are
equal up to the common orientation, retain the \((\mathbb Z/2)^2\) ambiguity
as genuine integral coefficient data rather than choosing a host-preserving
ordering.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_repeated_block_gauge.rs`;
- packet:
  `research/benincasa/string-six-point-repeated-block-gauge.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_repeated_block_gauge`;
- allocator claim:
  `seqclaim-a420be388dd32c24bcad59fd`.
- epistemic event:
  `ev-000000000589-b6ce6eb5-fc9d-4437-8585-8598292fa390`.
