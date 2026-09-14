# Effective-divisor cubical realization gate

```rzk
#lang rzk-1

#data NimaCubicalDegree
  := nima-cubical-degree-zero
  | nima-cubical-degree-one
  | nima-cubical-degree-two
  | nima-cubical-degree-higher

#data NimaShellMultiplicityScope
  := nima-distinct-shell-directions
  | nima-repeated-labelled-shell-directions
  | nima-unlabelled-repeated-shell-directions

#define nima-effective-divisor-cube-data
  (Points Subsets Directions : U)
  : U
  := Sigma (base : Points),
       Sigma (directions : Directions),
       (Subsets -> Points)

#define nima-source-derived-effective-divisor-cube
  (Points Subsets Directions : U)
  (Effective : Points -> U)
  (CommutingFaces : (Subsets -> Points) -> U)
  : U
  := Sigma
       (cube : nima-effective-divisor-cube-data Points Subsets Directions),
       Sigma (_ : (subset : Subsets) -> Effective ((second (second cube)) subset)),
       CommutingFaces (second (second cube))

#define nima-cubical-chain-realization
  (ExteriorPacket CubicalChain : U)
  (realize : ExteriorPacket -> CubicalChain)
  : U
  := ExteriorPacket -> CubicalChain

#define nima-inhabit-cubical-chain-realization
  (ExteriorPacket CubicalChain : U)
  (realize : ExteriorPacket -> CubicalChain)
  : nima-cubical-chain-realization ExteriorPacket CubicalChain realize
  := realize

#data NimaEffectiveDivisorRealizationResult
  := nima-degree-one-shell-is-an-edge
  | nima-two-distinct-shells-form-a-square
  | nima-distinct-exterior-degree-matches-cubical-degree
  | nima-cubical-boundary-is-partial-Koszul-boundary
  | nima-canonical-attachment-is-contractible
  | nima-noncanonical-relative-class-need-not-persist

#define nima-new-source-derived-realization
  : NimaEffectiveDivisorRealizationResult
  := nima-distinct-exterior-degree-matches-cubical-degree

#data NimaEffectiveDivisorRealizationLimit
  := nima-repeated-shell-requires-labelled-chips-or-divided-powers
  | nima-cube-filler-does-not-supply-ringed-support-map
  | nima-relative-homology-does-not-imply-persistent-class
  | nima-cellular-realization-does-not-imply-six-functor-realization
  | nima-cubical-coordinate-count-does-not-imply-independent-detectors

#define nima-first-effective-divisor-limit
  : NimaEffectiveDivisorRealizationLimit
  := nima-repeated-shell-requires-labelled-chips-or-divided-powers

#define nima-geometric-connector-limit-after-cubical-upgrade
  : NimaEffectiveDivisorRealizationLimit
  := nima-cube-filler-does-not-supply-ringed-support-map

#data NimaAmplitudePacketCubicalDisposition
  := nima-cellular-three-direction-carrier-candidate
  | nima-three-independent-target-detectors-not-derived
  | nima-ringed-amplitude-realization-still-open

#define nima-amplitude-packet-after-cubical-upgrade
  : NimaAmplitudePacketCubicalDisposition
  := nima-ringed-amplitude-realization-still-open
```
