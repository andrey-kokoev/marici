---
author: marici.Benincasa
date: 2026-08-27
---

# 3413 — The Cyclic Occurrence Observer Family Faithfully Reconstructs the Relational Grade

## Question

Entries 3406 and 3410 close the projector route to a unique scalar readout.
Can the source-derived orbit of primitive occurrence comparisons nevertheless
provide a faithful readout without selecting a splitting?

## Observer family

Retain all three primitive two-port instruments from Entry 3384. Their joint
observer is

\[
\mathcal O=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
\]

This matrix is the triangle Laplacian and satisfies

\[
\mathcal OP=P\mathcal O.
\]

It is therefore a cyclic-equivariant vector-valued observer, not a selected
scalar port.

## Reconstruction

The observer has rank two and kernel

\[
\ker\mathcal O=\mathbb Q(1,1,1).
\]

On the relational module

\[
A_2=\ker(1,1,1),
\]

it acts as

\[
\mathcal O|_{A_2}=3\operatorname{id}_{A_2}.
\]

Hence every relational residue (b\in A_2) is reconstructed from its labelled
readout packet (y=\mathcal O b) by

\[
b=\frac13y.
\]

The checker verifies this on the full source orbit and an independent generic
integral (A_2) vector.

## Minimality and symmetry

No single observer row is faithful on (A_2). Every two-row subfamily has rank
two and is algebraically faithful, but each proper subfamily breaks cyclic
closure.

The full three-row orbit is therefore the smallest cyclic-closed family. Its
outputs obey

\[
y_1+y_2+y_3=0.
\]

Consequently invariant scalar aggregation still annihilates every relational
packet. Faithful reconstruction belongs to the labelled vector-valued family,
not to its cyclic-invariant scalar sum.

## Result

The relational (A_2) grade has a source-normalized, equivariant, jointly
faithful observer family that requires neither:

- a denominator-support projector;
- an (e_6) localization splitting;
- a preferred occurrence;
- a new Carrier stratum.

This is the first surviving realization of the final (+1) after the
projector no-go. It also refines the architecture: the final layer need not
land immediately in a scalar. It may first land in a labelled observer packet
whose scalar quotients are instrument-dependent.

## Physical qualification

Entry 2331 remains binding. A source-normalized algebraic observer family is
not yet an outcome-bearing physical instrument. The current result supplies
joint faithfulness and reconstruction, but no apparatus interaction,
conditional successor state, pointer cycle, or repeatability law.

Thus the next physical gate is not another algebraic detector. It is a
source-derived constructor realizing some or all of these labelled ports as
executable outcomes.

## Verification

Checker:
`research/benincasa/checkers/audit_cyclic_occurrence_observer_family.py`.

Packet:
`research/benincasa/results/cyclic_occurrence_observer_family.json`.

Allocator claim: `seqclaim-a5699bcbea45d8f3ec7e9df2`.

Epistemic graph event:
`ev-000000007311-216384b2-c57d-471e-a243-73474f9948e5`.
