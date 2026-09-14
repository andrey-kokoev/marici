# Soft D1 labelled derived fibre

```rzk
#lang rzk-1
#data NimaSoftD1LabelledTotalComplex
  := nima-full-gradient-lift-H-plus-C-a-over4-zero-u-over2
  | nima-labelled-total-differential-squares-zero
  | nima-principal-cell-and-source-labels-retained
#define nima-soft-D1-labelled-total-complex : NimaSoftD1LabelledTotalComplex
  := nima-labelled-total-differential-squares-zero
#data NimaSoftD1LocalDerivedFibre
  := nima-even-Tor-object-Cartier-length-two
  | nima-odd-cokernel-object-Cartier-length-one
  | nima-total-local-length-three-reduced-rank-two
#define nima-soft-D1-local-derived-fibre : NimaSoftD1LocalDerivedFibre
  := nima-total-local-length-three-reduced-rank-two
#data NimaSoftD1FibreTypingConstraint
  := nima-singularity-category-alone-insufficient
  | nima-global-quartic-tail-transport-uncomputed
#define nima-soft-D1-fibre-typing-constraint : NimaSoftD1FibreTypingConstraint
  := nima-singularity-category-alone-insufficient
#data NimaSoftD1CompletionProgress
  := nima-local-labelled-derived-fibre-typed
  | nima-global-tail-needed-for-road-Cech-map
#define nima-soft-D1-completion-progress : NimaSoftD1CompletionProgress
  := nima-local-labelled-derived-fibre-typed
```
