# L2 integral Bockstein Smith presentation at D12

```rzk
#lang rzk-1
#data NimaL2IntegralRelationPresentationD12
  := nima-odd-target-rank42
  | nima-452-labelled-columns
  | nima-saturated-integral-relation-kernel-rank433
#define nima-L2-integral-relation-presentation-D12
  : NimaL2IntegralRelationPresentationD12
  := nima-saturated-integral-relation-kernel-rank433
#data NimaL2IntegralBocksteinRanksD12
  := nima-u0-image-rank19
  | nima-image-plus-Bockstein-rank27
  | nima-integral-Bockstein-rank-gain8
#define nima-L2-integral-Bockstein-ranks-D12 : NimaL2IntegralBocksteinRanksD12
  := nima-integral-Bockstein-rank-gain8
#data NimaL2IntegralBocksteinSmithD12
  := nima-image-nonunits-six2-one6-two12
  | nima-augmented-nonunits-eight2-eight6-one12
#define nima-L2-integral-Bockstein-Smith-D12 : NimaL2IntegralBocksteinSmithD12
  := nima-augmented-nonunits-eight2-eight6-one12
#data NimaL2IntegralSmithScopeD12
  := nima-true-labelled-L2-relation-matrix
  | nima-exact-only-at-D12-so-far
#define nima-L2-integral-Smith-scope-D12 : NimaL2IntegralSmithScopeD12
  := nima-true-labelled-L2-relation-matrix
```
