# L2 integral Bockstein Smith presentation at D20

```rzk
#lang rzk-1
#data NimaL2IntegralRelationPresentationD20
  := nima-odd-target-rank110
  | nima-1924-labelled-columns
  | nima-integral-relation-kernel-rank1853
#define nima-L2-integral-relation-presentation-D20
  : NimaL2IntegralRelationPresentationD20
  := nima-integral-relation-kernel-rank1853
#data NimaL2IntegralBocksteinRanksD20
  := nima-u0-image-rank71
  | nima-image-plus-Bockstein-rank89
  | nima-integral-Bockstein-rank-gain18
  | nima-rank-gain-matches-modular-beta-rank18
#define nima-L2-integral-Bockstein-ranks-D20 : NimaL2IntegralBocksteinRanksD20
  := nima-rank-gain-matches-modular-beta-rank18
#data NimaL2IntegralBocksteinSmithD20
  := nima-image-nonunits-twentysix2-one4-six12-one24-one840
  | nima-augmented-nonunits-thirtysix2-twelve6-two12-three24
  | nima-Bockstein-removes-5-and-7-primary-factors
  | nima-D20-transition-removes-one-order-two-factor
#define nima-L2-integral-Bockstein-Smith-D20 : NimaL2IntegralBocksteinSmithD20
  := nima-Bockstein-removes-5-and-7-primary-factors
#data NimaL2TransitionStableIntegralEffect
  := nima-transition-index-ratio-two-at-D12-D16-D20
#define nima-L2-transition-stable-integral-effect : NimaL2TransitionStableIntegralEffect
  := nima-transition-index-ratio-two-at-D12-D16-D20
```
