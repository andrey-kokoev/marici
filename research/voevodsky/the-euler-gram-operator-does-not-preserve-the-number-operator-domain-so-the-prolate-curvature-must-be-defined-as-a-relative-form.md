# The Euler Gram operator does not preserve the number-operator domain, so the prolate curvature must be defined as a relative form

## Ground-column lower bound

For one prime `p`, the Euler Gram operator

\[
G_p=
|L_p(1/2-iX)|^2
\]

has, along an even subsequence

\[
m_k\asympp^{2k},
\]

the lower bound

\[
\boxed{
|(G_p)_{m_k,0}|
\ge
c_pm_k^{-3/4}.
}
\]

This follows from the exact lowest-weight `SU(1,1)` matrix coefficient and positivity of the even Poisson summands.

## Number-operator domain

In the polynomial basis,

\[
Ne_m=me_m.
\]

Hence

\[
\operatorname{Dom}N
=
\left\{
(a_m):
\sum_{m\ge0}
m^2|a_m|^2<\infty
\right\}.
\]

The vacuum vector `e_0` belongs to every power domain of `N`. But

\[
G_pe_0
=
\sum_m
(G_p)_{m0}e_m.
\]

Along the subsequence `m_k`,

\[
m_k^2
|(G_p)_{m_k,0}|^2
\ge
c_p^2m_k^{1/2}.
\]

The terms do not even tend to zero. Therefore

\[
\boxed{
G_pe_0
\notin
\operatorname{Dom}N.
}
\]

## Raw commutator is not defined on the polynomial core

The expression

\[
[N,G_p]e_0
=
NG_pe_0-G_pNe_0
=
NG_pe_0
\]

is undefined as a Hilbert-space vector because `G_p e_0 notin Dom N`. Consequently

\[
\boxed{
[N,G_p]
\text{ is not defined on the full polynomial core}.}
\]

This is stronger than failure of boundedness or trace class.

The same issue propagates to any formula for the transported degree operator obtained by naively differentiating or commuting the Euler Gram metric with `N`.

## Correction to the Cholesky formula

Finite polynomial truncations admit positive Cholesky factors

\[
G_{p,n}=R_{p,n}^*R_{p,n}.
\]

But passage to an infinite triangular operator does not imply that

\[
R_p^{-1}NR_p-N
\]

is defined on finite sequences. The Cholesky operator can send a finite sequence to a vector outside `Dom N`, exactly as `G_p` does to `e_0`.

Therefore the transported degree operator must be defined by unitary transport from the completed semilocal Hilbert space, with its domain transported simultaneously. Subtracting it from `N` requires an intersection or form-domain theorem.

## Form-level formulation

Let

\[
q_N(f)=
\|N^{1/2}f\|^2,
\qquad
\operatorname{Dom}q_N=
\operatorname{Dom}N^{1/2}.
\]

The semilocal degree form, transported to the archimedean carrier by the scaling unitary, is

\[
q_{N,S}(f)
=
\|N_S^{1/2}
\Omega_S^-f\|_{H_S}^2
\]

with domain

\[
\operatorname{Dom}q_{N,S}
=
(\Omega_S^-)^{-1}
\operatorname{Dom}N_S^{1/2}.
\]

The curvature should be the form difference

\[
\boxed{
\delta q_{N,S}
=q_{N,S}-q_N
}
\]

on

\[
\operatorname{Dom}q_{N,S}
\cap
\operatorname{Dom}q_N.
\]

This intersection must first be shown dense. It cannot be assumed to contain the polynomial core.

## Relative form boundedness target

A workable prolate perturbation theorem would prove

\[
\boxed{
|\delta q_{N,S}(f)|
\le
C_S
\left(
q_{W_\infty}^{(\alpha)}(f)
+
\|f\|^2
\right)
}
\]

for an appropriate positive graph form associated with a sufficiently high power of the archimedean prolate operator.

Equivalently, one seeks boundedness of the sandwiched form

\[
(1+|W_{\lambda,\infty}|)^{-r/2}
(\widetilde N_S-N)
(1+|W_{\lambda,\infty}|)^{-r/2}
\]

in the quadratic-form sense before asking for Schatten membership.

Two-sided smoothing is natural because a one-sided product may not map into the domain of the curvature operator.

## Why right-resolvent smoothing cannot be asserted yet

The earlier expression

\[
(\widetilde N_S-N)
(W_{\lambda,\infty}-i)^{-r}
\]

presupposes the range inclusion

\[
\operatorname{ran}
(W_{\lambda,\infty}-i)^{-r}
\subseteq
\operatorname{Dom}\widetilde N_S
\cap
\operatorname{Dom}N.
\]

The ground-column calculation shows that bounded Euler metric transformations can destroy `Dom N`. Hence this inclusion is a substantive theorem, not automatic resolvent regularization.

## Geometric interpretation

Large prime powers create coherent states centered at degrees

\[
m\asympp^{2k}.
\]

Their coefficients are small in Hilbert norm but carry large degree energy. Thus the Euler resolvent is bounded on `H` while being singular relative to the number-operator graph norm.

This is precisely why semilocal Hilbertian stability does not imply prolate-domain stability.

## Revised hierarchy of gates

Before a Birman--Krein determinant for the prolate pair can be defined, one must prove in order:

1. density of
   \[
   \operatorname{Dom}q_{N,S}
   \cap
   \operatorname{Dom}q_N;
   \]
2. closability and lower-order control of `delta q_N,S` relative to a prolate graph form;
3. compactness of an appropriately sandwiched form resolvent difference;
4. Schatten or semifinite trace-ideal membership;
5. equality of its scattering phase with the Euler pairing phase.

The previous analysis had begun at gate 4 without establishing gates 1--3.

## Disposition

The one-prime Euler Gram operator already violates number-domain preservation:

\[
\boxed{
G_pe_0
\notin
\operatorname{Dom}N.
}
\]

Accordingly the raw degree curvature and its commutator formulas are not operators on the polynomial core. The prolate comparison must be rebuilt as a closed relative quadratic-form problem with two-sided smoothing.
