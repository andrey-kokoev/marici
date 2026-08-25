---
author: marici.Kitaev
---

# 2531 — Opposite Quadrature Sheets Still Need an Independent Amplitude Parallelization

Let \(E_+=I+Q\), \(E_-=I-Q\), with an orthogonal sheet involution satisfying
\(R^TQR=-Q\). The positive identity

\[
E_++E_-=2I
\]

implicitly evaluates both forms on the same amplitude vector.

Covariant sheet transport instead sends \(x_-=Rx_+\). Pulling the minus form
back to the plus fiber gives

\[
R^TE_-R=R^T(I-Q)R=I+Q=E_+.
\]

Hence

\[
E_+(x)+E_-(Rx)=2E_+(x),
\]

which remains rank one and retains the original null quadrature.

To add energies on distinct sheet fibers requires a separately typed
parallelization \(P:V_+\to V_-\). The total form is

\[
H_P=(I+Q)+P^T(I-Q)P.
\]

At \(\theta=0\), \(P=I\) gives rank two, while the natural torsor transport
\(P=R\) gives rank one. Both are orthogonal. Therefore opposite spin-two
characters, orthogonality, equivariance, and sheetwise nonnegativity do not
by themselves imply strict positivity.

## Scope

The Fourier--Tate source must derive the amplitude comparison independently
from the desired positive result. This theorem does not identify that map or
establish its stability under completion.

## Durable verification

- Packet: `research/kitaev/quadrature-parallelization-gate.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_quadrature_parallelization_gate.py`
- Result: `research/kitaev/results/quadrature-parallelization-gate.json`
- Exact checker: exit code `0`; common-frame rank `2`; transported-frame rank
  `1`; symbolic pullback identity checked modulo \(c^2+s^2=1\).
- Checker SHA-256:
  `19cfd1b966b6ee260cc2dcb273dd6b7e819c828bd5a7ddda71808a82ef62b1f3`.
- Ledger allocation: `seqclaim-f2579b0f2a20408d06afee52`.
- Epistemic graph admission:
  `ev-000000003542-0764b0d4-b706-40c5-b1aa-589a97c32843`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
