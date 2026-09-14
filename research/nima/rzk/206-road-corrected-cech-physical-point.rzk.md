# Road-corrected Cech physical point

```rzk
#lang rzk-1
#define nima-road-Cech-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (y' = z) -> (x = z)),
       (\ q' -> q'), y, p) q
#define nima-road-Cech-rev
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)
#define nima-road-corrected-physical
  (Physical RoadCell : U) : U
  := Sigma (_ : Physical), RoadCell

#define nima-road-corrected-Cech-difference
  (Coefficient Physical RoadCell Cech : U)
  (rawCech : Coefficient -> Physical -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (subtractCech : Cech -> Cech -> Cech)
  (coefficient : Coefficient)
  (physicalRoad : nima-road-corrected-physical Physical RoadCell)
  : Cech
  := subtractCech
       (rawCech coefficient (first physicalRoad))
       (roadBoundary (second physicalRoad))

#define nima-road-corrected-Cech-vanishes
  (Coefficient Physical RoadCell Cech : U)
  (zeroCech : Cech)
  (rawCech : Coefficient -> Physical -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (subtractCech : Cech -> Cech -> Cech)
  (cancelCech : (x y : Cech) -> (x = y) -> (subtractCech x y = zeroCech))
  (coefficient : Coefficient)
  (physical : Physical)
  (cell : RoadCell)
  (target : Cech)
  (rawComparison : rawCech coefficient physical = target)
  (roadComparison : roadBoundary cell = target)
  : nima-road-corrected-Cech-difference Coefficient Physical RoadCell Cech
      rawCech roadBoundary subtractCech coefficient (physical, cell) = zeroCech
  := cancelCech
       (rawCech coefficient physical)
       (roadBoundary cell)
       (nima-road-Cech-concat Cech
         (rawCech coefficient physical) target (roadBoundary cell)
         rawComparison
         (nima-road-Cech-rev Cech (roadBoundary cell) target roadComparison))

#define nima-selected-log-road-corrected-point
  (Coefficient Physical RoadCell Cech : U)
  (rawCech : Coefficient -> Physical -> Cech)
  (roadBoundary : RoadCell -> Cech)
  (coefficient : Coefficient)
  (physical : Physical)
  (cell : RoadCell)
  : nima-road-corrected-physical Physical RoadCell
  := (physical, cell)

#data NimaRoadCorrectedPhysicalMeaning
  := nima-raw-Cech-residual-equals-selected-v
  | nima-log-road-boundary-equals-selected-v
  | nima-subtracting-road-boundary-kills-Cech-direction
#define nima-road-corrected-physical-meaning : NimaRoadCorrectedPhysicalMeaning
  := nima-subtracting-road-boundary-kills-Cech-direction

#data NimaRoadCorrectedPhysicalGate
  := nima-prove-actual-raw-physical-Cech-residual-equals-image-of-v
  | nima-prove-log-road-boundary-equals-image-of-v
  | nima-road-correction-then-supplies-zero-Cech-witness
#define nima-road-corrected-physical-gate : NimaRoadCorrectedPhysicalGate
  := nima-prove-actual-raw-physical-Cech-residual-equals-image-of-v
```
