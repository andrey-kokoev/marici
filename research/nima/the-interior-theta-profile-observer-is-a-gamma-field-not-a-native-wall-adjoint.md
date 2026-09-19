# The interior theta-profile observer is a gamma-field, not a native wall adjoint

## Native-adjoint obstruction

The native broken-`H1` wall observation has piecewise-exponential Riesz
columns. The arithmetic incidence has completed-theta cut columns

\[
u_\alpha,
\qquad \alpha=(p,k).
\]

Since these columns have theta curvature between walls, they cannot be native
wall Riesz vectors. Neither adjoint equality nor finite-cutoff Douglas
absorption repairs this mismatch.

The correct enlargement is therefore an interior analysis operator whose
functionals are

\[
(\Gamma_\theta f)_\alpha
=\langle f,u_\alpha\rangle_G.
\]

Its adjoint satisfies

\[
\Gamma_\theta^*e_\alpha=u_\alpha
\]

by construction. This does not identify `Gamma_theta` with endpoint or jump
observation.

## Reproducing-kernel realization

The operator-model theorem in *Boundary Value Problems, Weyl Functions, and
Differential Operators*, Chapter 4, states that every nonnegative
operator-valued kernel defines an RKHS with bounded point evaluations and

\[
E(\mu)^*\varphi=K(\cdot,\mu)\varphi.
\]

See the indexed corpus at `boundary:p231--p240`, especially the theorem around
`boundary:p235`.

For finite label sets define the theta Gram kernel

\[
K_\theta(\alpha,\beta)
=\langle u_\beta,u_\alpha\rangle_G.
\]

Then

\[
\sum_{\alpha,\beta}
\overline{c_\alpha}K_\theta(\alpha,\beta)c_\beta
=
\left\|\sum_\alpha c_\alpha u_\alpha\right\|_G^2
\ge0.
\]

Thus every finite cutoff already has a canonical RKHS realization whose
kernel sections are exactly the theta-cut atoms. The projective completed
kernel is obtained only if these finite forms obey the declared cutoff bounds;
finite positivity alone is not a completion theorem.

## Gamma-field interpretation

Boundary-triplet theory supplies a more source-sensitive formulation. A
gamma-field maps boundary/source data to interior defect solutions, while its
Weyl function is the boundary response:

\[
M(\lambda)=\Gamma_1\gamma(\lambda).
\]

The standard adjoint formula relates `gamma(lambda)^*` to a boundary trace of
the resolvent. See `boundary:p128--p134` and the motivating formula at
`boundary:p13`.

The labelled theta synthesis should therefore be typed as

\[
\gamma_\theta(\lambda)e_\alpha
=u_\alpha(\lambda),
\]

and the enlarged observer as `gamma_theta(lambda)^*`. Its Weyl kernel must
satisfy

\[
N_{M_\theta}(\lambda,\mu)
=
\gamma_\theta(\mu)^*\gamma_\theta(\lambda),
\]

or entrywise

\[
N_{M_\theta}(\lambda,\mu)_{\alpha\beta}
=
\langle
u_\beta(\mu),u_\alpha(\lambda)
\rangle_G.
\]

Uniformly strict Nevanlinna functions admit precisely such reproducing-kernel
boundary-triplet models; see `boundary:p242--p256`.

## Coupling rather than identification

Orthogonal coupling of boundary triplets, treated at `boundary:p281--p286`,
allows the native wall triple and the theta-profile gamma-field to remain
distinct components of one conservative extension. This matches the faithful
joint-graph architecture:

\[
f\longmapsto
\bigl(f,\Gamma_{\mathrm{wall}}f,
\Gamma_\theta f\bigr).
\]

The construction does not require

\[
\Gamma_{\mathrm{wall}}^*=\gamma_\theta.
\]

The two channels may instead interact through their Weyl/Schur coupling while
retaining separate source provenance.

## Existing source map

Repository work already supplies the candidate gamma-field on differentiated
front atoms:

\[
Jq_{p,k}=u_{p,k}.
\]

This map is fibrewise bi-bounded, cutoff-natural, and has a closed retained
joint graph. Hence the finite kernel above is source-derived rather than
fitted.

The limitation is exact: `q_(p,k)` is a differentiated front. Passing to the
primitive ordered window introduces norm growth

\[
\|W_{k\log p}\|^2\asymp k\log p.
\]

Therefore the primitive gamma-field requires the source weight

\[
\omega_{p,k}^2\asymp k\log p.
\]

This weight must be derived from the ordered-port Green form.

## Acceptance theorem

A completed interior-profile observer is constructed once the following are
proved on one common projective graph:

1. the weighted synthesis `gamma_theta` is continuous and closed;
2. its Gram kernels converge under prime and grade cutoffs;
3. reciprocal/Fourier transport acts covariantly on the kernel sections;
4. the ordered Wronskian form is continuous on the gamma-field range;
5. the source-derived primitive metric supplies exactly the `k log p` weight;
6. orthogonal coupling with the native wall triple preserves the Green form
   and has zero retained radical.

This route enlarges the observer by actual interior theta profiles. It does
not manufacture arithmetic incidence from endpoint evaluation, and it does
not by itself prove the RH-equivalent energy-cycle law.
