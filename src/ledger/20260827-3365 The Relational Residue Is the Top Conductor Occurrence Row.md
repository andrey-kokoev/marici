---
author: marici.Benincasa
date: 2026-08-27
---

# 3365 — The Relational Residue Is the Top Conductor Occurrence Row

## Question

Entry 3358 constructs the primitive four-corner residue

\[
R_{fb}=
\begin{pmatrix}
-1&1\\
1&-1
\end{pmatrix}.
\]

Entry 3362 rejects the raw second-Rees coefficient as a realization of this
cell. Does the frozen source contain a gauge-independent occurrence map with
the same relational content?

## Source occurrence quotient

Entry 312 derives the unimodular quotient

\[
K=
\begin{pmatrix}
0&0&1&-1\\
0&1&0&-1\\
1&-1&-1&1
\end{pmatrix},
\]

with

\[
\ker K=\mathbb Z(1,1,1,1).
\]

Its rows are the two primitive wall occurrences and the top conductor
occurrence. In the compatible four-corner order, flattening \(R_{fb}\) gives

\[
(-1,1,1,-1).
\]

The top row of \(K\) is

\[
(1,-1,-1,1)=-R_{fb}.
\]

The minus sign is the orientation sign between the vertical-first tensor
order of Entry 3358 and the source enhanced-point order of Entry 312.

Thus the fifth-tower residue is not a newly fitted object. It is exactly the
top component of the already source-derived augmentation quotient.

## Conductor realization

Entry 312 also derives

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}
\]

and the exact factorization

\[
\Phi_{\mathrm{exc}}=JK.
\]

In the enhanced character basis, the three conductor columns are

\[
c_1=(2,0,0),
\qquad
c_2=(0,2,0),
\qquad
c_{\mathrm{top}}=(1,1,1).
\]

The common top line after removing the two wall legs is

\[
c_{\mathrm{top}}-\frac12c_1-\frac12c_2=(0,0,1).
\]

Entry 367 identifies this remaining coordinate with the common \(e_6\)
bridge in the filtered Cut–nearby cospan.

## Result

The fifth-tower composability residue has a source-derived realization:

\[
R_{fb}
\longrightarrow
\widetilde g_{111}
\longrightarrow
\langle e_6\rangle.
\]

This realization is integral and gauge-independent because it is defined by
the occurrence quotient \(K\) and conductor map \(J\), not by a selected
rank-twelve primitive or raw Rees coefficient.

It does not produce a scalar physical readout. It establishes only the
universal relational route from the four-corner occurrence cell to the common
coefficient bridge.

## Remaining comparison

The current result realizes the residue in the common \(e_6\) bridge. The
global tangent extension studied in Entries 3315–3345 additionally requires
cyclic transport of that bridge around the two soft divisors. The next test is
therefore whether the source-derived cyclic Leray transition carries this
specific top conductor row to the intrinsic logarithmic extension class,
rather than merely carrying an abstract rank-one frame.

No instrument pairing enters that test. A physical scalar remains conditional
on a separate preparation–instrument constructor.

## Verification

The checker is
`research/benincasa/checkers/audit_relational_residue_conductor_realization.py`;
its packet is
`research/benincasa/results/relational_residue_conductor_realization.json`.

Allocator claim: `seqclaim-78ff6cb092ef51bf6695635c`.

Epistemic graph event:
`ev-000000007218-ddfa8b7e-7dd2-4944-816f-b3cf8b24aa55`.