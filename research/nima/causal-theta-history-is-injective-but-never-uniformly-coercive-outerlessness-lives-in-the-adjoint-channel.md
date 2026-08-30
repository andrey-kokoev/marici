# Causal theta history is injective but never uniformly coercive; outerness lives in the adjoint channel

## Three properties must be separated

For the Hardy--Laplace multiplier

\[
m_\Phi(z)
=
\int_0^\infty\Phi(u)e^{-zu}\,du,
\]

the following are different:

1. injectivity of the causal history;
2. density of its range, equivalently injectivity of the anti-causal adjoint;
3. a uniform lower operator bound.

The previous minimality frontier grouped them under “outerness.” Only the second is genuinely an outer-factor question.

## Causal injectivity

Under the Hardy--Laplace transform, the causal Volterra operator is multiplication:

\[
H^*
\simeq
M_{m_\Phi}.
\]

Assume \(m_\Phi\) is not identically zero. If

\[
m_\Phi f=0
\]

for \(f\in H^2\), then the product vanishes on the open half-plane. On the nonempty open set where \(m_\Phi\ne0\), one has \(f=0\); analyticity then gives \(f\equiv0\).

Therefore

\[
\ker H^*=\{0\}.
\]

This requires no zero-free theorem for \(m_\Phi\). Isolated transfer zeros do not create an \(H^2\) input kernel for a multiplication operator.

## Adjoint dark space

The anti-causal history is

\[
H\simeq M_{m_\Phi}^*.
\]

Hence

\[
\ker H
=
\bigl(\overline{m_\Phi H^2}\bigr)^\perp.
\]

Write the Hardy factorization

\[
m_\Phi=I_\Phi O_\Phi
\]

with inner factor \(I_\Phi\) and outer factor \(O_\Phi\). Since \(O_\Phi H^2\) is dense,

\[
\overline{m_\Phi H^2}
=
I_\Phi H^2,
\]

so

\[
\ker H
=
H^2\ominus I_\Phi H^2.
\]

Thus

\[
\ker H=\{0\}
\quad\Longleftrightarrow\quad
I_\Phi\text{ is constant}
\quad\Longleftrightarrow\quad
m_\Phi\text{ is outer up to a unit}.
\]

The no-inner-factor theorem is exactly an adjoint-channel faithfulness theorem. It is not needed for causal injectivity.

## Uniform coercivity is impossible

If \(\Phi\in L^1(0,\infty)\), the boundary multiplier obeys the Riemann--Lebesgue limit

\[
m_\Phi(i\omega)\longrightarrow0
\qquad(|\omega|\to\infty).
\]

Therefore the multiplication operator has no positive lower bound on the full Hardy space:

\[
\inf_{\|f\|=1}\|M_{m_\Phi}f\|=0.
\]

One may choose normalized Hardy functions concentrated near boundary frequencies where \(|m_\Phi(i\omega)|\) is arbitrarily small.

The same conclusion holds for \(M_{m_\Phi}^*\). Even when \(m_\Phi\) is outer and both histories are injective, neither is uniformly coercive on the full completed Hardy carrier.

This reproduces the earlier compact-incidence obstruction in the exact shift-semigroup representation.

## Consequence for the history Dirac

For

\[
\mathscr D_H
=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix},
\]

one has

\[
\ker\mathscr D_H
=
\ker H\oplus\ker H^*.
\]

The causal summand is automatically trivial when \(\Phi\ne0\). The entire exact kernel question is therefore

\[
\ker\mathscr D_H
=
H^2\ominus I_\Phi H^2.
\]

So the history Dirac is injective precisely when the theta transfer has no nonconstant inner factor. But even then zero remains in its approximate spectrum because the singular values decay along high boundary frequencies.

Injectivity and coercivity must not be conflated.

## RH-strength warning

If the source theta transfer is later identified with a scalar function whose inner zeros encode the completed zeta divisor, proving it outer would be equivalent to excluding those zeros, not an upstream explanation.

The audit must first determine exactly which scalar section \(m_\Phi\) represents. There are two possibilities:

- \(m_\Phi\) is a zero-free propagation factor, while the zeta divisor enters only through arithmetic boundary sewing;
- \(m_\Phi\) already contains the zeta divisor, in which case an outer theorem is RH-strength and cannot be assumed as a minimality lemma.

The finite-rank sewing architecture requires the first typing.

## Correct minimal realization statement

The shift boundary input is cyclic for the shift reservoir in the usual extrapolation-space sense. The causal theta filter is injective. This gives algebraic controllability and one-sided faithfulness.

The remaining realization gates are:

1. prove the boundary incidence is cyclic in the declared weighted rigging;
2. factor \(m_\Phi\) canonically;
3. identify any inner model space with a typed source sector;
4. show whether that sector is removed by the reference-extension quotient or remains a genuine adjoint dark space;
5. do not demand a global lower bound from the theta filter;
6. obtain global Green coercivity from the noncompact arithmetic observer and typed direct-sum packet instead.

## Localized lower bounds

Although global coercivity fails, compact frequency windows may have positive bounds if

\[
\inf_{|\omega|\le R}|m_\Phi(i\omega)|>0.
\]

Such estimates are local spectral-window statements. They cannot be made uniform as \(R\to\infty\) for an \(L^1\) theta kernel.

This is the correct scope for finite-cutoff metric comparisons involving the history filter.

## Minimal hostiles

An outer transfer such as \((1+z)^{-1}\) gives injective causal and adjoint histories but has no uniform lower bound.

A Blaschke factor times an outer decay gives injective causal history and a nontrivial adjoint model-space kernel.

A nonzero transfer with isolated interior zeros still defines an injective multiplication operator, showing why transfer zeros are not automatically state kernels.

## Frontier contraction

The next source calculation is no longer a generic “minimality theorem.” It is the canonical Hardy factorization of the independently defined theta transfer and a typing audit of its inner model space.

The result must decide whether the inner factor belongs to zero-free propagation or already carries the RH divisor. Only the former permits the finite boundary sewing determinant to remain the unique zero mechanism.
