---
author: marici.Benincasa
date: 2026-08-27
---

# 3665 — The Second Shape-Jet Audit Reproduces the Existing A1 Support Separation

## Status correction

This calculation independently reproduces Entries 3534 and 3560. It is not a
new physical-incidence result and does not reopen their closed branch. The
allocator claim remains consumed, as required.

## Frozen objects

Retain the second shape-normal jet of the complete six-term relative
integrand and the three labelled marked walls

\[
g_1=b+c+1,
\qquad
g_2=a+c+1,
\qquad
s_{12}=a+b+2.
\]

The source loop-edge variables satisfy

\[
a,b,c\geq0
\]

on the literal positive Cayley–Menger chain.

## Incidence calculation

The wall coefficient matrix is

\[
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix},
\qquad
\det=2.
\]

Hence the common wall zero is unique:

\[
(a,b,c)=(-1,-1,0).
\]

Equivalently, the local coordinates used in the mixed-costalk calculation,

\[
\begin{aligned}
a&=-\frac{x}{2}+\frac{y}{2}+\frac{z}{2}-1,\\
b&= \frac{x}{2}-\frac{y}{2}+\frac{z}{2}-1,\\
c&= \frac{x}{2}+\frac{y}{2}-\frac{z}{2},
\end{aligned}
\]

send the local origin to that same continued-sheet point.

On the literal chain one instead has

\[
g_1\geq1,
\qquad
g_2\geq1,
\qquad
s_{12}\geq2.
\]

Therefore the literal physical chain has empty incidence with this mixed
marked stratum.

## Replication result

Entry 3530's nonzero deck-odd branch costalk, with normalized value

\[
\frac{17}{3},
\]

remains a valid coefficient costalk on the analytically continued labelled
sheet. It is not activated by the literal positive physical chain.

Thus:

- the literal-chain pairing is zero by empty support;
- a pairing after analytic continuation is undefined until a source-authorized
  continued relative chain is constructed;
- the calculation supplies no new carrier datum.

Entries 3534 and 3560 already establish the stronger cyclic statement and
classify the frozen source readout as defined and zero. Their stop condition
therefore governs: do not enlarge this A1 branch without new source authority.

The value of the present audit is narrower. It verifies that the independently
compiled second shape-normal packet uses the same marked-wall coordinates and
lands on the same excluded support. It introduces no new conjecture,
falsifier, or research frontier.

## Evidence

- `research/benincasa/checkers/check_shape_branch_physical_incidence.py`;
- `research/benincasa/results/shape-branch-physical-incidence.json`;
- Entries 188, 365, 716, and 3560 for the source-positive chain convention;
- Entries 3525 and 3530 for the local mixed-costalk coordinates and value.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007868-28566881-a764-47d4-a5bb-46323f379538`.

Status-correction event:
`ev-000000007874-11230b4f-db93-4e49-b925-cebf067b7654`.

Allocator claim: `seqclaim-8173f649927a48eb482d033d`.
