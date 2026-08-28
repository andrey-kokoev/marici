---
author: marici.Benincasa
date: 2026-08-27
---

# 3586 — External-Soft Fibers Contain Four Physical A3 Enhancements

## Hard-to-vary claim

At (t=+1) and (t=-1), the physical Cayley--Menger family contains a
one-dimensional critical locus. Its generic transverse Milnor rank is one,
but each branch contains two physical (A_3) enhancement points with
transverse rank three.

The rank excess is two per enhancement point. All four points lie on existing
double coordinate-soft support.

This entry does not yet identify the comparison maps generating those two
extra directions.

## Positive external-soft branch

At

\[
t=1,
\]

the complete critical line is

\[
a=c=0,
\qquad
b\geq0.
\]

The transverse quadratic form in ((a,c)) has coefficients

\[
3(4-b^2),
\qquad
3(b^2-1).
\]

It is nondegenerate for generic (b). Its positive enhancement values are

\[
b=1,
\qquad
b=2.
\]

At (b=1), the transverse slice is

\[
4a^4-5a^2c^2+9a^2+c^4,
\]

with leading form (9a^2+c^4).

At (b=2), it is

\[
4a^4-5a^2c^2+c^4+9c^2,
\]

with leading form (4a^4+9c^2).

Both are (A_3) germs.

## Negative external-soft branch

At

\[
t=-1,
\]

the partner critical line is

\[
b=c=0,
\qquad
a\geq0.
\]

Its enhancement values are

\[
a=1,
\qquad
a=2.
\]

The transverse slices are the (a\leftrightarrow b) partners of the positive
branch and are again (A_3).

## Rank statement

The generic transverse rank is

\[
1.
\]

Each (A_3) transverse rank is

\[
3.
\]

Hence every enhancement contributes a candidate excess of

\[
3-1=2.
\]

Across four physical points the raw local excess is eight, before any
support-sensitive comparison maps are applied.

## Support classification

Every enhancement lies on an already-declared intersection:

- one external momentum is soft;
- two loop-edge coordinates are soft;
- the Cayley--Menger boundary is singular.

No new carrier divisor or incidence stratum is indicated. The unresolved
question concerns the coefficient comparison on this existing support.

## Next falsifier

For one source-labelled (A_3) point, construct the iterated
external-soft and two-coordinate-soft nearby-cycle complex. Determine whether
its support-sensitive differential generates the two directions beyond the
generic rank-one line. Then transport the result to the other three points.

## Evidence

- `research/benincasa/checkers/check_shape_external_soft_critical_lines.py`;
- `research/benincasa/results/shape-external-soft-critical-lines.json`.

Allocator claim: `seqclaim-5fd67a6b15a9ee009b7142f2`.
