# Soft D1 oriented road correction

```rzk
#lang rzk-1
#define nima-soft-D1-oriented-road-correction
  (Cell Cech Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (unitScalar : Scalars)
  (residual : Cech)
  : U
  := Sigma (cell : Cell),
       Sigma (_ : boundary cell = neg residual),
       Sigma (_ : add residual (boundary cell) = zeroCech),
         detector (boundary cell) = negScalar unitScalar
#define nima-soft-D1-oriented-road-correction-cell
  (Cell Cech Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (unitScalar : Scalars)
  (residual : Cech)
  (correction : nima-soft-D1-oriented-road-correction Cell Cech Scalars
    boundary add neg detector negScalar zeroCech unitScalar residual)
  : Cell
  := first correction
#define nima-soft-D1-oriented-road-cancellation
  (Cell Cech Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (unitScalar : Scalars)
  (residual : Cech)
  (correction : nima-soft-D1-oriented-road-correction Cell Cech Scalars
    boundary add neg detector negScalar zeroCech unitScalar residual)
  : add residual (boundary (first correction)) = zeroCech
  := first (second (second correction))
#define nima-soft-D1-oriented-detector-hit
  (Cell Cech Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (unitScalar : Scalars)
  (residual : Cech)
  (correction : nima-soft-D1-oriented-road-correction Cell Cech Scalars
    boundary add neg detector negScalar zeroCech unitScalar residual)
  : detector (boundary (first correction)) = negScalar unitScalar
  := second (second (second correction))
#data NimaSoftD1OrientedCorrectionGate
  := nima-boundary-must-be-negative-residual
  | nima-detector-sign-fixed-by-cancellation
  | nima-geometric-cell-remains-uninhabited
#define nima-soft-D1-oriented-correction-gate : NimaSoftD1OrientedCorrectionGate
  := nima-geometric-cell-remains-uninhabited
```
