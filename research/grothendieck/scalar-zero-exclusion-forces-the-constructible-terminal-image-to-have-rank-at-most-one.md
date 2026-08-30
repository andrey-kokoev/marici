# Scalar zero exclusion forces the constructible terminal image to have rank at most one

## The actual pullback

Let `P_s` be the source packet at a fixed spectral parameter, let

\[
T_s:P_s\longrightarrow W_s
\]

be the source-derived terminal-state constructor, and let

\[
q_s:W_s\longrightarrow \mathbb C
\]

be the scalar Evans readout. The admissible scalar-null object is not the
kernel of an observer added afterward. It is the pullback

\[
Z_s=P_s\times_{W_s}\ker q_s=\ker(q_sT_s).
\]

Thus zero exclusion is exactly the assertion that `q_s T_s` has no nonzero
admissible input.

## Rank obstruction

Write `S_s=im T_s`. If `S_s` is a complex linear subspace and
`S_s intersect ker q_s` is zero, then the restriction

\[
q_s|_{S_s}:S_s\longrightarrow\mathbb C
\]

is injective. Consequently

\[
\dim_{\mathbb C} S_s\leq 1.
\]

Equivalently, every complex linear constructibility image of dimension at
least two contains a nonzero scalar-null state. This is only rank-nullity, but
it rules out a large class of proposed lifts at once.

Adding a faithful terminal observer

\[
C_s:W_s\longrightarrow Y_s
\]

does not change the pullback. Even `C_s` equal to the identity merely
distinguishes the different elements already lying in `S_s intersect ker
q_s`; it does not remove them.

## Smallest exact hostile

Take

\[
W=\mathbb C^2,\qquad S=W,\qquad q(x,y)=x+y,
\]

and let the complete observer be `C=I`. The state `(1,-1)` is constructible,
nonzero, perfectly observed, and scalar-null. The observer has condition
number one, so no improvement of observational conditioning repairs the
failure.

The obstruction persists for every source map whose image contains two
linearly independent terminal states. The checker constructs an explicit
kernel vector from two such states and verifies that a faithful observer still
detects it.

## Consequence for the theta/Tate programme

The terminal object must not be typed as a freely variable multi-dimensional
linear state space if its single scalar readout is expected to exclude zeros.
At a fixed `s`, one of the following additional structures is mandatory:

- the source constructor selects a single distinguished ray;
- admissible states form a nonlinear pointed locus avoiding `ker q_s`;
- boundary conditions cut the linear solution space to rank one before the
  Evans evaluation;
- a second independent equation is part of constructibility rather than an
  observer applied afterward.

This distinguishes two operations that had been conflated:

1. observation asks which terminal state was supplied;
2. constructibility asks which terminal states can exist at all.

Only the second can exclude a scalar-null state.

## Next finite target

For the doubled theta-tail system, compute the source-defined solution module
after imposing the infinity condition but before imposing the Evans condition.
Call its terminal image `S_s`. The decisive finite audit is its complex rank:

\[
\operatorname{rank}_{\mathbb C} S_s.
\]

- Rank zero means no state exists.
- Rank one makes a nonvanishing Evans coefficient a meaningful exclusion
  problem.
- Rank at least two proves that a single scalar terminal readout cannot be
  zero-free on the whole linear module.

Primitive, square, seam, and archimedean channels matter only if they enter the
source equations or boundary domain and reduce this rank. Their joint
faithfulness as readout ports is insufficient.

## Disposition

The first lift is not an observability problem. It is a source-domain rank
problem. The next attack should derive the pre-Evans solution module and test
whether the complete boundary conditions reduce it to one distinguished ray
in each open half-plane.
