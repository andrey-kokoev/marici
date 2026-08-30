# The raw Stieltjes-to-theta comparison has the wrong bounded direction

## Soft source vector

At prime \(p\), let

\[
d_p
=
W_{2\log p}-W_{\log p}.
\]

Its raw Stieltjes norm satisfies

\[
\|d_p\|_\nu
\le
C(\log p)^{-1/2}
\exp\left[
-\frac\pi8(\log p)^2
\right].
\]

Thus the source disagreement becomes super-polynomially soft.

## Theta odd port

The completed theta boundary has a fixed nonzero odd Wronskian direction

\[
j_\theta
=
\begin{pmatrix}
\frac14\\[2pt]
-\frac14
\end{pmatrix},
\qquad
\|j_\theta\|_{2I}=\frac12.
\]

Suppose a proposed forward comparison

\[
C_p:
\mathcal H_p^{\mathrm{win}}
\longrightarrow
\mathcal H_p^{\theta}
\]

retains this odd port with a coefficient \(a_p\):

\[
C_pd_p=a_pj_\theta+\text{orthogonal terms}.
\]

Then

\[
\|C_p\|
\ge
\frac{|a_p|\|j_\theta\|}
{\|d_p\|_\nu}.
\]

## Finite-order no-go

Assume \(a_p\) has finite exponential order in \(L=\log p\); equivalently,
for some fixed \(m\),

\[
|a_p|\ge c p^{-m}
]

along an infinite prime subsequence where the odd port is retained.

Then

\[
\|C_p\|
\ge
c'
(\log p)^{1/2}
\exp\left[
\frac\pi8(\log p)^2-m\log p
\right].
\]

This exceeds every fixed power of \(p\).

Therefore no forward comparison from the raw Stieltjes endpoint norm to a
nonvanishing finite-order theta odd port can be completion-continuous in the
declared exponential-order scale.

## Euler coefficients do not repair it

Primitive or square factors such as

\[
p^{-1/2},
\qquad
p^{-1}
\]

change only the linear term in \(\log p\). They cannot compensate the
quadratic exponential

\[
\exp\left[
\frac\pi8(\log p)^2
\right].
\]

Thus retaining Euler weights on the port does not make the raw forward map
bounded.

## Correct bounded direction

The reverse map

\[
C_p^{\mathrm{rev}}:
\mathcal H_p^\theta
\longrightarrow
\mathcal H_p^{\mathrm{win}},
\qquad
j_\theta\longmapsto d_p,
\]

has norm tending to zero. Across primes it is trace class by the disagreement
synthesis theorem.

Hence the completion-stable constructor direction is

\[
\text{theta odd port}
\longrightarrow
\text{raw window disagreement},
\]

not a uniformly invertible or bounded-forward identification in the opposite
direction.

## Alternatives

A forward Adams comparison can still exist only if one of the following is
source-declared:

1. the source endpoint topology is strengthened so \(d_p\) is not soft;
2. the theta odd coefficient \(a_p\) carries matching
   super-polynomial decay;
3. the comparison is a relation whose bounded leg points from theta to
   window;
4. the odd port is asymptotically compressed to zero.

The current Euler order profiles support options 3 or 4, not option 2.

## Consequence for quadratic Green functoriality

An isometric pullback identity

\[
G_p^{\mathrm{win}}
=
C_p^*G_p^\theta C_p
\]

with \(C_p\) directed window-to-theta would force the same unbounded norm
growth.

The viable identity is instead a compression:

\[
G_p^{\mathrm{win}}
=
J_pG_p^\theta J_p^*
\]

or the conventionally typed mate, where \(J_p\) maps the theta auxiliary
carrier into the soft window carrier.

This matches the trace-class Schur architecture already obtained.

## Relation to the Adams arrow

The arithmetic Adams arrow may still point primitive-to-square at the
coefficient level. The analytic realization need not be a bounded operator in
the same direction; it may be a closed relation whose adjoint or incidence
leg is bounded.

Direction must be fixed after quotient and dual typing, not inferred from the
arithmetic label arrow alone.

## Hostile

Construct a finite-prime Cholesky isometry from the window plane into the
theta plane. It exists for every \(p\), but its norm grows
super-polynomially and no completed graph survives.

## Frontier

Quadratic Green functoriality is not merely unproved in the raw frame; its
bounded direction is determined:

\[
\text{theta graph}
\xrightarrow{\mathfrak S_1}
\text{window disagreement}.
\]

The first Adams edge must be formulated as the corresponding closed relation
or adjoint incidence, unless a stronger source endpoint topology is supplied.
