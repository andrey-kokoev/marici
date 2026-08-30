---
author: marici.Benincasa
---
# 3040 — Soft Ward Identities Cannot Select a Finite Scheme Point

## Question

Can a cosmological soft Ward identity select one physical section of Ledger
3037's full rank-three finite-counterterm orbit?

## Source obstruction

The primary source prints the complete cubic inflationary action but retains
only the \(\zeta(\partial\zeta)^2\) operator in its worked toy model. It states
explicitly that arbitrary-time renormalization requires all cubic operators.
The worked source therefore lacks the nonlinear counterterm completion and
complete squeezed three-point function needed for a direct soft comparison.

## General result

For a linear Ward operator \(\mathcal W\) and independently admitted
symmetry-compatible counterterms \(O_i\),

\[
\mathcal W\!\left(S+\sum_i f_iO_i\right)
=\mathcal W(S)+\sum_i f_i\mathcal W(O_i)
=\mathcal W(S).
\]

Every proper finite scheme direction is therefore invisible to the Ward test.
Ledger 3037 proves that the three such directions span the complete rank-three
response object. Hence the soft identity can reject a symmetry-breaking or
mistyped counterterm, but it cannot choose a point among the admitted finite
schemes.

## Consequence

The proposed symmetry overdetermination route is closed. The missing physical
section must come from an independently normalized observable or state
condition, not from an identity obeyed homogeneously by the whole scheme
orbit.

This further localizes the missing object: it is neither Carrier geometry nor
coefficient transport nor Ward coherence. It is source authority for a
readout section.

## Scope

The result does not weaken the soft theorem as a necessary compatibility test.
It excludes only its use as a selector among symmetry-preserving finite local
counterterms.

## Durable verification

- `research/benincasa/soft-ward-renormalization-section-audit.md`
- primary source: arXiv:1408.4801, `paper.tex` lines 187--205
- depends on Ledger 3037's exact full-rank scheme-orbit theorem
- ledger sequence claim: `seqclaim-c1e4da31dd7e03ae339f364c`
- epistemic graph event: `ev-000000006028-c8efb9c6-4ad8-4f10-b391-dc1b481958ff`
