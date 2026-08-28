---
author: marici.Benincasa
date: 2026-08-27
---

# 3593 — The External-Soft Source Jet Sees Exactly the Even A3 Plane

## Hard-to-vary claim

At all four physical external-soft (A_3) enhancements from Entries 3586 and
3589, the complete source-derived external-normal jet maps into

\[
\mathbb Q[x]/(x^3)
\]

with image exactly

\[
\langle[1],[x^2]\rangle.
\]

The odd class ([x]) is invisible to every external-normal order. Therefore
external-soft parameter transport cannot by itself activate the complete
rank-three local object.

## Source normals

The source shape family is

\[
P_1=1+t,
\qquad
P_2=1-t,
\qquad
P_3=1.
\]

Hence the canonical inward normals are (P_2=1-t) at (t=1) and
(P_1=1+t) at (t=-1). Reducing their derivatives modulo the local
(A_3) Jacobian ideal gives the following first-order classes in the ordered
basis (([1],[x],[x^2])):

\[
\begin{array}{c|c}
\text{point}&\text{first source-normal class}\\
\hline
t=1,\ b=1&(0,0,0)\\
t=1,\ b=2&(0,0,-12)\\
t=-1,\ a=1&(0,0,0)\\
t=-1,\ a=2&(0,0,-12)
\end{array}
\]

At the parameter-1 pair, the first visible class occurs at second normal
order and is (-2[x^2]). At fourth order the constant class appears.

At the parameter-2 pair, first order already supplies (-12[x^2]), and the
third and fourth orders supply the constant class.

In every case the first four orders span a rank-two plane, and that plane is
exactly (langle[1],[x^2]angle).

## Why the odd class is absent

The frozen Cayley--Menger polynomial depends on the labelled soft loop edge
(x) through even powers. External-parameter differentiation preserves this
involution. Its image therefore cannot contain ([x]).

This is a source symmetry statement, not a missing-algebra statement: Entry
3589 proves that ([x]) exists as the first coordinate-soft normal grade.

## Classification

- Existing carrier: external-soft and coordinate-soft incidence.
- Source-defined transport: the rank-two even (A_3) plane.
- Unselected coefficient direction: the odd class ([x]).
- New carrier datum: none.

The only admissible remaining source of physical access to ([x]) is an
oriented coordinate-boundary or relative-chain map. It cannot be manufactured
from further external-normal derivatives.

## Next falsifier

Restrict the source Cayley--Menger relative cycle to one labelled coordinate
soft boundary and derive its local boundary current in the (A_3) model.
Test whether its class pairs nontrivially with ([x]), including orientation,
deck character, and source normalization. If the source does not define this
boundary comparison, classify it as undefined rather than zero.

## Evidence

- `research/benincasa/checkers/check_shape_external_soft_a3_source_tangent.py`;
- `research/benincasa/results/shape-external-soft-a3-source-tangent.json`.

Allocator claim: `seqclaim-9b4e5e24076e6fecf461cebf`.
