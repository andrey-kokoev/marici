# Native excess, punctured blocks, and reciprocal trace

```rzk
#lang rzk-1
#data NimaNativeExcessTransport
  := nima-independent-eta-preserved-with-unit-coefficient
  | nima-six-first-conormal-channels-primitive
  | nima-eight-higher-wedge-images-in-proper-Rees-ideals
#data NimaNativeExcessCentralFace
  := nima-six-first-conormal-channels-survive
  | nima-eight-higher-wedge-images-vanish
#define nima-native-excess-central-face : NimaNativeExcessCentralFace
  := nima-six-first-conormal-channels-survive
#data NimaNativeExcessIdentificationGate
  := nima-ordinary-unit-top-identification-space-acyclic
#define nima-native-excess-identification-gate : NimaNativeExcessIdentificationGate
  := nima-ordinary-unit-top-identification-space-acyclic
#data NimaPuncturedBlockStatus
  := nima-128-punctured-terms-decompose-into-20-blocks
  | nima-endpoint-blocks-link-obstruction-and-residue
  | nima-intrinsic-third-differential-cancels-Tor-towers
#data NimaPuncturedDualityStatus
  := nima-completed-affine-dual-kills-punctured-complex
  | nima-chart-local-punctured-dual-nonzero
#define nima-punctured-duality-status : NimaPuncturedDualityStatus
  := nima-completed-affine-dual-kills-punctured-complex
#data NimaW03ReciprocalTrace
  := nima-reciprocal-currying-chain-isomorphism
  | nima-two-primitive-independent-excess-traces
  | nima-excess-deletion-detected
#define nima-W03-reciprocal-trace : NimaW03ReciprocalTrace
  := nima-two-primitive-independent-excess-traces
#data NimaExcessPhysicalStatus
  := nima-excess-data-does-not-select-physical-Delta-J
#define nima-excess-physical-status : NimaExcessPhysicalStatus
  := nima-excess-data-does-not-select-physical-Delta-J
```
