# Smith augmentation provenance correction

```rzk
#lang rzk-1
#data NimaIntegralSmithActualAugmentation
  := nima-plus-exact-image-augmented-by-a2-times-image-columns
#define nima-integral-Smith-actual-augmentation : NimaIntegralSmithActualAugmentation
  := nima-plus-exact-image-augmented-by-a2-times-image-columns
#data NimaIntegralSmithMissingIdentification
  := nima-no-labelled-s11-column-in-Smith-checker
  | nima-no-L2-Bockstein-transition-matrix-in-Smith-checker
  | nima-a2-product-equals-L2-transition-not-proved
#define nima-integral-Smith-missing-identification : NimaIntegralSmithMissingIdentification
  := nima-a2-product-equals-L2-transition-not-proved
#data NimaIntegralSmithClaimCorrection
  := nima-D12-through-D28-Smith-data-apply-to-Cartier-a2-augmentation
  | nima-integral-L2-Smith-presentation-remains-open
  | nima-prime-support-cannot-yet-be-ascribed-to-L2
#define nima-integral-Smith-claim-correction : NimaIntegralSmithClaimCorrection
  := nima-integral-L2-Smith-presentation-remains-open
```
