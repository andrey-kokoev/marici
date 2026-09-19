# The history resolvent gives the theta-profile Weyl kernel off the seam

## Self-adjoint history convention

Let

\[
A=iD
\]

on the bilateral history carrier with its standard self-adjoint whole-line
domain. Then

\[
\operatorname{spec}(A)=\mathbb R.
\]

Use a spectral parameter `lambda` off the real axis. Let

\[
B_\theta:
\mathcal U_{\mathrm{ord}}
\longrightarrow H
\]

be the weighted labelled theta-cut synthesis on the source-pulled ordered
carrier. At finite cutoff this is an ordinary finite-column operator; on the
completed carrier use its already declared closed synthesis graph.

Define

\[
\gamma_\theta(\lambda)
=(A-\lambda)^{-1}B_\theta
\]

and

\[
M_\theta(\lambda)
=B_\theta^*(A-\lambda)^{-1}B_\theta.
\]

These formulas use the independently defined history generator and theta
incidence. They do not fit a Weyl function to a desired Gram.

## Resolvent identity

For `lambda,mu` off the real axis, the first resolvent identity gives

\[
(A-\lambda)^{-1}-(A-\overline\mu)^{-1}
=
(\lambda-\overline\mu)
(A-\lambda)^{-1}(A-\overline\mu)^{-1}.
\]

Since `A` is self-adjoint,

\[
\gamma_\theta(\mu)^*
=
B_\theta^*(A-\overline\mu)^{-1}.
\]

Consequently

\[
M_\theta(\lambda)-M_\theta(\mu)^*
=
(\lambda-\overline\mu)
\gamma_\theta(\mu)^*\gamma_\theta(\lambda).
\]

Thus

\[
N_{M_\theta}(\lambda,\mu)
:=
\frac{M_\theta(\lambda)-M_\theta(\mu)^*}
{\lambda-\overline\mu}
=
\gamma_\theta(\mu)^*\gamma_\theta(\lambda).
\]

This is exactly the operator-valued Nevanlinna divided-difference identity
required by the boundary-triplet model.

## Positivity

For parameters `lambda_j`, source vectors `c_j`, and finite sums,

\[
\sum_{i,j}
\left\langle
N_{M_\theta}(\lambda_i,\lambda_j)c_j,c_i
\right\rangle
=
\left\|
\sum_j\gamma_\theta(\lambda_j)c_j
\right\|_H^2
\ge0.
\]

Hence the parameter-dependent theta kernel is positive off the seam for a
source-derived reason: it is a resolvent Gram.

On a label basis `e_alpha`,

\[
N_{M_\theta}(\lambda,\mu)_{\alpha\beta}
=
\left\langle
(A-\mu)^{-1}B_\theta e_\beta,
(A-\lambda)^{-1}B_\theta e_\alpha
\right\rangle_H,
\]

with the argument order adjusted to the declared inner-product convention.
These are interior theta-history profiles, not wall Riesz columns.

## Relation to stable histories

The two stable Evans histories are the restrictions/boundary values of the
resolvent construction from opposite half-planes, after translating between
`A=iD` and the centered Laplace parameter. Their failure to agree on the
continuous-spectrum seam is the retained Evans wall mismatch.

Thus the plus and minus gamma-fields are not to be identified before taking
boundary values. Reciprocal reflection exchanges their charts, while the
ordered Hardy port records the principal-value part of their seam limit.

## Cutoffs and ordered weights

At every finite prime/grade cutoff, the identity is exact by bounded operator
algebra. Since cutoffs commute with the labelled synthesis and converge in
the source-pulled ordered graph topology, the identity passes to the
completion wherever the resolvents remain uniformly bounded on compact
subsets of the upper or lower half-plane.

The primitive weight

\[
\omega_{p,k}^2\asymp k\log p
\]

enters through the source metric defining `B_theta`; it does not alter the
resolvent proof.

## What remains at the seam

This closes the Weyl/gamma-field identity off the history spectrum. It does
not provide a bounded whole-line resolvent on the seam. The seam theorem must
construct boundary values in the wall-extended rigging and show that:

1. the resolvent Gram splits into principal-value and residue coordinates;
2. the principal-value coordinate equals the ordered Hardy current;
3. the residue coordinate matches the retained endpoint/Wronskian packet;
4. reciprocal upper/lower boundary values satisfy the declared Green
   orientation;
5. the resulting generalized Weyl family couples continuously to the native
   wall boundary relation.

The interior theta-profile observer is therefore a genuine source-derived
Weyl gamma-field on both open resolvent half-planes. Its generalized boundary
value on the seam is the remaining coupling gate.
