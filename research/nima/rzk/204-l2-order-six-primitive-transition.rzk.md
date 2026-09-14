# L2 primitive transition has order six through D20

```rzk
#lang rzk-1
#data NimaL2PrimitiveTransitionOrders
  := nima-divided-transition-index-ratio-six-at-D12-D16-D20
  | nima-labelled-triple-index-ratio-two-at-D12-D16-D20
#define nima-L2-primitive-transition-orders : NimaL2PrimitiveTransitionOrders
  := nima-divided-transition-index-ratio-six-at-D12-D16-D20
#data NimaL2CyclicTorsionDirection
  := nima-class-v-has-order-six
  | nima-three-v-has-order-two
  | nima-log-selector-rho0-sends-v-to-one
#define nima-L2-cyclic-torsion-direction : NimaL2CyclicTorsionDirection
  := nima-class-v-has-order-six
#data NimaL2PrimitiveTransitionFormula
  := nima-v-equals-a3-plus-a3b
  | nima-labelled-s11-transition-equals-three-v
#define nima-L2-primitive-transition-formula : NimaL2PrimitiveTransitionFormula
  := nima-labelled-s11-transition-equals-three-v
#data NimaL2PrimitiveCellInterpretation
  := nima-one-Z-over6-derived-cell-controls-selected-log-line
  | nima-s11-supplies-only-its-Z-over2-subclass
#define nima-L2-primitive-cell-interpretation : NimaL2PrimitiveCellInterpretation
  := nima-one-Z-over6-derived-cell-controls-selected-log-line
```
