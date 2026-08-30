---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2163 — The Positive Blowup Separates Strict Support from the Radial Cartier Grade

## Deeper corner

For one cyclic occurrence, the physical closure can meet
\(\{q_{jk}=y_{jk}=0\}\) only when

\[
X_j=X_k=y_{ij}=y_{ik}=y_{jk}=0.
\]

Blow up these five nonnegative normals with common radial coordinate
\(\rho\):

\[
(X_j,X_k,y_{ij},y_{ik},y_{jk})
=
\rho(\widehat X_j,\widehat X_k,
\widehat y_{ij},\widehat y_{ik},\widehat y_{jk}).
\]

Then

\[
q_{jk}=\rho\widehat q_{jk},
\qquad
y_{jk}=\rho\widehat y_{jk},
\]

where

\[
\widehat q_{jk}
=
\widehat X_j+\widehat X_k
+\widehat y_{ij}+\widehat y_{ik}.
\]

## Empty positive weak transform

On the positive exceptional simplex, all hatted coordinates are
nonnegative and not all zero. If

\[
\widehat q_{jk}=0,\qquad \widehat y_{jk}=0,
\]

then every one of the five hatted coordinates is zero, contradicting
projectivity. Hence

\[
\boxed{
V(\widehat q_{jk},\widehat y_{jk})
\cap E_{\ge0}
=\varnothing.
}
\]

The exact checker confirms this on all 1820 integral directions of the
denominator-12 simplex.

## Total versus weak transform

The pulled-back ideal is

\[
(q_{jk},y_{jk})
=
\rho(\widehat q_{jk},\widehat y_{jk}).
\]

Thus the positive chain has no strict-transform incidence with the
component-soft support. The only common geometric factor is the exceptional
Cartier divisor \(\rho=0\).

This sharply types the remaining physical question:

- the weak-transform Tor packet has zero literal positive pairing;
- a radial nearby/Rees grade may remain because both generators have
  valuation one;
- whether that grade is nonzero depends on the complete transformed source
  measure and coefficient form.

One must not retain or remove the common \(\rho\) factor by convention.

## Consequence

The next finite calculation is an exceptional valuation table for the full
grade-two and grade-three source integration forms, including:

1. the Cayley--Menger measure;
2. all component-energy and endpoint denominators;
3. the normal Jacobian;
4. the physical orientation and deck character.

If the net radial form has no logarithmic coefficient, the literal physical
activation branch closes. If it has one, its residue supplies the canonical
pairing with Entry 2160's Cartier grade.

## Classification

- strict positive incidence: absent;
- weak-transform supported class: physically invisible;
- possible radial Cartier grade: unresolved;
- required new Carrier support: none.

## Evidence

- Entries 2160--2162
- research/benincasa/checkers/positive_component_soft_blowup.rs
- allocator claim seqclaim-ab4c4c273b0f73d8047c8de2
