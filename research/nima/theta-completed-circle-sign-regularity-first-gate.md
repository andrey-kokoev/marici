# Completed circle operator: first sign-regularity gate

## Source family

Grothendieck's completion differential produces the positive diagonal family

\[
B_t=\pi t^{5/4}
A^{1/2}(2\pi tA-3I)A^{1/2}e^{-\pi tA},
\qquad t\ge1,
\]

on integral mean-zero winding energies \(x=n^2\ge1\). Up to a positive
constant, its spectral kernel is

\[
b(t,x)=t^{5/4}x(2\pi tx-3)e^{-\pi tx}.
\]

Pointwise positivity follows from \(2\pi tx-3>0\). The stronger question is
whether ordered minors have the reverse-total-positive sign pattern

\[
\operatorname{sgn}\det[b(t_i,x_j)]_{i,j=1}^k
=(-1)^{k(k-1)/2}
\]

for \(t_1<\cdots<t_k\) and \(x_1<\cdots<x_k\).

## Exact order-two theorem

Positive factors depending only on \(t\) or \(x\) do not affect minor signs.
For fixed \(x_2>x_1\), consider the ratio

\[
R(t)=\frac{b(t,x_2)}{b(t,x_1)}.
\]

The common \(t^{5/4}\) factor cancels. With \(q=\pi tx\), the
\(t\)-dependent logarithmic derivative of
\((2q-3)e^{-q}\) is \(t^{-1}\phi(q)\), where

\[
\phi(q)=\frac{2q}{2q-3}-q.
\]

On the completed integral chart \(q\ge\pi\),

\[
\phi'(q)=-1-\frac{6}{(2q-3)^2}<0.
\]

Therefore \(R(t)\) strictly decreases with \(t\), and every ordered
\(2\times2\) minor is strictly negative. The family is strictly
reverse-sign-regular of order two on the whole source domain.

## Higher-order hostile scan

A high-precision Decimal checker tested every ordered minor of orders
\(2,\ldots,6\) on

\[
t\in\{1,1.02,1.05,1.1,1.25,1.5\},
\qquad
x\in\{1,4,9,16,25,36\}.
\]

All minors had the expected sign
\((-1)^{k(k-1)/2}\). The full sixth-order determinant was negative and
nonzero, approximately

\[
-3.22130685107387\times10^{-114}.
\]

This is supported numerical evidence only. It does not establish strict
sign regularity of every order or any consequence for zeros of the cosine
transform.

## Why this is a genuine next gate

Unlike the earlier scalar positivity reformulations, the kernel \(b(t,n^2)\)
is derived before the scalar trace:

\[
\text{integrality projection}
\to \text{circle Laplacian}
\to \text{completion differential}
\to B_t.
\]

A proof that this source family is sign-regular or totally positive after
the correct order reversal would be an independent operator-variation law.
It would still require a precise theorem connecting that law to the real-zero
property of the completed cosine transform; that implication must not be
assumed.

## Sharp next tests

1. Prove or falsify order three symbolically.
2. Identify whether
   \((2z-3)e^{-z}\) belongs to a known sign-regular kernel class on
   \(z\ge\pi\).
3. Search continuously near the boundary \(t=x=1\), where the completion
   polynomial is least separated from zero.
4. Test whether the trace mixture over \(x=n^2\) preserves the exact
   variation-diminishing hypothesis required by a real-zero theorem.

The first finite falsifier is any ordered \(k\times k\) minor with zero or
the wrong sign. A passing finite scan is evidence, never proof.

## Current status

\[
\boxed{\text{SSR}_2\text{ proved on }t\ge1,\ x\ge1;}
\]

\[
\boxed{\text{expected signs observed through order }6
\text{ on the stated grid}.}
\]

This is the first live RH-side candidate in this lane that is both
source-local and stronger than pointwise positivity, though its higher-order
theorem and analytic consequence remain open.

