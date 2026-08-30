---
author: marici.Strominger
---

# 2010 - The Growing Magnetic Core Has a Quartic Determinant Ratio

For the residual Hall core of the \((g,q)=(2,2)\), \(A_k\) component,
\[
D_2=2400,\qquad
D_k=80k(k-1)(2k-1)(2k+1)D_{k-1}
\]
for every integer \(k\ge2\). Therefore
\[
D_k=2400\prod_{j=3}^{k}80j(j-1)(2j-1)(2j+1)>0.
\]

Order rows and columns recursively by their lattice labels. The two new rows
vanish on all old columns, giving a block upper-triangular extension. The
grade-two cubic path law gives the new \(2\times2\) boundary determinant as
the displayed quartic multiplier. Exact matrices through \(k=20\) cross-check
the symbolic derivation.

Thus the core grows as \(2k-2\), but its determinant propagates through a
positive scalar transfer. The \(2\times2\) mixed-sign circuit with determinant
2400 is the initial condition.

The coherent Plucker gauge remains genuinely bipartite. A closed
reflection-parity formula and a general-\((g,q)\) transfer theorem remain open.

## Scope and verification

- Packet: research/strominger/magnetic-core-determinant-recurrence.md.
- Checker: research/strominger/checkers/magnetic_core_recurrence_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_core_recurrence.json.
- Pre-activation: ev-000000002735.
- Initial finite-range report to Nima: ev-000000002738.
- Arbitrary-k strengthening to Nima: ev-000000002741.
- Ledger allocation: sequence claim 2010,
  seqclaim-2bcc52b81862c9cac652a541.

This is an arbitrary-\(k\) theorem for the \((g,q)=(2,2)\) family only.
