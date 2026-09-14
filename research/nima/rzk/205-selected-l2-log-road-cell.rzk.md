# Selected L2-to-log road cell

The physical rank-one comparison needs one detected relation, not a road cell
for every Bockstein direction.

```rzk
#lang rzk-1
#define nima-selected-L2-road-realization
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (source : Source)
  (relation : A source = zeroTarget)
  : U
  := Sigma (cell : RoadCell),
       roadBoundary cell = coefficientToCech (B source)

#define nima-selected-L2-log-cell-realization
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (source : Source)
  (relation : A source = zeroTarget)
  (logPrimitiveCell : RoadCell)
  (comparison : roadBoundary logPrimitiveCell
    = coefficientToCech (B source))
  : nima-selected-L2-road-realization Source Target RoadCell Cech
      zeroTarget A B coefficientToCech roadBoundary source relation
  := (logPrimitiveCell, comparison)

#define nima-selected-L2-road-cell
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (source : Source)
  (relation : A source = zeroTarget)
  (realization : nima-selected-L2-road-realization Source Target RoadCell Cech
    zeroTarget A B coefficientToCech roadBoundary source relation)
  : RoadCell
  := first realization

#define nima-selected-L2-road-boundary
  (Source Target RoadCell Cech : U)
  (zeroTarget : Target)
  (A B : Source -> Target)
  (coefficientToCech : Target -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (source : Source)
  (relation : A source = zeroTarget)
  (realization : nima-selected-L2-road-realization Source Target RoadCell Cech
    zeroTarget A B coefficientToCech roadBoundary source relation)
  : roadBoundary (first realization) = coefficientToCech (B source)
  := second realization

#data NimaSelectedL2LogRoadDatum
  := nima-selected-class-v-equals-a3-plus-a3b
  | nima-rho0-v-equals-one
  | nima-v-has-order-six-through-D20
  | nima-log-primitive-cell-gamma
#define nima-selected-L2-log-road-datum : NimaSelectedL2LogRoadDatum
  := nima-log-primitive-cell-gamma

#data NimaSelectedL2LogRoadGate
  := nima-prove-physical-Cech-image-of-v-is-boundary-of-gamma
  | nima-prove-v-is-authorized-by-ringed-filtered-Q-comparison
  | nima-full-all-relation-realizer-not-required
#define nima-selected-L2-log-road-gate : NimaSelectedL2LogRoadGate
  := nima-prove-physical-Cech-image-of-v-is-boundary-of-gamma
```
