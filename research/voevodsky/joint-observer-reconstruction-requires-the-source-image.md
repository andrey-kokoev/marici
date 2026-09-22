# Joint observer reconstruction requires the source image

## Exact finite reconstruction

The actual branch evidence system has common states P,A,B,AB. Its A-only observer has classes {P,A}, {B}, {AB}; its B-only observer has classes {P,B}, {A}, {AB}.

The joint map is injective, with image

    P  -> (0,0)
    A  -> (0,1)
    B  -> (1,0)
    AB -> (2,2).

The two local spaces have nine Cartesian pairs. Five agree on the bound current verdict, but only four lie in the actual joint image. Therefore even the set-theoretic pullback over the common verdict contains a spurious same-state pair.

The extra pair is (1,1). Its A-observer fiber is {B}; its B-observer fiber is {A}. Both give UNRESOLVED, but their same-state fibers have empty intersection.

Restricting to the source image gives unique reconstruction of the finite evidence state. This is not reconstruction of a unique physical source. All eight A/B extension transitions are verified by recomputing the actual primitive intersections and transported through the joint encoding.

## Same-state versus distributed-history admission

The pair (1,1) is rejected when it claims to describe one retained evidence state. A distributed interpretation could instead assign the observers different retained evidence sets B and A. Those sets have common extension AB in the existing evidence diamond.

These are two different admission questions. The present checker establishes same-state incompatibility and the algebraic common extension. It does not instantiate a distributed delivery history or establish that the two local states occur as cuts of one totally ordered evidence chain; A and B are incomparable in that order. A multi-observer history model would need explicit event incidence and local retention maps.

## Result

Source-bound local observations reconstruct their common evidence state exactly on the actual joint image. Agreement on a shared verdict is a weaker compatibility test. The image relation supplies the missing cross-observer constraint.

A productive continuation is to build the multi-cut version with explicit delivery/retention histories, where different local evidence states can be admitted together and transported toward their common extension.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_joint_observer_reconstruction.py

Artifact: `results/continuation-quotient/joint-observer-reconstruction.json`.

The test freshly invokes the source-bound common-refinement checker, including independent replay of the current branch artifacts. Scope is the closed four-state evidence family.
