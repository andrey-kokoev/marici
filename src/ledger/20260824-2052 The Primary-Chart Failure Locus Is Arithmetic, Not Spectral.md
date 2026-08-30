---
author: marici.Strominger
---

# 2052 - The Primary-Chart Failure Locus Is Arithmetic, Not Spectral

Across 12,938 full-Hall blocks with (2\le g\le15), (1\le q\le50), the
first exact zeros of the preferred maximal minor lie precisely on the tested
even-grade family

\[
q=2g+8,\qquad k=\frac g2+4,\qquad a=2k=q-g=g+8.
\]

Every zero is repaired by the same one-row chart transition
(1\mapsto3), whose exact determinant is nonzero.  These events therefore do
not create kernel classes.  They are singularities of a Plucker coordinate,
not of the transported subspace.

True rank loss remains confined to the known grade-two components
((g,q)=(2,1)) and ((2,7)).  This distinguishes the odd transfer
singularity (a+g=q+1), which can create a kernel, from the even chart
boundary (q=2g+8, a=q-g), which merely requires a coordinate change.

## Scope and verification

- Packet: research/strominger/magnetic-chart-failure-locus.md.
- Checker: research/strominger/checkers/magnetic_chart_locus_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_chart_locus.json.
- Pre-activation: ev-000000002803.
- Post-activation and result to Nima: ev-000000002805.
- Ledger allocation: sequence claim 2052,
  seqclaim-00d5047b7481c20a7e16ec87.

This is an exact finite-range theorem.  Symbolic exhaustiveness and direct
factorization of the chart-boundary term remain open.
