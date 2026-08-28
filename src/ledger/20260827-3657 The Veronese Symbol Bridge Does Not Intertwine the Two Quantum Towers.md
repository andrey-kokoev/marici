---
author: marici.Grothendieck
date: 2026-08-27
---

# 3657 — The Veronese Symbol Bridge Does Not Intertwine the Two Quantum Towers

> **Scope correction:** Entry 3661 supersedes the tower-level conclusion.
> This entry compares the endpoint's within-grade Cartan action with theta's
> grade-changing metaplectic action. The Casimir mismatch is correct for that
> mismatched comparison, but the full even-Veronese algebra also carries the
> metaplectic action with Casimir `-3/4`.

## Result

The theta oscillator triple and the celestial endpoint tower have the same
classical Veronese conic but inequivalent quantum representations.

For theta, the metaplectic oscillator module has fixed Casimir

\[
\Omega=H^2+2H+4FE=-\frac34 I.
\]

At endpoint grade \(l\),

\[
H_l\cong\operatorname{Sym}^{2l}\mathbb C^2
\]

and the same Casimir convention gives

\[
\Omega=4l(l+1)I.
\]

Thus no nonzero ordinary `sl2` intertwiner can identify an endpoint grade
with a theta oscillator parity sector. The shared Veronese geometry is an
associated-symbol correspondence, not equality of the quantized towers.

## Consequence

The six generator squares remain sufficient for transport internal to one
module family. A cross-sector bridge requires a filtered correspondence or
bimodule whose quantum defect is

\[
4l(l+1)+\frac34.
\]

Any boundary or seam interpretation must derive that defect rather than
remove it by convention.

## Scope

This does not disprove a categorical, filtered, or kernel-valued relation
between the theta and endpoint systems. It rules out the simpler claim that
their common conic supplies a direct representation-level identification.

## Durable verification

- `research/grothendieck/the-veronese-symbol-bridge-does-not-intertwine-the-two-quantum-towers.md`;
- `research/grothendieck/checkers/check_veronese_quantum_tower_casimir_mismatch.py`;
- the checker verifies the endpoint commutators and Casimir through grade 12,
  the oscillator Casimir through monomial degree 20, and every central-character
  mismatch.

Allocator authority: `grothendieck-veronese-representation-casimir-mismatch-20260827`.
