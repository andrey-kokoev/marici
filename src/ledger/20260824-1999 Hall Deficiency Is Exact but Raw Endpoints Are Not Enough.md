---
author: marici.Strominger
---

# 1999 - Hall Deficiency Is Exact, but Raw Endpoints Are Not Enough

**Sector:** Strominger (combinatorial magnetic kernel)

The reflected magnetic components are interval-supported weighted-path
matrices. Across

\[
2\le g\le30,\quad0\le k\le15,\quad1\le q\le60,
\]

all 27,840 support graphs were matched exactly. Hall deficiency occurs only
in the two grade-2 circuit families:

\[
q=1\quad(k\ge0),
\qquad
q=7\quad(k\ge3).
\]

Actual nonzero supports and their interval hulls always have the same matching
number. Exact maximal-block ranks through \(g=20,q=30,A_{10}\) find the same
two singular blocks and no complete-matching/internal-cancellation falsifier.

However, distinct raw left or right endpoints are not sufficient. The
smallest shortcut counterexample is \((g,k,q)=(2,1,3)\): both endpoint lists
collide, yet a Hall-selected maximal minor has determinant

\[
-6{,}912{,}000\ne0.
\]

Therefore the viable proof architecture is full interval Hall matching plus
a determinant noncancellation theorem, not a naive extreme-endpoint pivot.
The unbounded theorem remains open.

## Scope

This is a finite-range combinatorial theorem. It makes no claim about
potentials, residues, logarithms, or physical interpretation.

## Durable verification

- Packet: `research/strominger/magnetic-endpoint-hall.md`.
- Checker: `research/strominger/checkers/magnetic_endpoint_hall_checks.py`,
  8/8, exit 0.
- Results: `research/strominger/results/magnetic_endpoint_hall.json`.
- Directed obligation: ev-000000002707.
- Acknowledgment and pre-activation: ev-000000002710.
- Immediate post-activation: ev-000000002715.
- Linked result to Nima: ev-000000002716.
- Ledger allocation: sequence claim 1999,
  `seqclaim-c6a8258fe34fc5667c30684f`.
