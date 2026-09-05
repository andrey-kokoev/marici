# Generic polygon face-product theorem

## Question

For every convex polygon and every noncrossing dissection, does refinement above that dissection factor canonically into independent dissections of its regions?

## Definitions

Let `P_n` be a convex polygon with cyclically ordered vertices, where `n >= 3`.
A diagonal is an unordered pair of nonadjacent vertices. A dissection `D` is a
set of diagonals whose interiors are pairwise disjoint. Refinement is inclusion.
Write

\[
\operatorname{Face}(D)=\{E\mid D\subseteq E,\ E\text{ is a dissection}\}.
\]

Cutting `P_n` along `D` gives a set `Regions(D)` of convex subpolygons. For a
region `R`, let `Fact(R)` be its set of noncrossing internal-diagonal sets.
Boundary edges of `R`, including edges inherited from `D`, are excluded from
`Fact(R)`.

## Unique-region lemma

If `E` refines `D` and `e` lies in `E - D`, then exactly one region of `D`
contains `e` as an internal diagonal.

Existence follows because the interiors of diagonals in `E` avoid every cut in
`D`. The connected interior of `e` therefore lies in one component of the
polygon interior minus `D`; its closure is a region containing both endpoints.
Since `e` is not in `D`, it is not an edge introduced by the cut, and hence is
internal in that region.

For uniqueness, interiors of distinct regions are disjoint. An internal
diagonal has a nonempty connected interior, so it cannot be internal to two
regions. Merely sharing its endpoints does not violate uniqueness because an
edge on a region boundary is not an internal diagonal of that region.

## The maps

Define restriction by the unique-region lemma:

\[
\rho_D(E)_R=(E-D)\cap\operatorname{Diag}(R).
\]

Each component is noncrossing because it is a subset of `E`.

Define union by

\[
\mu_D((A_R)_R)=D\cup\bigcup_R A_R.
\]

This is a dissection. Diagonals within one `A_R` are noncrossing by definition.
Diagonals belonging to distinct regions have interiors in disjoint region
interiors. Every member of `A_R` also avoids `D` because its interior lies in
the interior of `R`. Thus the union is pairwise noncrossing and refines `D`.

## Theorem

For every `n >= 3` and every dissection `D` of `P_n`, restriction and union are
inverse equivalences:

\[
\operatorname{Face}(D)\simeq
\prod_{R\in\operatorname{Regions}(D)}\operatorname{Fact}(R).
\]

For `E` in `Face(D)`, every diagonal of `E-D` has exactly one regional
component, so

\[
\mu_D(\rho_D(E))=D\cup(E-D)=E.
\]

For a tuple `(A_R)_R`, no member of `A_R` belongs internally to another region.
Restriction of its union therefore returns each component unchanged:

\[
\rho_D(\mu_D((A_R)_R))=(A_R)_R.
\]

Both equalities preserve refinement inclusion componentwise. Consequently this
is also an order isomorphism.

## Nested-cut naturality

If `D` is contained in `E`, each region of `E` lies in a unique region of `D`.
Restricting a further refinement first along `D` and then along the induced
cuts inside its regions assigns every new diagonal to the same final region as
direct restriction along `E`. This follows from uniqueness in the lemma, not
from a choice of cut order. Union is associative because all maps forget only
the regional partition and take set union. Hence the face-product equivalences
commute for nested cuts.

## Executable falsification

`research/nima/checkers/check_generic_polygon_face_product.py` independently
constructs the maps and exhaustively compares their images for every dissection
of each polygon with `3 <= n <= 7`. The result is
`research/nima/results/generic_polygon_face_product.json`. It checks 1,849 face
elements and the same number of factor tuples, plus 2,878 unique-region
assignments.

These finite checks can falsify the stated algorithm but are not used to infer
the unbounded quantifier. The theorem above depends instead on convexity,
noncrossing, and the connected-component argument.

## Claim boundary and disposition

This proves the generic set-level and refinement-order face-product theorem and
nested-cut naturality. It does not internalize polygons in Rzk and does not
supply the missing interpretation from the external simplicial nerve to an Rzk
Segal type. The mathematical generic-region gate is closed; the foundation
transport gate remains open.
