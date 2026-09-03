# The endpoint is one superunit Hausdorff mode

## Question

What does the endpoint residual become in the sampled-heat positive-contraction chart?

## Endpoint moments

At zero character, the endpoint heat term is

\[
H_E(t)=e^{t/4}.
\]

For mesh `h>0`, its sampled moments are

\[
b_n^E(t,h)
=e^{t/4}(e^{h/4})^n.
\]

Thus the endpoint alone is a positive rank-one moment sequence located at

\[
y_E=e^{h/4}>1.
\]

It lies outside the Hausdorff support interval `[0,1]` required for a positive heat generator.

## Two cone signatures

The endpoint Hankel matrix is

\[
M_0^E=e^{t/4}vv^*,
\qquad v_i=e^{ih/4},
\]

so it is PSD and rank one.

Its contraction localizer is

\[
M_{1-y}^E
=
(1-e^{h/4})e^{t/4}vv^*,
\]

which is negative semidefinite and rank one. Therefore the endpoint creates exactly one superunit support defect, not generic Hankel indefiniteness.

## Coupled completion problem

Write the full localizer as

\[
M_{1-y}=L_{\Gamma+\mathbb P}-
(e^{h/4}-1)e^{t/4}vv^*.
\]

If the gamma-plus-prime remainder `L_(Gamma+P)` is PSD, endpoint repair reduces to one rank-one domination inequality. In finite rank, with the necessary range condition, this is the Schur-complement bound

\[
(e^{h/4}-1)e^{t/4}
\langle v,L_{\Gamma+\mathbb P}^{\dagger}v\rangle
\le1.
\]

Equivalently, the endpoint defect vector must lie in the remainder feature range with contraction norm at most one.

## Hostile condition

The route fails immediately if the remainder localizer has a negative direction orthogonal to `v`, because a rank-one endpoint coupling cannot repair it. It also fails if `v` is outside the remainder range or the displayed domination exceeds one.

Thus the first source test is sharper than full determinant enumeration:

1. compute the inertia of the gamma-plus-prime localizer on `v^perp`;
2. test its range coupling to `v`;
3. evaluate the scalar Schur residual.

## Relation to prior repair mechanisms

Prior Marici sectors repeatedly found a source-fixed rank-one channel repairing one negative direction. Here the rank-one defect is not guessed: it is forced by the polar endpoint and appears as one atom beyond the contraction boundary. This is the first direct bridge from completion residuals to the Hausdorff semigroup cone.

## Boundary

No positivity of `L_(Gamma+P)` has been proved. The decomposition only localizes the possible mechanism. Prime and gamma terms must be retained together; separate sector positivity is already falsified in prior work.

## Disposition

Use the sampled localizer, not the raw Hankel cone, to isolate the endpoint anomaly. Test whether the coupled gamma-plus-prime source supplies a positive background and a source-fixed rank-one contraction certificate for the superunit endpoint mode.