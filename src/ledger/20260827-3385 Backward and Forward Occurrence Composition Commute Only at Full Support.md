---
author: marici.Benincasa
date: 2026-08-27
---

# 3385 — Backward and Forward Occurrence Composition Commute Only at Full Support

## Question

Can the middle (+2) of the proposed (3+2+1) architecture be realized as
distinct backward and forward composition operators on the same frozen finite
model?

## Directed incidence operators

Use the three oriented occurrence differences as columns of the forward
boundary operator

\[
F=
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix}.
\]

Forward compositionality sends labelled edge or coherence coefficients to
their occurrence boundary. The source-normalized backward coboundary is

\[
D=F^T.
\]

It evaluates occurrence data on the same labelled differences.

## Full-support square

Exact calculation gives

\[
FD=DF=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}.
\]

Writing

\[
\pi_{A_2}=I-\frac13\mathbf 1\mathbf 1^T,
\]

the common composite is

\[
FD=DF=3\pi_{A_2}.
\]

Thus backward and forward composition are mutually compatible on the complete
labelled triangle. Their common kernel is the invariant line, and their common
restriction to (A_2) is invertible after normalization by (1/3).

## Supported hostile test

Remove the third labelled route with

\[
S=\operatorname{diag}(1,1,0).
\]

The supported operators are

\[
F_S=FS,\qquad D_S=SD.
\]

Their two composites no longer agree. The exact mixed residue is

\[
F_SD_S-D_SF_S=
\begin{pmatrix}
-1&1&-1\\
1&-1&-1\\
-1&-1&2
\end{pmatrix}.
\]

Its rank is three. This falsifies the initial expectation that support deletion
would leave only another rank-two (A_2) residue. The incompatibility can reach
the invariant direction even though the full-support composite kills it.

Reversing one forward orientation while retaining the backward source
orientation also produces a nonzero defect. Hence the strict square depends on
the shared labelled orientation, not merely on equal dimensions.

## Narrow result

The middle (+2) admits a finite operational realization:

- backward compositionality is the occurrence coboundary;
- forward compositionality is the occurrence boundary;
- their full-support comparison closes strictly;
- deleting one route creates a full-rank mixed commutator.

This makes the interaction of the two towers support-sensitive. The mixed
residue is not reducible to either tower separately.

## Scope

This is an occurrence-incidence theorem. Identifying the supported commutator
with a cosmological physical class still requires source-derived Cut/sewing
maps and an instrument comparison. No new carrier stratum is proposed.

## Verification

Checker:
`research/benincasa/checkers/audit_backward_forward_occurrence_composition.py`.

Packet:
`research/benincasa/results/backward_forward_occurrence_composition.json`.

Allocator claim: `seqclaim-c9543ab4b508584e5f7a7788`.

Epistemic graph event:
`ev-000000007254-443b2daf-0ab7-438d-9f55-7780ab0a1a77`.
