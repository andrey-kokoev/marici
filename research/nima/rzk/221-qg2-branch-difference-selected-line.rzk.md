# qg2 branch difference to selected line

```rzk
#lang rzk-1
#data NimaQG2OddBranchDifference
  := nima-xi-plus-minus-xi-minus-equals-d-over-A
  | nima-deck-involution-negates-branch-difference
#define nima-qg2-odd-branch-difference : NimaQG2OddBranchDifference
  := nima-xi-plus-minus-xi-minus-equals-d-over-A
#data NimaQG2BranchPrimitiveNormalization
  := nima-multiply-branch-difference-by-A-over-d
  | nima-normalized-branch-difference-equals-one
#define nima-qg2-branch-primitive-normalization
  : NimaQG2BranchPrimitiveNormalization
  := nima-normalized-branch-difference-equals-one
#data NimaQG2SelectedRankOneComparison
  := nima-normalized-branch-generator-maps-to-gamma
  | nima-gamma-coordinate-one-maps-to-v-with-rho0-one
  | nima-generator-preserving-selected-line-map-constructed
#define nima-qg2-selected-rank-one-comparison
  : NimaQG2SelectedRankOneComparison
  := nima-generator-preserving-selected-line-map-constructed
#data NimaQG2PhysicalDescentGate
  := nima-ramified-local-road-comparison-constructed
  | nima-descend-with-occurrence-and-branch-labels
  | nima-prove-equality-with-raw-physical-Cech-defect
#define nima-qg2-physical-descent-gate : NimaQG2PhysicalDescentGate
  := nima-descend-with-occurrence-and-branch-labels
```
