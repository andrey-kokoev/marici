---
title: "The P6-Wall Exceptional Divisor Reopens One Relative-Sign Slot"
entry: 1767
date: 2026-08-21
status: established-indicial-slot
---

# 1767 — The (P_6)-Wall Exceptional Divisor Reopens One Relative-Sign Slot

## Question

Entry 1766 proves that the relative-sign extension is gauge-removable at a
generic point of (P_6=0).  Can an existing deeper carrier intersection
change the indicial spectrum and reopen a supported extension slot?

## Exceptional residues

Consider a transverse branch of either

\[
P_6=D=0
\qquad\text{or}\qquad
P_6=H=0.
\]

On the ordinary blowup, the exceptional residue is the sum of the two
incident logarithmic residues.

In doubled units, Entry 867 gives the split algebraic target spectrum

\[
(-1,0).
\]

Entries 864 and 874 give the marked quotient spectrum along either wall:

\[
(0,0,-1).
\]

The (-1) source eigendirection is labelled:

- wall 1 at (D=0);
- wall 2 at (H=0).

## Hom-indicial calculation

The zero-exponent pairs are exactly

\[
(-1)-(-1)=0
\]

once, and

\[
0-0=0
\]

twice.  Therefore

\[
\boxed{
\dim\ker L_0^{\rm exc}=3,
\qquad
\dim\ker L_0^{\rm exc}|_{\mathcal L_-}=1.
}
\]

The total zero-exponent multiplicity remains three, but one resonant slot
has moved from the trivial-monodromy line to the relative-sign line.

## Narrow result

The generic (P_6) obstruction is not uniform over its compactification.
At the existing codimension-two (P_6)-wall intersections, one and only one
labelled relative-sign extension slot is indicially admissible.

This does not prove that the source extension occupies that slot.  The next
finite falsifier is the exceptional normal symbol of the complete marked
extension:

\[
\operatorname{gr}_{(P_6,D)}B
\quad\text{and}\quad
\operatorname{gr}_{(P_6,H)}B,
\]

projected respectively from the labelled wall-1 and wall-2 source directions
to (mathcal L_{P_6^{-1/2}}).  A zero projection closes the route; a nonzero
projection constructs a genuine supported coefficient extension on the
unchanged carrier.

## Durable artifacts

- checker: `research/benincasa/checkers/p6_wall_exceptional_indicial.rs`;
- result: `research/benincasa/results/p6-wall-exceptional-indicial.json`;
- convention note: `research/benincasa/p6-wall-exceptional-indicial.md`;
- allocator claim: `seqclaim-84f2300006f69d6a82dc1b5d`.

