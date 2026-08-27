# Semantic pullback needs a source-authority gate

## Result

The four semantic gates constrain the behavior of a compiler, but they do not
authorize the compiler itself. For an authority- or frame-bearing claim there
is a fifth, logically independent question:

> Which source operation selects this identification rather than another
> extensionally valid one?

The fifth residual is `missing_source_authority`. Its repair is a
source-authorized constructor, normalization, or comparison cell. Transported
evidence and good extensional behavior cannot supply that authority.

## Exact hostile

Let the source and target both be \(\mathbb R^2\). Compare

\[
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Both maps are:

- injective;
- surjective;
- orthogonal, hence uniformly stable;
- compatible with the identity constructor and its relations.

Thus both pass the first four gates. Now let the source declare the first basis
vector as its normalized authority root. The identity preserves that root,
whereas the swap transports it to the second basis vector. The four semantic
tests cannot choose between them; the source normalization can.

## Five-gate compiler

For claims that carry source identity or operative authority, the backward
compiler must check:

1. source-state separation;
2. target-image admission;
3. preservation of composition and relations;
4. distinction-preserving completion;
5. source authority for the chosen constructor and frame.

The fifth gate is not a universal extra mathematical axiom. If the target claim
is explicitly invariant under the swap, then the two maps are equivalent and
no frame selection is required. The gate activates when the claimed result
distinguishes the source root, orientation, protocol identity, calibration, or
authority lineage.

## Falsifier

Any compiler that accepts the swap solely because it is an orthogonal
isomorphism has transported behavior into authority. The checker requires an
explicit source-root preservation witness for an authority-bearing target.

