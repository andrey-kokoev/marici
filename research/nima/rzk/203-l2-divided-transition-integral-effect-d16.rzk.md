# Divided L2 transition integral effect at D16

```rzk
#lang rzk-1
#data NimaL2DividedTransition
  := nima-divided-transition-is-a3-plus-a3b
  | nima-three-times-divided-transition-is-labelled-transition
  | nima-divided-transition-is-integral-in-target-lattice
#define nima-L2-divided-transition : NimaL2DividedTransition
  := nima-divided-transition-is-integral-in-target-lattice
#data NimaL2DividedTransitionSmithD16
  := nima-divided-D16-full-Bockstein-nonunits-twentyone2-nine6-four12
  | nima-after-divided-transition-twentyone2-eight6-four12
  | nima-saturation-index-divided-by6
#define nima-L2-divided-transition-Smith-D16 : NimaL2DividedTransitionSmithD16
  := nima-saturation-index-divided-by6
#data NimaL2DividedVersusLabelledTransition
  := nima-labelled-threefold-transition-removes-only-order2-part
  | nima-divided-transition-removes-complete-order6-class
  | nima-divided-transition-pairs-log-detector-by-unit
#define nima-L2-divided-versus-labelled-transition
  : NimaL2DividedVersusLabelledTransition
  := nima-divided-transition-removes-complete-order6-class
#data NimaL2IntegralLogCellGate
  := nima-adjoin-one-integral-divided-transition-cell
  | nima-prove-geometric-log-link-authorizes-that-cell
#define nima-L2-integral-log-cell-gate : NimaL2IntegralLogCellGate
  := nima-prove-geometric-log-link-authorizes-that-cell
```
