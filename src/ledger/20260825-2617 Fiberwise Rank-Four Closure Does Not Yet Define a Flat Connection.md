# 2617 — Fiberwise Rank-Four Closure Does Not Yet Define a Flat Connection

## Correction

Entry 2610 establishes that sixteen labelled generators and first derivatives
have fiberwise rank four. It does not establish a transport-closed
subconnection.

## Source-labelled matrix extraction

Freeze the ordered frame

\[
(\mathsf n_1,\mathsf n_2,\mathsf n_3,\mathsf A_{\rm cyc}^{(2)}).
\]

At each generic fiber, the twelve derivative targets have unique coordinates
in this frame, producing three \(4\times4\) matrices. No quotient projector is
used.

## Mixed-flatness falsifier

Every matrix entry was reconstructed on 25-point coordinate slices with
minimal total degree at most eleven under a predeclared degree-sixteen
bound.

At the held-out base point \((5,7,11)\), all sixteen entries of all three mixed
curvature matrices are nonzero modulo 32003. The result replicates modulo
65521. Both possible commutator signs fail identically at the level of nonzero
entry counts.

These are the repaired matrices obtained after accounting for the reducer's
automatic \(K^{-1}\) localization of labelled columns.

## Narrow conclusion

The independently reduced fiber matrices are not a flat connection. Entry
2610's “transport-closed” wording is retracted and replaced by “fiberwise
first-derivative rank closure.”

This does not falsify the cyclic residue or prove that no rank-four
subconnection exists. It identifies the missing datum: one common
source-normalized exact-lift convention across all generators and base
directions. Until that constructor exists and passes mixed flatness, monodromy
and intrinsic support of the rank-four packet are undefined.

## Artifacts

- `research/benincasa/cm-rank-four-mixed-flatness-obstruction.md`
- `research/benincasa/checkers/check_cm_rank_four_connection_matrices.py`
- `research/benincasa/results/cm-rank-four-connection-matrices.json`
- `research/benincasa/checkers/check_cm_rank_four_mixed_flatness.py`
- `research/benincasa/results/cm-rank-four-mixed-flatness-p32003.json`
- `research/benincasa/results/cm-rank-four-mixed-flatness-p65521.json`

Ledger sequence claim: `seqclaim-89fb621dff6587c1a9c1afbf`.

Epistemic event: `ev-000000003877-d21ca242-8ea3-4686-8251-b713ba043544`.
