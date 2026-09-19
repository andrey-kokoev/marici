# The amplituhedron boundary carrier is a projective correspondence semigroup, so it cannot directly supply global SU(1,1) holonomy

## Bounded real-form test

The proposed real-form filler requires every boundary transport to define an
invertible projective `2 by 2` map, so that loop holonomy and membership in
`PSU(1,1)` are defined.

The existing exact seven-point NNMHV transport census was rerun. The adjacent
dual edge

\[
x_{(7,6)}
\]

has

\[
\det x_{(7,6)}=0,
\qquad
\operatorname{rank}x_{(7,6)}=1.
\]

Four of the six histories, with indices `2,3,4,5`, use this singular prefix.
The full census contains both rank-two automorphisms and rank-one collapse
correspondences.

## Consequence

The source-authorized carrier is

\[
\mathbb P(\operatorname{Mat}_2),
\]

stratified by rank. It is a projective semigroup/category of correspondences,
not a global `PGL(2,C)` connection. On rank-one cells:

- determinant normalization is undefined;
- inversion is unavailable;
- loop holonomy is unavailable;
- `PSU(1,1)` membership is unavailable.

Therefore amplituhedron boundary sewing cannot directly prove that the prime
spectral transport lies in `PSU(1,1)`.

## Surviving restricted statement

On the open rank-two stratum, determinant-normalized transport and a
source-fixed Cayley real-form test remain well typed. But restricting to that
stratum removes physical boundary cells used by the canonical-form residue
construction. A proof on the open stratum does not automatically extend across
the rank-one divisor.

The correct extension target would be a `J`-compatible projective
correspondence law that remains meaningful at rank one, for example a relation
between image and kernel lines rather than a unitary group equation.

## Fresh verification

Both exact checkers pass:

- `check_nnmhv_boundary_transport_frame_obstruction.py`;
- `check_nnmhv_projective_transport_correspondences.py`.

They certify the singular edge, the four affected histories, and coexistence
of rank-one and rank-two strata.

## Disposition

The direct global `SU(1,1)`-holonomy route is rejected. The metric-defect
identity for prime transport remains valid, but a positive-geometric filler
must be formulated in the compactified correspondence carrier, including its
rank-one image/kernel boundary data.