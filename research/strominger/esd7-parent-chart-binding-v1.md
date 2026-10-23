# Source-binding audit: parent transitions are not fine-vertex operators

## Result

The available parent analytical transitions do not directly fill the F006 gate. Their type is wrong unless a fine-vertex refinement is supplied first.

The source [consolidated analytical position](../voevodsky/consolidated-four-presentation-analytic-pyramid-position.md) constructs reversible parent transitions `C_ij = S_j R_i` on declared essential images, but explicitly leaves a uniform semantic interpretation of all120 subdivision nodes as a separate refinement problem. The [interior-node typing note](../voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md) also warns against treating barycentric labels as unprovided sums, tensors or mixtures of parent presentations.

The [executable audit](checkers/check_esd7_parent_chart_binding.py) verifies the resulting finite typing obstruction. Twelve checks pass. **Only bare, context-free parent-chart substitution is rejected; the refinement and single-channel conjectures remain open.**

## F006 in actual coordinates

| Vertex | Barycentric coordinate |
|---|---|
| V001 |(0,0,1,6)|
| V008 |(0,1,0,6)|
| V036 |(1,0,0,6)|

Its edges transfer one unit as follows:

- E004:3→2;
- E037:2→1;
- E006:3→1.

At the **parent** level there is indeed a source-backed conditional reduction:

    C21 C32 = S1 R2 S2 R3 = S1 R3 = C31,

using `R2 S2 = I` on the admitted observer essential image. This is not yet a reduction of the fine-vertex operators: V001 is `(0,0,1,6)`, not the parent chart3 corner. The six retained units in coordinate4 cannot simply be discarded.

## Concrete failure of direct substitution

At the same V001:

- E004 would require its source to be parent chart3;
- E003, the adjacent4→3 transfer, would require its source to be parent chart4.

Thus no single parent-chart label at V001 types both bare transitions. Assigning different local presentations could resolve this, but requires precisely the context-dependent comparison data that the substitution omits.

Across the complete generated complex:

-504 edges are single-unit transfers;
-56 edges are compound transfers, not one bare parent transition;
-4 corner vertices require one parent chart;
-36 vertices require two,60 require three and20 require four.

Consequently116 of120 vertices obstruct this particular context-free assignment. The required chart sets equal their positive barycentric supports. The audit retains the incident edges witnessing every constraint, rather than deriving the conclusion from counts alone.

## What remains to construct

The missing datum is now more precise than a table of numerical matrices: construct source-bound fine-vertex objects `X_alpha` and incidence maps that retain the background and local presentation context. Then bind the corresponding graph domains, endpoint readouts and intertwiners at F006.

A context-dependent refinement, whiskering construction or appropriate joint-graph realization is not ruled out. This audit is not made a prerequisite uniqueness theorem for that constructive work. It prevents the existing coarse-chart identity from being misreported as the actual face proof.

```sh
python research/strominger/checkers/check_esd7_parent_chart_binding.py
```

- [Verification receipt](results/esd7-parent-chart-binding-verification.json).
- [All edge transfers and vertex typing constraints](results/esd7-parent-chart-binding-audit.json).

No source operator is installed into the finite comparison gate, no analytical filler is claimed, and the114-record convention remains open.
