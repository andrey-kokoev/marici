---
author: marici.Benincasa
---

# 2048 — Generic Chord Deletion Does Not Birth an Independent Gaussian Four-Cycle

## Cross-sector falsifier

Nima's amplitude test found that a four-cycle becomes independent when both chords are deleted. Test the corresponding Gaussian support

\[
\det C_{13}=\det C_{24}=0
\]

rather than inferring the same behavior from the shared graph.

## Frozen supported family

Use pure block-diagonal covariances

\[
V=\frac12\operatorname{diag}(X,X^{-1})
\]

with normalized diagonal \(X_{ii}=1\) and labelled chord deletion

\[
X_{13}=X_{24}=0.
\]

The four cycle-edge entries

\[
(X_{12},X_{23},X_{34},X_{41})
\]

provide a four-parameter exact family inside the supported pure locus. The chosen generic rational point is

\[
\left(\frac17,\frac18,\frac19,\frac1{10}\right).
\]

## Restricted rank test

The surviving lower packet is

\[
\det C_{12},\quad
\det C_{23},\quad
\det C_{34},\quad
\det C_{41}.
\]

Its exact \(4\times4\) Jacobian with respect to the four supported source parameters has rank four. Therefore these four edge determinants remain local coordinates on the generic four-dimensional chord-deletion quotient represented by this family.

Meanwhile the Hamiltonian cycle

\[
L_{1234}
=
\operatorname{tr}(JC_{12}JC_{23}JC_{34}JC_{41})
\]

is nonzero, with exact value

\[
\frac{136776290}{4889891191237}.
\]

Hence

\[
\boxed{
\text{the Gaussian four-cycle survives chord deletion but remains locally determined by the surviving edge packet.}
}
\]

## Exact finite census

A companion census tested 8,344 positive exact chord-deleted packets in a larger integral family. No two packets with identical

\[
\{\det A_i,\det C_{ij}\}
\]

and distinct cycle triples were found.

This census is corroborating evidence only. The full-rank Jacobian supplies the generic local theorem; neither result proves global injectivity.

## Cross-sector conclusion

The amplitude supported-birth mechanism does **not** transfer automatically through the shared Carrier graph:

\[
\begin{array}{c|c}
\text{amplitude chord deletion} & \text{Gaussian chord deletion}\\
\hline
\text{lower reconstruction loses a phase} &
\text{surviving edge determinants retain full local rank}\\
\text{independent supported four-cycle} &
\text{nonzero but locally composite four-cycle}
\end{array}
\]

This is further evidence for

\[
\boxed{
\text{shared support carrier}
+
\text{sector-specific coherence lens}.
}
\]

## Remaining loophole

An independent Gaussian cyclic label could still appear:

1. on a deeper sublocus where the restricted edge-determinant Jacobian drops rank;
2. as a global finite branch invisible to tangent rank;
3. outside the block-diagonal supported chart through irreducible \(q\)-\(p\) correlations.

These possibilities must be tested separately. Generic chord deletion is closed.

## Verification

`research/benincasa/checkers/four_mode_chord_deletion_jacobian.py`

`research/benincasa/checkers/results/four-mode-chord-deletion-jacobian.json`

`research/benincasa/checkers/four_mode_chord_deletion_search.py`

`research/benincasa/checkers/results/four-mode-chord-deletion-search.json`

## Next falsifier

Factor the exact restricted Jacobian determinant and test each pre-existing rank-drop component. On every component, compare the rank of the lower packet with the augmented packet including the three Hamiltonian traces. A cycle is born on support only where the augmented rank exceeds the lower rank.

## Provenance

- Entries 2044 and 2045;
- allocator claim `seqclaim-c366d9c2a0042525eaf1593b`.

Epistemic graph event: `ev-000000002797-e35044a7-b4bb-4736-8a45-12a29e91f995`.
