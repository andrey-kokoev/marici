# Soft D1 candidate correction bridge

```rzk
#lang rzk-1
#define nima-soft-D1-candidate-correction-bridge
  (Physical Cell Cech Group Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (zeroGroup : Group) (unitScalar : Scalars)
  (residual : Cech)
  (physical : Physical)
  (cechDifference : Physical -> Cech)
  (groupDifference : Physical -> Group)
  : U
  := Sigma (cell : Cell),
       Sigma (_ : boundary cell = neg residual),
       Sigma (_ : add residual (boundary cell) = zeroCech),
       Sigma (_ : detector (boundary cell) = negScalar unitScalar),
       Sigma (_ : cechDifference physical = zeroCech),
         groupDifference physical = zeroGroup
#define nima-soft-D1-bridge-Cech-witness
  (Physical Cell Cech Group Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (zeroGroup : Group) (unitScalar : Scalars)
  (residual : Cech) (physical : Physical)
  (cechDifference : Physical -> Cech)
  (groupDifference : Physical -> Group)
  (bridge : nima-soft-D1-candidate-correction-bridge Physical Cell Cech Group Scalars
    boundary add neg detector negScalar zeroCech zeroGroup unitScalar residual
    physical cechDifference groupDifference)
  : cechDifference physical = zeroCech
  := first (second (second (second (second bridge))))
#define nima-soft-D1-bridge-group-witness
  (Physical Cell Cech Group Scalars : U)
  (boundary : Cell -> Cech)
  (add : Cech -> Cech -> Cech)
  (neg : Cech -> Cech)
  (detector : Cech -> Scalars)
  (negScalar : Scalars -> Scalars)
  (zeroCech : Cech) (zeroGroup : Group) (unitScalar : Scalars)
  (residual : Cech) (physical : Physical)
  (cechDifference : Physical -> Cech)
  (groupDifference : Physical -> Group)
  (bridge : nima-soft-D1-candidate-correction-bridge Physical Cell Cech Group Scalars
    boundary add neg detector negScalar zeroCech zeroGroup unitScalar residual
    physical cechDifference groupDifference)
  : groupDifference physical = zeroGroup
  := second (second (second (second (second bridge))))
#data NimaSoftD1CandidateBridgeGate
  := nima-road-cell-Cech-zero-and-group-zero-required-at-same-point
  | nima-road-algebra-does-not-prove-group-reflection
  | nima-bridge-uninhabited
#define nima-soft-D1-candidate-bridge-gate : NimaSoftD1CandidateBridgeGate
  := nima-road-algebra-does-not-prove-group-reflection
```
