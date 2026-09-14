# L2 integral Bockstein Smith presentation at D16

```rzk
#lang rzk-1
#data NimaL2IntegralRelationPresentationD16
  := nima-odd-target-rank72
  | nima-1060-labelled-columns
  | nima-integral-relation-kernel-rank1019
#define nima-L2-integral-relation-presentation-D16
  : NimaL2IntegralRelationPresentationD16
  := nima-integral-relation-kernel-rank1019
#data NimaL2IntegralBocksteinRanksD16
  := nima-u0-image-rank41
  | nima-image-plus-Bockstein-rank55
  | nima-integral-Bockstein-rank-gain14
  | nima-rank-gain-matches-modular-beta-rank14
#define nima-L2-integral-Bockstein-ranks-D16 : NimaL2IntegralBocksteinRanksD16
  := nima-rank-gain-matches-modular-beta-rank14
#data NimaL2IntegralBocksteinSmithD16
  := nima-image-nonunits-fifteen2-five12
  | nima-augmented-nonunits-twentyone2-nine6-four12
  | nima-transition-removes-one-order-two-factor
#define nima-L2-integral-Bockstein-Smith-D16 : NimaL2IntegralBocksteinSmithD16
  := nima-transition-removes-one-order-two-factor
#data NimaL2StructuredKernelAlgorithm
  := nima-paired-lattice-row-Hermite-intersection
  | nima-avoids-full-unimodular-transform
#define nima-L2-structured-kernel-algorithm : NimaL2StructuredKernelAlgorithm
  := nima-paired-lattice-row-Hermite-intersection
```
