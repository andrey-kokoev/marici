# L2 integral Bockstein Smith presentation at D28

```rzk
#lang rzk-1
#data NimaL2IntegralRelationPresentationD28
  := nima-D28-odd-target210-labelled4420-kernel4265
#define nima-L2-integral-relation-presentation-D28
  : NimaL2IntegralRelationPresentationD28
  := nima-D28-odd-target210-labelled4420-kernel4265
#data NimaL2IntegralBocksteinRanksD28
  := nima-D28-image155-augmented181-gain26
  | nima-D28-gain-matches-modular-beta-rank26
#define nima-L2-integral-Bockstein-ranks-D28 : NimaL2IntegralBocksteinRanksD28
  := nima-D28-gain-matches-modular-beta-rank26
#data NimaL2IntegralBocksteinSmithD28
  := nima-D28-image-has-2-3-5-7-11-13-primary-parts
  | nima-D28-augmented-nonunits-seventyeight2-eighteen6-three12-one24-three48
  | nima-D28-full-Bockstein-support-only-2-and3
  | nima-D28-transition-removes-one-order-two-factor
#define nima-L2-integral-Bockstein-Smith-D28 : NimaL2IntegralBocksteinSmithD28
  := nima-D28-full-Bockstein-support-only-2-and3
#data NimaL2FiveCutoffIntegralConclusion
  := nima-beta-rank-gains-8-14-18-22-26
  | nima-D16-through-D28-match-modular-ranks
  | nima-full-Bockstein-torsion-support-2-3-through-all-cutoffs
  | nima-transition-index-ratio-two-through-all-cutoffs
#define nima-L2-five-cutoff-integral-conclusion : NimaL2FiveCutoffIntegralConclusion
  := nima-full-Bockstein-torsion-support-2-3-through-all-cutoffs
```
