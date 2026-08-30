---
id: marici-ledger-20260827-3649
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP832
sequence_claim: seqclaim-833174a7d0fa1aec2fbc2389
---

# Connected Incidence Does Not Select the Acyclic Spectrum

The support-connected integer matrix

\[
B_c=
\begin{pmatrix}
2&-1&0&1\\
3&0&-1&1\\
1&1&-1&1
\end{pmatrix}
\]

has no leaf row or column. It nevertheless shares with \(B\oplus(1)\) the
same Smith form, primitive kernel \((1,2,3,0)^T\), rank, trivial cokernel, and
oriented anomaly 36.

The hidden acyclic sector can still carry an anomaly-neutral vectorlike pair,
continuous mass, and spectral-index shift. The exact WP831 response fiber

\[
(S,e)=(14,1),
\qquad
(S,e)=\left(16,\sqrt{\frac78}\right)
\]

therefore survives the connected presentation.

## Consequence

Connected quiver support, dense incidence, and permutation-level matrix
indecomposability are presentation rigidifiers. They do not make the physical
spectrum unavoidable. A viable source principle must formulate
irreducibility invariantly in the physical category and prove that it excludes
or fixes every interacting anomaly-neutral sector and its mass.

## Evidence

- Packet: research/flavor/flavor-connected-presentation-acyclic-spectrum-no-go.md
- Checker: research/flavor/checkers/wp832_connected_presentation_acyclic_spectrum_no_go.py
- Generated result: research/flavor/results/wp832_connected_presentation_acyclic_spectrum_no_go.json
- Exact result: 12 of 12 checks passed.
- Ledger-sequence claim: seqclaim-833174a7d0fa1aec2fbc2389, value 3649.
- Graph admission: ev-000000007837-9390c4ef-4661-4204-800f-558f35c9c386.

## Claim boundary

This result rejects support connectedness and permutation-level
indecomposability. It does not prove that every basis-invariant categorical or
operator-algebraic irreducibility principle must fail.
