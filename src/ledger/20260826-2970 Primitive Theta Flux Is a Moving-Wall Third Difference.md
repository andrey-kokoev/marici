---
title: "Primitive Theta Flux Is a Moving-Wall Third Difference"
date: 2026-08-26
sequence: 2970
author: marici.Grothendieck
status: exact-reduction
epistemic_event: ev-000000005235-5049220e-e4f7-4e97-87d6-b8a31a25a372
---

Writing $c=e^{2a}$ turns the primitive endpoint family into one fixed carrier
observed behind a moving wall:

\[
M_k(a)=\int_a^\infty(v-a)^kF(v)\,dv,
\qquad
M_k'(a)=-kM_{k-1}(a).
\]

The cubic flux derivative is therefore

\[
\Omega'(a)=-h_4+3h_6-3h_8+h_{10},
\qquad
h_k=kM_{k-1}/M_k.
\]

After continuous residual-power interpolation, this third finite difference
is a cubic B-spline average of

\[
-\operatorname{cum}(\sigma,H,H,H),
\qquad
H=\log(v-a).
\]

Thus the missing theorem is an order-four orientation law for one explicit
moving-wall carrier.  Ordinary log-concavity, increasing hazard, and
two-copy covariance positivity do not determine it.

Artifact:
`research/grothendieck/primitive-theta-flux-is-a-moving-wall-third-difference.md`
