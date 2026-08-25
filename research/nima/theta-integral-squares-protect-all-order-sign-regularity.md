# Integral squares protect all-order sign regularity

## Theorem

Let

\[
b(t,m^2)
=t^{5/4}m^2(2\pi tm^2-3)e^{-\pi tm^2},
\qquad t\ge1,\quad m\in\mathbb Z_{>0}.
\]

For every order \(n\), every \(t_1<\cdots<t_n\), and every set of distinct
ordered positive integers \(m_1<\cdots<m_n\), the spectral matrix has

\[
\boxed{
\operatorname{sgn}\det[b(t_i,m_j^2)]_{i,j=1}^n
=(-1)^{n(n-1)/2}.
}
\]

Thus the faithful integral-winding kernel is strictly sign regular of all
orders even though its continuous relaxation fails at order seven.

## General Wronskian polynomial

The preceding derivation gives

\[
W_n
=e^{-x\sum y_i}V(y)(-1)^{n(n-1)/2}Q_n(z),
\]

where

\[
Q_n(z)
=\sum_{j=0}^n
(-1)^{n-j}2^j(2(n-j)+1)!!\,e_j(z).
\]

For the discrete proof, factor the top elementary-symmetric term:

\[
Q_n(z)
=2^ne_n(z)
\sum_{r=0}^n(-1)^r
\frac{(2r+1)!!}{2^r}e_r(z^{-1}).
\]

Write

\[
A_r=\frac{(2r+1)!!}{2^r}e_r(z^{-1}).
\]

All \(A_r\) are positive and \(A_0=1\).

## Arithmetic reciprocal bound

For distinct positive integers \(m_j\), at any \(t\ge1\),

\[
z_j=\pi t m_j^2,\qquad S=\sum_jz_j^{-1}.
\]

The maximal reciprocal sum occurs for the initial integers. Without using
the Basel identity,

\[
\sum_{m=1}^{\infty}\frac1{m^2}
<1+\sum_{m=2}^{\infty}\frac1{m(m-1)}
=2.
\]

Since \(\pi>3\),

\[
\boxed{S<\frac23.}
\]

This is the integrality protection unavailable in the continuous chamber,
where seven spectral points may cluster near one.

## Alternating-term domination

For positive variables \(w_j=z_j^{-1}\),

\[
(r+1)e_{r+1}(w)
=\sum_{|I|=r}w_I\sum_{j\notin I}w_j
\le S e_r(w).
\]

Consequently

\[
\frac{A_{r+1}}{A_r}
\le
\frac{2r+3}{2(r+1)}S
\le\frac32S
<1.
\]

Hence \(A_0>A_1>\cdots>A_n>0\). The alternating sum

\[
A_0-A_1+A_2-\cdots+(-1)^nA_n
\]

is strictly positive by pairing successive terms. Therefore \(Q_n(z)>0\)
for every order and every faithful square spectrum.

## From Wronskians to evaluation minors

Fix any ordered set of modes \(m_1<\cdots<m_n\) and regard
\(b(t,m_j^2)\) as functions of \(t\). Every initial Wronskian has the
required nonzero sign because the reciprocal bound applies to every subset.
They form an extended complete Chebyshev system on \(t\ge1\).

The generalized Vandermonde criterion then gives the stated sign for every
ordered evaluation matrix \(b(t_i,m_j^2)\). The positive common factor
\(t^{5/4}\) and positive column factors \(m_j^2\) do not affect signs.

## Relationship to the continuous falsifier

There is no contradiction:

- continuous points \(x_j=1+j/1000\) can cluster and violate order seven;
- distinct square energies satisfy the global reciprocal bound and cannot
  cluster;
- the source integrality projection is therefore doing real mathematical
  work, not merely restricting notation.

This theorem resolves the discrete qualification left open in the prior
SSR6/order-seven-falsifier packet. The continuous wrong-sign minor remains
valid and shows why the integrality typing cannot be erased.

## RH significance and remaining gap

This is an independently derived, all-order, source-local orientation law:

\[
\text{adelic integrality}
\Longrightarrow
\text{square spectral separation}
\Longrightarrow
\text{all-order strict sign regularity}.
\]

It is stronger than pointwise positivity and is not obtained by dividing by
\(\Xi\), inspecting zeros, assuming Herglotz positivity, or rewriting the
Weil criterion.

It still does not prove RH. The remaining analytic bridge must show that this
discrete sign-regular spectral family gives the precise
variation-diminishing or real-zero property required for

\[
\Phi(u)=\sum_{m\ge1}b(e^{2u},m^2)
\]

and its cosine transform. Infinite summation, the nonlinear chart
\(t=e^{2u}\), and cosine transformation must each preserve the needed
property under a named theorem with verified hypotheses.

## Status

\[
\boxed{\text{faithful integral-square kernel is SSR}_{\infty}.}
\]

