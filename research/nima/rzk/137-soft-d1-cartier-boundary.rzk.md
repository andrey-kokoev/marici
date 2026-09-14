# Soft D1 Cartier boundary

```rzk
#lang rzk-1
#data NimaSoftD1CartierBoundaryOrders
  := nima-boundary-orders-three-four
#define nima-soft-D1-Cartier-boundary-orders : NimaSoftD1CartierBoundaryOrders
  := nima-boundary-orders-three-four
#data NimaSoftD1OddLatticeClass
  := nima-odd-generator-a-t3-b-plus-one
  | nima-normalized-Q-symbol-coefficient-minus-six
#define nima-soft-D1-odd-lattice-class : NimaSoftD1OddLatticeClass
  := nima-normalized-Q-symbol-coefficient-minus-six
#data NimaSoftD1BoundaryMap
  := nima-Q-rational-coefficient-is-unit
  | nima-odd-first-Cartier-map-surjective-at-b-plus-minus-one
  | nima-boundary-cokernel-zero
#define nima-soft-D1-boundary-map : NimaSoftD1BoundaryMap
  := nima-boundary-cokernel-zero
#data NimaSoftD1GlobalSpecializationStatus
  := nima-local-boundary-obstruction-cleared
  | nima-global-specialization-map-not-asserted
#define nima-soft-D1-global-specialization-status
  : NimaSoftD1GlobalSpecializationStatus
  := nima-global-specialization-map-not-asserted
```
