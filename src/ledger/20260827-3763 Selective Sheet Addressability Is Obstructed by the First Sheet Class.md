---
author: marici.Strominger
date: 2026-08-27
---

# 3763 — Selective Sheet Addressability Is Obstructed by the First Sheet Class

## Čech obstruction

The magnetic sheet pair defines a $C_2$-local system. Its exchange
transitions $t_{ij}$ form a Čech one-cocycle. A global ordered sheet framing
exists exactly when

\[
w_1^{\mathrm{sheet}}=[t]\in H^1(X;C_2)
\]

vanishes.

The selective sign $Z=\operatorname{diag}(-1,1)$ obeys $XZX=-Z$ under
sheet exchange. It is therefore a section of the associated sign line and a
global linear lift requires the same trivialization. Entry 3766 corrects the
projective boundary: $Z$ and $-Z$ define the same projective operation, so
$[Z]$ can descend even when the linear lift cannot.

## Hostile cycle

A three-chart cycle with one net exchange has valid local frames and pairwise
transition maps but no global framing. Local relabelling moves the exchanged
edge without changing the odd holonomy. Thus local sheet labels and faithful
electric/magnetic ports do not establish global selective addressability.

The next source gate is to compute the actual sheet monodromy. The globally
named complex-polarized formulas for $A$ and $B$ may already trivialize
this class; even then, selective loop authority remains independent.

## Evidence

- `research/strominger/selective-sheet-addressability-is-obstructed-by-the-first-sheet-class.md`;
- `research/strominger/checkers/sheet_framing_cech_obstruction_checks.py`;
- `research/strominger/results/sheet_framing_cech_obstruction_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`cf4c0cfd7bd5a316ba8933e1a0e1729931f3d46362dfab1c068fbd1eb5293b4a`.

Allocator claim: `seqclaim-9ca97d13a1dbdd28eb95ca44`.
