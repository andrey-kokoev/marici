# The ground-state SU(1,1) matrix coefficient shows polynomial semilocal degree tails and obstructs naive trace-class curvature

## Exact ground-state column

Let

\[
M_{m0}(x)
=
\langle P_m,
e^{ixX}P_0\rangle
\]

for the archimedean orthonormal-polynomial basis. The representation is the lowest-weight even metaplectic representation, and

\[
M_{00}(x)
=(\cosh x)^{-1/2}.
\]

The standard `SU(1,1)` coherent-state formula, with lowest-weight parameter `2k=1/2`, gives

\[
\boxed{
M_{m0}(x)
=
i^m
\sqrt{
\frac{(1/2)_m}{m!}
}
(\tanh x)^m
(\operatorname{sech}x)^{1/2}
}
\]

for the phase convention in which the Jacobi off-diagonal coefficients are positive. A harmless replacement of `i^m` by `(-i)^m` may occur under the opposite Fourier convention.

The formula agrees with the differential identity at `m=1`: since

\[
P_1(s)=
\frac{s}{a_0}
=
\sqrt2s,
\]

one gets

\[
M_{10}(x)
=
\frac{i}{\sqrt2}
\tanh x(\operatorname{sech}x)^{1/2}.
\]

## Degree prefactor

Stirling's formula gives

\[
\frac{(1/2)_m}{m!}
=
\frac{\Gamma(m+1/2)}
     {\sqrt\pi\Gamma(m+1)}
\sim
\frac1{\sqrt{\pi m}}.
\]

Hence

\[
\boxed{
\sqrt{
\frac{(1/2)_m}{m!}
}
\sim
\pi^{-1/4}m^{-1/4}.
}
\]

For fixed `x`, the factor `|tanh x|^m` gives exponential degree decay. It is not uniform as `|x| -> infinity`, because `tanh x -> 1`.

## One-prime Gram column

For one prime `p`, the Euler-weighted Gram operator has bilateral Poisson expansion

\[
G_p
=
\frac1{1-p^{-1}}
\sum_{k\in\mathbb Z}
p^{-|k|/2}
 e^{ik(\log p)X}.
\]

Therefore

\[
(G_p)_{m0}
=
\frac1{1-p^{-1}}
\sum_{k\in\mathbb Z}
p^{-|k|/2}
M_{m0}(k\log p).
\]

Because `G_p` preserves parity, the odd entries vanish. For even `m`, the terms at `plus-or-minus k` add with the same real phase.

## Large-prime-power optimization

Put

\[
x=k\log p,
\qquad
y=e^{-x}=p^{-k}.
\]

For large positive `x`,

\[
(\operatorname{sech}x)^{1/2}
\asymp
y^{1/2},
\]

\[
(\tanh x)^m
=
\left(1-2y^2+O(y^4)
\right)^m
\asymp
\exp(-2my^2)
\]

when `my^4` is controlled. The Euler coefficient is

\[
p^{-k/2}=y^{1/2}.
\]

Thus one summand in the even Gram column has magnitude

\[
\boxed{
\asymp
m^{-1/4}
ye^{-2my^2}.
}
\]

As a continuous function of `y`, this is maximized at

\[
y\asympm^{-1/2},
\]

and the maximal scale is

\[
\boxed{
m^{-3/4}.}
\]

## Discrete prime-power subsequence

The allowed values are `y=p^(-k)`. Choose degrees

\[
m_k\asympp^{2k}.
\]

Then

\[
p^{-k}\asympm_k^{-1/2},
\]

so the `k`-th prime-power term attains the same scale:

\[
\boxed{
|(G_p)_{m_k,0}|
\gtrsim
m_k^{-3/4}
}
\]

for an even-degree subsequence, modulo the fixed phase sign.

For even degrees the Poisson coefficients are positive and the `plus-or-minus k` terms have matching phase, so this contribution is not removed by conjugate cancellation. All nonzero terms in a fixed even row have the same phase `i^m`; their remaining factors are nonnegative. Hence there is no destructive cancellation, and the selected summand gives the stated lower bound after fixing uniform asymptotic constants.

## Consequence for the number commutator

Formally,

\[
[N,G_p]_{m0}
=m(G_p)_{m0}.
\]

Along the preceding subsequence,

\[
|[N,G_p]_{m_k,0}|
\gtrsim
m_k^{1/4}.
\]

Thus the ground-state column of `[N,G_p]` is not square summable and is not even bounded as a vector, subject to the stated lower-bound completion. This rules out the previously hoped-for estimate

\[
|G_{mn}-\delta_{mn}|
\le
Ce^{-c|m-n|}
P(m+n)
\]

with sufficiently mild `P`, uniformly over all Euler frequencies.

## Interpretation

Every fixed scaling displacement has exponential off-diagonal decay in degree. But the Euler resolvent contains arbitrarily large displacements

\[
k
\log p
\]

with coefficient `p^(-k/2)`. A displacement of size `k log p` reaches degrees of order

\[
e^{2k\log p}=p^{2k}.
\]

At precisely that degree, the Euler coefficient and coherent-state amplitude combine to leave only the polynomial tail `m^(-3/4)`.

This is the degree-space counterpart of the infinite prime-power translation channel.

## What this does and does not disprove

The calculation strongly obstructs:

- trace-class or boundedness of the raw commutator `[N,G_p]`;
- an unregularized trace-class curvature `widetilde N_p-N` obtained by naive Cholesky perturbation;
- uniform exponential off-diagonal estimates after summing all prime powers.

It does not by itself prove that

\[
(\widetilde N_p-N)
(W_{\lambda,\infty}-i)^{-r}
\]

fails to be trace class for sufficiently large `r`. The prolate resolvent supplies degree decay and may regularize the polynomial tail.

Nor does it rigorously transfer the lower bound from `G_p` to its Cholesky factor without additional triangular-factor analysis.

## Revised Schatten target

The correct question is a **relative-order** estimate. If the degree curvature grows like a positive fractional power of `N`, then multiplication by a sufficiently high prolate resolvent power can still be trace class.

One should seek bounds of the form

\[
\boxed{
\widetilde N_S-N
=
O((1+N)^\alpha)
}
\]

in quadratic-form or matrix sense, followed by

\[
(\widetilde N_S-N)
(1+W_{\lambda,\infty}^2)^{-r/2}
\in
\mathcal L^1
\]

for `r` above the resulting order threshold.

## Disposition

The explicit `SU(1,1)` ground-state coefficient reveals a polynomial semilocal degree tail:

\[
\boxed{
M_{m0}(k\log p)
p^{-k/2}
\sim
m^{-3/4}
\quad
\text{when }m\asymp p^{2k}.
}
\]

Thus naive trace-class curvature is not the right expectation. The viable bridge is a relatively trace-class perturbation after enough prolate resolvent smoothing.
