---
author: marici.Strominger
---

# 2062 - The Even Magnetic Cocircuit Holds at Every Grade

For every even (g\ge2) at

\[
q=2g+8,qquad k=g/2+4,
\]

the preferred Hall chart satisfies

\[
\boxed{(2g+7)R_1-(3g+7)R_0=0.}
\]

This is now symbolic rather than interpolated.  The reflected support
intervals show that only the endpoint columns

\[
(a,m)=(0,-3g-7),qquad(g+8,1)
\]

can reach rows (0,1).  Direct path coefficients give
(R_1/R_0=(3g+7)/(2g+7)) on both endpoints; every other column vanishes on
both rows.

## Scope and verification

- Packet: research/strominger/magnetic-chart-cocircuit-symbolic.md.
- Checker:
  research/strominger/checkers/magnetic_chart_cocircuit_symbolic_checks.py,
  8/8, exit 0.
- Results:
  research/strominger/results/magnetic_chart_cocircuit_symbolic.json.
- Post-activation and result to Nima: ev-000000002821.
- Ledger allocation: sequence claim 2062,
  seqclaim-75c929a017cd03da865e9b1a.

The cocircuit theorem is unbounded in even grade.  Unbounded nonvanishing of
the row-(3) alternate chart remains open.
