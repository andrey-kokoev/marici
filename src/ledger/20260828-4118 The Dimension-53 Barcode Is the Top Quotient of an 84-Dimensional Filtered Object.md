# 4118 — The Dimension-53 Barcode Is the Top Quotient of an 84-Dimensional Filtered Object

## Claim

The stable modular free-column set from Entry 4113 decomposes by the labelled pole filtration as

\[
84=53+22+7+1+1.
\]

The 53-dimensional summand is exactly the top block

\[
(k;q_1,q_2,q_3,q_{23},q_{31})=(3;2,2,2,2,2).
\]

The remaining 31 columns occupy four lower blocks:

\[
(1;1,1,1,1,1):22,
\]

\[
(3;1,1,1,1,1):7,
\]

\[
(0;1,2,1,1,1):1,
\qquad
(0;2,1,1,1,1):1.
\]

## Evidence

Five independently computed modular eliminations use the same pivot-column set, with SHA-256

`b29007aae732f97de64bdfb73ea75789f7bd9e80ea2d699a42ee60f759cd5b12`.

The primes are

\[
31991, 32003, 32009, 32027, 32029.
\]

Each has rank 2,194 and the same 84 free columns. The column labels come from the characteristic-zero source filtration before reduction.

## Correction

Entry 4113 correctly rejected the identification of the full residual quotient with dimension 53. The present decomposition explains the mismatch more sharply:

- 53 is the top barcode quotient;
- 31 records lower-block extension data retained by the full filtered object.

Thus the old 53-dimensional computation was not numerically wrong. It was a statement about a graded quotient that had been mistyped as a statement about the complete filtered object.

## Interpretation

The integral lift must preserve the extension

\[
0\longrightarrow B_{31}
\longrightarrow F_{84}
\longrightarrow Q_{53}
\longrightarrow0,
\]

where \(Q_{53}\) is the familiar top barcode quotient and \(B_{31}\) is assembled from four labelled boundary blocks.

This identifies the concrete object hidden by fieldwise top-block calculations: not another barcode sector, but the attachment data relating the top quotient to lower pole grades.

The next test is to construct the induced block-triangular residual matrix for \(B_{31}\to F_{84}\to Q_{53}\), then determine whether the extension splits over \(\mathbf Q\), over \(\mathbf Z\), over neither, or only after localizing specific primes.

## Durable artifacts

- `research/benincasa/results/interaction-net-integral-residual-free-labels.json`
- `research/benincasa/results/interaction-net-integral-residual-free-column-classification.json`
- `research/benincasa/checkers/classify_interaction_net_residual_free_columns.cjs`

Sequence claim: `seqclaim-ee7b071f666a1cd8f499468e`.
