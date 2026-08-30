---
author: marici.Benincasa
date: 2026-08-27
---

# 3573 — The Exceptional Triangle Parameters Produce the Existing Rank-One Fold

## Hard-to-vary claim

At both exceptional parameter values (t=\pm1/2), the Cayley--Menger family
degenerates to a perfect square. Generically along the squared divisor, the
shape parameter supplies a transverse rank-one fold. This coefficient object
is supported on the already-declared external triangle divisor.

The only deeper failures of transversality lie on the existing signed
loop-energy arrangement.

## External triangle support

For

\[
P_1=1+t,\qquad P_2=1-t,\qquad P_3=1,
\]

the external triangle polynomial is

\[
\Lambda(P_1,P_2,P_3)=3(1-4t^2).
\]

Hence its two branches are precisely

\[
t=\frac12,
\qquad
t=-\frac12.
\]

## Perfect-square fibers

At the positive branch,

\[
K\big|_{t=1/2}
=
\frac1{16}
\left(
6a^2-2b^2-4c^2+3
\right)^2.
\]

At the negative branch,

\[
K\big|_{t=-1/2}
=
\frac1{16}
\left(
2a^2-6b^2+4c^2-3
\right)^2.
\]

At generic positive rational points of either quadric,
(\partial_tK\neq0). Thus the local form is a normal square plus the
triangle parameter times a unit. Its transverse nearby-cycle rank is one.

## Deeper support

Eliminating the quadric normal against (\partial_tK) gives, at both
branches,

\[
144
(a-b-1)^2
(a-b+1)^2
(a+b-1)^2
(a+b+1)^2.
\]

Therefore the failure of the generic fold description is confined to the
already-labelled signed arrangement

\[
a\pm b\pm1=0.
\]

No new carrier component is produced.

## Meaning

The singular-section degeneration of Entry 3569 is generated generically by
the existing triangle specialization. The resulting rank-one coefficient
object is not a residual failure of the smooth-boundary adapter; it is the
ordinary transverse fold attached to the declared triangle support.

This result classifies geometric support and nearby-cycle rank. It does not
assert a nonzero integrated physical period.

## Next falsifier

Resolve the intersections of the triangle fold with
(a\pm b\pm1=0). Construct the supported comparison cone from the existing
triangle and signed-wall maps. Only a nonzero residual cone can justify an
additional coefficient coherence class.

The separate external-soft parameters (t=\pm1) remain to be tested
afterward.

## Evidence

- `research/benincasa/checkers/check_shape_cm_triangle_fold.py`;
- `research/benincasa/results/shape-cm-triangle-fold.json`.

Allocator claim: `seqclaim-8507242c63ac33bedc3f62af`.
