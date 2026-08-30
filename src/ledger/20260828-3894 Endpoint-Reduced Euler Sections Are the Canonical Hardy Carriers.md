---
author: marici.Grothendieck
---

# 3894 — Endpoint-Reduced Euler Sections Are the Canonical Hardy Carriers

The raw completed function is not the correct full-half-plane Hardy carrier:
its gamma factor has superlinear Stirling growth. The canonical source
normalization is instead

\[
E_+(s)=\frac{s-1}{s}\zeta(s),
\qquad
E_-(s)=E_+(1-s).
\]

The endpoint–zeta pole cancellation makes the apparent singularities
removable. These functions preserve exactly the open-sector zeros of the
completed section and are of bounded type in their respective half-planes.
They extend analytically through every finite seam point and have zero mean
type, so no separate singular-inner measure remains.

The anti-diagonal Hardy residual is therefore rigorous on these carriers: its
class vanishes exactly when the two open-sector Blaschke divisors are empty.
That is an RH equivalence, not yet the source-derived explanation.

## Scope

This supplies the correct analytic carrier and closes the singular-inner
typing gate. It does not derive vanishing of the Blaschke current or prove RH.

## Durable verification

- Research packet:
  `research/grothendieck/endpoint-reduced-euler-sections-are-the-canonical-hardy-carriers.md`.
- The divisor comparison is algebraic; bounded type follows from uniform
  vertical-strip zeta bounds and convergence in `Re(s) >= 2`.
- Epistemic graph admission:
  `ev-000000008520-22adbaeb-22c6-475d-a46c-47e350bd7978`.
- No build was run, following the operator's standing instruction.
