# The filling pencil is the joint path fiber product

## Corrected equivalence

For the actual four-boundary arrangement in the filling-fiber test, let U be the independently joined uv path set and V the independently joined xw path set. Both project to the common boundary pair (a,c).

The tested equivalence is

    W = U fiber_product_(A x C) V.

Here W is the set of 70 source-admitted behavioral fillings. U has 61 elements and V has 1,820. Neither separately represents the complete filling space. Matching BOTH path descriptions on the same diagonal leaves exactly the 70 admitted fillings, with no duplicate witness.

For each fixed (a,c), the corrected fiberwise equation is

    P_AC(a,c) = U(a,c) x V(a,c).

The two full path sets, not their separately asserted equivalence, contribute complementary boundary information. The claim is exact for this actual independently admitted source and chosen four coordinates; arbitrary higher-arity sources do not satisfy it.

## Orientation and comparison coherence

Rotate all four boundary coordinates and their constraints together. In the four successive orientations the two path-space sizes are

    (61,1820), (54,70), (1820,61), (70,54).

Every joint fiber product still has 70 elements. The AC diagonal has 61 nonempty pencils, with nine two-element fibers. The other diagonal has 54 nonempty pencils, with sixteen two-element fibers. Thus the same total source filling space has different conditioned-pencil families.

The checker also constructs all eight dihedral coordinate presentations and verifies their complete joint-edge reconstruction. All 35,840 pointwise comparison triangles agree. Four rotations and two reflections return the original presentation, and the reflection/rotation dihedral law holds.

These are coordinate-transported presentations of the same source relation. They do not establish fixed-label rotational invariance, interchangeability of the local observer protocols, or reverse execution. Coherence of the comparison maps is a permutation identity; exact reconstruction by edge factors is the substantive source-specific test.

## Structural synthesis

The source filling space is primary. Individual path factorizations are partial descriptions whose compatible pairing recovers it in this instance. Rotating changes which boundary coordinates are fixed and therefore changes the number and size of pencils, while preserving the total witnessed relation.

This replaces the failed equivalences of each path with the filling pencil by a verified joint presentation. It retains ambiguous fillings rather than imposing uniqueness on each diagonal fiber.

## Reproduction

    python research/voevodsky/checkers/check_joint_square_pencil_descent.py

Artifact: `results/joint-square-pencil-descent.json`.

The checker freshly replays the filling restriction test, including the independent owning runtime verifier.
