# Normalization pullback and endpoint-extension obstruction

```rzk
#lang rzk-1

#data NimaNormalizationResidue14
  := nima-normalization-old-residue
       (residue : NimaLiftOverlapResidue12)
  | nima-normalization-positive-endpoint-triple-pole
  | nima-normalization-negative-endpoint-triple-pole

#data NimaNormalizationPullbackSource
  := nima-normalization-source-12
  | nima-normalization-source-14
#data NimaNormalizationComparisonTarget
  := nima-endpoint-quotient-E
  | nima-full-215-state-FK
#define nima-normalization-comparison-target
  : NimaNormalizationPullbackSource -> NimaNormalizationComparisonTarget
  := \ source -> match source
       (nima-normalization-source-12 => nima-endpoint-quotient-E
       | nima-normalization-source-14 => nima-full-215-state-FK)

#data NimaEndpointExtensionNormalProduct9
  := nima-normal-product-13-02 | nima-normal-product-13-24
  | nima-normal-product-13-04 | nima-normal-product-35-02
  | nima-normal-product-35-24 | nima-normal-product-35-04
  | nima-normal-product-15-02 | nima-normal-product-15-24
  | nima-normal-product-15-04

#data NimaEndpointExtensionStatus
  := nima-endpoint-extension-nonsplit
  | nima-endpoint-extension-split
#define nima-endpoint-extension-status : NimaEndpointExtensionStatus
  := nima-endpoint-extension-nonsplit

#data NimaEndpointExtensionAnnihilatorGenerator
  := nima-endpoint-annihilator-positive-occurrence-tail
  | nima-endpoint-annihilator-negative-occurrence-tail
  | nima-endpoint-annihilator-normal-product
       (product : NimaEndpointExtensionNormalProduct9)

#data NimaEndpointMultipleLiftStatus
  := nima-normal-product-multiple-has-endpoint-preserving-lift
#define nima-endpoint-normal-product-lift
  : NimaEndpointExtensionNormalProduct9 -> NimaEndpointMultipleLiftStatus
  := \ product -> nima-normal-product-multiple-has-endpoint-preserving-lift

#data NimaEndpointTriplePoleDetector2
  := nima-positive-endpoint-first-pole-detector
  | nima-negative-endpoint-first-pole-detector
#define nima-endpoint-triple-pole-value
  : NimaEndpointTriplePoleDetector2 -> MariciInt
  := \ detector -> marici-int-one
#define nima-positive-endpoint-triple-pole-is-primitive
  : nima-endpoint-triple-pole-value
      nima-positive-endpoint-first-pole-detector = marici-int-one
  := refl
#define nima-negative-endpoint-triple-pole-is-primitive
  : nima-endpoint-triple-pole-value
      nima-negative-endpoint-first-pole-detector = marici-int-one
  := refl

#data NimaNormalizationSourceProvenance
  := nima-target-residue-selected-normalization-source
  | nima-native-physical-source
#define nima-constructed-normalization-source-provenance
  : NimaNormalizationSourceProvenance
  := nima-target-residue-selected-normalization-source
```
