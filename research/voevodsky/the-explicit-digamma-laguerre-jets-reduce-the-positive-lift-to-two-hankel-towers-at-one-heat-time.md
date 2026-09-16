# The explicit digamma--Laguerre jets reduce the positive lift to two Hankel towers at one heat time

## Objective

Combine the explicit completed heat-jet formula with the one-time Stieltjes reconstruction theorem.

This removes the continuous heat-time quantifier from the positive-lift target. The remaining source inequality is positivity of two nested Hankel towers at one chosen \(t_0>0\).

## Completed jet sequence

Fix

\[
t_0>0
\]

and define

\[
d_k
=
D_k(t_0)
=
(-1)^k
\Theta^{(k)}(t_0).
\]

The source-side formula is

\[
\begin{aligned}
d_k
={}&
(-1)^k
4^{-k}

e^{t_0/4}\\
&-
\frac{
\log\pi
}
{
4\sqrt\pi
}
\left(
\frac12
\right)_k

t_0^{-k-1/2}\\
&+
\frac1{4\pi}
\int_{\mathbb R}

u^{2k}

e^{-t_0u^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du\\
&-
\frac{
k!
}
{
2\sqrt\pi

t_0^{k+1/2}
}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}

e^{-y_n}
L_k^{-1/2}(y_n),
\end{aligned}
\]

where

\[
y_n
=
\frac{
(
\log n
)^2
}
{
4t_0
}.
\]

## Two Hankel towers

For every \(r\ge0\), define

\[
H_r(t_0)
=
(
d_{i+j}
)_{0\le i,j\le r},
\]

and

\[
H_r^+(t_0)
=
(
d_{i+j+1}
)_{0\le i,j\le r}.
\]

The exact one-time gate is

\[
\boxed{
H_r(t_0)
\succeq0,
\qquad
H_r^+(t_0)
\succeq0
\quad
\text{for every }r\ge0.
}
\]

The first tower is the ordinary moment tower. The second forces the representing measure to lie on the nonnegative squared-spectral axis.

## Polynomial form

For a polynomial

\[
p(\lambda)
=
\sum_{j=0}^r
c_j
\lambda^j,
\]

the ordinary Hankel form is

\[
\mathcal Q_{t_0}(p)
=
\sum_{i,j=0}^r
\overline{c_i}
c_j
d_{i+j}.
\]

The shifted form is

\[
\mathcal Q_{t_0}^+(p)
=
\sum_{i,j=0}^r
\overline{c_i}
c_j
d_{i+j+1}.
\]

If a positive squared-spectral measure exists, these are

\[
\mathcal Q_{t_0}(p)
=
\int_0^\infty
|p(
\lambda
)|^2

e^{-t_0\lambda}
\,d\nu(
\lambda
),
\]

\[
\mathcal Q_{t_0}^+(p)
=
\int_0^\infty
\lambda
|p(
\lambda
)|^2

e^{-t_0\lambda}
\,d\nu(
\lambda
).
\]

The source problem is to establish these signs directly from the coupled endpoint--digamma--prime formula, without assuming \(\nu\).

## Explicit coupled polynomial formula

Let

\[
\mathcal D_p
=
\sum_{j=0}^r
c_j
(-\partial_t)^j.
\]

Then

\[
\mathcal Q_{t_0}(p)
=
\left.
\overline{
\mathcal D_p
}
\mathcal D_p
\Theta(t)
\right|_{t=t_0},
\]

where conjugation acts on the polynomial coefficients.

Expanding with the jet formula gives four coupled contributions.

### Endpoint

\[
\mathcal Q_{t_0}^E(p)
=

e^{t_0/4}
\left|
p(-1/4)
\right|^2.
\]

This is positive in the ordinary Hankel form even though the individual endpoint jets alternate.

### Gamma constant

\[
\mathcal Q_{t_0}^{G,0}(p)
=
-
\frac{
\log\pi
}
{
4\sqrt\pi
}
\sum_{i,j}
\overline{c_i}
c_j
\left(
\frac12
\right)_{i+j}

t_0^{-i-j-1/2}.
\]

This block is signed and must remain coupled to the digamma integral and prime block.

### Digamma integral

\[
\mathcal Q_{t_0}^{G,int}(p)
=
\frac1{4\pi}
\int_{\mathbb R}
|p(u^2)|^2

e^{-t_0u^2}
\operatorname{Re}
\psi
\left(
\frac14+
\frac{iu}{2}
\right)
\,du.
\]

### Prime block

\[
\mathcal Q_{t_0}^{P}(p)
=
\sum_{i,j}
\overline{c_i}
c_j
D_{i+j}^{P}(t_0),
\]

with

\[
D_q^P(t_0)
=
-
\frac{
q!
}
{
2\sqrt\pi

t_0^{q+1/2}
}
\sum_{n\ge2}
\frac{
\Lambda(n)
}
{
\sqrt n
}

e^{-y_n}
L_q^{-1/2}(y_n).
\]

No entrywise estimate on the Laguerre terms proves positivity of this matrix block. The endpoint square, digamma integral, gamma constant, and prime block must be added before testing the polynomial form.

## Shifted tower

The shifted form is obtained by replacing every moment \(d_q\) with \(d_{q+1}\). Equivalently,

\[
\mathcal Q_{t_0}^+(p)
=
\mathcal Q_{t_0}(
\sqrt\lambda p
)
\]

at the level of a putative positive measure.

Source-side, it is the same coupled formula with one extra operator \(-\partial_t\). It must be proved independently; ordinary Hankel positivity alone permits representing mass on the full real moment line rather than \([0,\infty)\).

## One-time reconstruction

Assume

\[
H_r(t_0)
\succeq0,
\qquad
H_r^+(t_0)
\succeq0
\]

for every \(r\). The Stieltjes moment theorem gives a positive measure \(\mu_{t_0}\) on \([0,\infty)\) such that

\[
d_k
=
\int_0^\infty
\lambda^k
\,d\mu_{t_0}(
\lambda
).
\]

The completed source is holomorphic for

\[
\operatorname{Re}t>0.
\]

Its Taylor series at \(t_0\) therefore converges throughout every disk of radius less than \(t_0\). Hankel positivity makes every \(d_k\ge0\), so the required exponential moment bounds follow from absolute Taylor convergence.

Define

\[
d\nu(
\lambda
)
=

e^{t_0\lambda}
\,d\mu_{t_0}(
\lambda
).
\]

Then

\[
\Theta(t)
=
\int_0^\infty

e^{-t\lambda}
\,d\nu(
\lambda
)
\]

for all \(t>0\), first locally and then by analytic continuation.

Thus the two towers at one heat time imply complete monotonicity globally.

## Faithfulness

The completed spectral distribution is even. Pushforward under

\[
u
\longmapsto
\lambda=u^2
\]

is therefore faithful: a positive squared-spectral measure uniquely lifts to a positive symmetric spectral measure.

Consequently the one-time two-tower condition supplies every translated Gaussian Gram and excludes every hostile off-axis rotor.

## First nontrivial minors

The first coupled tests are

\[
d_0
\ge0,
\qquad

d_1
\ge0,
\]

\[
\boxed{
d_0d_2-d_1^2
\ge0,
}
\]

and

\[
\boxed{
d_1d_3-d_2^2
\ge0.
}
\]

The first determinant is log-convexity of \(\Theta\). The second is the corresponding shifted Stieltjes condition.

These rank-two inequalities are the cheapest coupled diagnostics that test common-measure correlations rather than individual jet signs.

## Tetrahedral interpretation

At fixed \(t_0\), the polynomial degree \(r\) supplies a finite positive observation cell. Successor inclusion

\[
p
\longmapsto
p+
0\lambda^{r+1}
\]

makes the Hankel towers principal-compatible.

A positive filler at every rank, together with faithful completion, constructs the Bernstein/Stieltjes carrier. A hostile rotor appears at a least finite rank as failure of one ordinary or shifted principal minor.

Thus the infinite positive tetrahedral lift can be tested as one nested pair of finite-rank towers rather than as a two-parameter family of derivative signs.

## What prior estimates provide

Prior research gives:

1. exact formulas for every entry;
2. broad-smoothing positivity at order zero;
3. Laguerre-root positivity for selected near-null diagonal directions;
4. finite-packet coercivity in restricted windows;
5. exact source successor coherence.

It does not provide positivity of the off-diagonal Laguerre matrix entries or the two complete Hankel towers.

The first missing matrix estimate is already

\[
d_0d_2
-
d_1^2
\ge0
\]

for the full coupled source.

## Disposition

The source-faithful positive-lift theorem is equivalent to one explicit one-time matrix hierarchy:

\[
\boxed{
H_r(t_0)
\succeq0,
\qquad
H_r^+(t_0)
\succeq0
\quad
(r=0,1,2,\ldots).
}
\]

Every matrix entry is the coupled digamma--Laguerre expression above. The continuous heat-time variable is no longer part of the proof target.
