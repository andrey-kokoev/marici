# Canonical-L2 and relation-image lattice incomparability at D16

```rzk
#lang rzk-1
#data NimaL2SumLatticeSmithD16
  := nima-sum-nonunits-seventeen2-two4-one12
  | nima-sum-index-2pow23-times3
#define nima-L2-sum-lattice-Smith-D16 : NimaL2SumLatticeSmithD16
  := nima-sum-nonunits-seventeen2-two4-one12
#data NimaL2LatticeSumIndicesD16
  := nima-sum-over-canonical-L2-index-2pow2-times3pow5
  | nima-sum-over-full-Bockstein-index-2pow15-times3pow12
#define nima-L2-lattice-sum-indices-D16 : NimaL2LatticeSumIndicesD16
  := nima-sum-over-canonical-L2-index-2pow2-times3pow5
#data NimaL2LatticeContainmentD16
  := nima-canonical-L2-not-contained-in-relation-image
  | nima-relation-image-not-contained-in-canonical-L2
  | nima-lattices-commensurable-but-incomparable
#define nima-L2-lattice-containment-D16 : NimaL2LatticeContainmentD16
  := nima-lattices-commensurable-but-incomparable
#data NimaL2IntegralComparisonRequirement
  := nima-requires-explicit-two-and-three-primary-saturation-maps
  | nima-rational-rank-equality-cannot-close-integral-road-map
#define nima-L2-integral-comparison-requirement : NimaL2IntegralComparisonRequirement
  := nima-requires-explicit-two-and-three-primary-saturation-maps
```
