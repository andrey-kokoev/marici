# Road correction and group-coherence independence

```rzk
#lang rzk-1
#data NimaRoadCorrectionCountermodel
  := nima-singleton-road-cell-additive-Cech-cancels-unit-residual
  | nima-two-point-group-has-nonzero-candidate-difference
#define nima-road-correction-countermodel : NimaRoadCorrectionCountermodel
  := nima-two-point-group-has-nonzero-candidate-difference
#data NimaRoadGroupIndependenceConclusion
  := nima-oriented-road-correction-does-not-parametrically-imply-group-zero
  | nima-group-reflection-needs-independent-geometric-input
#define nima-road-group-independence-conclusion : NimaRoadGroupIndependenceConclusion
  := nima-oriented-road-correction-does-not-parametrically-imply-group-zero
#data NimaPhysicalCompletionWorkSplit
  := nima-finish-road-unit-cell-from-nearby-cycle
  | nima-compute-group-reflection-at-candidate-separately
  | nima-join-only-at-same-physical-point
#define nima-physical-completion-work-split : NimaPhysicalCompletionWorkSplit
  := nima-compute-group-reflection-at-candidate-separately
```
