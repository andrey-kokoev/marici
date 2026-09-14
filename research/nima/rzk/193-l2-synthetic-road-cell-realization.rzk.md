# Synthetic coefficient-side road-cell realization

```rzk
#lang rzk-1
#define nima-L2-synthetic-road-cell
  (Source Target : U)
  (zeroTarget : Target)
  (A : Source -> Target)
  : U
  := Sigma (source : Source), A source = zeroTarget
#define nima-L2-synthetic-road-boundary
  (Source Target : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  : nima-L2-synthetic-road-cell Source Target zeroTarget A -> Target
  := \ relation -> B (first relation)
#define nima-L2-synthetic-relation-realizer
  (Source Target : U)
  (zeroTarget : Target)
  (A : Source -> Target)
  : (relation : Sigma (source : Source), A source = zeroTarget) ->
      nima-L2-synthetic-road-cell Source Target zeroTarget A
  := \ relation -> relation
#define nima-L2-synthetic-boundary-comparison
  (Source Target : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (relation : Sigma (source : Source), A source = zeroTarget)
  : nima-L2-synthetic-road-boundary Source Target zeroTarget A B relation
      = B (first relation)
  := refl
#data NimaL2SyntheticRealizationStatus
  := nima-coefficient-side-realization-inhabited
  | nima-boundary-comparison-definitional
  | nima-no-physical-road-geometry-in-synthetic-cell
#define nima-L2-synthetic-realization-status : NimaL2SyntheticRealizationStatus
  := nima-coefficient-side-realization-inhabited
#data NimaL2RemainingGeometricComparison
  := nima-map-synthetic-relation-cells-to-physical-road-cells
  | nima-preserve-boundary-under-that-map
#define nima-L2-remaining-geometric-comparison : NimaL2RemainingGeometricComparison
  := nima-map-synthetic-relation-cells-to-physical-road-cells
```
