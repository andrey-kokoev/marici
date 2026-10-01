# Dowker identification and a product recurrence

## Computation: restoring the primitive arrow

The original fixture removes primitive arrow(0,1) before forming arrow pairs:
11^2+16=137 slots. Restoring that arrow gives12^2+16=160 slots. Applying the
same local biclique boundary rule gives:

| Input | Nonzero rational Betti numbers |
|---|---|
| Missing-arrow137-slot relation | b0=17 |
| Restored-arrow160-slot relation | b0=17, b2=2, b4=1 |

The restored biclique chain dimensions are64,160,1152,2496,2192,864,132;
boundary ranks are47,113,1037,1459,732,132. Every boundary composite vanishes.
Sixteen isolated state components account for16 of the degree0 classes.

An independently constructed Dowker simplicial chain complex gives the same
homology for both inputs. Additional controls yield the expected homology of
a point (complete K(2,3)), a circle (six-cycle incidence), and a sphere (the
four-label off-diagonal relation).

## Mathematical identification

For a bipartite relation R subset S x T, its source Dowker complex D(R) contains
all nonempty subsets of S having a common target neighbor.

Consider the polyhedral relation complex B(R), the union of products
Delta(A) x Delta(B) over complete bipartite blocks A x B subset R, including
one-element sides. Its face poset projects to the Dowker face poset by
(A,B)->A. Over a lower ideal ending in face A0, choose a common neighbor t0.
The maps

    (A,B) <= (A,B union {t0}) >= (A,{t0}) <= (A0,{t0})

contract that inverse-image poset. The finite-poset fibre theorem therefore
identifies B(R) up to homotopy with D(R).

The subcomplex Z consisting of cells with at least one singleton side is a
union of source-star and target-star simplices. Same-side stars are disjoint;
a source/target pair intersects in one point exactly when its edge belongs
to R. Its good-cover nerve is the original bipartite incidence graph.

Relative chains C_*(B(R),Z) in degree>=2 are precisely the complete K(p,q)
cells with p,q>=2 used in the checker. Their differential omits singleton-side
faces. The connecting map sends each rectangle to its four-edge cycle in the
incidence graph. Replacing the star subcomplex by this graph yields the low-degree
boundary used in our complex. The long exact sequence of the pair identifies
its homology with that of B(R), hence the Dowker complex. This is the geometric
explanation of the independently checked rank agreement.

These arguments concern the finite relation and its chain model. They do not
identify operational record versions with topological points.

## Primitive geometry: sphere versus disk

For four labels with every off-diagonal arrow, each target neighborhood is the
other three labels. The Dowker complex is exactly the boundary of a tetrahedron,
so its realization is S^2.

Removing arrow(0,1) removes vertex0 from target1's neighborhood. The corresponding
triangular facet {0,2,3} disappears; all its edges remain in other facets. The
Dowker complex is the remaining three triangles, a closed disk D^2. Its
nonempty face count drops from14 to13.

This explains the input-specific exactness of the137-slot model.

## Arrow pairs produce a product

The arrow block is the product relation R x R. A set of pairs is a Dowker face
exactly when each of its coordinate projections is a face of D(R).
Rectangular completion

    A -> projection_1(A) x projection_2(A)

is an extensive, monotone, idempotent closure on this face poset. Its fixed
faces form the product of the two primitive face posets. Therefore

    |D(R x R)| is homotopy equivalent to |D(R)| x |D(R)|.

The checker verifies this closure for every face of both arrow-pair fixtures.
The fixed-face counts are13^2=169 and14^2=196.

The missing-arrow block consequently has the homotopy type of D^2 x D^2 and
is contractible. The restored block has type S^2 x S^2, explaining b2=2 and
b4=1 exactly.

## A specified quantity with recurrence1,2,4

If the recursive comparison operation is relational squaring,

    R_(k+1)=R_k x R_k,

and R0 is the full four-label off-diagonal relation, its Dowker realization
has homotopy type (S^2)^(2^k). The rational Poincare polynomial is

    P_k(t)=(1+t^2)^(2^k),

so b2 obeys b2(k+1)=2*b2(k), starting at1. This derives1,2,4 as the number
of independent degree2 homology classes for that operation. The product law
and Kunneth formula give the recurrence; full enumeration of the four-factor
relation is unnecessary.

The tower bridge is now specific: establish whether its family promotion
implements relational squaring and whether it retains the full primitive
sphere rather than the punctured disk. Current grouping/promotion code does
not implement that operation. In the absolute137-slot complex the degree2
classes vanish. The gauge assignments also require their own identification.

## Verification

    python research/nima/checkers/check_biclique_comparison_complex.py
    python research/nima/checkers/check_biclique_dowker_identification.py

Shared exact sparse chain utilities are in checkers/biclique_complex.py.
Both original and restored fixtures, three small controls, and rectangular
completion pass. General poset/product statements above are mathematical
arguments; the scripts verify their finite instances and rational homology.
