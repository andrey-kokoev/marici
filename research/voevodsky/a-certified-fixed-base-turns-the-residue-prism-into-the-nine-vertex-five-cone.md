# A certified fixed base turns the residue prism into the nine-vertex five-cone

## The missing normalization gate

The previous result supplied a constraint-presentation prism Delta^1 x Delta^4. Identifying its two base vertices is not free: refinement must preserve the retained base, and the cone legs must commute with the vertical comparison.

This note gives an explicit normalized diagram with shape

    B * (Delta^1 x Delta^3),

the SAME combinatorial shape as the earlier retained-base presentation cone. It has one base and eight phase-presentation vertices, dimension five, and four nondegenerate top staircase simplices. The match is combinatorial and certificate-algebraic; the analytic roles have not been identified.

## A nontrivial retained base

Use the nonempty two-dimensional base attribute

    B={h>=0, k>=0, h+k<=1/4}.

The four presentation objects T0,...,T3 all describe the larger triangle h,k>=0, h+k<=1. They differ by redundant rows, row selection/permutation and changes of reference. Farkas arrows certify their inclusions and base changes.

Refine each presentation by h<=1/2. This condition already holds on ALL of B, not merely at a chosen base point. Its certificate is

    -k<=0 plus h+k<=1/4 implies h<=1/4<=1/2.

The certificate has nonnegative multiplier vector (0,1,1) and surplus 1/4. Thus the actual base attribute is unchanged by refinement.

## Do not confuse redundancy with a strict categorical inverse

Appending a redundant row and dropping it are mutually valid inclusions, but their Farkas proof matrices need not compose to an identity in both directions. Therefore blindly quotienting the old proof category by a redundant row would overclaim strict coherence.

Instead the checker constructs the normalized FINITE diagram directly. It retains the base-preservation proof and sets the refined base object to the original B. The original cone legs and refined cone legs are chosen explicitly. The added target row on each refined leg uses the retained Farkas proof on B, with the correct reference shift.

The vertical base arrow is then literally the identity in this normalized diagram, and every square

    B -- refined cone leg --> refined Ti
    | identity                       | drop added row
    v                                v
    B ---- original cone leg -----> Ti

commutes at the level of the complete nonnegative matrices, reference shifts and certificate surpluses—not merely at the level of set inclusion.

## Four checked five-simplices

The presentation prism Delta^1 x Delta^3 has four staircase 4-simplices. Coning each with B gives four 5-simplices. Equivalently, in the original Delta^1 x Delta^4 triangulation, the fifth staircase simplex becomes degenerate after identifying the certified fixed-base edge.

For each of the four remaining routes, the checker composes five arrows: start at B, enter the refined presentation chain, move to one of its four vertices, drop the new row there, then finish along the original chain. All fourteen parenthesizations of each route give the same final Farkas/base-change certificate. That is 56 checked five-arrow parenthesizations. The collapsed fifth route is also checked by inserting the base identity.

## An obstruction to the base identification

Change the refinement to h>=1/2. On B, the previous positive combination proves h<=1/4. Together they give

    0<=-1/4.

The refined base is empty, whereas B is nonempty (the origin is an explicit witness). Consequently B cannot be identified with its refined version. A formal topological cone still exists as a combinatorial object, but this retained-base constraint diagram cannot be filled by the same admitted B.

Choosing an empty base would hide the failure by vacuity and would not retain the original admitted base. Choosing a different nonempty base would change the comparison rather than solve it. This is the concrete normalization gate absent from a dimension-only analogy.

## What this adds to structural synthesis

We now have, in one exact polyhedral model:

1. a relative residue (normals and reference slack);
2. explicit transport certificates and their associative composition;
3. four-simplex presentation coherence;
4. a refinement prism;
5. a certified fixed-base normalization to the nine-vertex five-cone;
6. a hostile refinement that forbids that normalization.

These are not yet the old S,A,R,C,G presentations. The retained B is a constraint attribute, not automatically a history archive or analytic source coordinate. The affine residual is not automatically the old residue jet. And no Farkas implication grants historical authority to erase or restore fine information.

The useful next identification must map those earlier objects and constructors into this diagram while preserving the base gate, not simply rename the four presentation vertices. This example demonstrates exactly what such a mapping must explain.

## Reproduction

    python research/voevodsky/checkers/check_based_residue_cone.py

Artifact: `results/based-residue-cone.json`.

The checker reuses the explicit constraint-certificate algebra from the preceding prism control. This is a small exact algebraic model, not an independent analytic source realization, general higher-category prover or provenance service.
