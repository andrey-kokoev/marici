# Soft D1 primitive free-cokernel detector

```rzk
#lang rzk-1
#data NimaSoftD1FreeCokernelDetector
  := nima-alternating-evaluation-on-a-zero-monomials
#define nima-soft-D1-free-cokernel-detector : NimaSoftD1FreeCokernelDetector
  := nima-alternating-evaluation-on-a-zero-monomials
#data NimaSoftD1DetectorFormula
  := nima-sum-over-b-of-minus-one-pow-b-times-coefficient-u0-a0-b
#define nima-soft-D1-detector-formula : NimaSoftD1DetectorFormula
  := nima-sum-over-b-of-minus-one-pow-b-times-coefficient-u0-a0-b
#data NimaSoftD1DetectorVerification
  := nima-primitive-left-nullvector-after-L2-at-D12-16-20-24-28
  | nima-free-cokernel-rank-one-at-all-five-cutoffs
#define nima-soft-D1-detector-verification : NimaSoftD1DetectorVerification
  := nima-primitive-left-nullvector-after-L2-at-D12-16-20-24-28
#data NimaSoftD1DetectorConsequence
  := nima-L2-cannot-remove-free-alternating-boundary-class
  | nima-global-extension-must-hit-detector-with-unit
  | nima-formula-invites-direct-all-degree-proof
#define nima-soft-D1-detector-consequence : NimaSoftD1DetectorConsequence
  := nima-global-extension-must-hit-detector-with-unit
```
