# All Euler-resolvent Gram entries reduce exactly to derivatives of the archimedean sech characteristic function

## Archimedean characteristic function

Connes--Consani--Moscovici Proposition 5.2 computes the exponential generating function of the normalized moments of the archimedean cyclic measure. In the source normalization,

\[
\boxed{
\Phi_\infty(x)
=
\int_\mathbb R
e^{isx}d\mu_\infty(s)
=
\left(
\frac{2}{e^x+e^{-x}}
\right)^{1/2}
=
(\cosh x)^{-1/2}.
}
\]

Here `dmu_infinity` is the probability measure proportional to

\[
|\Gamma(1/4+is/2)|^2ds.
\]

Thus the full archimedean matrix-coefficient problem is controlled by one explicit function.

## Polynomial basis

Let

\[
P_n(s)
\]

be the real orthonormal polynomials for `dmu_infinity`. The source gives their Jacobi coefficients

\[
\boxed{
a_n=
\frac12
\sqrt{(2n+1)(2n+2)}
}
\]

in its Jacobi normalization.

The scaling unitary is

\[
U(x)=e^{ixX},
\qquad
X=M_s.
\]

Its polynomial-basis matrix coefficients are

\[
M_{mn}(x)
=
\langle P_m,
e^{ixX}P_n\rangle.
\]

## Exact differential formula

Since

\[
(-i\partial_x)^j
e^{isx}
=s^j e^{isx},
\]

functional calculus gives

\[
P_n(-i\partial_x)
e^{isx}
=P_n(s)e^{isx}.
\]

Therefore

\[
\boxed{
M_{mn}(x)
=
P_m(-i\partial_x)
P_n(-i\partial_x)
(\cosh x)^{-1/2}.
}
\]

This identity is exact. It replaces every unknown scaling matrix coefficient by a finite derivative of an elementary hyperbolic function.

Because the measure is even and the polynomials have parity `(-1)^n`, one also has the symmetry

\[
M_{mn}(-x)
=
\overline{M_{mn}(x)},
\]

and the coefficient is real or purely imaginary according to the parity of `m+n`.

## Euler-resolvent Gram matrix

For the finite-prime resolvent

\[
\widetilde B_S
=
\prod_{p\in S}
(I-p^{-1/2}e^{i(\log p)X})^{-1},
\]

write its norm-convergent expansion

\[
\widetilde B_S
=
\sum_{\mathbf k\ge0}
a_{\mathbf k}
e^{i\omega_{\mathbf k}X},
\]

where

\[
a_{\mathbf k}
=
\prod_{p\in S}p^{-k_p/2},
\qquad
\omega_{\mathbf k}
=
\sum_{p\in S}k_p\log p.
\]

The Gram operator is

\[
G_S=
\widetilde B_S^*\widetilde B_S.
\]

Its polynomial-basis entries are therefore

\[
\boxed{
(G_S)_{mn}
=
\sum_{\mathbf k,\mathbf l\ge0}
a_{\mathbf k}a_{\mathbf l}
P_m(-i\partial_x)
P_n(-i\partial_x)
(\cosh x)^{-1/2}
\bigg|_{
x=\omega_{\mathbf l}-\omega_{\mathbf k}}.
}
\]

The geometric Euler coefficients make the double series absolutely convergent for each fixed `m,n`.

## Equivalent one-sum Poisson formula

Using

\[
G_S(t)
=
\prod_{p\in S}
|1-p^{-1/2}e^{it\log p}|^{-2},
\]

and its bilateral Fourier expansion

\[
G_S(X)
=
C_S
\sum_{\mathbf k\in\mathbb Z^S}
c_{\mathbf k}
e^{i\omega_{\mathbf k}X},
\]

one obtains the simpler expression

\[
\boxed{
(G_S)_{mn}
=
C_S
\sum_{\mathbf k\in\mathbb Z^S}
c_{\mathbf k}
P_m(-i\partial_x)
P_n(-i\partial_x)
(\cosh x)^{-1/2}
\bigg|_{x=\omega_{\mathbf k}}.
}
\]

Here

\[
c_{\mathbf k}
=
\prod_{p\in S}p^{-|k_p|/2}.
\]

This formula preserves all cross-prime frequencies before summation.

## Analytic structure

The function

\[
(\cosh x)^{-1/2}
\]

is holomorphic in the strip

\[
|\operatorname{Im}x|<\pi/2
\]

and has square-root singularities at

\[
x=i\pi/2+i\pi n.
\]

On the real line,

\[
\Phi_\infty(x)
\sim
\sqrt2e^{-|x|/2}.
\]

Every fixed derivative has the same exponential real-axis decay times a bounded rational polynomial in `tanh x`. Thus for fixed `m,n`,

\[
|M_{mn}(x)|
\le
C_{mn}
e^{-|x|/2}.
\]

This gives direct exponential suppression of every fixed nonzero Euler frequency without passing through moments.

## Recurrence for matrix coefficients

The Jacobi relation

\[
sP_n(s)
=a_nP_{n+1}(s)
+a_{n-1}P_{n-1}(s)
\]

gives

\[
-i\partial_xM_{mn}(x)
=a_nM_{m,n+1}(x)
+a_{n-1}M_{m,n-1}(x).
\]

There is a symmetric recurrence in the `m` index. Starting from

\[
M_{00}(x)=(\cosh x)^{-1/2},
\]

these relations generate all matrix coefficients without symbolic high-order differentiation.

They also provide the appropriate framework for uniform off-diagonal estimates.

## Required uniform estimate

Fixed-index decay does not imply Schatten decay because the constants `C_mn` may grow rapidly with the degrees. The needed theorem is a joint estimate such as

\[
\boxed{
|M_{mn}(x)|
\le
Ce^{-c|x|}
e^{-c'|m-n|}
P(m+n)
}
\]

or a representation-theoretically correct variant.

Inserted into the geometric Euler sum, such a bound would control the off-diagonal entries of `G_S` and its Cholesky factor.

## Representation-theoretic interpretation

The source identifies the archimedean Jacobi system with the even component of the metaplectic representation of `SL(2,R)`. Therefore

\[
M_{mn}(x)
=
\langle P_m,
e^{ixX}P_n\rangle
\]

is a matrix coefficient of a fixed irreducible unitary representation. Sharp joint estimates should follow from explicit `SU(1,1)`/Meixner--Pollaczek matrix-coefficient formulas rather than generic derivative bounds.

## Disposition

The matrix coefficients required for the semilocal Cholesky problem are now explicit:

\[
\boxed{
\langle P_m,
e^{ixX}P_n\rangle
=
P_m(-i\partial_x)
P_n(-i\partial_x)
(\cosh x)^{-1/2}.
}
\]

Hence every finite-prime Gram matrix entry is an absolutely convergent arithmetic sum of derivatives of `sech(x)^(1/2)` at logarithms of `S`-units. The remaining gate is a uniform joint degree/frequency estimate strong enough to imply weighted Schatten control.
