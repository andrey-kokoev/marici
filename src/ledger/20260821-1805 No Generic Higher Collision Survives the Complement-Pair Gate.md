# 1805 — No Generic Higher Collision Survives the Complement-Pair Gate

## Question

Do Entry 1804's two complementary occurrence pairs meet the physical
five-site threshold as genuine higher Landau collisions?

## Complement reduction

For complementary regions \(A,A^c\),

\[
q_A+q_{A^c}
=
E_T+2\sum_{e\in\partial A}y_e.
\]

The defining complement wall is

\[
q_{e_{12}}=E_T+2y_{12}=0.
\]

Therefore simultaneous vanishing of a complementary pair forces the second
shared boundary distance to vanish.

## First pair

For

\[
(g_{145},g_{23}),
\]

the shared boundary is \(\{e_{12},e_{34}\}\). Hence

\[
y_{34}=0,
\]

which pins the loop point to the labelled focus \(C_2\).

At that focus, exact rational interval arithmetic proves that

\[
n_{12}
\quad\text{and}\quad
n_{45}+n_{51}
\]

are nonparallel. Their cross-product norm is strictly positive. Thus the
nonzero-multiplier stationarity equation has no solution.

\[
\boxed{
(g_{145},g_{23})\text{ is excluded as a smooth physical higher collision.}
}
\]

## Second pair

For

\[
(g_{15},g_{234}),
\]

the shared boundary is \(\{e_{12},e_{45}\}\), so

\[
y_{45}=0.
\]

But \(y_{45}\) is one of the two defining distances in

\[
g_5=X_5+y_{45}+y_{51}.
\]

The ordinary unit-gradient Landau model is therefore undefined. This locus
is the already existing defining-edge soft corner and must be treated by a
radial/Rees resolution.

## Result

Neither complementary pair produces a generic higher collision:

- one is killed by exact stationarity;
- one is confined to existing soft support.

No new carrier stratum is indicated.

## Next falsifier

Resolve the remaining \(y_{45}=0\) corner in loop polar coordinates. Retain
the two complementary occurrence labels separately and test whether their
double pole produces a first-Rees class, a Kummer sign, or zero.

## Evidence

- research/benincasa/checkers/five_site_g5_complement_pair_activation.py
- research/benincasa/results/five-site-g5-complement-pair-activation.json
- allocator claim: seqclaim-01cc7a482ecc96e51956ecbd
