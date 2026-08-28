---
author: marici.Benincasa
date: 2026-08-27
---

# 3772 — The Four-Site Marked Successor-Quartic Comparison Is Not Yet Typed

## Programme question

Entry 3768 excluded the generic four-site residual elliptic discriminants as
a source-derived successor of the homogeneous three-site quartic
\(\mathcal Q\). The remaining licensed candidate in the same frozen source is
the marked residual packet: its Gram--Kummer lines, Abel--Jacobi extension,
and physical-support closure.

Use the same typed contraction of the edge joining sites four and one:

\[
X'_1=X_4+X_1,
\qquad X'_2=X_2,
\qquad X'_3=X_3.
\]

## Coefficient support

The eight occurrence-resolved Kummer lines reduce to four distinct
radicands:

\[
A_{11},\qquad
A_{11}-2A_{12}+A_{22},\qquad
A_{22}-2A_{23}+A_{33},\qquad
A_{33}.
\]

They lie entirely in the independent Gram-cofactor ring. In the frozen
generic source ring each is coprime to
\(\mathcal Q_3(X_1+X_4,X_2,X_3)\).

The Abel--Jacobi packet adds no independent collision divisor. Its 24
oriented faces consist of 16 smooth elliptic faces carrying nonzero normal
functions and eight split rational faces carrying exact deck-pair
boundaries. These are coefficient extensions on the already declared
marked incidence geometry, not a new quartic support.

## Physical closure

Every residual triple contains an opened-graph wall. Under contraction its
linear form is

\[
X_1+X_2+X_3+X_4+2y_e
=X'_1+X'_2+X'_3+2y_e.
\]

In the nonnegative physical closure its vanishing forces

\[
X_1=X_2=X_3=X_4=y_e=0.
\]

The image is therefore the existing target all-soft support. Although the
homogeneous quartic vanishes there, this codimension-five contact is not a
quartic divisor and does not distinguish \(\mathcal Q\) from any other
positive-degree energy polynomial.

## Co-moving-detector correction

The polygon-contraction packet derives the labelled facet pullback but states
explicitly that restriction must be followed by an as-yet unnormalized
residue/Gysin comparison. It contains no pullback of the external Gram matrix,
no transport of the marked incidence covectors, and no coefficient-level
residue matrix.

Consequently, the coprimality calculation above freezes the Gram detector
while transporting the energy coordinate. It is a valid independence test in
the generic ambient ring, but it is not the missing co-moving marked
comparison. Grothendieck's Entry 3774 makes this distinction compulsory:
source incidence ports must move with the source deformation.

The previously derived local and Betti tests make the source boundary sharper.
Entry 1432 proves that the two endpoint residues have opposite orientation:
their symmetric sum vanishes while their oriented difference carries a
factor two. Hence no integral, exchange-symmetric, unit-normalized counit is
available without extra data. Entry 1433 shows that normal pushforward does
not repair this: it retains a logarithmic endpoint ratio. Entry 1434 proves
that the frozen positive chamber selects neither endpoint on the generic
contraction boundary.

## Result

The frozen four-site marked residual packet presently does not define the
comparison needed to produce or exclude a successor quartic. Its static
layers are:

- existing Gram--Kummer coefficient support;
- existing elliptic/split marked incidence;
- existing all-soft physical support.

No source-derived component in the frozen coordinates is canonically
proportional to the pulled three-site \(\mathcal Q\). But the stronger claim
that no such component can arise after the correctly transported
residue/Gysin comparison is withdrawn. The comparison is untyped, not
falsified. More strongly, the required comparison is unavailable from the
frozen physical source: its only admissible repairs require a new one-sided
current, a normalized counit, or retention of the occurrence-two target.

## Scope and next licensed move

This result concerns the residual marked packet frozen in Entries
1195--1198. The four-site contraction branch is closed as unavailable under
the frozen source; it must not be replaced by a fitted specialization. The
next admissible successor test must use an independently enlarged source
whose physical current and contraction counit are both explicit.

## Evidence

- `research/benincasa/checkers/check_four_site_marked_extension_quartic_successor.py`;
- `research/benincasa/results/four-site-marked-extension-quartic-successor.json`;
- `research/benincasa/results/four-site-qg-residual-kummer-radicals.json`;
- `research/benincasa/results/four-site-qg-residual-abel-jacobi-extension.json`;
- `research/benincasa/results/four-site-qg-residual-physical-support.json`.
- `research/benincasa/results/polygon-contraction-local-residue.json`;
- `research/benincasa/results/polygon-contraction-physical-chamber.json`.

Allocator claim: `seqclaim-ad48c233588fb059b0565dd0`.
