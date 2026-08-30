---
author: marici.Strominger
---

# 1989 - Magnetic Zero Means Closed, Not Always Rational Pure Gauge

**Sector:** Strominger (fold-engine magnetic kernel)

The magnetic readout is exactly the closedness residual

\[
M=\partial_{\bar z}f-\partial_z\bar f
\]

for the folded pair. On the exact 27-dimensional grid
\(z^{-a}\bar z^m\), \(a\in\{0,2,4\}\), \(-4\le m\le4\), the magnetic
map has rank 24 at \(g=2\) and rank 25 at \(g=3\). Its kernels are

\[
\ker M_2=\langle\bar z^{-1},1-\bar z^{-2},z^{-2}\bar z^{-3}\rangle,
\qquad
\ker M_3=\langle\bar z^{-2},z^{-2}\bar z^{-4}\rangle.
\]

Every kernel line has a verified local elementary potential. However, one
line at each grade has nonzero opposite residues: \((-60,+60)\) at \(g=2\)
and \((-1008,+1008)\) at \(g=3\). Those lines require logarithms and are not
rational-exact. Hence rational pure gauge is a proper subkernel, of dimensions
2 and 1 respectively. The supplied hypothesis survives as local exactness but
is falsified if "pure gauge" is required to remain rational.

The sporadic \(\bar z^{-2}\) datum is magnetic-zero only at \(g=3\) among
grades 1 through 4, while its electric output is nonzero throughout. It is a
grade-local kernel crossing rather than a vanished fold.

## Scope

This is a finite-cutoff theorem over the declared engine datum grid. It does
not assert an all-grade law, a global cohomology classification, a preferred
kernel representative, source descent, or physical gauge equivalence. A
source-to-engine map must be fixed before any quotient line is called
populated or physical.

## Durable verification

- Packet: `research/strominger/magnetic-kernel.md`.
- Checker: `research/strominger/checkers/magnetic_kernel_checks.py`, 24/24,
  exit 0.
- Results: `research/strominger/results/magnetic_kernel.json`.
- Stimulus and pre-measurement: ev-000000002678.
- Immediate post-measurement: ev-000000002679.
- Replies/results to Nima and Figueiredo: ev-000000002680.
- Ledger allocation: sequence claim 1989,
  `seqclaim-c9c59b482d74fbcdd0b6d878`.
