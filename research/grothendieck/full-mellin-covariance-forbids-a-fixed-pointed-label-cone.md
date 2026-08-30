# Full Mellin covariance forbids a fixed pointed label cone

## Question

Can the missing RH-bearing wall be a fixed source-derived pointed cone on the
theta-labelled coefficient module, preserved by vertical Mellin transport?

## No-go theorem

Let a real convex cone `C` live in the realification of a complex labelled
module. Suppose:

1. `C` contains a nonzero pure label vector `e_q` with `q` nonzero;
2. every vertical Mellin action preserves `C`;
3. that action on the label is

   \[
   M_t e_q=e^{itq}e_q.
   \]

Choose

\[
t=\frac{\pi}{q}.
\]

Then

\[
M_t e_q=-e_q.
\]

Hence both `e_q` and `-e_q` belong to `C`. Therefore

\[
C\cap(-C)\ne\{0\},
\]

so `C` is not pointed.

The same proof applies to the arithmetic label `q=log n`: vertical spectral
translation multiplies its coefficient by `n^(it)`, and a suitable height
reverses its real direction exactly.

## Consequence

There is no nontrivial fixed pointed cone that simultaneously:

- contains independently prepared theta or arithmetic labels;
- is preserved by the full vertical spectral action;
- supplies one global order for all heights.

This is not a numerical failure and does not depend on zeros. It follows from
the constructor representation itself.

## What survives

An order-based route must weaken at least one premise. The live possibilities
are:

1. a cone field `C_t` transported with spectral height rather than one fixed
   cone;
2. a relational cone on direct--dual pairs where the common phase is quotiented
   and only relative phase is ordered;
3. an ordered module containing completed source packets but not individual
   pure labels;
4. a semigroup of restricted transports rather than the full Mellin group;
5. a nonlinear source orbit whose transversality is not inherited from a
   global cone.

The first two are the most native to the multi-tower picture. They say order
is not an attribute of one coefficient fiber. It is a comparison structure
transported between input, output, and control towers.

## Relation to previous hostile results

The positive two-cell source showed that source positivity alone permits an
off-seam zero. The local theta Krein calculation showed that actual theta
packets enter a negative two-point corridor. The present result explains why
attempts to repair those facts with one Mellin-invariant positive cone must
fail: vertical transport itself rotates every isolated label through the
opposite ray.

## Falsifier for replacements

For any proposed ordered structure, state explicitly whether it contains pure
labels and how `M_t` acts. If the same pointed cone contains a pure label and
is invariant under every `M_t`, the construction is inconsistent before any
RH argument begins.

## Disposition

The fixed-cone branch is closed. The next viable cone attack is a transported
cone field or a phase-quotiented relational cone, followed by a test of whether
the scalar zero section can enter its polar boundary off the seam.

