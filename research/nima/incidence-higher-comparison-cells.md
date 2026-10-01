# Higher comparison cells from retained family incidence

## Boundary data

Let C1 be the rational leaf-edit space (dimension137), C0 the signed family-total
space (dimension64), and d1 the incidence map of rank47. A2-cell is a labelled
comparison with an explicit boundary in ker(d1). Its boundary acts on retained
leaf values while preserving all family means. Positive and negative boundary
terms are two edge chains with the same family totals.

The construction stores cells and their boundaries. Computing homology treats
boundaries as equivalences of comparisons; it does not erase the90 operational
hidden edit directions or their retained member records.

## Minimal filling: a terminating control

Attach one2-cell for each of the90 fundamental cycles of a spanning forest.
Their chord-coordinate minor is identity. Hence d2 is injective and its image
is exactly ker(d1). The chain dimensions are (64,137,90), with ranks (47,90).
Homology dimensions are H0=17, H1=0, H2=0.

This choice fills all first-level cycles and leaves no next linear kernel.
More generally, attaching an independent basis of a kernel gives an injective
next boundary. The prescription terminates rather than generating another
nontrivial comparison layer.

## Local rule: all complete bipartite comparison blocks

Use retained incidence itself to select local cells. Every complete K(2,2)
subgraph supplies a rectangle2-cell. For source families u,w and target families
v,z its boundary is

    e_uv - e_uz - e_wv + e_wz.

All four leaf records exist by construction. This rule is independent of a
spanning forest; ordering only fixes orientations. The fixture contains672
rectangles. Their boundary rank is90, so they fill all first-level cycles and
have582 independent relations among their boundaries.

A complete K(2,3) or K(3,2) block gives a3-cell with three rectangle faces:

    c_01 - c_02 + c_12.

The edge boundaries cancel exactly. There are1304 such local3-cells, and their
boundary rank is582. They fill all582 relations among rectangle boundaries.
The resulting next kernel has dimension1304-582=722.

Thus this local construction produces successive comparison layers with
explicit boundaries:

    C3 (1304) --d3, rank582--> C2 (672)
      --d2, rank90--> C1 (137) --d1, rank47--> C0 (64).

Every tested d1*d2 and d2*d3 is zero using exact rational arithmetic.

## Recursive rule and next prediction

Continue the same local pattern: for p,q>=2, a complete K(p,q) incidence block
supplies a cell of dimension p+q-2. Above dimension2, use alternating source-
and target-deletion faces, omitting faces with fewer than two vertices on a
side. The target-deletion sum carries the usual (-1)^p sign relative to the
source-deletion sum. At dimension2, use the four-edge boundary above.

This reproduces the checked rectangle and three-rectangle boundaries. It
predicts1074 dimension4 cells, from K(2,4), K(3,3), K(4,2) blocks in this fixture.
The completed [finite hierarchy](complete-biclique-comparison-hierarchy.md)
now verifies d3*d4=0 and rank(d4)=722: all those relations are filled. The same
rule continues with416 dimension5 cells of boundary rank352 and64 dimension6
cells of boundary rank64. Every positive-degree rational homology group vanishes
in this fixture.

The cell dimensions increase by one per boundary layer. Cell counts here are
137,672,1304,1074, rather than a derived1,2,4 progression. A connection to the
stated tower requires an explicit identification of its promoted objects with
these comparison types and an explanation of the quantity represented by the
superscripts.

## Verification

    python research/nima/checkers/check_incidence_higher_cells.py

The checker builds all rectangle boundaries, reduces them in the90 fundamental
cycle coordinates, constructs582 explicit independent relation vectors, and
verifies their boundaries vanish. It separately constructs all1304 local
three-rectangle boundaries and verifies their rank582. The minimal filling
and its terminating kernel serve as a control. All computations are exact;
no numerical rank tolerance is used.
