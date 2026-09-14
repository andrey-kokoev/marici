# Road/group-corrected five-direction lift

```rzk
#lang rzk-1
#define nima-road-group-corrected-physical
  (Physical RoadCell GroupCell : U) : U
  := Sigma (_ : Physical), Sigma (_ : RoadCell), GroupCell

#define nima-road-group-corrected-five-lift
  (Coefficient Physical RoadCell GroupCell Endpoint Cech Normal Group Operation : U)
  (zeroEndpoint : Endpoint) (zeroCech : Cech) (zeroNormal : Normal)
  (zeroGroup : Group) (zeroOperation : Operation)
  (endpointDifference : Coefficient -> Physical -> Endpoint)
  (rawCech : Coefficient -> Physical -> Cech)
  (normalDifference : Coefficient -> Physical -> Normal)
  (rawGroup : Coefficient -> Physical -> Group)
  (operationDifference : Coefficient -> Physical -> Operation)
  (roadBoundary : RoadCell -> Cech)
  (groupBoundary : GroupCell -> Group)
  (subtractCech : Cech -> Cech -> Cech)
  (subtractGroup : Group -> Group -> Group)
  (coefficient : Coefficient)
  (physical : Physical) (roadCell : RoadCell) (groupCell : GroupCell)
  (endpointZero : endpointDifference coefficient physical = zeroEndpoint)
  (cechZero : subtractCech (rawCech coefficient physical)
    (roadBoundary roadCell) = zeroCech)
  (normalZero : normalDifference coefficient physical = zeroNormal)
  (groupZero : subtractGroup (rawGroup coefficient physical)
    (groupBoundary groupCell) = zeroGroup)
  (operationZero : operationDifference coefficient physical = zeroOperation)
  : Sigma (decorated : nima-road-group-corrected-physical
       Physical RoadCell GroupCell),
      Sigma (_ : endpointDifference coefficient (first decorated) = zeroEndpoint),
      Sigma (_ : subtractCech (rawCech coefficient (first decorated))
        (roadBoundary (first (second decorated))) = zeroCech),
      Sigma (_ : normalDifference coefficient (first decorated) = zeroNormal),
      Sigma (_ : subtractGroup (rawGroup coefficient (first decorated))
        (groupBoundary (second (second decorated))) = zeroGroup),
        operationDifference coefficient (first decorated) = zeroOperation
  := ((physical, (roadCell, groupCell)),
      (endpointZero, (cechZero, (normalZero, (groupZero, operationZero)))))

#data NimaRoadGroupCorrectedLiftMeaning
  := nima-one-physical-point-retains-road-and-group-cells
  | nima-endpoint-normal-operation-witnesses-transport-unchanged
  | nima-road-and-group-boundaries-kill-two-missing-directions
  | nima-five-direction-lift-assembled
#define nima-road-group-corrected-lift-meaning : NimaRoadGroupCorrectedLiftMeaning
  := nima-five-direction-lift-assembled

#data NimaRoadGroupCorrectedLiftGate
  := nima-raw-Cech-equals-selected-v-and-road-boundary
  | nima-raw-group-equals-supported-reflection-cell-boundary
  | nima-both-comparisons-produce-full-lift
#define nima-road-group-corrected-lift-gate : NimaRoadGroupCorrectedLiftGate
  := nima-both-comparisons-produce-full-lift
```
