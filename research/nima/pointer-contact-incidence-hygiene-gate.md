# Pointer-contact incidence and the hygiene-layer gate

## Concrete application

Kitaev's shared predicate \(111\) contacts the C, F, and G Wilson pointers
twice:

\[
\text{controlled }U,\qquad \text{controlled }U^2.
\]

Whether this is one-fault safe depends on the pointer-block incidence map,
not only on the ideal logical operation.

## Incidence model

Let columns denote physical contact episodes and rows denote independently
correctable pointer blocks. Define

\[
M_{bc}=1
\]

when contact \(c\) touches block \(b\).

For one monolithic ququart pointer,

\[
M_{\rm mono}=\begin{pmatrix}1&1\end{pmatrix}.
\]

Its row load is two. A persistent predicate fault can act twice on the same
correction block before recovery.

For two independently protected binary components,

\[
M_{\rm split}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Every row load is one. The two contacts are separated by correction-block
typing even if they originate from the same logical predicate.

For C/F/G, the global matrices are direct sums of three copies. The
monolithic model has three overloaded rows; the split model has none.

## Hygiene-layer theorem

Given a fault budget permitting at most one contact per correction block
between recovery boundaries, partition contacts into the fewest layers such
that every row has layer load at most one.

Construct the conflict graph:

- vertices are contacts;
- two contacts are adjacent when they touch a common correction block.

The minimum number of hygiene layers is the chromatic number of this graph.

For each monolithic pointer, its \(U\) and \(U^2\) contacts form an edge.
All three edges are disjoint, so two layers suffice and one layer is
impossible. A recovery, discard/recompute, or independently authorized
fault-clearing constructor is required between the layers.

For the split model the conflict graph has no edges, so one layer suffices
for this particular contact-multiplicity audit.

## Typed boundary

The split result is conditional on:

1. the two binary components being independently correctable blocks;
2. the two contacts actually targeting different components;
3. their recovery and governance roots satisfying the declared fault model;
4. compute/uncompute propagation not coupling them through sector data;
5. microscopic gadgets not introducing additional repeated contacts.

Logical factorization into two bits does not by itself establish physical
block independence.

## Compiler witness

For every row \(b\), compute

\[
\ell_b=\sum_cM_{bc}.
\]

If \(\ell_b>1\), return the exact contact subset and either:

- require a hygiene-layer coloring;
- require an authorized recovery boundary;
- or reject the claimed one-fault interpretation.

The smallest witness is

\[
\texttt{repeated\_fault\_source\_contact},
\quad
\texttt{block}=C,
\quad
\texttt{contacts}=(C_U,C_{U^2}).
\]

## Cross-sector relation

This is the physical-support analogue of joint selector correlation:

- selector rank asks which joint choices are reachable;
- contact incidence asks which choices or operations share a correction
  block and fault source;
- authority compilation requires both matrices.

A family may have full selector rank but unsafe contact load, or safe
contact load but deficient selector rank.

## Decision

The frozen logical text does not distinguish \(M_{\rm mono}\) from
\(M_{\rm split}\). Therefore the 193T ideal theorem has no unique
fault-safe interpretation until the pointer encoding supplies its physical
block incidence matrix.

