# Distinguished L2 transition integral effect at D12

```rzk
#lang rzk-1
#data NimaL2DistinguishedTransitionD12
  := nima-transition-is-3a3-plus-3a3b
  | nima-transition-adds-no-rational-rank-at-D12
  | nima-transition-kills-order-two-torsion-class
#define nima-L2-distinguished-transition-D12 : NimaL2DistinguishedTransitionD12
  := nima-transition-kills-order-two-torsion-class
#data NimaL2SmithBeforeTransitionD12
  := nima-nonunits-eight2-eight6-one12
#define nima-L2-Smith-before-transition-D12 : NimaL2SmithBeforeTransitionD12
  := nima-nonunits-eight2-eight6-one12
#data NimaL2SmithAfterTransitionD12
  := nima-nonunits-seven2-eight6-one12
  | nima-saturation-index-divided-by-two
#define nima-L2-Smith-after-transition-D12 : NimaL2SmithAfterTransitionD12
  := nima-saturation-index-divided-by-two
#data NimaL2D16ComputationStatus
  := nima-direct-saturated-Hermite-computation-timed-out
  | nima-structured-kernel-reduction-required
#define nima-L2-D16-computation-status : NimaL2D16ComputationStatus
  := nima-structured-kernel-reduction-required
```
