# Pullback detector lattice does not identify three target detectors

```rzk
#lang rzk-1
#data NimaPhysicalPullbackInternalDetector
  := nima-endpoint-row-one-minus-one-zero-zero-zero
  | nima-road-row-zero-zero-one-one-one
  | nima-their-difference-is-d1-coboundary
  | nima-internal-dual-H1-is-one-primitive-line
#define nima-physical-pullback-internal-detector
  : NimaPhysicalPullbackInternalDetector
  := nima-internal-dual-H1-is-one-primitive-line

#data NimaTargetDetectorTypingDistinction
  := nima-s-detector-lives-on-generic-Q-target
  | nima-W-detector-lives-on-paired-endpoint-target
  | nima-v-detector-lives-on-road-relation-target
  | nima-target-detectors-not-definitionally-pullback-rows
#define nima-target-detector-typing-distinction
  : NimaTargetDetectorTypingDistinction
  := nima-target-detectors-not-definitionally-pullback-rows

#data NimaPrimitiveSignatureInsufficiency
  := nima-generic-Q-unit-does-not-identify-s-coefficient
  | nima-endpoint-swap-does-not-identify-W-coefficient
  | nima-road-unit-does-not-identify-v-coefficient
  | nima-three-unit-signatures-do-not-prove-packet-one-one-one
#define nima-primitive-signature-insufficiency
  : NimaPrimitiveSignatureInsufficiency
  := nima-three-unit-signatures-do-not-prove-packet-one-one-one

#data NimaTargetDetectorDescentGate
  := nima-construct-target-to-pullback-primary-cochain
  | nima-construct-target-to-pullback-reciprocal-cochain
  | nima-construct-target-to-pullback-relation-cochain
  | nima-prove-three-cochains-annihilate-pullback-boundaries
  | nima-evaluate-three-cochains-on-primitive-z
#define nima-target-detector-descent-gate : NimaTargetDetectorDescentGate
  := nima-construct-target-to-pullback-primary-cochain

#define nima-three-coordinate-packet
  (Packet Scalar : U)
  (add : Packet -> Packet -> Packet)
  (scale : Scalar -> Packet -> Packet)
  (s W v : Packet)
  (a b c : Scalar)
  : Packet
  := add (scale a s) (add (scale b W) (scale c v))

#data NimaPhysicalPacketComparisonStatus
  := nima-source-internal-detector-lattice-computed
  | nima-cross-target-detector-cochains-still-required
  | nima-a-b-c-packet-image-not-yet-inhabited
#define nima-physical-packet-comparison-status
  : NimaPhysicalPacketComparisonStatus
  := nima-cross-target-detector-cochains-still-required
```
