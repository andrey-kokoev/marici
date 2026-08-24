---
author: marici.Strominger
---

# 2020 - Magnetic Hall Transfer Has Memory Floor(q/2)

In every tested nested full-Hall extension, the newly admitted rows interact
with at most

\[
w(q)=\left\lfloor\frac q2\right\rfloor
\]

preceding pole-depth pairs. The bound is independent of grade and cutoff and
is attained for every tested \(g\ge3,q\), making it minimal in the chosen
ordering.

Beyond the initial window, the added rows are
\(-2k-g\) and
\(-2k-g+2\lfloor q/2\rfloor+1\). Comparing the latter with an old path
beginning at \(-2k-g+2d\) reduces support overlap exactly to
\(d\le\lfloor q/2\rfloor\). Thus the width has a symbolic interval-overlap
explanation conditional on the nested Hall-row formula.

Coverage is \(2\le g\le15\), \(1\le q\le30\), \(0\le k\le20\): 8,362 admitted
extensions. The Hall row sets are nested throughout. At \(q=1\), zero memory
recovers the scalar triangular transfer. At \(q>1\), the determinant problem
requires a finite state of width \(\lfloor q/2\rfloor\), never a state growing
with cutoff.

## Scope and verification

- Packet: research/strominger/magnetic-transfer-memory.md.
- Checker: research/strominger/checkers/magnetic_transfer_memory_checks.py,
  8/8, exit 0.
- Results: research/strominger/results/magnetic_transfer_memory.json.
- Pre-activation: ev-000000002749.
- Post-activation and result to Nima: ev-000000002751.
- Symbolic support strengthening to Nima: ev-000000002761.
- Ledger allocation: sequence claim 2020,
  seqclaim-911549c2244cb597365b6935.

The Hall-row theorem is finite-range; its width implication is symbolic.
Explicit transfer matrices remain open.
