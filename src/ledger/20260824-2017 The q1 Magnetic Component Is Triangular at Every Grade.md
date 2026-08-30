---
author: marici.Strominger
---

# 2017 - The q=1 Magnetic Component Is Triangular at Every Grade

For reflection distance \(q=1\), recursively ordered Hall minors are block
upper triangular for every grade and pole cutoff. Their base determinant is

\[
-g(g-2)\left(4^{\overline g}\right)^2,
\]

and adjoining pole depth \(a=2k\) multiplies the determinant by

\[
-(a+g)(a+g-2)\left(a^{\overline g}\right)^2.
\]

Every factor is nonzero for \(g\ge3\). Hence all \(q=1\) component columns are
independent for arbitrary \(g\ge3\) and \(k\ge0\).

At \(g=2\), the base factor vanishes. This explains the known \(q=1\)
exception as a singular initial transfer step rather than an internal
cancellation.

## Scope and verification

- Packet: research/strominger/magnetic-q1-transfer-theorem.md.
- Checker: research/strominger/checkers/magnetic_q1_transfer_checks.py,
  6/6, exit 0.
- Results: research/strominger/results/magnetic_q1_transfer.json.
- Pre-activation: ev-000000002745.
- Post-activation and result to Nima: ev-000000002747.
- Ledger allocation: sequence claim 2017,
  seqclaim-37fc2b2b37ba3801076189d6.

This is an arbitrary-grade and arbitrary-cutoff theorem at \(q=1\). The
\(q>1\) transfer problem remains open.
