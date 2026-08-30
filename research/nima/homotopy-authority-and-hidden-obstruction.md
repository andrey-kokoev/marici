# Homotopy authority and the scalar-invisible obstruction

## Exact equivalence gate

For chain maps (F,G:C^\bullet\to \bar C^\bullet), equality of projected
outputs does not make the reductions equivalent.  A relaxation of strict
equality is valid only when a typed degree (-1) comparison (S) is
provided with

\[
\boxed{F-G=\bar D S+S D.}
\]

Thus (E=F-G) must be a boundary in the Hom complex

\[
\operatorname{Hom}^\bullet(C,\bar C),\qquad
\partial S=\bar D S+S D.
\]

Because (F) and (G) are chain maps, (E) is automatically a
degree-zero cycle.  Its class

\[
[E]\in H^0\operatorname{Hom}(C,\bar C)
\]

is the exact obstruction to a chain homotopy.

## Smallest scalar-invisible falsifier

Take a complex concentrated in degree zero:

\[
C^0=\bar C^0=\mathbf F_2^2,\qquad D=\bar D=0.
\]

Let

\[
F=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
G=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]

and let the scalar observation retain only the first coordinate:

\[
P=\begin{pmatrix}1&0\end{pmatrix}.
\]

Then (PF=PG), so every permitted scalar observation agrees.  But there
is no degree (-1) group and hence no possible (S).  Therefore

\[
[F-G]=
\left[
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\right]\ne0.
\]

This is a two-state finite falsifier for any compiler rule that promotes
scalar equality to coherent equivalence.

## Authority consequence

Even when the equation has a solution, existence is not authority.
The comparison (S) must carry:

- its exact source and target complexes;
- degree and modality;
- a source-authorized constructor;
- support and fault assumptions;
- compatibility cells for every later composition.

Transporting an algebraic solution from another evidence domain does not
authorize the equivalence.

## Composition

If (F\simeq G) through (S) and (F'\simeq G') through (S'), the
composite comparison is constructed from whiskered terms such as
(F'S+S'G).  Alternative whiskerings need not be identical.  Their
comparison is another higher-coherence obligation, so a compiler must
retain the homotopy constructor tree rather than flatten it to an
“equivalent” flag.

## Compiler rejection

```json
{
  "code": "projected_equality_without_chain_homotopy",
  "projected_maps_equal": true,
  "hom_obstruction_degree": 0,
  "obstruction_rank": 1
}
```

## Cross-sector reading

- Benincasa: a source-wall reducer may preserve the total cocycle strictly
  or through an authorized homotopy; scalar direct-image equality is not
  enough.
- Strominger: two constructor trees with matching output bytes require a
  typed invertible comparison cell and its coherence data.
- Kitaev: equal logical action can hide a physical-sector discrepancy.
- Completed arithmetic: equality after scalar trace cannot certify an
  operator-level orientation law.

