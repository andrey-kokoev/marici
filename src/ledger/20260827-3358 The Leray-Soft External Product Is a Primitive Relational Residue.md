---
author: marici.Benincasa
date: 2026-08-27
---

# 3358 — The Leray–Soft External Product Is a Primitive Relational Residue

## Question

Entry 3357 separates universal composability from instrument-indexed scalar
readout. Can the fifth tower already construct a canonical relational residue
from the frozen vertical and horizontal incidence data?

## Frozen difference lines

The vertical integration-fiber boundary is

\[
d_f=[p_+]-[p_-]=(-1,1)
\]

in the ordered basis \((p_-,p_+)\).

The horizontal base-soft divisor difference is

\[
d_b=[s_3]-[s_2]=(1,-1)
\]

in the ordered basis \((s_3,s_2)\).

These vectors belong to different variance directions. They must not be
identified componentwise. Their canonical composable construction is the
external product

\[
R_{fb}=d_f\otimes d_b.
\]

## Exact relational cell

In the ordered corner basis

\[
(p_-,s_3),\ (p_-,s_2),\ (p_+,s_3),\ (p_+,s_2),
\]

the cell is

\[
R_{fb}=
\begin{pmatrix}
-1&1\\
1&-1
\end{pmatrix}.
\]

It has the following intrinsic properties:

- rank one;
- primitive integral coefficients;
- zero row sums;
- zero column sums;
- odd parity under reversal of either one orientation;
- even parity under simultaneous reversal of both orientations.

The vanishing row and column sums express that the cell is purely relational:
forgetting either the vertical occurrence label or the horizontal soft label
kills it.

## Interpretation

This cell is a concrete fifth-tower output. It records which two incidence
directions were composed and the residue that survives only while both labels
are retained. It contains no scalar physical amplitude.

Its reduced span is one-dimensional, matching the rank of the
\(q_0\)-by-\(e_6\) logarithmic extension residue. That rank match does not yet
identify the two objects. A source-derived comparison is still required:

\[
\kappa:
\mathbb Q\langle R_{fb}\rangle
\longrightarrow
R_{q_0,e_6}.
\]

The fifth-tower naturality test is whether \(\kappa\) is forced by the complete
four-stratum specialization and commutes with both boundary operators. No
instrument or scalar pairing is involved in this test.

## Consequence for the instrument relation

If \(\kappa\) exists, an instrument constructor may subsequently attach:

- a \(q_0\) preparation port to the horizontal leg;
- the established physical \(e_6\) boundary to the vertical leg.

Only their contraction can produce a number. The universal residue itself
remains the primitive four-corner matrix above.

## Finite falsifier

Export the vertical and horizontal boundary maps of the weighted
four-stratum relative complex in the same corner basis. Test the mixed square

\[
d_fd_b+d_bd_f=0
\]

with its Koszul sign and determine the induced class on the rank-twelve
extension costalk.

- A canonical nonzero image establishes \(\kappa\).
- A zero image means the combinatorial residue does not activate the
  rank-twelve extension.
- Lift dependence means the proposed fifth-tower comparison is not natural.

## Scope

This entry constructs the primitive combinatorial relational residue. It does
not prove its identification with the coefficient extension or its activation
by a physical instrument.

## Verification

The checker is
`research/benincasa/checkers/audit_bigraded_leray_soft_residue.py`; its packet
is `research/benincasa/results/bigraded_leray_soft_residue.json`.

Allocator claim: `seqclaim-8931d5320cf78f2a3ed00836`.

Epistemic graph event:
`ev-000000007201-c765aa2d-baeb-41d8-8242-423e1491d3d1`.
