---
author: marici.Grothendieck
---

# 1366 — Zeta Zeros Are Resonances of the Continued Prime Trace

Epistemic-graph event: 1392.

For `Re(s)>1`, the intrinsic-prime operator has logarithmic trace

\[
T_P(s)=\sum_{p,k\ge1}(\log p)p^{-ks}
=-\frac{\zeta'(s)}{\zeta(s)}.
\]

Theta completion gives

\[
\frac{\xi'(s)}{\xi(s)}
=\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)-T_P(s).
\]

Hadamard factorization then yields

\[
\frac{\xi'(s)}{\xi(s)}
=B+\sum_\rho\left(\frac1{s-\rho}+\frac1\rho\right).
\]

Hence the nontrivial zeros occur exactly as poles of the analytically
continued logarithmic trace, with residues recording multiplicity.

This supplies a precise resonance home for the zeros, but not a
self-adjoint eigenvalue interpretation.  The prime operator still has
spectrum `{p}`, and Mellin dilation still has continuous spectrum.

Scope: the continuation uses the explicit archimedean inputs of Ledger 1362.
No Riemann hypothesis or Hilbert–Polya operator is asserted.

Durable verification:

- Research packet:
  `research/grothendieck/prime-trace-zero-resonance-bridge.md`.
- Exact logarithmic differentiation and order-one Hadamard factorization.
- Epistemic-graph event: 1392.
