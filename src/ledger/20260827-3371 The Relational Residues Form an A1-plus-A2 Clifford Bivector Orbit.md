---
author: marici.Benincasa
date: 2026-08-27
---

# 3371 — The Relational Residues Form an A1-plus-A2 Clifford Bivector Orbit

## Question

Entry 3365 identifies one Leray–soft relational residue with the top conductor
occurrence row. Can the three cyclic occurrence sectors be organized in a
source-derived Clifford algebra without choosing a convenient metric?

## Source lattices

Let \(f\) be the primitive vertical Leray difference. It spans an \(A_1\)
root lattice with

\[
(f,f)=2.
\]

The three soft-divisor differences lie in the energy-shape lattice

\[
A_2=\ker(\mathbb Z^3\xrightarrow{(1,1,1)}\mathbb Z).
\]

In a simple-root basis its Cartan form and cyclic action are

\[
C=
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
0&-1\\
1&-1
\end{pmatrix}.
\]

Exact calculation gives

\[
R^3=1,
\qquad
R^TCR=C.
\]

## Metric gate

The global occurrence space is

\[
V=A_{1,\mathrm{Leray}}\oplus A_{2,\mathrm{soft}}.
\]

A cross metric between the fixed \(A_1\) generator and the \(A_2\) plane
would be an invariant covector \(c\) satisfying

\[
cR=c.
\]

The coefficient matrix of this equation has rank two, so \(c=0\). Thus cyclic
naturality forces the two variance directions to be orthogonal.

Among symmetric forms on \(A_2\), the equation

\[
R^TSR=S
\]

has a one-dimensional solution space. Primitive root norm two fixes its scale
to the Cartan form \(C\). The resulting source-normalized Gram matrix is

\[
Q=
\begin{pmatrix}
2&0&0\\
0&2&-1\\
0&-1&2
\end{pmatrix}.
\]

The global cyclic transport

\[
T=1\oplus R
\]

satisfies

\[
T^3=1,
\qquad
T^TQT=Q.
\]

Therefore the Clifford algebra \(\operatorname{Cl}(V,Q)\) is source-derived
from the primitive occurrence lattices and their cyclic transport. No
Euclidean metric was added after seeing the desired bivector.

## Bivector orbit

Choose the source-labelled soft root

\[
\alpha_{32}=e_3-e_2.
\]

Its cyclic orbit consists of three norm-two roots whose sum is zero. The
three relational residues are

\[
B_i=f\alpha_i,
\qquad
\alpha_i\in
\{\alpha_{32},R\alpha_{32},R^2\alpha_{32}\}.
\]

Because \(f\) is orthogonal to every \(\alpha_i\),

\[
f\alpha_i=-\alpha_if,
\qquad
B_i^2=-4.
\]

Their orbit closes under \(T\), and

\[
B_0+B_1+B_2=0.
\]

This is the Clifford form of Entry 3326’s conclusion: the global object is an
\(A_2\)-valued boundary cocycle. It cannot be collapsed to a cyclic-trivial
line by an ordinary equivariant projection.

## Hostile metric test

The checker inserts the nonzero cross term \(c=(1,0)\). Its cyclic invariance
defect is nonzero. Thus the orthogonal direct sum is not an aesthetic choice;
the simplest competing cross metric is explicitly rejected.

## Current frontier

Entry 3365 identifies one local bivector coordinate with the top conductor
row and then with the common \(e_6\) bridge. The next comparison is now
Clifford-equivariant:

\[
\rho_{i+1}(T B_i)
\stackrel{?}{=}
\tau_i\rho_i(B_i),
\]

where \(\tau_i\) is the source cyclic transport on the rank-twelve
coefficient system.

If this square closes for the three bivectors, the induced logarithmic
connection on the transported residue system can be compared with

\[
d\log\frac{X_3}{X_2}.
\]

This remains a universal composability test. An instrument constructor and
scalar physical readout are separate.

## Scope

This entry derives the Clifford metric and cyclic bivector orbit on the frozen
occurrence lattices. It does not yet identify the complete rank-twelve cyclic
transport, select a scalar extension amplitude, or define a physical readout.

## Verification

The checker is
`research/benincasa/checkers/audit_a1_a2_clifford_residue.py`; its packet is
`research/benincasa/results/a1_a2_clifford_residue.json`.

Allocator claim: `seqclaim-a23bd4052bba9e7bc45ec64d`.

Epistemic graph event:
`ev-000000007226-b042c199-dd0f-4eca-805a-c9736cb1bccc`.
