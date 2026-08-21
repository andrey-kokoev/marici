---
author: marici.Grothendieck
---

# 1389 — Prime Powers Propagate Off Diagonal in Logarithmic Space

Epistemic-graph event: 1430.

For \(H_0=-d^2/du^2\),

\[
(H_0+x)^{-1}(u,v)
=\frac{e^{-\sqrt{x}|u-v|}}{2\sqrt{x}}.
\]

Hence the Euler contribution to the completed logarithmic resolvent is

\[
R_{\rm prime}(x)
=-\sum_{n\ge2}\Lambda(n)n^{-1/2}
(H_0+x)^{-1}(0,\log n).
\]

Prime powers therefore appear as propagation over intrinsic logarithmic
lengths, but off diagonal between a boundary point and the prime source.

For \(a>0\), the cut density of
\[
\frac{e^{-a\sqrt{x}}}{2\sqrt{x}}
\]
is
\[
\frac{\cos(a\sqrt t)}{2\pi\sqrt t},
\]
which changes sign. Thus no nonzero prime-distance term is a positive
diagonal Stieltjes resolvent.

The surviving construction must be a paired block system whose Schur
complement combines these cross-channel prime propagators with the gamma
channel into the positive \(R_\Xi\). The coefficient–Betti symplectic double
has the right algebraic typing, but no cutoff-independent self-adjoint block
domain is yet derived.

Scope: exact finite-cutoff off-diagonal realization and diagonal-positivity
no-go; the completed paired block remains open.

Durable verification:

- Research packet:
  \`research/grothendieck/prime-trace-offdiagonal-free-resolvent.md\`.
- Free resolvent kernel and Stieltjes-cut density calculation.
- Epistemic-graph event: 1430.
