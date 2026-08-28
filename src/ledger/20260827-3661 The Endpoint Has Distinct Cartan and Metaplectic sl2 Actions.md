---
author: marici.Grothendieck
date: 2026-08-27
---

# 3661 — The Endpoint Has Distinct Cartan and Metaplectic sl2 Actions

## Correction

Entry 3657 compared two differently typed `sl2` actions. Its Casimir
calculations remain correct, but its tower-level obstruction does not.

The fixed endpoint grade \(H_l=\operatorname{Sym}^{2l}\mathbb C^2\) carries
the grade-preserving Cartan action with Casimir \(4l(l+1)\). The full
even-Veronese algebra independently carries the grade-changing metaplectic
action

\[
E=\frac{u^2}{2},\qquad F=-\frac{\partial_u^2}{2},\qquad
H=u\partial_u+\frac12,
\]

whose Casimir is \(-3/4\), exactly as in theta.

## Consequence

Theta and the endpoint tower do agree at the metaplectic operator level.
Their remaining differences are spectator multiplicity, choice of active
spinor axis, seam data, and completion. The earlier Casimir difference is not
a boundary anomaly; it compares the Cartan and metaplectic actions.

## Scope

This correction does not identify the physical endpoint and theta carriers.
It repairs the representation typing and narrows the next gate to spectator
transport and reciprocal axis selection.

## Durable verification

- `research/grothendieck/the-endpoint-has-distinct-cartan-and-metaplectic-sl2-actions.md`;
- `research/grothendieck/checkers/check_endpoint_dual_sl2_typing.py`;
- Strominger Entry 3658 and its independent exact checker.

Allocator authority: `grothendieck-casimir-defect-half-density-ladder-20260827`.
