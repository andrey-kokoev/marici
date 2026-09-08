# Triangle-incidence rank theorem

## Question

Can the dimension of the triangle-additive function space be proved for every polygon size?

## Claim boundary

This proves the triangle-incidence rank. It does not yet prove that every function satisfying all local facet minors is triangle-additive.

Orient every vertex triple increasingly and regard triangle weights as a simplicial two-cochain on the full vertex simplex. If a triangle cochain evaluates to zero on every polygon triangulation, comparing triangulations related by a flip on vertices `i<j<k<l` gives

\[
h_{ijk}+h_{ikl}-h_{ijl}-h_{jkl}=0.
\]

Every four-vertex flip can be embedded by triangulating the surrounding regions. Hence the two-cochain is closed. Exactness of the simplex cochain complex gives `h=delta u` for an edge cochain `u`.

Discrete Stokes says that the sum of `delta u` over any consistently oriented polygon triangulation equals the integral of `u` around the polygon boundary. Therefore `h` lies in the triangle-incidence kernel exactly when `u` has zero boundary integral.

There are `binomial(n,2)` edge variables. Vertex coboundaries form an `(n-1)`-dimensional kernel of `delta`, and the boundary-integral condition removes one further dimension from the image. The triangle-incidence kernel consequently has dimension

\[
\binom n2-(n-1)-1=\frac{n(n-3)}2.
\]

Subtracting from `binomial(n,3)` gives rank

\[
1+\binom{n-1}{3}.
\]

Exact matrices through `n=8` verify the incidence rank, the boundary-zero coboundary rank, and discrete Stokes annihilation.

## Disposition

The rank half of the local-relation conjecture is proved. The remaining edge is the converse spanning theorem: local facet-minor vanishing must imply that a triangulation function is a sum of triangle weights.
