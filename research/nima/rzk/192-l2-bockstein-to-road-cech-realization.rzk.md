# L2 Bockstein-to-road-Cech realization

```rzk
#lang rzk-1
#define nima-L2-Bockstein-road-realization
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  : U
  := Sigma (realizeRelation :
       (relation : Sigma (source : Source), A source = zeroTarget) -> RoadCell),
       (relation : Sigma (source : Source), A source = zeroTarget) ->
         roadBoundary (realizeRelation relation)
           = coefficientToCech (B (first relation))
#define nima-L2-road-cell-of-relation
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target) (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (realization : nima-L2-Bockstein-road-realization Source Target RoadCell Cech
    zeroTarget A B coefficientToCech roadBoundary)
  (relation : Sigma (source : Source), A source = zeroTarget)
  : RoadCell
  := first realization relation
#define nima-L2-road-boundary-comparison
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target) (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (realization : nima-L2-Bockstein-road-realization Source Target RoadCell Cech
    zeroTarget A B coefficientToCech roadBoundary)
  (relation : Sigma (source : Source), A source = zeroTarget)
  : roadBoundary (first realization relation)
      = coefficientToCech (B (first relation))
  := second realization relation
#data NimaL2RoadRealizationStrength
  := nima-one-road-cell-for-every-integral-A-relation
  | nima-boundary-identifies-with-Bockstein-representative
  | nima-stronger-than-finite-rank-comparison
#define nima-L2-road-realization-strength : NimaL2RoadRealizationStrength
  := nima-boundary-identifies-with-Bockstein-representative
#data NimaL2RoadRealizationGate
  := nima-coefficient-to-Cech-map-required
  | nima-relation-cell-realizer-required
  | nima-boundary-comparison-required
  | nima-no-realizer-inhabitant-yet
#define nima-L2-road-realization-gate : NimaL2RoadRealizationGate
  := nima-relation-cell-realizer-required
```
