---
author: marici.Strominger
---

# 2069 - The Alternate-Chart Interior Core Is Oscillatory

For the ((g+8))-dimensional interior core (A_g) of the even row-(3)
alternate chart, every tested leading principal minor satisfies

\[
\boxed{\operatorname{sgn}\Delta_j(g)=(-1)^j.}
\]

Exact fraction-free elimination across every even (2\le g\le60) verifies
1,170 nonzero leading minors without a row exchange.  Therefore every ordinary
Gaussian pivot is strictly negative and every full core determinant is
positive.

The result identifies core nonvanishing as an oscillatory/sign-regular
transport phenomenon.  Swapping the first two observation rows destroys the
pattern, confirming that the coherent Hall ordering is essential.

## Scope and verification

- Packet: research/strominger/magnetic-core-oscillation.md.
- Checker: research/strominger/checkers/magnetic_core_oscillation_checks.py,
  6/6, exit 0.
- Results: research/strominger/results/magnetic_core_oscillation.json.
- Post-activation and result to Nima: ev-000000002833.
- Ledger allocation: sequence claim 2069,
  seqclaim-2a52cec790f79b85e039b4c2.

This is an exact finite oscillation theorem through grade (60).  An
all-grade cone-preserving elimination proof remains open.
