# Group-corrected physical point

```rzk
#lang rzk-1
#define nima-group-path-concat-local
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (y' = z) -> (x = z)),
       (\ q' -> q'), y, p) q
#define nima-group-path-rev-local
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)

#define nima-group-corrected-physical
  (Physical GroupCell : U) : U
  := Sigma (_ : Physical), GroupCell

#define nima-group-corrected-difference
  (Coefficient Physical GroupCell Group : U)
  (rawGroup : Coefficient -> Physical -> Group)
  (groupBoundary : GroupCell -> Group)
  (subtractGroup : Group -> Group -> Group)
  (coefficient : Coefficient)
  (physicalCell : nima-group-corrected-physical Physical GroupCell)
  : Group
  := subtractGroup
       (rawGroup coefficient (first physicalCell))
       (groupBoundary (second physicalCell))

#define nima-group-corrected-difference-vanishes
  (Coefficient Physical GroupCell Group : U)
  (zeroGroup : Group)
  (rawGroup : Coefficient -> Physical -> Group)
  (groupBoundary : GroupCell -> Group)
  (subtractGroup : Group -> Group -> Group)
  (cancelGroup : (x y : Group) -> (x = y) ->
    (subtractGroup x y = zeroGroup))
  (coefficient : Coefficient)
  (physical : Physical)
  (cell : GroupCell)
  (target : Group)
  (rawComparison : rawGroup coefficient physical = target)
  (cellComparison : groupBoundary cell = target)
  : nima-group-corrected-difference Coefficient Physical GroupCell Group
      rawGroup groupBoundary subtractGroup coefficient (physical, cell)
      = zeroGroup
  := cancelGroup
       (rawGroup coefficient physical)
       (groupBoundary cell)
       (nima-group-path-concat-local Group
         (rawGroup coefficient physical) target (groupBoundary cell)
         rawComparison
         (nima-group-path-rev-local Group
           (groupBoundary cell) target cellComparison))

#data NimaGroupCorrectionCellMeaning
  := nima-group-cell-retains-reflection-coherence-homotopy
  | nima-group-boundary-matches-raw-physical-defect
  | nima-subtracting-group-boundary-kills-group-direction
#define nima-group-correction-cell-meaning : NimaGroupCorrectionCellMeaning
  := nima-subtracting-group-boundary-kills-group-direction

#data NimaGroupCorrectionPhysicalGate
  := nima-construct-supported-reflection-group-cell
  | nima-prove-its-boundary-is-the-raw-group-defect
  | nima-physical-trace-cyclicity-controls-its-readout
#define nima-group-correction-physical-gate : NimaGroupCorrectionPhysicalGate
  := nima-prove-its-boundary-is-the-raw-group-defect
```
