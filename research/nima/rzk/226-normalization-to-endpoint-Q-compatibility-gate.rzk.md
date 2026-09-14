# Normalization to endpoint-Q compatibility gate

```rzk
#lang rzk-1
#data NimaEndpointQTargetConnector
  := nima-target-ring-has18-labelled-Laurent-generators
  | nima-omega-has-explicit-endpoint-connector
  | nima-W-has-six-term-endpoint-correction
#define nima-endpoint-Q-target-connector : NimaEndpointQTargetConnector
  := nima-omega-has-explicit-endpoint-connector
#data NimaRamifiedNormalizationSource
  := nima-source-ring-Q-p-kappa-d-over-d-squared-Delta
  | nima-source-odd-generator-is-d-over16p4
#define nima-ramified-normalization-source : NimaRamifiedNormalizationSource
  := nima-source-odd-generator-is-d-over16p4
#data NimaConnectorCompatibilityResidual
  := nima-no-map-from18-labelled-Rees-generators-to-p-kappa-d
  | nima-no-cell-map-from-ramified-branch-pair-to-K6-endpoint-cells
  | nima-equal-odd-character-does-not-supply-either-map
#define nima-connector-compatibility-residual : NimaConnectorCompatibilityResidual
  := nima-no-map-from18-labelled-Rees-generators-to-p-kappa-d
#data NimaConnectorReopeningTest
  := nima-define-labelled-coefficient-ring-map
  | nima-map-endpoint-and-conductor-branches-to-Vplus-and-Vminus
  | nima-prove-differential-and-endpoint-connector-square
#define nima-connector-reopening-test : NimaConnectorReopeningTest
  := nima-define-labelled-coefficient-ring-map
```
