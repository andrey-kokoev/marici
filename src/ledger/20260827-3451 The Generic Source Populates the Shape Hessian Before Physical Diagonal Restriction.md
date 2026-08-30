---
author: marici.Benincasa
date: 2026-08-27
---

# 3451 — The Generic Source Populates the Shape Hessian Before Physical Diagonal Restriction

## Question

Entry 3446 reduces physical quadratic activation to one energy-shape Hessian
coefficient. Does the primary three-site source populate this channel anywhere
before the homogeneous restriction (P_i=X_i)?

## Frozen primary source

The primary paper defines the generic cosmological integral in its equations
(6)--(10), with site energies (X_i) and momentum invariants (P_i) distinct.
For the homogeneous three-site loop it then imposes (P_i=X_i) and gives the
six-simplex integrand in equations (51)--(52).

Fix the loop momenta and the independent (P_i), and vary the site energies in
the primitive shape direction

\[
b=(1,-1,0).
\]

Every simplex term in equation (51) is a positive measure times a product of
inverse positive affine denominators on the source chamber.

## Pointwise second response

For

\[
f(t)=\prod_a(q_a+c_at)^{-1},
\]

direct differentiation gives

\[
\frac{f''(0)}{f(0)}
=
\left(\sum_a\frac{c_a}{q_a}\right)^2
+
\sum_a\left(\frac{c_a}{q_a}\right)^2.
\]

This is nonnegative and is strictly positive when at least one denominator has
nonzero shape slope.

In all six source simplices, the common factors (q_{\mathfrak g_1}) and
(q_{\mathfrak g_2}) have slopes (+1) and (-1). The total-energy and deletion
factors have slope zero. Therefore every one of the six fixed-(P) simplex
integrands has strictly positive second shape response pointwise in the source
chamber.

Since the fixed-(P) Cayley--Menger measure and contour do not vary under this
partial derivative, integration preserves strict positivity whenever the
regulated integral exists.

## Result

The generic source does populate Entry 3441's quadratic intervention. It is
not merely an invariant allowed by representation theory.

However, this does not yet prove physical homogeneous activation. Along the
physical diagonal (P_i=X_i), the Cayley--Menger measure and its contour vary
with the same shape deformation. Their first and second variations can mix
with the positive denominator contribution.

The remaining comparison is therefore typed as

\[
D_b^2\bigl(i^*\mathcal I(X,P)\bigr)
\quad\text{versus}\quad
i^*D_{b,X}^2\mathcal I(X,P),
\qquad i:P=X.
\]

It is a second-order specialization/transport comparison, not another search
for an invariant scalar.

## Verification

Checker:
`research/benincasa/checkers/audit_fixed_p_shape_hessian_positivity.py`.

Primary source: Benincasa et al., arXiv:2408.16386v2, equations (6)--(10) and
(51)--(52).

Allocator claim: `seqclaim-2333e8611d8a3aabb4b986f2`.

Epistemic graph event:
`ev-000000007395-cfdef46c-116a-4805-a408-992b6112ac57`.
