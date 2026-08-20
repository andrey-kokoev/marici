---
title: "The Mod-Four Conductor Carries Two Mod-Two Parity Grades"
date: 2026-08-20
entry: 1143
status: established-finite-coefficient-grade
sector: cosmology
---

# 1143 — The Mod-Four Conductor Carries Two Mod-Two Parity Grades

Sequence claim: `seqclaim-2b4f5aecca0ab64aa74bb43e`.

## Rational result revisited integrally

Entries 1101--1102 identify the anti-invariant normalization/conductor
complex as

\[
[R\xrightarrow{2}R].
\]

Over characteristic zero it contracts by \(h=1/2\), including on the faces

\[
s=0,
\qquad B-1=0,
\qquad s=B-1=0.
\]

Entry 1142 supplies the transported finite coefficient quotient

\[
\mathcal D_{e_6}=\mathbb Z/4.
\]

On this coefficient object the same typed conductor complex is

\[
\boxed{
[\mathbb Z/4\xrightarrow{2}\mathbb Z/4].}
\]

## Exact finite cohomology

Multiplication by two on \(\mathbb Z/4\) has

\[
\ker(2)=\{0,2\}\simeq\mathbb Z/2,
\]

and image \(\{0,2\}\), hence cokernel \(\mathbb Z/2\). Therefore

\[
\boxed{
H^0\simeq\mathbb Z/2,
\qquad
H^1\simeq\mathbb Z/2.}
\]

The rational contraction cannot descend because \(1/2\) does not exist in
\(\mathbb Z/4\). Derived restriction to either support face and their corner
does not change the constant differential, so the same pair of
\(\mathbb Z/2\) grades survives on all four tested loci.

Reduction modulo two makes the differential zero and gives the same two
one-dimensional parity grades directly.

## Type verdict

This is the first structure in this branch that is genuinely invisible over
\(\mathbb Q\): the finite quarter-lattice quotient remembers the parity map
that rational normalization descent contracts.

It is not yet physical cohomology. Entry 1104's labelled Gysin simplex is a
separate typed complex, integrally contractible by unit incidence maps. No
map identifying its totalization with the finite conductor complex has been
constructed here.

The narrow conclusion is

\[
\boxed{
\text{the transported }\mathbb Z/4\text{ coefficient quotient carries}
\quad
\mathbb Z/2\text{ grades in conductor degrees }0\text{ and }1.}
\]

No new carrier datum is required; this is finite coefficient/Cartier data
on the existing normalization conductor.

## Next falsifier

Construct the integral totalization relating the normalization/conductor
complex to the three-face Gysin simplex. Preserve occurrence labels, deck
signs, and support variance. Determine whether the two \(\mathbb Z/2\)
grades cancel, extend one another into \(\mathbb Z/4\), or survive as a
supported finite coefficient class. Do not infer the answer from dimensions.

Evidence:

- `research/benincasa/checkers/rank12_e6_mod4_conductor.py`;
- `research/benincasa/results/rank12-e6-mod4-conductor.json`;
- Entries 1100--1104 and 1140--1142.
