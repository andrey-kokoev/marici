# The derived sector pullback is the shifted interface

## Setup

Let `C_+` and `C_-` be the completed complexes of the two reciprocal
sectors, and let

\[
f_+:C_+\longrightarrow B,
\qquad
f_-:C_-\longrightarrow B
\]

be their source-derived boundary maps into the common seam/interface
complex `B`. The homotopy pullback is represented by

\[
P=\operatorname{Cone}(f_+-f_-) [-1].
\]

It lies in the distinguished triangle

\[
P\longrightarrow C_+\oplus C_-
\xrightarrow{,f_+-f_-,}B
\longrightarrow P[1].
\]

## Theorem

If both sector complexes are contractible, then

\[
P\simeq B[-1].
\]

Consequently,

\[
H^j(P)\cong H^{j-1}(B).
\]

The proof is formal: the middle term in the distinguished triangle is
acyclic, so the connecting morphism `B -> P[1]` is a quasi-isomorphism.

This replaces a vague compatibility obstruction by an exact location. The
derived sewing of two individually trivial sectors contains precisely a
degree-shifted copy of whatever survives on their interface.

## Meaning for the RH programme

Invertible reciprocal sewing cannot create a class. A derived pullback can,
but when both sectors are contractible the resulting class is not new bulk
information. It is seam information, shifted into the global complex.

Thus an off-critical zero-state in this architecture would require a
nontrivial interface class. The research question becomes:

> What is the source-derived interface complex `B_s`, and can its cohomology
> survive when `Re(s) != 1/2`?

This is closer to the operator intuition: the half-planes are two ordinary
realizations, while the zero record is a failure of their common boundary
meaning. The failure is represented by the interface, not by either sector
alone.

## Important distinction

The ordinary pullback

\[
C_+\times_B C_-
\]

computes the derived pullback only under an appropriate fibrancy or
surjectivity condition on the boundary map. Without it, an ordinary
intersection can erase the very interface class being sought. The cone model
is therefore the canonical first construction.

## Smallest falsifiers

The proposed route fails in any of the following cases:

1. `C_+` or `C_-` has off-seam cohomology before sewing;
2. the maps to `B` are fitted from the scalar zero set rather than derived
   from theta/Tate boundary operations;
3. the chosen ordinary pullback is not a model of the homotopy pullback;
4. `B_s` has classes throughout the open sectors, so interface localization
   does not distinguish the critical seam;
5. the scalar determinant does not detect the shifted interface class.

## Next calculation

Build `B_s` from the retained primitive, prime-square, archimedean, and mixed
seam currents. Then compute its differential before scalar aggregation. The
RH-bearing target is no longer bulk positivity. It is the source-local
statement

For `Re(s) != 1/2`, the target is

\[
H^\bullet(B_s)=0,
\]

together with a noncircular determinant map from `H(B_s)[-1]` to the scalar
zero-state.

## Scope

This theorem identifies the categorical location and degree of any class
created by two-sector derived sewing. It does not construct `B_s`, prove its
off-seam acyclicity, establish the determinant bridge, or prove RH.
