# Canonical-L2 and relation-image lattice incomparability at D20

```rzk
#lang rzk-1
#data NimaL2CanonicalCompletionD20
  := nima-D20-canonical-gain17-plus-L2-gain18
  | nima-D20-canonical-plus-L2-reaches-full-rational-rank
  | nima-D20-canonical-plus-L2-nonunits-twentysix2-seven12-one24-one840
#define nima-L2-canonical-completion-D20 : NimaL2CanonicalCompletionD20
  := nima-D20-canonical-plus-L2-reaches-full-rational-rank
#data NimaL2SumLatticeSmithD20
  := nima-D20-sum-nonunits-thirtyone2-two4-one8-one24
#define nima-L2-sum-lattice-Smith-D20 : NimaL2SumLatticeSmithD20
  := nima-D20-sum-nonunits-thirtyone2-two4-one8-one24
#data NimaL2LatticeSumIndicesD20
  := nima-D20-sum-over-canonical-L2-index-2pow5-3pow8-5-7
  | nima-D20-sum-over-full-Bockstein-index-2pow20-3pow16
#define nima-L2-lattice-sum-indices-D20 : NimaL2LatticeSumIndicesD20
  := nima-D20-sum-over-canonical-L2-index-2pow5-3pow8-5-7
#data NimaL2LatticeContainmentD20
  := nima-D20-lattices-incomparable
  | nima-sum-removes-canonical-5-and7-primary-obstructions
#define nima-L2-lattice-containment-D20 : NimaL2LatticeContainmentD20
  := nima-D20-lattices-incomparable
```
