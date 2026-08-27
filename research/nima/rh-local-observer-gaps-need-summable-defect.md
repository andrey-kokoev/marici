# RH local observer gaps need summable defect

## Composition problem

At a finite stage, a transported positive observer may dominate the next
observer with a strict relative margin. This does not by itself produce a
nonzero observer after restricted-product completion.

Let `m_j` denote the positive margin after stage `j`. Suppose the authorized
comparison at that stage gives

\[
m_j\geq (1-\rho_j)m_{j-1},
\qquad 0\leq\rho_j<1.
\]

After `N` stages,

\[
m_N\geq m_0\prod_{j=1}^{N}(1-\rho_j).
\]

Every finite product is positive. The completed margin is positive only if the
infinite product remains nonzero, equivalently

\[
\sum_j-\log(1-\rho_j)<\infty.
\]

For small defects, this is the same gate as summability of the `rho_j`.

## Exact completion hostile

Choose

\[
\rho_j=\frac{1}{j+1}.
\]

Every local comparison is strict, yet

\[
\prod_{j=1}^{N}\left(1-\frac{1}{j+1}\right)
=\prod_{j=1}^{N}\frac{j}{j+1}
=\frac{1}{N+1}\longrightarrow0.
\]

Thus finite source-local angular separation can disappear entirely at
completion.

## Categorical interpretation

The observer comparisons are lax coherence cells. Their defects compose
multiplicatively, rather than disappearing under ordinary diagram
commutativity. A restricted product therefore needs a resource law for
coherence loss. Pairwise admissibility is not enough.

The appropriate completed constructor must carry at least:

- the local observer comparison;
- its relative defect `rho_j`;
- the accumulated logarithmic defect;
- proof that the accumulated defect stays finite;
- compatibility with the endpoint and seam completion.

## DPC

Pass only if one of the following is source-derived:

1. a uniform global comparison with one `rho < 1` after full completion;
2. local comparisons whose logarithmic defects are summable;
3. exact cancellations or conservation laws that reduce the accumulated
   defect below the naive product bound.

Reject:

- checking `rho_j < 1` separately at every finite cutoff;
- taking a limit of positive finite margins without a lower bound;
- renormalizing the vanishing product after scalar projection;
- using the completed Evans function to define the comparison constants.

## Consequence

The RH frontier is not merely a local strict-gap problem. It is a
restricted-product coherence-budget problem. The primitive, square, seam, and
archimedean channels must either have summable observer defect or participate
in an exact source conservation law.

