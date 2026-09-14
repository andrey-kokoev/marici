# Soft D1 quartic-tail gate

```rzk
#lang rzk-1
#data NimaSoftD1MinusQuarticTail
  := nima-restored-conormal-a7-times-two-minus-c
  | nima-minus-residue-two-a7-exact
  | nima-no-new-minus-boundary-class
#define nima-soft-D1-minus-quartic-tail : NimaSoftD1MinusQuarticTail
  := nima-minus-residue-two-a7-exact
#data NimaSoftD1PlusQuarticTail
  := nima-a2-does-not-preserve-exact-image
  | nima-stable-plus-defect-rank-one
  | nima-Smith-over-Aplus-undefined
#define nima-soft-D1-plus-quartic-tail : NimaSoftD1PlusQuarticTail
  := nima-stable-plus-defect-rank-one
#data NimaSoftD1GlobalTailDecision
  := nima-minus-tail-closes
  | nima-plus-tail-requires-defect-extension
  | nima-global-road-Cech-map-not-yet-closed
#define nima-soft-D1-global-tail-decision : NimaSoftD1GlobalTailDecision
  := nima-plus-tail-requires-defect-extension
```
