# 2756 — The Complete Moving-Relation Image Closes the Differentiated Euler Defect

## Frozen construction

Retain the finite quotient transport from Entry 2708 and totalize it with the derivative image of the complete labelled marked-pole multiplication relation map from Entries 2728 and 2751.

No occurrence projector is selected. The adapter contains all 25,200 labelled relation generators in the ambient-14 presentation. A shorter generator prefix may certify finite containment, but it is not part of the definition.

## Differentiated Euler test

For each external direction (j=0,1,2), test

\[
x\nabla_jD_0+y\nabla_jD_1+z\nabla_jD_2=27D_j
\]

at the three frozen points

\[
(2,3,4),\qquad(3,5,7),\qquad(5,7,11).
\]

Before the correction, the quotient defects have supports (32,32,39) in the three directions. After adjoining the moving-relation image, every residual support is zero.

The finite containment witnesses are stable across all three points:

| direction | processed prefix | derived-span rank | initial defect | residual |
|---|---:|---:|---:|---:|
| (x) | 6722 | 2068 | 32 | 0 |
| (y) | 1695 | 840 | 32 | 0 |
| (z) | 2522 | 1240 | 39 | 0 |

The repeated direction-dependent counts are evidence about this serialization only. The source-natural object remains the complete labelled relation map.

## Presentation-alignment correction

The first execution built moving relations with the chart module's default ambient cutoff 10 and reduced them against an ambient-14 presentation. Integer column identifiers therefore referred to different labelled bases. The aligned rerun derives the relation rows directly in the frozen ambient-14 column map. The theorem survives, while the earlier 13,200-generator count and 891-row witness are withdrawn.

## Narrow result

The differentiated Euler failure of Entry 2708 was not evidence for a new cosmological carrier or coefficient primitive. It was the boundary of a missing moving-presentation coherence cell. Once the quotient transport and complete relation-map derivative are totalized, all nine tests close.

Together with the three-chart naturality theorem of Entry 2751, this establishes a source-natural second-jet adapter on the tested finite atlas.

This is still a finite-model theorem. It does not prove all-order jet compatibility, global de Rham exactness, or physical-cycle descent.

## Artifacts

- `research/benincasa/check_rank26_corrected_adapter_euler.py`
- `research/benincasa/rank26-corrected-adapter-euler.json`
- `research/benincasa/check_rank26_moving_relation_coherence.py`

## Next falsifier

Test third-order mixed derivatives of the corrected adapter. Freeze the same complete labelled relation map and ask whether pairwise coherence satisfies the first nontrivial associativity condition without adjoining a new relation family or choosing primitive lifts.
