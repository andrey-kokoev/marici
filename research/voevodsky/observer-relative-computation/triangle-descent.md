# Filled-triangle observations: a checked descent equivalence

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverTriangleDescent.agda`; output is retained in `results/agda-triangle-descent.log`. This rebuilds the preceding triangle-coherence obstruction and its upstream dependencies. No older whole-programme receipt is asserted current for this module.

## Actual finite descent

The support is an explicit higher inductive type with three vertices, three edges, and a specified two-dimensional face. The face is represented as a square whose left boundary is collapsed: the two other routes form the triangle boundary.

For ANY dependent family F over this support, LocalData contains:

- three fibre inhabitants;
- three dependent edge comparison witnesses;
- a dependent two-dimensional compatibility witness across the face.

The module constructs `glue : LocalData → Observation` and `restrict : Observation → LocalData`. Both roundtrips are checked, including the face clause. These give an actual `LocalData ≃ Observation`, not merely an implication or a condition declared well-typed. No edge or face witnesses are propositionally truncated. The local-data roundtrip is definitional; the section roundtrip is established by higher-inductive elimination.

## Connection and obstruction

Checked conversions connect a base equation p·q=r to the square presentation and back. They suffice to build the joint probe into an ambient X, and the descent theorem then applies to any ambient family pulled back along that probe. Definitional inverse laws for those conversions are NOT claimed.

A constant-Unit regression constructs local data and recovers all of it after gluing. Conversely, the earlier refl/refl/nontrivial-loop counterexample cannot admit a square filling: converting any supposed square to a composite-path cell contradicts the previously checked obstruction.

The transport-equation formulation of fibre compatibility in ObserverTriangleCoherence and the native dependent-square formulation here have not separately been proved equivalent. The latter is the exact checked interface of the descent theorem; no claim about the former's sufficiency is smuggled in.

## Foundational status

This establishes a finite, direction-free way to assemble observer-relative content. Compatibility, including its higher witness, is exactly the data of a coherent observation on this constructed support. It does not force arbitrary loops to fill, prove general descent for all covers, assign a geometric area, or derive temporal causality.

Next take the existing direction-and-records branch. The construction so far is reversible at the level of comparison witnesses and has no clock. Investigate whether any alleged execution arrow comes from additional forgetting/record structure rather than from observation positivity itself. Further higher-dimensional generalization remains possible but is not needed to start that test.
