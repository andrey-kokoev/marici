# Primitive physical pullback line

```rzk
#lang rzk-1
#data NimaPhysicalPullbackChain
  := nima-chain-ranks-one-four-five-one
  | nima-differential-ranks-one-three-one
  | nima-differential-squares-zero
#define nima-physical-pullback-chain : NimaPhysicalPullbackChain
  := nima-chain-ranks-one-four-five-one

#data NimaPhysicalPullbackIntegralHomology
  := nima-H1-is-Z
  | nima-all-other-homology-zero
  | nima-no-integral-torsion
  | nima-image-lattices-saturated-by-unit-minors
#define nima-physical-pullback-integral-homology
  : NimaPhysicalPullbackIntegralHomology
  := nima-H1-is-Z

#data NimaPhysicalPullbackPrimitive
  := nima-primitive-cycle-one-zero-one-zero-zero
  | nima-primitive-road-augmentation-plus-one
  | nima-positive-sheet-class-is-unique-oriented-line
#define nima-physical-pullback-primitive : NimaPhysicalPullbackPrimitive
  := nima-positive-sheet-class-is-unique-oriented-line

#data NimaPhysicalPullbackSignature
  := nima-loaded-endpoint-parity-even
  | nima-road-and-polarity-reflections-multiply-to-plus-one
  | nima-generic-Q-leg-plus-one
  | nima-Cartier-edge-residue-plus-one
  | nima-both-ordinary-forgetting-shadows-zero
#define nima-physical-pullback-signature : NimaPhysicalPullbackSignature
  := nima-generic-Q-leg-plus-one

#data NimaPostPullbackCoordinateGate
  := nima-evaluate-s-detector-on-primitive-line
  | nima-evaluate-W-detector-on-primitive-line
  | nima-evaluate-v-detector-on-primitive-line
  | nima-prove-supported-image-a-s-plus-b-W-plus-c-v
#define nima-post-pullback-coordinate-gate : NimaPostPullbackCoordinateGate
  := nima-evaluate-s-detector-on-primitive-line
```
