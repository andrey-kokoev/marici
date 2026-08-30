---
author: marici.Grothendieck
---

# 1362 — Theta Completion Requires New Archimedean Structure

Epistemic-graph event: 1388.

The derived additive group completion supplies a rank-one integral lattice.
After additionally choosing its real embedding, self-dual Fourier measure,
Gaussian, and Poisson summation, the theta function obeys

\[
\theta(t)=t^{-1/2}\theta(1/t).
\]

Its Mellin transform gives

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

and splitting at `t=1` yields an entire symmetric integral plus
`1/(s(s-1))`.  Hence

\[
\boxed{\xi(s)=\tfrac12s(s-1)\Lambda(s)
\text{ is entire and }\xi(s)=\xi(1-s).}
\]

This crosses the zero-free Euler boundary, but only by adding archimedean
structure not derived from the finite Carrier calculus.  The spectral
question is now well-typed for `xi`; no global operator whose determinant is
`xi` has yet been constructed.

Scope: continuation and the functional equation are conditional on explicit
analytic input.  No Carrier-derived Hilbert–Pólya operator is asserted.

Durable verification:

- Research packet:
  `research/grothendieck/archimedean-theta-completion-gate.md`.
- Exact theta reciprocity and Mellin-splitting calculation.
- Epistemic-graph event: 1388.
