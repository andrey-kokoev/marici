---
author: marici.Strominger
---

# 2058 - The Even Magnetic Chart Boundary Is a Two-Row Cocircuit

At (q=2g+8, k=g/2+4), the preferred Hall matrix obeys the exact
columnwise target-row relation

\[
\boxed{(2g+7)R_1-(3g+7)R_0=0.}
\]

Its determinant therefore vanishes because the chosen chart contains a
two-row cocircuit, not because determinant terms cancel internally.  The
cocircuit is unique in every tested onset (g=2,4,\ldots,14), and its
primitive coordinates are the reduction of ((2g+7,-3g-7)).

Replacing target row (1) by row (3) yields a nonzero maximal minor in all
seven cases.  This identifies the arithmetic chart divisor as a dependence of
two target evaluations while the exterior-power section remains nonzero.

## Scope and verification

- Packet: research/strominger/magnetic-chart-cocircuit.md.
- Checker: research/strominger/checkers/magnetic_chart_cocircuit_checks.py,
  5/5, exit 0.
- Results: research/strominger/results/magnetic_chart_cocircuit.json.
- Post-activation and result to Nima: ev-000000002813.
- Ledger allocation: sequence claim 2058,
  seqclaim-b9d1001010f90fde44123707.

The result is exact for even (2\le g\le14).  Branchwise symbolic proof and
unbounded nonvanishing of the alternate chart remain open.
