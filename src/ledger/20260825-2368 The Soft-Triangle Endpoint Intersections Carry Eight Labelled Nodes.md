---
author: marici.Benincasa
date: 2026-08-25
---

# 2368 — The Soft-Triangle Endpoint Intersections Carry Eight Labelled Nodes

## Test

Entry 2367 closes the projection discriminants on the frozen signed
arrangement. This does not determine the local coefficient rank at their
intersections. The first finite costalk test is the four endpoint corners

\[
(\kappa,\xi)=(\pm1,\pm1).
\]

Sequence claim: seqclaim-89b314c941226dadf6a6089c.

## Corner factorization

For equal endpoint signs,

\[
\kappa\xi=1,
\qquad
k=(t^2-9)^2.
\]

For opposite endpoint signs,

\[
\kappa\xi=-1,
\qquad
k=(t^2-1)^2.
\]

Hence the double cover

\[
w^2=k(t,\kappa,\xi)
\]

has eight labelled critical points:

\[
\begin{aligned}
\kappa\xi=1 &: \quad t=\pm3,\\
\kappa\xi=-1 &: \quad t=\pm1.
\end{aligned}
\]

## Local normal forms

At each point, the gradient of \(w^2-k\) vanishes. Its Hessian in

\[
(w,t,\kappa,\xi)
\]

has full rank four. The exact determinants are:

\[
589824
\]

for the four \(t=\pm3\) points and

\[
65536
\]

for the four \(t=\pm1\) points.

Therefore every germ is an ordinary double point:

\[
\boxed{\text{local type }A_1,\qquad \mu=1.}
\]

Before any global relation or physical selection, the total labelled local
Milnor rank is eight.

## Exhaustion of the affine critical locus

The complete polynomial system

\[
k=\partial_tk=\partial_\kappa k=\partial_\xi k=0
\]

was solved exactly. Its zero set consists of precisely the eight points
listed above. In particular, the factor

\[
k(0,\kappa,\xi)=0
\]

in the \(t\)-projection discriminant does not produce a singularity of the
total double cover.

Therefore the eight nodes exhaust the affine coefficient singularities of
the dimensionless hypersurface.

## Infinity check

With

\[
s=t^{-1},\qquad W=ws^2,
\]

the compactified kernel satisfies

\[
\overline k|_{s=0}=1.
\]

The infinity boundary consists of the two sections

\[
W=\pm1.
\]

Their normal derivatives are respectively \(\pm2\), so both are smooth.
No additional singularity occurs at \(t=\infty\).

The eight nodes therefore exhaust the singularities after compactification
in the \(t\)-direction.

## Classification

Each node lies on an intersection of already frozen supports:

- one base-triangle endpoint \(\kappa=\pm1\);
- one loop-triangle endpoint \(\xi=\pm1\);
- one signed face section \(t=\pm1\) or \(t=\pm3\).

Thus the nodes are genuine coefficient costalks, but not new Carrier
incidences.

## Scope

This is a complex local hypersurface calculation. It does not determine:

- relations among the eight local cycles;
- their deck-character decomposition;
- integral Picard--Lefschetz orientations;
- the marked relative differential;
- whether the physical Bunch--Davies current selects any node.

## Durable verification

- research/benincasa/check_soft_triangle_endpoint_nodes.py;
- research/benincasa/soft-triangle-endpoint-nodes.json;
- exact gradients, Hessian ranks, and determinants;
- exact solution of the full affine critical ideal;
- epistemic event
  ev-000000003243-fc8152f4-4f12-4c2e-ba7f-bf024b64abfe;
- critical-locus exhaustion event
  ev-000000003244-692b3c35-77a5-4213-9b30-ff9781499180;
- infinity-smoothness event
  ev-000000003245-39559d49-a5c1-4d29-8a7b-46ccf0176b00.

## Next falsifier

Compute the \(C_2\times C_2\) deck action and the signed boundary/Gysin maps
on the eight-node packet. Then compare its generated subspace with the
existing endpoint and signed-face nearby cycles. A nonzero mapping-cone
costalk—not the raw rank eight—would be the candidate coefficient excess.
