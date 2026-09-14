# Canonical plus L2 integral completion at D16

```rzk
#lang rzk-1
#data NimaL2CanonicalRanksD16
  := nima-canonical-rank-gain13
  | nima-canonical-plus-L2-rank-gain14
  | nima-canonical-plus-L2-reaches-full-Bockstein-rational-rank
#define nima-L2-canonical-ranks-D16 : NimaL2CanonicalRanksD16
  := nima-canonical-plus-L2-reaches-full-Bockstein-rational-rank
#data NimaL2CanonicalSmithD16
  := nima-canonical-nonunits-fifteen2-five12
  | nima-canonical-plus-L2-nonunits-fourteen2-one6-five12
#define nima-L2-canonical-Smith-D16 : NimaL2CanonicalSmithD16
  := nima-canonical-plus-L2-nonunits-fourteen2-one6-five12
#data NimaL2IntegralLatticeComparisonD16
  := nima-full-Bockstein-nonunits-twentyone2-nine6-four12
  | nima-same-rational-rank-does-not-imply-same-integral-lattice
  | nima-canonical-generators-not-yet-proved-inside-integral-Bockstein-image
#define nima-L2-integral-lattice-comparison-D16 : NimaL2IntegralLatticeComparisonD16
  := nima-same-rational-rank-does-not-imply-same-integral-lattice
#data NimaL2IntegralCompletionGate
  := nima-compute-inclusions-between-canonical-L2-and-relation-image-lattices
  | nima-Smith-rank-completion-alone-insufficient
#define nima-L2-integral-completion-gate : NimaL2IntegralCompletionGate
  := nima-compute-inclusions-between-canonical-L2-and-relation-image-lattices
```
