# W survival and physical transport split

```rzk
#lang rzk-1
#data NimaWNativeSurvival
  := nima-W-decomposable-term-nonzero-in-native-algebra
  | nima-reflection-action-nonzero-at-endpoint
#define nima-W-native-survival : NimaWNativeSurvival
  := nima-W-decomposable-term-nonzero-in-native-algebra
#data NimaWEndpointSurvival
  := nima-comparison-fibre-endpoint-class-retained
  | nima-endpoint-integral-detector-nonzero
  | nima-primitive-endpoint-orientation-fixed
#define nima-W-endpoint-survival : NimaWEndpointSurvival
  := nima-comparison-fibre-endpoint-class-retained
#data NimaWPhysicalSurvivalGate
  := nima-physical-collar-Verdier-identification-required
  | nima-conormal-readout-must-not-annihilate-W
  | nima-native-nonzero-does-not-alone-imply-physical-nonzero
#define nima-W-physical-survival-gate : NimaWPhysicalSurvivalGate
  := nima-conormal-readout-must-not-annihilate-W
#data NimaWTransportReduction
  := nima-only-nonannihilating-endpoint-to-physical-map-remains
#define nima-W-transport-reduction : NimaWTransportReduction
  := nima-only-nonannihilating-endpoint-to-physical-map-remains
```
