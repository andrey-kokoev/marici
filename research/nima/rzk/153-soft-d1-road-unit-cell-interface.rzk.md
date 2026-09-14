# Soft D1 road unit-cell interface

```rzk
#lang rzk-1
#define nima-soft-D1-road-unit-cell-realization
  (Cell Target Scalars : U)
  (boundary : Cell -> Target)
  (detector : Target -> Scalars)
  (oneTarget : Target) (oneScalar : Scalars)
  : U
  := Sigma (cell : Cell),
       Sigma (_ : boundary cell = oneTarget),
         detector (boundary cell) = oneScalar
#define nima-build-soft-D1-road-unit-cell-realization
  (Cell Target Scalars : U)
  (boundary : Cell -> Target)
  (detector : Target -> Scalars)
  (oneTarget : Target) (oneScalar : Scalars)
  (cell : Cell)
  (boundaryIsUnit : boundary cell = oneTarget)
  (detectorIsUnit : detector (boundary cell) = oneScalar)
  : nima-soft-D1-road-unit-cell-realization
      Cell Target Scalars boundary detector oneTarget oneScalar
  := (cell, (boundaryIsUnit, detectorIsUnit))
#define nima-soft-D1-road-unit-cell
  (Cell Target Scalars : U)
  (boundary : Cell -> Target)
  (detector : Target -> Scalars)
  (oneTarget : Target) (oneScalar : Scalars)
  (realization : nima-soft-D1-road-unit-cell-realization
    Cell Target Scalars boundary detector oneTarget oneScalar)
  : Cell
  := first realization
#define nima-soft-D1-road-unit-boundary
  (Cell Target Scalars : U)
  (boundary : Cell -> Target)
  (detector : Target -> Scalars)
  (oneTarget : Target) (oneScalar : Scalars)
  (realization : nima-soft-D1-road-unit-cell-realization
    Cell Target Scalars boundary detector oneTarget oneScalar)
  : boundary (first realization) = oneTarget
  := first (second realization)
#define nima-soft-D1-road-unit-detector-hit
  (Cell Target Scalars : U)
  (boundary : Cell -> Target)
  (detector : Target -> Scalars)
  (oneTarget : Target) (oneScalar : Scalars)
  (realization : nima-soft-D1-road-unit-cell-realization
    Cell Target Scalars boundary detector oneTarget oneScalar)
  : detector (boundary (first realization)) = oneScalar
  := second (second realization)
#data NimaSoftD1RoadUnitCellGate
  := nima-algebraic-unit-target-now-explicit
  | nima-global-road-cell-with-unit-boundary-required
  | nima-no-road-unit-cell-inhabitant-yet
#define nima-soft-D1-road-unit-cell-gate : NimaSoftD1RoadUnitCellGate
  := nima-global-road-cell-with-unit-boundary-required
```
