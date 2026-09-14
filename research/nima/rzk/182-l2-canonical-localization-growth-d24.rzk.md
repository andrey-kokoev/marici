# Canonical-L2 localization growth through D24

```rzk
#lang rzk-1
#data NimaL2CanonicalCompletionD24
  := nima-D24-canonical-gain21-plus-L2-gain22
  | nima-D24-canonical-plus-L2-reaches-full-rational-rank
#define nima-L2-canonical-completion-D24 : NimaL2CanonicalCompletionD24
  := nima-D24-canonical-plus-L2-reaches-full-rational-rank
#data NimaL2SumLatticeSmithD24
  := nima-D24-sum-nonunits-fortynine2-five12
#define nima-L2-sum-lattice-Smith-D24 : NimaL2SumLatticeSmithD24
  := nima-D24-sum-nonunits-fortynine2-five12
#data NimaL2LatticeSumIndicesD24
  := nima-D24-sum-over-canonical-index-2pow11-3pow12-5pow3-7-11
  | nima-D24-sum-over-relation-index-2pow23-3pow20
#define nima-L2-lattice-sum-indices-D24 : NimaL2LatticeSumIndicesD24
  := nima-D24-sum-over-canonical-index-2pow11-3pow12-5pow3-7-11
#data NimaL2CanonicalLocalizationGrowth
  := nima-D16-comparison-primes-2-3
  | nima-D20-adds-5-7
  | nima-D24-adds-11
  | nima-no-uniform-finite-localization-supported
#define nima-L2-canonical-localization-growth : NimaL2CanonicalLocalizationGrowth
  := nima-no-uniform-finite-localization-supported
```
