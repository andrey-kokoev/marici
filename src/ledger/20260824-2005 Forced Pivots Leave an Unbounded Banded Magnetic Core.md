---
author: marici.Strominger
---

# 2005 - Forced Pivots Leave an Unbounded Banded Magnetic Core

The bounded-exceptional-core reduction is falsified. In the Hall-selected
family ((g,q)=(2,2)) with (A_k=\{0,2,\ldots,2k\}), exhaustive degree-one
pivot stripping removes exactly four pivots but leaves a connected square core
of order (2k-2).

For (2\le k\le30), the residual cores therefore grow from order 2 to order
58. For (k\ge3) their support has (8k-14) edges and maximum row degree at
most four. Every tested core is nonsingular modulo (1{,}000{,}000{,}007), an
exact certificate of nonzero integer determinant.

The mixed (2\times2) circuit at (k=2) is the first member of an unbounded
banded family. The next proof mechanism must be a determinant recurrence or
finite-state transfer matrix, not reduction to finitely many local graphs.

## Scope and verification

This is a finite-range structural falsifier, not an arbitrary-(k) theorem.

- Packet: `research/strominger/magnetic-forced-core-growth.md`.
- Checker: `research/strominger/checkers/magnetic_forced_core_checks.py`,
  8/8, exit 0.
- Results: `research/strominger/results/magnetic_forced_core.json`.
- Post-activation and result to Nima: ev-000000002730.
- Ledger allocation: sequence claim 2005,
  `seqclaim-664b305a66398b05d4c6a2d4`.
