# Higher-dimensional common lifting requires a compatibility hypergraph

## Owning varying-domain construction

Use m=4, center t=(50,51,52,53), slopes r_j=128^-j and delta=128^-4. Public parameters vary on the segment

    U=206+delta*p, V=V(center), 0<=p<=1.

Two fine parameters are h=(t0-50)/delta and k=(t1-51)/delta, restricted to [0,1]^2. For given p,h,k, set t0=50+delta*h, t1=51+delta*k and solve the remaining two independent moment equations for t2,t3. This is an affine source lift. Exact strict admission at the eight corners of the (p,h,k) cube proves the entire cube lies in the owning atom box by convexity.

Retain three histories, each with that public domain and common fine square:

    A: h<=1/4,
    B: k<=1/4,
    C: h+k>=1.

All are rational linear evidence in the original moments and raw atom audits; the local normalization is a presentation, not a changed accuracy norm or additional source-admission assumption.

## Every pair has a continuous common section

Use (h,k)=(0,0) for A,B; (0,1) for A,C; and (1,0) for B,C. Each pair choice is fixed in fine parameters and varies affinely with p through the source inverse. Thus every pair has a continuous, source-admitted common lifting procedure over the entire public segment. Every individual history has the same full public image.

## The triple has no lift at any public point

Add the three defining inequalities with weights one:

    h<=1/4, k<=1/4, -h-k<=-1
    --------------------------------
    0<=-1/2.

This exact Farkas certificate is independent of p. There is no triple-compatible source witness anywhere on the common public domain.

The pairwise incompatibility graph has no edges and would incorrectly allow one lifting state. Two are necessary and sufficient: group A,B and keep C separate. Their explicit sections prove achievability. This does not contradict the earlier graph criterion, whose complete fine fibers were scalar intervals.

## General finite convex-fiber statement

Suppose all histories have a common public image Q, and at each y their fine fibers are convex subsets of one affine space of dimension at most r. If a finite group has empty common fiber at y, Helly's theorem supplies an incompatible subfamily of at most r+1 histories at that same y.

Define an incompatibility hyperedge when a subfamily has empty common fiber at some admitted public point. Every minimal hyperedge then has size at most r+1. Groupwise POINTWISE lifting compatibility is equivalent to containing no such hyperedge. A partition into groups with nonempty common fibers is a hypergraph coloring problem; the owning example has one minimal hyperedge of size three.

This statement is conditional on the common fiber dimension and convexity. It does not bound how hard it is to find the witnessing public point or enumerate all hyperedges. For a fixed rational linear public point, source-fiber infeasibility admits a Farkas proof; a global parameter search is a separate problem.

Nor does pointwise compatibility alone assert an effective continuous common section in every possible family. The finite-affine interval theorem already supplies continuity for r=1. The construction here supplies explicit affine sections for its successful groups. Any general continuous or efficient-selection claim must add and verify the appropriate parameterized hypotheses.

## Structural consequence

Minimal sufficient lifting state is not always governed by a graph. Higher-dimensional fine fibers create genuinely higher-order compatibility obstructions, even when every pair admits a continuous shared selection. The appropriate state-compression object is a family of jointly admissible history groups, with dimension bounding the size of minimal pointwise convex obstructions—not a transitive equivalence quotient.

## Reproduction

    python research/voevodsky/checkers/check_common_lift_hypergraph.py

Artifact: `results/common-lift-hypergraph.json`.

The checker verifies eight strict source-admission corners, nine pair-section controls and the exact triple Farkas identity. The continuum statements follow from affine source lifting and the displayed contradiction, not finite extrapolation. This is a mathematical checker, not an independently verified migration protocol or a fresh upstream source-admission proof.
