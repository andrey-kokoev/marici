# Cyclic-row connector quartic census

## Row-Gram representation

Let \(R=SS^T\). Its six independent entries split into two cyclic triples:
the three diagonal entries \(d_i\) and the three off-diagonal entries
\(o_i=(R_{01},R_{12},R_{20})\).

A connector quartic is a quadratic form in these six variables. Solving the
exact invariance equation under simultaneous cyclic permutation gives a
seven-dimensional space.

## Explicit orbit basis

One basis consists of

\[
\sum_i d_i^2,
\quad \sum_i d_id_{i+1},
\quad \sum_i o_i^2,
\quad \sum_i o_io_{i+1},
\]

and the three relative cyclic contractions

\[
\sum_i d_io_i,
\quad \sum_i d_io_{i+1},
\quad \sum_i d_io_{i-1}.
\]

All seven forms are exactly invariant and linearly independent.

## Current action and authority

The WP483 frame Frobenius quartic and the WP493 radial square span only two
directions:

\[
\operatorname{Tr}(R^2)=\sum_i d_i^2+2\sum_i o_i^2,
\]

\[
(\operatorname{Tr}R)^2=\sum_i d_i^2+2\sum_i d_id_{i+1}.
\]

Hence the current connector action has codimension five inside the declared
\(C_3\)-invariant quartic space. At the isotropic vacuum only the first two
orbit sums are nonzero, but the remaining coefficients affect fluctuations and
need not stay zero under RG flow.

The source must either declare a stronger row symmetry that forbids the five
directions or promote all seven cyclic invariants to independent running
couplings. Until then the scalar truncation and full Hessian are incomplete.
