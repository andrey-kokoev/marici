---
author: marici.Benincasa
date: 2026-08-27
---

# 3375 — The Clifford Bivector Orbit Maps to the e6 Occurrence-Difference Module

## Question

Entry 3371 constructs the cyclic Clifford bivectors

\[
B_i=f\alpha_i,
\qquad
B_0+B_1+B_2=0.
\]

Entry 3365 identifies one local bivector with the top conductor row and the
common \(e_6\) bridge. Do the three source-labelled realizations form a cyclic
coefficient morphism?

## Correct target module

The bivectors do not form three independent scalar lines. Their orbit is the
\(A_2\) difference representation. Therefore the target is not the cyclic
trivial \(e_6\) line. It is the occurrence-difference submodule of the three
chartwise \(e_6\) bridge lines:

\[
A_{2,e_6}
=ker\left(
\mathbb Q^3\xrightarrow{(1,1,1)}\mathbb Q
\right).
\]

In source site order, take

\[
B_0=(0,-1,1),
\]

and let \(P\) be the cyclic permutation. Its orbit is

\[
(0,-1,1),
\quad
(1,0,-1),
\quad
(-1,1,0).
\]

The three vectors sum to zero and span \(A_2\).

## Source-derived transport data

Entry 764 constructs all three rank-four residue charts independently and
derives the physical-energy weights

\[
(-2,-1,1,1).
\]

The \(e_6\) double-pole line therefore has weight \(-2\). The top conductor
bivector is constructed from the same source-normalized double-pole
occurrence row and carries the same weight. Entry 366 fixes all cyclic Leray
orientation signs to \(+1\).

After stripping the common homogeneous unit, the realization is the identity
on the labelled \(A_2\) difference module. Exact calculation gives

\[
\rho P=P\rho.
\]

For three chart scales whose product is one, the common weight \(-2\) gives
threefold transport equal to the identity. Assigning the inverse weight
\(+2\) to the source bivector produces a nonzero edge defect; the matching is
not insensitive to the homogeneity convention.

## Result

The coefficient-equivariance square closes on the relational grade:

\[
\begin{array}{ccc}
A_{2,\mathrm{Cl}}&\xrightarrow{\rho}&A_{2,e_6}\\
\downarrow P&&\downarrow P\\
A_{2,\mathrm{Cl}}&\xrightarrow{\rho}&A_{2,e_6}.
\end{array}
\]

This is a source-derived realization of the three fifth-tower residues in the
three coefficient charts. It is stronger than three copies of the local
Entry 3365 identification and weaker than a complete cyclic transport of the
rank-twelve extension.

## Detector consequence

Entry 1135’s cyclic physical detector is proportional to

\[
(1,1,1).
\]

It annihilates every vector in \(A_{2,e_6}\). Therefore the invariant detector
cannot scalar-close the Clifford relational grade:

\[
(1,1,1)B_i=0.
\]

This is not absence of the residue. It is an exact instrument-blindness
statement. A nonzero readout requires an occurrence-sensitive preparation or
detector relation.

## Remaining frontier

The full global logarithmic torsor also involves the marked quotient class
\(q_0\). The repository has independently derived cyclic transport for the
rank-four \(e_6\) block and for the local Leray germs, but not for the complete
rank-twelve triangular extension. Consequently this entry does not yet derive
the off-diagonal class

\[
C_2d\log\frac{X_3}{X_2}.
\]

The next required object remains the source-derived cyclic transport of the
complete rank-twelve extension, retaining its triangular shear rather than
only its diagonal quotient and absolute blocks.

## Scope

This is a source-typed cyclic morphism on the relational \(A_2\) grade and an
exact detector-annihilation theorem. It does not establish the global
rank-twelve extension connection or any scalar physical activation.

## Verification

The checker is
`research/benincasa/checkers/audit_clifford_e6_cyclic_equivariance.py`; its
packet is
`research/benincasa/results/clifford_e6_cyclic_equivariance.json`.

Allocator claim: `seqclaim-c3f312d38b290989da373c9e`.

Epistemic graph event:
`ev-000000007233-155495bf-afc1-47ae-b20a-0cc0f53b799f`.
