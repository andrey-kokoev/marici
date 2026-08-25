# Completed circle kernel: global SSR6 and continuous order-seven failure

## Decisive outcome

For

\[
b(t,x)=t^{5/4}x(2\pi tx-3)e^{-\pi tx},
\qquad t,x\ge1,
\]

the source-derived kernel is globally strict reverse-sign-regular through
order six. It is not reverse-sign-regular of order seven on the continuous
completed chamber.

The physically discrete winding restriction \(x=n^2\) is not falsified by
the continuous counterexample and remains a separate question.

## General Wronskian formula

Put \(y=\pi t\) and

\[
f_y(x)=(2yx-3)e^{-yx}.
\]

Its \(k\)-th derivative is

\[
\frac{d^k}{dx^k}f_y(x)
=(-1)^k y^k\bigl(2yx-(2k+3)\bigr)e^{-yx}.
\]

Each derivative column has exactly two adjacent monomial degrees, \(k\) and
\(k+1\). In an order-\(n\) alternant, a monomial selection survives only
when it switches once from the lower to the upper degree. Dividing by the
Vandermonde gives

\[
W_n
=e^{-x\sum_i y_i}
V(y)(-1)^{n(n-1)/2}Q_n(z_1,\ldots,z_n),
\]

where \(z_i=xy_i\) and

\[
\boxed{
Q_n(z)
=\sum_{j=0}^n
(-1)^{n-j}2^j(2(n-j)+1)!!\,e_j(z).
}
\]

The elementary-symmetric convention is \(e_0=1\).

## Inductive derivative law

The coefficient formula gives the exact recursion

\[
\boxed{
\frac{\partial Q_n}{\partial z_i}
=2Q_{n-1}(z_1,\ldots,\widehat z_i,\ldots,z_n).
}
\]

At the larger boundary \(z_i=3\), define

\[
q_n=Q_n(3,\ldots,3)
=\sum_{r=0}^n(-1)^r
\binom nr6^{n-r}(2r+1)!!.
\]

The first values are

\[
q_1=3,\quad q_2=15,\quad q_3=57,\quad q_4=369,
\quad q_5=891,\quad q_6=15903,\quad q_7=-78975.
\]

Since \(Q_1>0\), the derivative recursion and positive boundary values imply
inductively that \(Q_n>0\) on \(z_i\ge3\) for every \(n\le6\). Therefore the
required reverse-sign-regular signs hold globally through order six on the
actual source domain \(z_i\ge\pi>3\).

## Why order seven fails continuously

The induction cannot continue because \(q_7<0\). More sharply, at the actual
completed boundary,

\[
Q_7(\pi,\ldots,\pi)
\approx-45643.30910936585.
\]

Continuity therefore forces the seventh Wronskian to have the opposite sign
for seven sufficiently close parameters near \(t=x=1\).

A direct 220-digit Decimal witness uses

\[
t_i=x_i=1+\frac{i}{1000},
\qquad i=0,\ldots,6.
\]

Its ordered seventh determinant is

\[
\det[b(t_i,x_j)]
\approx
7.24334750795570\times10^{-114}>0,
\]

while reverse sign regularity requires
\((-1)^{21}=-1\). This is a finite continuous order-seven falsifier.

## Discrete-winding qualification

The spectral trace uses \(x=n^2\), not arbitrary continuous \(x\). Testing

\[
t_i=1+\frac{i}{1000},
\qquad x_j=(j+1)^2
\]

still gives the expected negative seventh-order sign. Thus:

- all-order continuous total positivity is disproved;
- global SSR6 is proved;
- order-seven sign regularity on the discrete square spectrum remains open.

This distinction matters. A continuous canonical-system argument requiring
all-order sign regularity cannot use this kernel unchanged. A theorem
specialized to the discrete winding mixture might still survive.

## RH boundary

The result is both constructive and limiting:

1. SSR6 is a genuine source-derived variation law stronger than pointwise
   positivity.
2. The most tempting all-order continuous total-positivity programme fails
   at a finite, explicit order.
3. No RH conclusion follows from finite-order sign regularity.
4. The next legitimate question is whether the discrete matrix
   \(b(t_i,n_j^2)\) is all-order sign regular, or whether it has its own first
   finite failing minor.

The lane must not report the earlier order-six scan as evidence for
all-order continuous total positivity; order seven now decisively refutes
that extrapolation.

