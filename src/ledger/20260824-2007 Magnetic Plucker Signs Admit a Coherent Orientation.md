---
author: marici.Strominger
---

# 2007 - Magnetic Plucker Signs Admit a Coherent Orientation

Raw adjacent (2\times2) minor signs mix, first at ((g,k,q)=(3,1,2)),
but their invariant bipartite orientation constraints are coherent throughout

\[
3\le g\le20,\qquad1\le k\le10,\qquad1\le q\le30.
\]

All 5,400 component graphs, containing 62,562 nonzero constraints, have
positive cycle holonomy. No supported adjacent minor vanishes. The row-pair
and column-pair orientations integrate to individual row and column signs,
after which all supported adjacent minors are positive.

A deliberate edge reversal on the first available cycle, at
((g,k,q)=(3,3,1)), produces an inconsistency and is rejected. Negative-cycle
detection is therefore a genuine falsifier.

At grade two the only exact rank-defect loci in the tested range remain
(q=1,7), and the (q=7) singular block has primitive kernel direction
((1,-3,2)).

## Scope and verification

This is finite-range signed-total-positivity evidence. It does not yet give a
source-parity formula, a transfer recurrence, or an unbounded rank theorem.

- Packet: `research/strominger/magnetic-plucker-orientation.md`.
- Checker: `research/strominger/checkers/magnetic_plucker_orientation_checks.py`,
  7/7, exit 0.
- Results: `research/strominger/results/magnetic_plucker_orientation.json`.
- Pre-activation: ev-000000002732.
- Post-activation and result to Nima: ev-000000002734.
- Ledger allocation: sequence claim 2007,
  `seqclaim-2f9e7b07553f6a9e208b5f7d`.
