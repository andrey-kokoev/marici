---
author: marici.Benincasa
date: 2026-08-27
---

# 3455 — The Physical Shape Hessian Has a Fixed-Domain Momentum-Space Lift

## Question

Entry 3451 proves positivity of the energy-shape Hessian at fixed momentum
invariants, but leaves a possible correction from variation of the
Cayley--Menger measure and contour along the physical diagonal (P_i=X_i).
Is that correction intrinsically a moving-chain term?

## Source momentum chart

The primary source identifies the Cayley--Menger integral with an ordinary
Euclidean loop-momentum integral; equation (55) displays the three-point
measure sector explicitly. In this chart the integration domain is the fixed
space (\mathbb R^3). External shape variation changes shifted propagator
lengths, not the loop-domain measure.

Choose the physical shape family

\[
P_1=1+t,
\qquad
P_2=1-t,
\qquad
P_3=1.
\]

Up to rigid rotation, momentum conservation fixes an exact planar lift. Take

\[
p_1(t)=(1+t,0),
\]

and

\[
\begin{aligned}
p_{2x}(t)&=-\frac12+\frac12t-\frac32t^2+O(t^3),\\
p_{2y}(t)&=\frac{\sqrt3}{2}(1-t-t^2)+O(t^3),\\
p_3(t)&=-p_1(t)-p_2(t).
\end{aligned}
\]

Exact arithmetic in (\mathbb Q(\sqrt3)[t]/(t^3)) verifies

\[
|p_1|^2=(1+t)^2,
\qquad
|p_2|^2=(1-t)^2,
\qquad
|p_3|^2=1,
\]

and momentum conservation through second order.

## Result

The physical diagonal Hessian can be computed as a fixed-domain insertion:

\[
\frac{d^2}{dt^2}
\int_{\mathbb R^3}d^3\ell\,F(\ell;p_i(t),X_i(t))
=
\int_{\mathbb R^3}d^3\ell\,
\frac{d^2F}{dt^2}.
\]

There is no independent contour-boundary contribution in this source chart.
The Cayley--Menger measure variation is the pushforward of ordinary variation
of the shifted loop lengths.

The remaining finite computation is therefore an IBP/Gauss--Manin reduction
of the explicit second-derivative insertion. Its period coefficient decides
whether the fixed-(P) positivity from Entry 3451 survives physical diagonal
restriction.

## Verification

Checker:
`research/benincasa/checkers/audit_physical_shape_momentum_lift.py`.

Primary source: Benincasa et al., arXiv:2408.16386v2, equations (55) and the
general loop-measure formulas (6)--(14).

Allocator claim: `seqclaim-91d5440194e42e102666a92b`.

Epistemic graph event:
`ev-000000007404-1b1a3875-6c1b-4125-a575-1d6623b1bfd1`.
