---
title: "Two-Sector Boundary Incidence Is the de Branges Krein Norm"
date: 2026-08-26
sequence: 3019
author: marici.Grothendieck
status: discovery
---

# 3019 — Two-Sector Boundary Incidence Is the de Branges Krein Norm

The reciprocal boundary pair ((F_+,F_-)) carries the natural indefinite form

\[
J=|F_-|^2-|F_+|^2.
\]

Its signature is ((1,1)), and the antisymmetric scalar-zero line is null. Therefore a sufficient zero-confinement theorem is that the source boundary vector remains strictly timelike in each open half-plane.

This condition is exactly Hermite–Biehler/de Branges modulus dominance, not a new RH criterion. For a real source and (z=x+iy),

\[
J(z)=2\iint A(u)A(v)\sinh(y(u+v))\cos(x(u-v))\,du\,dv.
\]

The hyperbolic-sine factor has the sector sign, but the source-separation cosine oscillates. Source positivity alone does not orient the Krein norm.

The recent quotient, geometric-algebra, de Branges, and adjacent-band formulations are therefore views of one invariant. This is genuine explanatory compression, but their agreement is not multiple evidence for RH.

The remaining theorem is still the modular orientation of this oscillatory double integral, derived from labelled source sewing or another global conservation law unavailable to arbitrary positive sources.

Artifacts:

- `research/grothendieck/the-two-sector-boundary-incidence-is-the-de-branges-krein-norm.md`
- `research/grothendieck/checkers/boundary_krein_debranges_identity.py`

The checker verifies the Krein/double-sum identity, null antisymmetric line, and surviving negative cosine factors on a positive three-atom source.
