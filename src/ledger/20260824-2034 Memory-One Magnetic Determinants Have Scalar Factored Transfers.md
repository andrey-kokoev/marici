---
author: marici.Strominger
---

# 2034 - Memory-One Magnetic Determinants Have Scalar Factored Transfers

With \(a=2k\), every tested stable nested determinant ratio at \(q=2,3\)
equals

\[
R_{g,2}(a)=
2g(g+3)a^{\overline g}a^{\overline{g-1}}(a+g+1)
\]

or

\[
R_{g,3}(a)=
-\left(a^{\overline g}\right)^2(a+g-4)(a+g+2).
\]

The memory-one Schur complement is anti-triangular for \(q=2\) and triangular
for \(q=3\). All older-state dependence lies in the complementary starred
entry and therefore drops out of its determinant. The remaining entries are
the direct path endpoints, whose products give the displayed factors.

This proves the formulas for arbitrary \(g\ge2\) and stable \(k\ge3\).
All 180 exact ratios for \(2\le g\le10\), \(3\le k\le12\) independently
cross-check the symbolic theorem.

## Scope and verification

- Packet: research/strominger/magnetic-memory-one-transfer.md.
- Checker: research/strominger/checkers/magnetic_memory_one_checks.py,
  8/8, exit 0.
- Results: research/strominger/results/magnetic_memory_one.json.
- Pre-activation: ev-000000002766.
- Preliminary report to Nima: ev-000000002770.
- Certified finite result to Nima: ev-000000002772.
- Symbolic Schur-compression theorem to Nima: ev-000000002774.
- Ledger allocation: sequence claim 2034,
  seqclaim-7abb97312761aa0c709c6b60.

This is an arbitrary-grade, arbitrary-stable-cutoff theorem for \(q=2,3\).
Initial cutoffs remain a finite boundary problem.
