# Smith theorem for polygon triangulation incidence

## Question

Do the finite Smith invariants `1,...,1,n-3` hold for every polygon size, and what generates the lattice?

## Claim boundary

The theorem concerns the integer incidence lattice of polygon triangulations and diagonals. It does not provide source coefficients, facet equations, or embedding provenance.

Let `F` be the number of polygon diagonals and let each triangulation define its incidence vector in `Z^F`. Every row has coordinate sum `n-3`, so the generated lattice lies in

\[
L=\{v\in\mathbb Z^F:\sum_c v_c\equiv0\pmod{n-3}\}.
\]

If two triangulations differ by one flip, their incidence-vector difference is `e_c-e_c'`, where the exchanged diagonals cross. Conversely, every crossing pair spans a quadrilateral; triangulating the four surrounding polygonal regions completes each diagonal to triangulations that differ by that flip. Thus every edge of the crossing graph supplies such a difference.

The crossing graph on polygon diagonals is connected. Every diagonal `(i,j)` crosses the short diagonal `(i-1,i+1)` at endpoint `i`, and consecutive short diagonals `(i-1,i+1)` and `(i,i+2)` cross. Hence flip differences generate every zero-sum vector `e_c-e_c'`.

One triangulation row has sum `n-3`. Together with the full zero-sum lattice it generates all of `L`. Therefore the incidence lattice has index `n-3` in `Z^F`, and its Smith invariants are

\[
1,\ldots,1,n-3.
\]

Consequently the monomial map from complex facet scales has kernel exactly the diagonal group of `(n-3)`rd roots of unity: connectivity removes every non-diagonal kernel element, while a common root fixes each product of `n-3` scales.

The checker independently verifies crossing connectivity and Smith forms for `n=4..8`. These computations test the implementation; the unbounded result follows from the lattice proof rather than finite extrapolation.

## Disposition

The prior finite root-branch pattern is promoted to a generic combinatorial theorem. Complex scale reconstruction is unique modulo one common `(n-3)`rd root of unity. Source authority for the coefficients and embedding remains separate.
