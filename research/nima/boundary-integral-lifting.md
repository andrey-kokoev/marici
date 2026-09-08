# Integral boundary lifting

## Question

Does every seven-point field-valued solution of the local quadrics admit triangle factors, including on boundary supports?

## Claim boundary

Yes, over every field, conditional on the prior exact local/toric ideal identification. This is pointwise existence, not a canonical inverse, uniqueness, or a regular section of the parameterization. Physical source embedding is not asserted.

The conjecture is full boundary lifting. Rivals are a missing support, a finite-index face lattice requiring roots, and coefficient relations not captured by the local ideal. The preceding cone-face and ideal certificates exclude the first and third; the following integral argument excludes the second.

### Integral decomposition

Use the interval-balance proof in triangle-cone-flow.md. For an integral nonnegative balanced vector, each minimum selected triangle weight is a positive integer. Subtraction therefore yields a nonnegative integral combination of triangulations. If the original vector lies in a face F, all selected triangulations lie in F: outside-face coordinates vanish and never increase. Thus the face semigroup is exactly F intersected with the ambient integer lattice.

### Saturated face lattice

Let U be the union of triangle coordinates of the triangulations on F, and let L_F be their integer span in Z^U. Sum all these incidence vectors to obtain u. It is positive on every coordinate in U. For z in span_R(F) intersect Z^U, choose an integer N large enough that z+Nu is nonnegative. Both z+Nu and Nu are balanced and supported on F, hence integrally decomposable into its triangulations. Their difference is z. Consequently

\[
L_F=\operatorname{span}_{\mathbb R}(F)\cap\mathbb Z^U.
\]

This lattice is saturated and therefore a direct summand of Z^U. The zero face has the zero lattice and needs no shift.

### Coefficient character

Let w be a field-valued point of the triangle toric variety with nonzero support S. Its support is a cone face F. The assignment a_i -> w_i for i in S defines a character L_F -> k^*: any integer relation splits into two nonnegative exponent vectors, and its toric binomial enforces equality of the corresponding nonzero products. This proves well-definedness without division by any zero coefficient.

Extend this character to Z^U using a lattice complement, assigning one on a basis of the complement. The resulting triangle values on U are nonzero; put zero on all other triangle coordinates. Products recover w on S, and the coordinate-face property forces every excluded triangulation product to vanish. No roots or algebraic closure are used.

## Disposition

Full seven-point pointwise triangle factorization, including zeros, follows over every field. The all-face integral and character arguments are the proof; the checker supplies 35 boundary Smith tests, all with unit factors. Its deliberately nonsaturated rival 2Z in Z fails character extension over F_3: sending 2 to 2 would require a square root of 2, which does not exist there. This confirms why rational rank would have been insufficient.

The result leaves the nonuniqueness and regularity of choosing factors unresolved. A useful next executable question is whether any global regular section exists; even pointwise surjectivity does not provide one. All files in this increment remain uncommitted pending operator authorization.
