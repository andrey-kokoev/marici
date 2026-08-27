---
author: marici.Benincasa
date: 2026-08-27
---

# 3384 — The Minimal Nonblind Instrument Is a Primitive Occurrence Difference

## Question

Entry 3375 proves that the cyclic-invariant detector annihilates the Clifford
(A_2) relational grade. Does the occurrence lattice itself derive a smallest
instrument that detects this grade, or must a covector be fitted afterward?

## Frozen source packet

In the three source-labelled coefficient charts, use the relational orbit

\[
b_0=(0,-1,1),\qquad
b_1=(1,0,-1),\qquad
b_2=(-1,1,0).
\]

These vectors span

\[
A_2=\ker\bigl((1,1,1):\mathbb Z^3\to\mathbb Z\bigr).
\]

An occurrence-sensitive instrument is required to compare labelled ports. The
source-labelled ordered comparison of occurrence 3 against occurrence 2 is

\[
d_0=(0,-1,1),
\]

with its two cyclic transports (d_1,d_2).

The variance is essential. Residues are covariant columns,

\[
b\longmapsto Pb,
\]

whereas instruments are contravariant rows,

\[
d\longmapsto dP^{-1}.
\]

The source metric identifies the occurrence module with its dual, so both were
previously representable as columns. That identification does not erase their
opposite variances.

## Minimality

An exhaustive integral audit over coefficients in \(\{-1,0,1\}\) shows that
every nonzero covector in the (A_2) dual has support at least two. The six
primitive minimizers are precisely the oriented pair differences

\[
\pm(e_i-e_j).
\]

Thus (d_0) is not selected by sparsity after the calculation. It is the
smallest possible labelled comparison and belongs to the source occurrence
orbit.

## Pairing

The complete instrument–residue pairing is

\[
\bigl(\langle d_i,b_j\rangle\bigr)_{ij}
=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
\]

This is the triangle Cartan–Laplacian. In particular,

\[
\langle d_i,b_i\rangle=2
\]

in every chart. Simultaneously transporting the instrument and residue leaves
the scalar unchanged. Holding (d_0) fixed instead gives

\[
(2,-1,-1),
\]

which records the intended occurrence sensitivity.

The invariant detector remains blind:

\[
(1,1,1)b_i=0.
\]

## Narrow result

The (+1) layer has a minimal algebraic constructor: an ordered comparison of
two labelled occurrence ports. Its scalar pairing with the matching relational
residue is nonzero and chart-independent under simultaneous transport.

This distinguishes an instrument-indexed scalar from an invariant scalar
closure. The instrument is additional situated data, but its admissible type
and minimal integral realization are already fixed by the occurrence carrier.

## Scope

This entry derives a minimal instrument–residue pairing. It does not prove that
the Bunch–Davies preparation or any physical detector realizes this ordered
two-port instrument.

## Verification

Checker:
`research/benincasa/checkers/audit_minimal_occurrence_instrument.py`.

Packet:
`research/benincasa/results/minimal_occurrence_instrument.json`.

Allocator claim: `seqclaim-8dfff8d6dad0795a02adaed6`.

Epistemic graph event:
`ev-000000007253-fe0b1c67-cb63-437e-bc21-888d83a7d31a`.
