---
title: "The Integral Kummer Wall Image Is Primitive and Saturated"
date: 2026-08-20
entry: 1146
status: established-integral-cousin-image
sector: cosmology
---

# 1146 — The Integral Kummer Wall Image Is Primitive and Saturated

Sequence claim: `seqclaim-cfe903e4dc4d7f90327f3f07`.

## Integral transport into the wall complex

Entry 1121 sends the source Kummer generator to

\[
\operatorname{Res}_W(k)
=
\left(\frac{s+7}{4},-1,-\frac{s+7}{4},0\right)^T.
\]

At \(s=-3+2\sqrt2\), Entry 1145's primitive integral generator is

\[
\kappa=\sqrt2\,k.
\]

Its wall image is

\[
\boxed{
\operatorname{Res}_W(\kappa)
=
(1+\sqrt2,-\sqrt2,-1-\sqrt2,0)^T.}
\]

## Saturation

The first coordinate is a unit because

\[
N_{\mathbb Q(\sqrt2)/\mathbb Q}(1+\sqrt2)=-1.
\]

Therefore the coordinates generate the unit ideal in
\(\mathbb Z[\sqrt2]\), and the image line is primitive and saturated in the
integral two-wall lattice. Its same-sheet top residue still vanishes:

\[
(1+\sqrt2)+(-1-\sqrt2)=0.
\]

Hence no additional integral index or extension appears in the Cousin map.

## Verdict

The index-two defect of Entry 1145 belongs entirely to the source-normalized
Kummer eigenline. Once replaced by its primitive integral generator, the
existing wall realization is unimodular:

\[
\boxed{
\text{Kummer source lattice: index two,}
\qquad
\text{integral wall image: index one}.}
\]

This closes the algebraic integral refinement of the quadratic Kummer
branch. Entries 1122--1123 continue to prohibit a physical pairing: the
frozen regulator data choose no chamber.

No new carrier datum is required.

## Next move

Retire this exceptional center under the frozen physical source. The next
source-defined calculation should concern an exceptional coefficient object
whose physical chain specialization is already fixed, rather than attempting
to activate this Kummer line by an unmotivated regulator hierarchy.

Evidence:

- `research/benincasa/checkers/rank12_quadratic_kummer_integral_wall_image.py`;
- `research/benincasa/results/rank12-quadratic-kummer-integral-wall-image.json`;
- Entries 1121--1123 and 1145.
