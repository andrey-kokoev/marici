# L2 relation-lattice localization

```rzk
#lang rzk-1
#data NimaL2RelationLatticeExactCutoffs
  := nima-exact-D12-D16-D20-D24-D28
  | nima-rank-gains-8-14-18-22-26
#define nima-L2-relation-lattice-exact-cutoffs : NimaL2RelationLatticeExactCutoffs
  := nima-rank-gains-8-14-18-22-26
#data NimaL2RelationLatticePrimeSupport
  := nima-full-Bockstein-nonunits-have-only-primes2-and3
  | nima-distinguished-transition-index-two-through-all-cutoffs
#define nima-L2-relation-lattice-prime-support : NimaL2RelationLatticePrimeSupport
  := nima-full-Bockstein-nonunits-have-only-primes2-and3
#data NimaL2TestedLocalizationConclusion
  := nima-invert6-saturates-full-relation-image-at-five-cutoffs
  | nima-no-larger-prime-localization-needed-for-relation-lattice
#define nima-L2-tested-localization-conclusion : NimaL2TestedLocalizationConclusion
  := nima-invert6-saturates-full-relation-image-at-five-cutoffs
#data NimaL2LocalizationScope
  := nima-not-all-degree-saturation-theorem
  | nima-not-integral-road-Cech-map
#define nima-L2-localization-scope : NimaL2LocalizationScope
  := nima-not-all-degree-saturation-theorem
```
