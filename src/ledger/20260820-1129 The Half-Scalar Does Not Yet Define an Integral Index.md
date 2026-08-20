---
title: "The Half-Scalar Does Not Yet Define an Integral Index"
date: 2026-08-20
entry: 1129
status: superseded-premise-by-1132
sector: cosmology
---

# 1129 — The Half-Scalar Does Not Yet Define an Integral Index

> **Premise superseded by Entry 1132.** The general warning about rational
> frames is valid, but the particular half-scalar being audited was not a
> typed comparison map.

Sequence claim: `seqclaim-d33957fc5dd1660cf20d7290`.

## Question

Does Entry 1128's rational comparison

\[
\tau\longmapsto-\frac12e_6
\]

prove that the physical soft-node lattice embeds with index two?

## Audit

The node side is integral: the normalization--conductor difference row is
primitive and \(H_1(\mathbb C^*)\simeq\mathbb Z\) has a primitive generator
\(\tau\).

The target packet is different.  The rank-twelve connection and (e_6)
bridge are rational de Rham data.  The existing filtered-cospan checker says
explicitly that its displayed integral columns are *independently rescaled
integral representatives*.  It does not construct the Betti lattice in the
(e_6) line.

Indeed a constant rational target gauge

\[
e_6'=q e_6,\qquad q\in\mathbb Q^\times,
\]

preserves the rational differential module while changing the displayed
scalar to (-1/(2q)).  The choices (q=1,1/2,2) produce respectively

\[
-\frac12,\qquad-1,\qquad-\frac14.
\]

Thus the denominator two is not an integral invariant of the frozen packet.

## Narrow result

\[
\boxed{
\text{the node-to-}e_6\text{ map is canonical over }\mathbb Q,
\quad
\text{its integral index is currently undefined.}
}
\]

Calling it index two would repeat the rational-frame error rejected in Entry
782.  Fixing the index requires an independently derived integral Betti or
relative-homology lattice, polarization, normalized period, or physical
pairing.  No new carrier datum is indicated.

## Evidence and next falsifier

- `research/benincasa/checkers/rank12_soft_node_e6_integral_lattice_gate.py`;
- `research/benincasa/results/rank12-soft-node-e6-integral-lattice-gate.json`;
- Entries 627, 782, 1086, 1103, and 1127--1128.

The next admissible route is to normalize the (e_6) line from the original
Cayley--Menger relative period: derive one source cycle and its intersection
pairing with the (e_6) form, then compare it with the primitive nodal loop.
Absent that datum, the rational comparison is the terminal statement.
