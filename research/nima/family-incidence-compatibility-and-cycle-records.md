# Family incidence: compatibility and retained cycle records

## Relation between families

Construct a bipartite multigraph whose vertices are source-indexed and
target-indexed families. Each retained leaf record is an edge from its source
family to its target family. Parallel records remain distinct edges.

For the137-slot fixture this gives64 vertices,137 edges and17 connected
components: one connected arrow component containing32 family vertices, and
16 state components, each a source/target pair with one edge.

This relation is determined by retained membership. No promoted endpoint
summary is needed to define it.

## Exact meaning of the readout rank

Orient every edge source->target and let D be its signed incidence matrix
(+1 at its source, -1 at its target). If O is the joint mean readout matrix,
then D is obtained from O by multiplying each source row by its family size
and each target row by minus its family size. All sizes are nonzero, so these
row scalings preserve rank and the leaf kernel.

For a graph with v vertices and c connected components, rank(D)=v-c. Each
component supplies one row relation. A spanning forest has v-c edges, whose
incidence columns are independent, proving the matching lower bound.

Thus the previously computed rank47 is explained structurally:

    rank(O)=64-17=47,
    dim ker(O)=137-47=90.

## Compatibility law for proposed family means

A requested mean increment dy is realizable exactly when, in every component C,

    sum_(source F in C) |F| dy_F
      = sum_(target T in C) |T| dy_T.

Necessity follows because both sides count the total leaf increment in that
component. Sufficiency follows by solving signed divergence on a spanning tree
of each component, eliminating leaves from the tree inward.

For this fixture there is one arrow-block balance condition and16 state-pair
conditions. Each state source/target mean is the same scalar readout. These
17 conditions identify the redundant directions and specify which simultaneous
requests conflict.

## What the90 invisible edits are

Every nonforest edge closes a unique fundamental cycle. Its alternating signed
edge vector changes retained leaf values while leaving all family means fixed.
There are137-(64-17)=90 such vectors. Giving each its own chord coefficient1
and all other chord coefficients0 proves their independence.

They span the kernel: subtract the corresponding chord-weighted cycles from
any divergence-free edit. The remainder is divergence-free and supported on
a forest, so successive leaf elimination forces it to vanish.

An arbitrary leaf edit therefore decomposes into a chosen compatible forest
lift of its family means plus90 cycle coordinates. The forest is a choice;
the kernel and its dimension are intrinsic. The fixture verifies this
reconstruction exactly with rational arithmetic.

The forest lift is a constructive existence witness, generally not the
minimum-Euclidean-change lift. The earlier induced-metric return chooses the
orthogonal representative instead. Both lifts have the same readouts and differ
by a cycle edit.

## What happens under relation-based promotion

A natural rule is to group family vertices by shared-member connected component.
It produces17 groups. Every original incidence edge then has both endpoints
in the same promoted group, leaving only self-relations. Applying connected
components again changes nothing.

Thus component promotion, like key-preserving singleton promotion, reaches a
stationary quotient. The incidence relation explains compatibility and hidden
content, but its component quotient alone supplies no growing1,2,4 hierarchy.

## Next structural object

The retained relation has more structure than its components:

    leaf-edge edits --D--> signed family totals.

Its kernel is the space of comparison cycles; its cokernel records component
balance obstructions. A recursive comparison construction should specify how
these cycle records become next-level cells and what their endpoints/boundaries
are. This is now a concrete candidate input, with90 independent cycle directions
in the fixture. Selecting a spanning forest gives coordinates, not a canonical
promotion law or a recurrence for the proposed gauge superscripts.

## Verification

    python research/nima/checkers/check_family_incidence_structure.py

Integer cycle checks, exact rational compatibility solver,17 incompatible-request
controls, arbitrary seeded-pattern edit reconstruction, and stationary component
promotion. No numerical rank computation or external dependency is required.
