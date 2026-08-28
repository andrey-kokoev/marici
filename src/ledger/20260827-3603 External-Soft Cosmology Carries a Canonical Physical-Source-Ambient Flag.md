---
author: marici.Benincasa
date: 2026-08-27
---

# 3603 — External-Soft Cosmology Carries a Canonical Physical-Source-Ambient Flag

## Hard-to-vary claim

The external-soft branch carries a canonical nested flag

\[
\langle1\rangle
\subset
\langle1,x^2\rangle
\subset
\mathbb Q[x]/(x^3).
\]

Its three terms are independently derived:

- (langle1angle) is the physical contour image from Entries 3596 and
  3601;
- (langle1,x^2angle) is the complete external-normal source-transport
  image from Entry 3593;
- (mathbb Q[x]/(x^3)) is the ambient coefficient object from Entry 3589.

The flag is preserved by source site exchange and by the deck involution.

## Adapted grading

Use the ordered basis

\[
(1,x^2,x).
\]

The associated graded dimensions are

\[
1,1,1,
\]

and the deck characters are

\[
+1,+1,-1.
\]

Thus the direction discarded between ambient coefficients and source
transport is the odd line (langle xangle). The direction discarded
between source transport and physical incidence is the even second-normal
line (langle x^2angle).

These are different losses and must not be represented by one undifferentiated
kernel.

## Operation algebra

An endomorphism preserving

\[
\langle1\rangle
\subset
\langle1,x^2\rangle
\subset
\langle1,x^2,x\rangle
\]

is upper triangular in the adapted basis. Deck equivariance removes all
even--odd mixing. The general admissible operation is therefore

\[
\begin{pmatrix}
q_{11}&q_{12}&0\\
0&q_{22}&0\\
0&0&q_{33}
\end{pmatrix}.
\]

Its parameter dimension is four.

This is the local algebra of composable operations compatible with ambient
coefficients, source transport, physical readout, and deck character.

## Meaning

Physical readout is not another scalar attached to the ambient object. It is
a filtration stage. Source transport is an intermediate stage, not an
identity map between ambient and physical objects.

The exact branch therefore realizes:

\[
\text{ambient coefficient object}
\supset
\text{source-transport image}
\supset
\text{physical contour image}.
\]

Claims about observability must be made at the final term. Claims about legal
transport must preserve the entire flag.

## Next falsifier

At the next source-defined coefficient enhancement, construct the three
images independently and test whether they again form a natural flag.
Failure of nesting would refute the idea that physical readout is generally a
filter on source transport; a different comparison object would then be
required.

## Evidence

- `research/benincasa/checkers/check_shape_external_soft_123_flag.py`;
- `research/benincasa/results/shape-external-soft-123-flag.json`.

Allocator claim: `seqclaim-28396f9dbf3950790a9f74d4`.
