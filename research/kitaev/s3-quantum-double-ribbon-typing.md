# The first non-Abelian ribbon typing test: `D(S3)`

Status: exact finite group/anyon-label audit; ribbon-operator and fusion
category construction remains bounded by the stated source requirements.

## Frozen source enlargement

Replace the `Z2` edge qubit by the group algebra `C[S3]` on each oriented
edge.  Vertex terms implement local gauge transformations and plaquette terms
project to trivial ordered holonomy.  Excitations of the quantum double are
labelled by

\[
(C,\rho),
\]

where `C` is a conjugacy class and `rho` an irreducible representation of the
centralizer of a representative.

The exact census finds conjugacy-class sizes `1,3,2`, centralizer orders
`6,2,3`, and eight anyon dimensions

\[
1,1,2,3,3,2,2,2,
\qquad \sum_a d_a^2=36=|S_3|^2.
\]

Dimensions larger than one already rule out an Abelian scalar-port model.

## Braiding is not an intersection sign

For fluxes `g=(01)` and `h=(12)`, the elementary conjugation action gives

\[
h\longmapsto ghg^{-1}=(02).
\]

On the three-transposition flux basis this braid fixes `(01)` and swaps
`(12)` with `(02)`.  It is a nontrivial matrix/permutation, not multiplication
by `+/-1`.  Mod-two intersection still types where ribbons cross, but it no
longer determines the coefficient action.

## Carrier versus quantum coefficient enlargement

Carrier geometry must retain more than an unframed cycle: an oriented ribbon
(a locally clockwise/counterclockwise sequence of primal/dual triangles),
ordered endpoints, and a base/framing convention for comparing flux labels.
This refines the existing endpoint-framed transport object rather than
introducing a selected physical branch.

The quantum coefficient lens must enlarge from the Pauli symplectic module to
the Drinfeld-double representation data: conjugacy classes, centralizer
representations, internal excitation spaces, fusion, and braid matrices.
The non-Abelian datum is therefore not hidden in Carrier incidence.

## Exact boundary and blocker

The checker establishes the source group census, quantum-dimension sum rule,
and one non-scalar flux braid.  It does not construct the full ribbon operator
algebra, fusion coefficients, associators, or pentagon/hexagon coherence.

That omission is theorem-changing for any categorical promotion.  Recent
ribbon-operator work emphasizes that locally clockwise and counterclockwise
ribbons must be distinguished even for finite non-Abelian groups; dropping
that orientation can break endpoint-localization properties.  A next theorem
must therefore freeze the ribbon triangulation and operator multiplication
before claiming a braided fusion category.

Primary sources: Kitaev's quantum-double construction (arXiv
`quant-ph/9707021`), the rigorous ribbon-orientation treatment
arXiv `2105.08202`, and the `D(S3)` surface-code account arXiv `2107.04411`.

## Falsifiers

The finite result fails if the class/centralizer census changes, if
`sum d_a^2 != 36`, or if conjugation leaves `(12)` fixed.  The stronger
categorical claim remains deliberately unmade until fusion and coherence are
derived from frozen ribbon operators.

