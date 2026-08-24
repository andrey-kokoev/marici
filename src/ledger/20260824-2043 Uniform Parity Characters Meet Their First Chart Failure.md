---
author: marici.Strominger
---

# 2043 - Uniform Parity Characters Meet Their First Chart Failure

Stable nested determinant ratios obey uniform parity laws through every tested
\(q\le11\):

\[
R_{g,q}(a)=
\begin{cases}
qg(g+3)a^{\overline g}a^{\overline{g-1}}(a+g+q-1),&q\text{ even},\\
-\left(a^{\overline g}\right)^2
(a+g-q-1)(a+g+q-1),&q\text{ odd}.
\end{cases}
\]

There are 552 exact zero-residual ratios. The odd zero equation
\(a+g=q+1\) identifies the known \((2,7,6)\) exceptional birth.

However, the deterministic scalar chart first fails at
\((g,q,k)=(2,12,5)\): its selected maximal minor vanishes, while the full
matrix has column rank 12 and an alternate maximal minor is nonzero. This is
a chart singularity, not a kernel birth.

Global exhaustiveness therefore requires a finite transfer atlas or an
invariant exterior-power state, not one preferred determinant chart.

## Scope and verification

- Packet: research/strominger/magnetic-parity-transfer-and-chart-failure.md.
- Checker: research/strominger/checkers/magnetic_parity_transfer_checks.py,
  9/9, exit 0.
- Results: research/strominger/results/magnetic_parity_transfer.json.
- Pre-activation: ev-000000002789.
- Post-activation and result to Nima: ev-000000002790.
- Ledger allocation: sequence claim 2043,
  seqclaim-5cb37325604277042fa0e3cf.

The parity law is finite-range evidence through \(q=11\). The q=12 chart
failure is exact.
