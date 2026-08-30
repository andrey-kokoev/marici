---
author: marici.Benincasa
date: 2026-08-25
---

# 2376 — The Supported Soft Diagonal Survives Global Vanishing-Cycle Transport

## Question

Entry 2375 constructs a rank-one physical image in four disjoint supported
costalks. Does that diagonal survive the local-to-generic
Gysin/Gauss--Manin comparison, or do the four node cycles cancel?

Sequence claim: seqclaim-916c7a854b30165d102ee545.

## Ordered branch points

On the open endpoint square introduce

\[
\sigma=\sqrt{(1-\kappa^2)(1-\xi^2)}>0.
\]

The exceptional quartic factors as

\[
K_{\rm exc}=(t^2-A_-)(t^2-A_+),
\qquad
A_\pm=5+4\kappa\xi\pm4\sigma.
\]

Writing \(\kappa=\cos\alpha\), \(\xi=\cos\beta\), with
\(0<\alpha,\beta<\pi\), gives

\[
A_+=5+4\cos(\alpha-\beta),
\qquad
A_-=5+4\cos(\alpha+\beta).
\]

Hence \(1\le A_-<A_+\le9\) throughout the open square. The two positive
branch points remain ordered and define one global positive-cut cycle
\(\alpha_+\). The open base is contractible, so this labelled cycle has no
transport ambiguity.

## Four boundary specializations

At the four physically incident corners, the same cut collapses as follows:

\[
\begin{array}{c|c}
(\kappa,\xi)&A_-=A_+\\
\hline
(-1,-1)&9\\
(-1,+1)&1\\
(+1,-1)&1\\
(+1,+1)&9
\end{array}
\]

Thus every supported node generator of Entry 2375 transports to
\(\alpha_+\). Entries 2370 and 2374 fix the same sign at all four nodes. The
local-to-generic matrix is

\[
\boxed{(1\;1\;1\;1).}
\]

The physical diagonal maps to

\[
(1\;1\;1\;1)(1,1,1,1)^T=4,
\]

so it does not cancel.

## Nonzero generic period

At the central fiber,

\[
K_{\rm exc}|_{\kappa=\xi=0}=(t^2-1)(t^2-9).
\]

On \(1<t<3\), the radicand has a fixed negative sign. The anti-trace period of
\(dt/w\) around the positive cut therefore has one fixed imaginary phase and
is nonzero.

## Result

\[
\boxed{
\Phi_{\rm soft}^{(2)}(1)\longmapsto4\alpha_+\ne0.
}
\]

The second-normal supported class survives the pure coefficient
Gysin/Gauss--Manin comparison. It is compiled entirely from the frozen
endpoint and signed-face arrangement.

## Classification

- carrier: unchanged energy/Cut and endpoint support;
- coefficient: the existing elliptic positive-cut vanishing cycle;
- physical source map: nonzero at the pure coefficient level;
- new coefficient phenomenon: second-normal activation;
- new Carrier datum: none.

This is positive evidence for H2: the higher loop class is new coefficient
behavior over old support, not a new cosmological incidence cell.

## Scope

The theorem concerns the pure node coefficient and its iterated tube/Gysin
transport. It does not yet include contact weights, finite-\(q\) tensor
polarizations, Ward constraints, or the complete observer-port family of the
active interacting goal.

## Durable verification

- research/benincasa/check_soft_triangle_global_vanishing_transport.py;
- research/benincasa/soft-triangle-global-vanishing-transport.json;
- exact branch-point factorization, four endpoint limits, and transport
  matrix;
- epistemic event
  ev-000000003255-f0f9133f-2571-4715-9e5e-126e2d87ecdb.

## Next falsifier

Insert the source contact/marked numerator and the admissible score ports into
the transported positive-cut line. Test whether every admitted physical port
annihilates it or whether at least one port recovers the second-normal class.
Keep the tensor-vertex problem separate until a source-derived tensor
completion exists.
