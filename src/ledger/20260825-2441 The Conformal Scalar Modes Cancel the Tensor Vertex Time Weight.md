---
author: marici.Benincasa
date: 2026-08-25
---

# 2441 — The Conformal Scalar Modes Cancel the Tensor Vertex Time Weight

## Question

Entry 2440 derives the finite-$q$ tensor numerator but leaves its
$\eta^{-2}$ factor unresolved. Does this factor raise a marked energy-pole
order, define a new contiguity operator, or cancel against the frozen scalar
mode functions?

## Frozen source modes

For a boundary scalar of weight $\Delta=2$, the bulk-to-boundary propagator
in Baumann et al., equations (6.13)--(6.14), specializes to

\[
\mathcal K_2(k,\eta)
=
\frac{\eta}{\eta_\star}
e^{ik(\eta-\eta_\star)},
\]

up to the common late-time normalization convention. The primary local
vertex is

\[
V_{\gamma\varphi\varphi}^{ij}
=
\frac{\beta^i\beta^j}{2\eta^2}.
\]

## Exact cancellation

Multiplying the vertex by its two conformally coupled scalar modes gives

\[
\frac{1}{2\eta^2}
\mathcal K_2(k_2,\eta)
\mathcal K_2(k_4,\eta)
=
\frac{e^{-i(k_2+k_4)\eta_\star}}{2\eta_\star^2}
e^{i(k_2+k_4)\eta}.
\]

There is no residual power of $\eta$. With the damped Bunch--Davies past
contour,

\[
i\int_{-\infty}^{0}d\eta\,
e^{i(E-i\epsilon)\eta}
=
\frac{1}{E-i\epsilon}.
\]

Therefore the local insertion preserves the ordinary simple exponential
energy seed. It does not by itself raise a marked pole order.

The two physical responses are consequently the same scalar time seed
multiplied by

\[
\frac14(\beta_x+i\beta_y)^2,
\qquad
\frac14(\beta_x-i\beta_y)^2.
\]

## Ward completion is not local multiplication

The cancellation does **not** imply that the complete tensor system is the
scalar marked-relative system tensored with a free quadratic numerator. The
same primary source proves that individual exchange channels are not
gauge-invariant. Its Ward identity fixes the relative channel and contact
normalizations, including

\[
\kappa_g=\kappa_c=\kappa.
\]

Thus two distinct statements must remain separated:

\[
\boxed{
\text{local time-weight cancellation}
}
\qquad\text{and}\qquad
\boxed{
\text{global Ward/contact completion across channels}.
}
\]

## Result

\[
\boxed{
\text{the conformally coupled scalar modes cancel the finite-$q$ tensor
vertex's $\eta^{-2}$ weight exactly.}
}
\]

The first tensor enlargement changes the coefficient numerator and physical
polarization ports, but introduces no local energy-pole shift and no new
Carrier support.

## Scope

This theorem applies to the source $Delta=2$ scalar--scalar--graviton
vertex. It does not type massless-scalar external legs, the graviton
bulk-to-bulk propagator, or the full one-loop Ward completion. In particular,
the source itself shows that nested graviton exchange contains additional
subleading total-energy poles and correlated contact terms.

## Durable evidence

- `research/benincasa/check_cc_scalar_tensor_time_weight.py`;
- `research/benincasa/cc-scalar-tensor-time-weight.json`;
- Baumann et al., arXiv:2005.04234v3, equations (6.13)--(6.14), (6.22),
  (6.48)--(6.51), and the channel-completion discussion;
- sequence claim `seqclaim-d9c4ee0f9ca4f7aeebeb882e`.

## Next falsifier

Construct the labelled loop insertion of the quadratic momentum numerator
on the frozen three-site marked-relative integrand. Retain both helicities
and every occurrence before summation. Then derive the Ward/contact
completion as a map between source-labelled channels rather than fitting a
gauge-invariant answer after reduction.
