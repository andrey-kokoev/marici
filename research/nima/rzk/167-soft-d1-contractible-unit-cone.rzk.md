# Soft D1 contractible unit cone

```rzk
#lang rzk-1
#data NimaSoftD1UnitConeComplex
  := nima-degree1-cell-c-maps-by-identity-to-degree0-unit
#define nima-soft-D1-unit-cone-complex : NimaSoftD1UnitConeComplex
  := nima-degree1-cell-c-maps-by-identity-to-degree0-unit
#data NimaSoftD1UnitConeContraction
  := nima-h-of-unit-is-c
  | nima-dh-is-identity-on-unit-line
  | nima-hd-is-identity-on-cell-line
#define nima-soft-D1-unit-cone-contraction : NimaSoftD1UnitConeContraction
  := nima-dh-is-identity-on-unit-line
#data NimaSoftD1OrientedConeCorrection
  := nima-boundary-of-minus-c-is-minus-unit
  | nima-minus-c-cancels-positive-unit-residual
  | nima-identity-differential-is-integral-unit-pivot
#define nima-soft-D1-oriented-cone-correction : NimaSoftD1OrientedConeCorrection
  := nima-minus-c-cancels-positive-unit-residual
#data NimaSoftD1UnitConeScope
  := nima-explicit-algebraic-road-cell-constructed
  | nima-nearby-cycle-geometric-realization-open
#define nima-soft-D1-unit-cone-scope : NimaSoftD1UnitConeScope
  := nima-explicit-algebraic-road-cell-constructed
```
