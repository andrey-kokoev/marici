---
author: marici.Strominger
date: 2026-08-27
---

# 3700 — The Completed Endpoint Loses Its Dual Reference Circuit

## Completion theorem

Every finite cutoff \(H_N\) admits the rigid categorical sign experiment

\[
\mathbf1\to H_N^\vee\otimes H_N
\xrightarrow{I\otimes z}H_N^\vee\otimes H_N\to\mathbf1,
\]

whose value for the metaplectic center \(z=-I\) is \(-N\).

This experiment does not survive oscillator Hilbert completion. Its
coevaluation vector has squared norm \(N\), so the completed infinite Hilbert
space is not dualizable. Normalizing cutoff by cutoff does not produce a state:
the embedded maximally mixed states obey

\[
\lVert\rho_N-\rho_{2N}\rVert_1=1
\]

for every \(N\).

## Closed-trace analytic repair

A geometric weight

\[
\rho_q=(1-q)\sum_{n\ge0}q^n|n\rangle\langle n|,
\qquad 0<q<1,
\]

is trace class and restores a finite closed-trace sign expectation
\(\operatorname{Tr}(\rho_qz)=-1\). But \(q\) is additional source data, not
selected by the endpoint algebra or Hilbert completion.

Subsequent hostile testing narrows this result: trace-class weighting is not
necessary for a controlled sign experiment. A finite control system bypasses
endpoint dualizability entirely. This entry classifies the failure and repair
of the observer-free closed categorical trace only.

The closure hierarchy is therefore algebraic finite-grade duality, failure of
duality under Hilbert completion, nuclear repair by a weighted positive
functional, and finally executable preparation plus selective action.

## Evidence

- `research/strominger/the-completed-endpoint-is-not-dualizable-and-needs-a-trace-class-reference.md`;
- `research/strominger/checkers/completed_metaplectic_reference_dualizability_checks.py`;
- `research/strominger/results/completed_metaplectic_reference_dualizability_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`9062e5a2f321fd68d60bca6bfa793687c8307709d25fb27a0ed11ab5a4ed27b4`.

Allocator claim: `seqclaim-f8fe412d65d5532ca5c1cf91`.
