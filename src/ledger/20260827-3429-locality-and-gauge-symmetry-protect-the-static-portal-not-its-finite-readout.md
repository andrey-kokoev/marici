---
author: marici.Figueiredo
---

# 3429 — Locality and Gauge Symmetry Protect the Static Portal, Not Its Finite Readout

## Claim

Separating the two flavor sectors on distinct boundaries forbids a local
cross-boundary Kähler counterterm. A unique massive bulk mediator generates
the finite response

\[
G(0,\ell)=
\frac{1}{(m+ab/m)\sinh(m\ell)+(a+b)\cosh(m\ell)}.
\]

Passive boundary completion preserves its sign but changes its magnitude.
For an unbroken boundary gauge current, Proca boundary masses are forbidden
and gauge-invariant boundary kinetic terms enter as (a=r_0p^2) and
(b=r_Lp^2). Therefore the static matching coefficient is protected:

\[
G_0(0,\ell)=\frac{1}{m\sinh(m\ell)}.
\]

At finite readout momentum the same legal kinetic terms change the response.
At (m=\ell=p=1), (r_0=0) and (r_0=1), with (r_L=0), give respectively

\[
\frac{1}{\sqrt2\sinh\sqrt2}
\qquad,qquad
\frac{1}{\sqrt2\sinh\sqrt2+\cosh\sqrt2}.
\]

## Classification

Locality plus gauge symmetry is the first tested architecture to remove the
additive cross-contact ambiguity and protect the static threshold sign within
the complete quadratic boundary class. It still does not fix the physical
finite-energy response. The boundary spectral function must be source-derived
or independently calibrated, and (m\ell), gauge normalization, RG basin,
and `physical16` descent remain open.

## Durable verification

- Packets:
  research/flavor/flavor-separated-boundary-exchange-completion-fiber.md and
  research/flavor/flavor-static-gauge-matching-finite-readout-fiber.md
- Checkers:
  research/flavor/checkers/wp768_separated_boundary_exchange_completion_fiber.py
  and
  research/flavor/checkers/wp769_static_gauge_matching_finite_readout_fiber.py
- Generated results:
  research/flavor/results/wp768_separated_boundary_exchange_completion_fiber.json
  and
  research/flavor/results/wp769_static_gauge_matching_finite_readout_fiber.json
- Exact checker outcomes: WP768 10/10 PASS; WP769 10/10 PASS.
- Sequence authority: seqclaim-403dd7c23398c95d516af988.
- Epistemic-graph admission:
  ev-000000007337-95c67819-f826-4738-b821-3e48c27b1e5e.
