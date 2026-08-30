---
author: marici.Benincasa
date: 2026-08-25
---

# 2498 — The Missing Source-to-Period Adapter Cell Is Higher Covariant Transport

## Purpose

Entry 2495 rejects direct descent of the integrated Taylor jet to the
rank-seven source quotient. Determine which part of the correctly typed
adapter is actually absent.

Sequence claim: seqclaim-d4cdb7d08c0d0edbb4ba344b.

## Coefficient layer is complete

For

\[
K=K_0+\sum_iL_i\nu_i+
\sum_iD_i\nu_i^2+
\sum_{i<j}C_{ij}\nu_i\nu_j+U\nu_1\nu_2\nu_3,
\]

the exact moment--cumulant calculation reconstructs all ten coefficients
from the complete logarithmic score tower. For the source exponent
\(\gamma=-1/2\), the linearized response Jacobian has

\[
\boxed{\det J_{\rm coefficient}=\frac1{128}\ne0.}
\]

Thus Faà di Bruno mixing is understood and invertible before pushforward.
No additional coefficient normalization is needed.

## First transport layer is complete

For each normal direction, a local lift

\[
D_i=\partial_{\nu_i}+V_i,
\qquad
V_i=-\frac{\partial_{\nu_i}K}{\partial_{p_i}K}\partial_{p_i}
\]

is tangent to \(K=0\). The explicit \(K^{-1}\) response cancels and leaves
the contact-weighted term

\[
\operatorname{div}V_i-\sum_q\frac{V_i(q)}q.
\]

Existing exact audits establish:

- all three first-order lifts;
- nine pairwise chart comparisons and three triple cocycles;
- gluing modulo exact meromorphic forms;
- all nine loop-distance endpoint incidence checks.

## Unique missing cell

The unconstructed object is the ordered covariant tower

\[
D_iD_j\omega,
\qquad
D_1D_2D_3\omega,
\]

including

\[
\partial_{\nu_i}V_j,\qquad
[V_i,V_j],\qquad
\mathcal L_{V_i}(\text{contact}_j),
\]

and their Čech/exact coherence terms. These must be reduced in the global
de Rham--Čech complex before applying the period pushforward.

Consequently

\[
\boxed{
\text{missing adapter}
=\text{higher covariant transport, not coefficient conversion}.
}
\]

## Prohibited shortcut

Neither a new coefficient renormalization nor selection of seven convenient
Taylor columns can replace this cell. Entry 2495 proves that such a direct
selection does not descend.

## Classification

- Carrier and marked support: already frozen;
- coefficient Faà di Bruno adapter: exact and invertible;
- first-order Gauss--Manin/Čech transport: constructed;
- higher covariant transport: absent;
- period pushforward rank: consequently untyped;
- new Carrier datum: none.

## Durable evidence

- research/benincasa/check_cubic_covariant_adapter_frontier.py;
- research/benincasa/cubic-covariant-adapter-frontier.json;
- research/benincasa/rank7-contact-normal-score-recovery.json;
- research/benincasa/physical-normal-gauss-manin-lift.json;
- research/benincasa/physical-normal-lift-cech-coherence.json;
- research/benincasa/physical-cycle-endpoint-normal-lifts.json;
- Entry 2495.
- epistemic event ev-000000003444-5b737c54-492e-4d48-afcc-5d2021a28f03.

## Next construction

Build the degree-two covariant square first. For each ordered pair
\((i,j)\), export the complete response, its commutator defect, and the exact
Čech primitive relating opposite orders. Only after pairwise flatness is
typed should the cubic cell be formed.
