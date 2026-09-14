# The relative `C_34` filler has `8(n+1)` feature slots at depth `n`, but no edgewise-simplex cell count

## Macro rows

The ordered relative positive feature has three binary coordinates:

1. observer placement:
   \[
   A_g
   \quad\text{or}\quad
   P A_g;
   \]
2. regulator polarity:
   \[
   \text{Tate}
   \quad\text{or}\quad
   \text{reference};
   \]
3. projection row:
   \[
   Q
   \quad\text{or}\quad
   I-Q.
   \]

Therefore the finite macro-presentation has

\[
\boxed{
2\times2\times2
=8
}
\]

positive rows.

These are the eight legs of the cross-polarized dilation.

## Finite dyadic truncation of one row

A row with Gram contraction `B` has the finite identity

\[
\boxed{
B
=B^{2^n}
+
\sum_{j=0}^{n-1}
B^{2^j}
(I-B^{2^j}).
}
\]

Thus at depth `n` it has:

- one unresolved soft-bulk slot `B^(2^n)`;
- `n` resolved positive defect slots.

The number of formal slots per row is

\[
\boxed{
n+1.
}
\]

For a projection-complement row, apply the same formula to `I-B`.

## Total formal feature slots

Refining all eight macro rows to the same depth gives

\[
\boxed{
N_{slots}(n)
=8(n+1).
}
\]

At depth zero, this is the original eight-leg feature. Every successor depth adds one defect coordinate to each row:

\[
N_{slots}(n+1)
-N_{slots}(n)
=8.
\]

## Zero reference defects

For the pure translated Hardy reference pair, the projection pair is nested. Its generic contraction is a projection, so all defect slots vanish:

\[
B_0^{2^j}
(I-B_0^{2^j})
=0.
\]

The formula `8(n+1)` counts formal typed slots before deleting zero summands. It is stable under deformation from reference to Tate and therefore preferable for coherence bookkeeping.

An economical reference-specific presentation has fewer nonzero slots, but its dimension jumps when Tate scattering creates generic angles.

## Terminal atoms

At infinite depth,

\[
B^{2^n}
\xrightarrow[s]{n\to\infty}
P_{\{1\}}(B).
\]

Thus the terminal soft-bulk slot becomes an exact endpoint atom. For the complementary contraction, it becomes

\[
P_{\{1\}}(I-B)
=P_{\{0\}}(B).
\]

The infinite row therefore consists of:

- one exact atom;
- countably many dyadic defect slots.

The complete eight-row carrier has countably many slots:

\[
\boxed{
8(1+\aleph_0)
=\aleph_0.
}
\]

## Conductor coordinate

At conductor cutoff `F`, only admitted angular sectors are retained. If their number is `M_S(F)`, the formal scalar-fiber slot count is

\[
\boxed{
8(n+1)
M_S(F).
}
\]

Each scalar slot still carries an infinite-dimensional radial Hilbert space. This is a decomposition count, not a finite vector-space dimension.

## Outer regulator coordinate

A finite outer regulator may make each row finite rank or trace class in a concrete discretization. Its rank depends on the exact regulator and is not determined by `n` or `F` alone.

Therefore no regulator-independent finite dimension follows from the feature-slot count.

## Slots are not edge nodes

The `8(n+1)` coordinates are parallel orthogonal feature summands. They do not form a linearly ordered sequence of realization nodes on one simplicial edge.

In particular, it is invalid to set

\[
N_{edge}
=8(n+1)
\]

and infer a tetrahedron count by

\[
N_{edge}^3.
\]

Edgewise subdivision counts require sequential composable edge stages. Direct-sum feature coordinates are a different sort of datum.

## Macro cell versus microscopic slots

The correct interpretation is:

- one macro `C_34` relative correspondence;
- eight positive rows in one chosen presentation;
- a countable internal orthogonal refinement of those rows;
- strict isometric transition maps between depths.

The dyadic slots refine the **interior feature carrier** of the macro edge. They do not add barycentric vertices to the ambient tetrahedron automatically.

## Why the earlier `729` denominator remains invalid

A prior ten-node proposal suggested a ninth edge subdivision and hence

\[
9^3=729
\]

elementary tetrahedra. The current construction does not validate those ten sequential nodes.

It supplies a relative correspondence with parallel rows and filtered depth. Therefore:

\[
\boxed{
729
\text{ is not a denominator for the completed positive filler}.
}
\]

Nor should it be replaced by

\[
[8(n+1)]^3.
\]

Both counts confuse feature multiplicity with edge subdivision length.

## Finite computational truncation

For numerical or symbolic work, a finite approximation may be specified by

\[
\boxed{
(L,R,N,F,n).
}
\]

Its feature presentation contains:

- up to `8(n+1)` row/depth slots;
- finitely many angular sectors after `N,F` restriction;
- whatever finite rank is induced by `R`.

This tuple completely specifies a computational truncation without pretending it is a final simplicial subdivision.

## Coherence count

Depth coherence is not certified by checking every pair of slots. It follows from the exact isometry identities

\[
J_n^*J_n=I
\]

and strict composition

\[
J_{m,k}J_{n,m}
=J_{n,k}.
\]

Sign preservation follows from

\[
J_n^*\mathcal J_{n+1}J_n
=\mathcal J_n.
\]

Thus infinitely many depth cells are proved uniformly by one functional-calculus theorem.

## Suggested simplicial encoding

If a simplicial model is required, retain:

1. the original finite macro edge as one correspondence arrow;
2. a simplicial/pro object internal to that arrow indexed by `n`;
3. conductor and regulator indices as additional filtered directions;
4. naturality squares rather than barycentric subdivision vertices.

This is a multi-simplicial or enriched-edge construction, not ordinary edgewise subdivision by a single integer.

## Exact cardinal statements

The honest size statements are:

\[
\boxed{
\text{macro positive presentation width}=8,
}
\]

\[
\boxed{
\text{depth-}n
\text{ formal slot count}=8(n+1),
}
\]

\[
\boxed{
\text{complete microscopic slot cardinal}=\aleph_0,
}
\]

and

\[
\boxed{
\text{ambient simplicial cell count: not defined by these data}.
}
\]

## Disposition

The completed positive refinement has finite macro-width and countable internal depth. It is rigorously countable as a feature decomposition but has no source-derived finite edgewise subdivision count. Any future cell count must first define a realization functor converting parallel relative-feature slots into sequential simplicial stages; no such conversion is presently required or canonical.
