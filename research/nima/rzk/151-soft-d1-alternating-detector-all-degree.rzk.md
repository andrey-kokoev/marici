# Soft D1 alternating detector in all degrees

```rzk
#lang rzk-1
#data NimaSoftD1AllDegreeAnnihilation
  := nima-p-columns-have-positive-a-order
  | nima-q-derivative-columns-have-positive-a-order
  | nima-q-zero-a-order-case-has-one-plus-b-factor
  | nima-a2-completion-has-positive-a-order
#define nima-soft-D1-all-degree-annihilation : NimaSoftD1AllDegreeAnnihilation
  := nima-q-zero-a-order-case-has-one-plus-b-factor
#data NimaSoftD1AllDegreePrimitivity
  := nima-alternating-detector-of-unit-is-one
#define nima-soft-D1-all-degree-primitivity : NimaSoftD1AllDegreePrimitivity
  := nima-alternating-detector-of-unit-is-one
#data NimaSoftD1RationalCokernelGeneration
  := nima-q11-i0-columns-span-seven-times-one-plus-b-ideal
  | nima-over-Q-they-span-one-plus-b-ideal
  | nima-evaluation-at-b-minus-one-is-rank-one-quotient
#define nima-soft-D1-rational-cokernel-generation
  : NimaSoftD1RationalCokernelGeneration
  := nima-evaluation-at-b-minus-one-is-rank-one-quotient
#data NimaSoftD1AllDegreeDetectorConclusion
  := nima-primitive-free-cokernel-rank-one-in-all-degrees
  | nima-integral-torsion-cokernel-remains-separate
#define nima-soft-D1-all-degree-detector-conclusion
  : NimaSoftD1AllDegreeDetectorConclusion
  := nima-primitive-free-cokernel-rank-one-in-all-degrees
```
