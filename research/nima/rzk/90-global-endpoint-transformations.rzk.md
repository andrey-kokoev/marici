# Global endpoint transformations

```rzk
#lang rzk-1
#data NimaGlobalEndpointTransformationGenerator
  := nima-nine-normal-row-relations
  | nima-twenty-one-occurrence-tail-maps
#data NimaSupportedJetGlobalizationStatus
  := nima-seven-generator-jet-obstruction-module
  | nima-constant-doubleton-corrections-do-not-globalize
#define nima-supported-jet-globalization-status
  : NimaSupportedJetGlobalizationStatus
  := nima-constant-doubleton-corrections-do-not-globalize
#data NimaDerivedNormalRestrictionClass
  := nima-normal-restriction-Tor1-rank-3
  | nima-normal-restriction-Tor2-rank-1
#data NimaEndpointTransformationFraming
  := nima-extension-and-generic-arrow-fixed
  | nima-full-215-state-map-not-pointwise-fixed
#define nima-endpoint-transformation-framing : NimaEndpointTransformationFraming
  := nima-extension-and-generic-arrow-fixed
```
