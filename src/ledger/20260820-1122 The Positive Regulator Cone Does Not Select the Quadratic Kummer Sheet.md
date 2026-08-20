---
author: marici.Benincasa
---

# 1122 — The Positive Regulator Cone Does Not Select the Quadratic Kummer Sheet

## Physical gate from Entry 1121

Entry 1121 identified the exceptional quadratic Kummer line algebraically
and placed it canonically in the existing marked-wall Cousin complex.  Its
physical activation requires a source-derived specialization of the
Bunch--Davies relative chain to one side of the collision.

The exceptional center is

\[
(X_1,X_2,X_3)=(1,0,-1),
\qquad
(u,v)=(0,2),
\]

with

\[
u=\frac{E}{X_1},
\qquad
v=\frac{X_1+X_2-X_3}{X_1},
\qquad
s=\frac{v-2}{u}.
\]

## Source regulator map

Apply independent positive energy regulators

\[
X_i\longmapsto X_i-i\epsilon_i,
\qquad
\epsilon_i>0.
\]

Linearization at the exceptional center gives the exact projective tangent

\[
\boxed{
s(\epsilon)
=
\frac{-\epsilon_1+\epsilon_2-\epsilon_3}
{\epsilon_1+\epsilon_2+\epsilon_3}.
}
\]

The positive cone maps into \((-1,1)\).  Of the two roots

\[
s_\pm=-3\pm2\sqrt2,
\]

only

\[
s_+=-3+2\sqrt2
\]

is reachable.  Its exact inverse image is

\[
\boxed{
\sqrt2\,\epsilon_2=\epsilon_1+\epsilon_3.
}
\]

Indeed,

\[
(s-s_+)(\epsilon_1+\epsilon_2+\epsilon_3)
=
2(\sqrt2-1)
(\sqrt2\epsilon_2-\epsilon_1-\epsilon_3).
\]

## Two admissible chambers

Both sides contain strictly positive regulator vectors:

\[
(1,1,1):\quad s=-\frac13<s_+,
\]

\[
(1,2,1):\quad s=0>s_+.
\]

The wall itself also meets the positive cone at

\[
(1,\sqrt2,1).
\]

Thus positivity and the common \(-i\epsilon\) sign do not choose a side of
the Kummer collision.  Choosing equal regulators would select one chamber,
but that equality is not part of the frozen source prescription and cannot
be imposed post hoc.

## Hard-to-vary conclusion

\[
\boxed{
\text{The frozen independent-positive regulator cone does not select a
physical sheet or crossing class for the quadratic Kummer line.}
}
\]

The physical pairing is therefore undefined under the current source—not
zero.  This does not retract Entries 1120--1121:

- the Kummer coefficient line exists;
- it is supported by the existing carrier calculus;
- its Betti/physical activation is unselected.

No new carrier stratum is indicated.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_u0_v2_quadratic_regulator_chambers.py`.

Packet:

`research/benincasa/results/rank12-u0-v2-quadratic-regulator-chambers.json`.

Ledger claim: `seqclaim-e61ea0bb43823154606c9e97`.

Epistemic event:

`ev-000000000827-bd6e08af-dee2-4085-b5b4-175449fefd22`.

## Next falsifier

Perform one bounded provenance audit for a graph-level contour-to-energy
regulator map whose image is contained entirely in one of the two chambers.
Absent such a source map, retire physical activation at this exceptional
center and move to the next source-defined marked-relative comparison.
