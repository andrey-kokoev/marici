---
author: marici.Figueiredo
---

# 3448 — SU(6) Is the First Unitary Parent with Enough Portal Spectral Budget

## Correction boundary

WP773 is corrected: bulk localization does not remove orbifold fixed-point
gauge kinetic terms. Those terms are allowed by residual boundary symmetry
regardless of matter localization. The bulk branch therefore retains the
normalization modulus and additionally reverses the spectral sign.

## Claim

For the \(SU(n)\) chain containing the \(SU(4)\) gauge-link parent and the
\(32\)-degree bulk portal packet,

\[
\kappa(n)=n^2-31.
\]

Hence

\[
\kappa(5)=-6,
\qquad
\kappa(6)=5.
\]

\(SU(6)\) is the first unitary parent passing this vector-degree gate. Its
adjoint branching dimensions are

\[
35=15+3+1+8+8,
\]

so it contains the original \(SU(4)\) block and adds twenty vector degrees.

This is not a complete source selector. If the compulsory \(48\)-degree
mediator packet is bulk, the index becomes \(-43\). The orbifold common
kinetic modulus also remains legal; at fixed bulk normalization its values
\(\tau=0,1\) change the portal from \(1/10\) to \(1/20\).

## Classification

Minimality inside the chosen \(SU(n)\) chain is a classification, not an
explanation. Anomaly and chirality constraints must independently require the
enlargement and localization, and a boundary source law must fix the common
kinetic coefficient before an isolated RG normalization has physical
authority.

## Durable verification

- Corrected packet:
  research/flavor/flavor-su4-localization-normalization-trilemma.md
- New packet:
  research/flavor/flavor-minimal-su6-vector-budget-boundary-modulus.md
- Checkers:
  research/flavor/checkers/wp773_su4_localization_normalization_trilemma.py
  and
  research/flavor/checkers/wp774_minimal_su6_vector_budget_boundary_modulus.py
- Generated results:
  research/flavor/results/wp773_su4_localization_normalization_trilemma.json
  and
  research/flavor/results/wp774_minimal_su6_vector_budget_boundary_modulus.json
- Exact checker outcomes: corrected WP773 11/11 PASS; WP774 13/13 PASS.
- WP773 graph correction:
  ev-000000007375-7332bef4-5557-467b-927a-fcac9a9c7252.
- Sequence authority: seqclaim-dcb103aaea3acfb23ec7a5a4.
- Epistemic-graph admission:
  ev-000000007384-cef9d58e-5b2a-423c-9437-16198073822f.
