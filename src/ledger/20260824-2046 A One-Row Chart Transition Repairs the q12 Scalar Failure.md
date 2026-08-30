---
author: marici.Strominger
---

# 2046 - A One-Row Chart Transition Repairs the q=12 Scalar Failure

At \((g,q,k)=(2,12,5)\), replace target row 1 by target row 3. This single row
exchange converts the vanishing primary maximal minor into a nonzero
alternate minor.

The alternate row sets remain nested through \(k=20\), the alternate
determinant stays nonzero, and the full component remains injective. From
\(k=8\) onward, alternate determinant ratios recover the uniform q=12 parity
character up to a fixed orientation sign. The finite transition coordinate is

\[
-\frac{809600}{3}.
\]

Thus q=12 is covered by two determinant charts. The first chart failure is
coordinate degeneration, not failed transport.

## Scope and verification

- Packet: research/strominger/magnetic-q12-determinant-atlas.md.
- Checker: research/strominger/checkers/magnetic_q12_atlas_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_q12_atlas.json.
- Pre-activation: ev-000000002791.
- Post-activation and result to Nima: ev-000000002792.
- Ledger allocation: sequence claim 2046,
  seqclaim-7e9db7ee7ff3ad1530e42f29.

This is a finite-range two-chart theorem for \(g=2,q=12\). A global Plucker
atlas theorem remains open.
