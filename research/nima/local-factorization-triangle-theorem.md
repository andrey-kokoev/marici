# Local factorization equals triangle additivity

## Question

Does every additive function on triangulations satisfying all facet-product separability relations arise by summing triangle weights?

## Claim boundary

The theorem is linear over a characteristic-zero coefficient field. Real signs, complex phases, and source provenance remain governed by separate gates.

Consider a flip in a quadrilateral with four surrounding polygonal regions. If one surrounding triangulation changes, a quadrilateral side separates that region from the rest. Facet separability writes the function as a sum of regional terms, so the difference across the flip cancels the changed region. The flip increment therefore depends only on the four quadrilateral vertices, not on the surrounding triangulations. Denote this context-free increment by `g`.

For any five vertices, fix triangulations outside their pentagon and traverse its five-flip cycle. Since increments of an actual function sum to zero around the cycle, `g` obeys the simplicial cocycle identity. Exactness of the full vertex simplex gives a triangle two-cochain `h` with

\[
g=\delta h.
\]

The triangle-additive function

\[
f_h(T)=\sum_{\Delta\in T}h_\Delta
\]

has the same increment on every flip. Their difference is constant because the triangulation flip graph is connected. That constant is triangle-additive by assigning `1/(n-2)` times it to every triangle. Thus every locally separable function is triangle-additive. The converse follows because triangles partition across every cut.

Combined with the triangle-incidence rank theorem, the local-solution dimension is

\[
1+\binom{n-1}{3},
\]

and the nonlocal quotient of global channel relations has dimension

\[
1+\binom{n-1}{3}-\frac{n(n-3)}2.
\]

Exact dimensions agree for `n=5..8`; the `n=9` modular rank is consistent but is not needed for the proof.

## Disposition

The local-rank conjecture is resolved in characteristic zero. Codimension-one residue factorization determines triangle-additive coefficient structure, while global channel factorability imposes the stated additional quotient. Neither theorem supplies source coefficient values or an embedding.
