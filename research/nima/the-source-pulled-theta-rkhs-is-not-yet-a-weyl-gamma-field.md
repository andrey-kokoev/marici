# The source-pulled theta RKHS is not yet a Weyl gamma-field

## Correction

The pulled-back ordered metric constructs a positive reproducing-kernel
carrier whose labelled sections are the theta-cut atoms. Positivity of a Gram
kernel is sufficient for an RKHS. It is not sufficient to identify that RKHS
with the gamma-field model of a boundary triple.

A boundary-triplet gamma-field has additional spectral structure. For a
self-adjoint reference extension `A_0`, it obeys a resolvent law of the form

\[
\gamma(\lambda)
=
\left[I+(\lambda-\mu)(A_0-\lambda)^{-1}\right]
\gamma(\mu),
\]

and its Weyl function satisfies

\[
M(\lambda)-M(\mu)^*
=
(\lambda-\overline\mu)
\gamma(\mu)^*\gamma(\lambda).
\]

These are the operator identities behind the Nevanlinna kernel in the
boundary-triplet corpus. A static positive label Gram does not imply either
identity.

## Exact theta gate

Let

\[
\gamma_\theta(\lambda)e_\alpha
=u_\alpha(\lambda)
\]

be the parameter-dependent interior theta synthesis on the source-pulled
ordered carrier. To promote it from an RKHS analysis map to a genuine
gamma-field, one must construct:

1. a closed symmetric history relation `S_theta`;
2. a self-adjoint reference extension `A_(theta,0)`;
3. boundary maps `Gamma_0,Gamma_1` satisfying the abstract Green identity;
4. the defect-space condition
   \[
   u_\alpha(\lambda)
   \in\ker(S_\theta^*-\lambda);
   \]
5. the normalization
   \[
   \Gamma_0u_\alpha(\lambda)=e_\alpha.
   \]

Only then is

\[
M_\theta(\lambda)e_\alpha
=
\Gamma_1u_\alpha(\lambda)
\]

a source-derived Weyl function.

## Executable kernel test

Before constructing the full relation, the necessary and nearly sufficient
observable test is the divided-difference identity

\[
\langle
u_\beta(\mu),u_\alpha(\lambda)
\rangle_{I,\mathrm{ord}}
=
\frac{
\langle M_\theta(\lambda)e_\alpha,e_\beta\rangle
-
\langle e_\alpha,M_\theta(\mu)e_\beta\rangle
}{\lambda-\overline\mu}.
\]

Equivalently,

\[
K_\theta(\lambda,\mu)
=
\frac{M_\theta(\lambda)-M_\theta(\mu)^*}
{\lambda-\overline\mu}.
\]

A failure of this identity rejects the proposed Weyl realization even though
the static Gram remains positive.

## Natural candidate from the history equation

The stable theta histories solve first-order equations of the form

\[
(\partial_q-\lambda)u(\lambda)=\Phi.
\]

Resolvent subtraction gives

\[
u(\lambda)-u(\mu)
=(\lambda-\mu)
(\partial_q-\lambda)^{-1}u(\mu)
\]

on a common resolvent chart, modulo the retained wall coordinate on the
continuous-spectrum seam. This is the correct source of a gamma-field
resolvent law.

For labelled cut atoms, the same identity must be checked after wall
extension, ordered primitive weighting, and reciprocal doubling. Endpoint
and Wronskian terms cannot be omitted because they supply the Green boundary
in the divided-difference calculation.

## Coupling consequence

Orthogonal coupling of the native wall triple with the theta-profile channel
is authorized only after the theta channel is shown to be a boundary triple,
boundary relation, or explicitly declared generalized Weyl family. Until
then the faithful joint graph is valid as a positive observer graph, but the
phrase “orthogonally coupled boundary triples” is premature.

## Revised frontier

The weighted interior observer and its RKHS are constructed. The next theorem
is the parameter-dependent Green identity that upgrades its Gram kernel to a
Nevanlinna divided-difference kernel. Concretely:

\[
\boxed{
M_\theta(\lambda)-M_\theta(\mu)^*
=(\lambda-\overline\mu)
\gamma_\theta(\mu)^*\gamma_\theta(\lambda)
}
\]

on the wall-extended ordered graph, with cutoff, reciprocal, and seam terms
retained.
