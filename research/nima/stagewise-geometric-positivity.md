# Stagewise positivity audit of the twelve-triangle nets

## Mandatory requirement

[Stagewise geometric positivity](stagewise-positivity-requirement.md) is now an admissibility requirement for the formation/minimality problem. Every intermediate realization and transition requires geometric evidence; missing evidence blocks certification. The tests below are necessary audits, not a complete verifier for that requirement.

## Subsequent geometric lift

[Executable atlas witnesses](stagewise-positive-atlas-witness.md) now supply the previously missing intermediate embeddings for the registered positive-homothetic tetrahedral family. All four atlas-augmented candidates pass stagewise geometric checks. The audit below remains the result for bare coefficient operators and their literal-coordinate interpretation; its failure is not contradicted by the new chart interpretation.

## Verdict of the original bare-operator audit

Stagewise positivity of oriented-cell amplitudes holds for both the 1836-arrow construction and its compressed 73-arrow realization. It does not distinguish their sizes.

Stagewise preservation of an embedded positive geometry has not been constructed for either network. Their existing operators act on complex coefficient fields. Interpreting those operators literally as spatial-coordinate maps fails already at the first local projection.

Thus the previous layered-network minima remain valid algebraic results, but are not certified minima in a class of positive-geometric stage transitions.

## The tested meanings of positivity

We separate three properties:

1. **PSD operator:** a Hermitian positive semidefinite coefficient-space matrix.
2. **Positive oriented-cell amplitude:** each coefficient of the twelve consistently oriented triangles is a positive real number.
3. **Positive geometric realization:** a well-defined real embedded cell complex, consistent shared vertices and edges, prescribed orientation, and nondegenerate positive enclosed volume (or an explicitly supplied equivalent atlas).

Neither the first nor the second property alone establishes the third. Negative Cartesian components also do not by themselves violate geometry: the tetrahedral rotations are proper rotations despite having signed matrix entries.

## Boundary cancellation derives the common mode

For the twelve-triangle surface, the oriented edge-boundary matrix D has shape 18 by 12 and rank eleven. Its nullspace is

    ker D = span{(1,...,1)}.

Therefore the strictly positive closed-chain weights are exactly

    {a*(1,...,1) : a>0}.

Closure of the weighted triangle assembly forces one common coefficient. This is a geometric source for the collective mode, rather than an extra independent identity at every triangle.

Over complex coefficients, closure similarly forces all twelve coefficients equal; it does not select their common phase. Positive oriented-chain normalization selects a positive real representative. These are weights on a fixed geometric support, not free changes of vertex positions.

## Every coefficient stage preserves the positive cell cone

Let E inject the twelve face amplitudes into the 36 local coefficient ports:

    E(a)_g = a_g v_g.

The original operators satisfy exactly

    L E = E,
    G E = E Q,
    N E = E Q,
    Q=ones(12,12)/12.

Thus local selection fixes the positive amplitudes; symmetry averaging replaces them by their positive mean; collective feedback retains that mean. Closed positive inputs are fixed at every stage.

For the compressed network:

    B E(a) = mean(a),
    middle map = identity,
    A(mean(a)) = E(mean(a),...,mean(a)).

These maps also preserve the appropriate positive cones at every stage. The common closed-chain ray is representable by one positive scalar. Positivity of this ray therefore cannot establish an 1836-arrow lower bound.

## Literal spatial-coordinate test

To test whether the existing maps themselves supply the missing geometric transitions, package the three spatial corners of each triangle as a 3-by-3 matrix X_g. Stack them into X of shape 36 by 3. The unprojected X gives the exact closed tetrahedral surface of volume 8/3.

Apply the specified stages directly:

    X -> L X -> G L X -> N G L X.

On this fixture the three outputs are equal. They have:

- 48 nonreal coordinate entries;
- six different images for each originally shared vertex A, B, C and D;
- all four face-centre positions mapped to zero;
- zero signed volume if one tries taking their real parts as spatial vertices.

These outputs are not a literal embedded real mesh with the original incidence identifications. In particular, the face seams do not match. A complex chart interpretation may be appropriate, but it needs its own embeddings, overlap transitions and orientation checks; those are not supplied merely by the projector matrices.

The compressed intermediate B X is a single row of complex chart coefficients. It is not an explicitly represented twelve-face spatial cell complex. Expanding it with A reproduces the same projected data L X, not the original spatial X under this literal interpretation.

## Fixed-frame hostile control

Rigidly rotate the original entire closed mesh by a 120-degree tetrahedral rotation while holding the numerical projector reference frames fixed. Its volume remains 8/3, but the collective projector annihilates the stacked corner data.

This is a fixed-reference test. A rule that transports the frames along with the input would be different and covariant. The example shows that the fixed coefficient operators cannot simply be called positivity-preserving spatial maps on arbitrary positive embeddings.

## What this means for minimality

There are two consistent next models, with different obligations:

- **Phase processing on a fixed positive carrier:** keep the spatial mesh as part of the stage state, and apply the coefficient operators only to phase data. Both networks can retain that carrier, and the algebraic compression is not ruled out by positivity of its cell weights.
- **Formation through positive geometric transitions:** define the embedded cells or atlas at each stage, prove compatible seam identifications and positivity of each transition, and count the operations needed to carry those data. Neither current graph has such a complete stage-by-stage geometric interpretation.

The previous claim that geometry was preserved meant that the same positive mesh remained available externally while its coefficient network was refactored. It was not a proof that the interaction maps themselves transported that mesh positively.

Consequently this audit does not promote 1836 to a geometric minimum or discard 73 merely because its interface is small. It identifies the missing admissibility condition and provides concrete tests that any proposed geometric transition must pass.

## Verification

    python research/nima/checkers/check_stagewise_geometric_positivity.py

Exact rational and Q(i*sqrt(3)) checks cover the boundary rank and positive closed cone, the induced amplitude maps of every stage, Hermitian projector identities, literal vertex-image/seam audits, and the rigid-rotation control.

Artifact: `results/stagewise-geometric-positivity.json`. Its `status: passed` means the audit assertions completed; its geometric-admissibility fields explicitly report failure of the literal coordinate interpretation.
