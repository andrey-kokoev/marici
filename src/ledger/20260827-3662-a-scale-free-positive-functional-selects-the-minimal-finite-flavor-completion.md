---
id: marici-ledger-20260827-3662
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP836
sequence_claim: seqclaim-5f7a57fef273b76b840e78a1
---

# A Scale-Free Positive Functional Selects the Minimal Finite Flavor Completion

For a nondegenerate \(n\)-state finite operator, define

\[
R_n(D)=
\frac{\operatorname{Tr}(D^TD)}
{\det(D^TD)^{1/n}},
\qquad
\Phi_\lambda=\operatorname{Tr}Q^2+\lambda R_n(D).
\]

Arithmetic-geometric mean gives \(R_n\geq n\). The primitive three-charge
packet admits an irreducible saturator and has score \(14+3\lambda\).

Adding \(k\) nonzero charged vectorlike pairs and \(\ell\) neutral states
raises the score by at least

\[
2\sum_jr_j^2+\lambda(2k+\ell)>0.
\]

This holds for every positive \(\lambda\). Within the declared finite
completion grammar, the functional therefore selects no charged pairs, no
neutral additions, and equal singular values without tuning its relative
weight.

## Remaining fibers

The functional is invariant under \(D\mapsto mD\), so it does not select an
absolute scale. Distinct irreducible Householder mixings also saturate the
same bound. Source authority for minimizing \(\Phi\), the interacting RG
basin, finite matching, and physical16 instrumentation remain absent.

## Evidence

- Packet: research/flavor/flavor-scale-free-ward-spectral-completion-selector.md
- Checker: research/flavor/checkers/wp836_scale_free_ward_spectral_completion_selector.py
- Generated result: research/flavor/results/wp836_scale_free_ward_spectral_completion_selector.json
- Exact result: 12 of 12 checks passed.
- Ledger-sequence claim: seqclaim-5f7a57fef273b76b840e78a1, value 3662.
- Graph admission: ev-000000007861-57b9fdb8-130e-4756-8c09-06ea65c54cf9.

## Claim boundary

The theorem covers the declared direct charged and neutral finite-completion
grammar. It does not establish physical authority for the functional or cover
arbitrary interacting quantum-field-theory completions.
