# Finite-packet scattering amplitude certificate

```rzk
#lang rzk-1

#define nima-finite-packet-amplitude-certificate
  (Incoming Outgoing Feature Scalars : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  : U
  := Sigma (scatter : Incoming -> Outgoing),
       Sigma (transition : Feature -> Feature),
       Sigma (_ : (x : Incoming) ->
         transition (incoming-feature x) = outgoing-feature (scatter x)),
       pairing (outgoing-feature selected-outgoing)
         (incoming-feature selected-incoming) = normalization

#define nima-finite-packet-transition
  (Incoming Outgoing Feature Scalars : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  (certificate : nima-finite-packet-amplitude-certificate
    Incoming Outgoing Feature Scalars incoming-feature outgoing-feature
    pairing selected-incoming selected-outgoing normalization)
  : Feature -> Feature
  := first (second certificate)

#define nima-finite-packet-selected-amplitude
  (Incoming Outgoing Feature Scalars : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  : Scalars
  := pairing (outgoing-feature selected-outgoing)
       (incoming-feature selected-incoming)

#define nima-finite-packet-amplitude-normalized
  (Incoming Outgoing Feature Scalars : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  (certificate : nima-finite-packet-amplitude-certificate
    Incoming Outgoing Feature Scalars incoming-feature outgoing-feature
    pairing selected-incoming selected-outgoing normalization)
  : nima-finite-packet-selected-amplitude Incoming Outgoing Feature Scalars
      incoming-feature outgoing-feature pairing selected-incoming
      selected-outgoing = normalization
  := second (second (second certificate))

#define nima-packet-restriction-compatible
  (Small Large FeatureSmall FeatureLarge : U)
  (include-state : Small -> Large)
  (include-feature : FeatureSmall -> FeatureLarge)
  (small-feature : Small -> FeatureSmall)
  (large-feature : Large -> FeatureLarge)
  : U
  := (x : Small) ->
       include-feature (small-feature x) = large-feature (include-state x)

#define nima-transition-restriction-compatible
  (FeatureSmall FeatureLarge : U)
  (include-feature : FeatureSmall -> FeatureLarge)
  (small-transition : FeatureSmall -> FeatureSmall)
  (large-transition : FeatureLarge -> FeatureLarge)
  : U
  := (x : FeatureSmall) ->
       include-feature (small-transition x)
       = large-transition (include-feature x)

#define nima-two-rung-amplitude-system
  (Small Large FeatureSmall FeatureLarge : U)
  (include-state : Small -> Large)
  (include-feature : FeatureSmall -> FeatureLarge)
  (small-incoming : Small -> FeatureSmall)
  (large-incoming-feature : Large -> FeatureLarge)
  (small-transition : FeatureSmall -> FeatureSmall)
  (large-transition : FeatureLarge -> FeatureLarge)
  : U
  := Sigma (_ : nima-packet-restriction-compatible
       Small Large FeatureSmall FeatureLarge include-state include-feature
       small-incoming large-incoming-feature),
       nima-transition-restriction-compatible FeatureSmall FeatureLarge
         include-feature small-transition large-transition

#define nima-finite-contraction-witness
  (Feature Bound : U)
  (transition : Feature -> Feature)
  (norm-bound : (Feature -> Feature) -> Bound)
  (one : Bound)
  (at-most : Bound -> Bound -> U)
  : U
  := at-most (norm-bound transition) one

#define nima-certified-finite-amplitude-data
  (Incoming Outgoing Feature Scalars Bound : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  (norm-bound : (Feature -> Feature) -> Bound)
  (one : Bound)
  (at-most : Bound -> Bound -> U)
  : U
  := Sigma (certificate : nima-finite-packet-amplitude-certificate
       Incoming Outgoing Feature Scalars incoming-feature outgoing-feature
       pairing selected-incoming selected-outgoing normalization),
       nima-finite-contraction-witness Feature Bound
         (first (second certificate)) norm-bound one at-most

#define nima-assemble-certified-finite-amplitude
  (Incoming Outgoing Feature Scalars Bound : U)
  (incoming-feature : Incoming -> Feature)
  (outgoing-feature : Outgoing -> Feature)
  (pairing : Feature -> Feature -> Scalars)
  (selected-incoming : Incoming)
  (selected-outgoing : Outgoing)
  (normalization : Scalars)
  (norm-bound : (Feature -> Feature) -> Bound)
  (one : Bound)
  (at-most : Bound -> Bound -> U)
  (certificate : nima-finite-packet-amplitude-certificate
    Incoming Outgoing Feature Scalars incoming-feature outgoing-feature
    pairing selected-incoming selected-outgoing normalization)
  (contraction : nima-finite-contraction-witness Feature Bound
    (first (second certificate)) norm-bound one at-most)
  : nima-certified-finite-amplitude-data Incoming Outgoing Feature Scalars
      Bound incoming-feature outgoing-feature pairing selected-incoming
      selected-outgoing normalization norm-bound one at-most
  := (certificate, contraction)

#data NimaFinitePacketAmplitudeEvidence
  := nima-source-incoming-and-outgoing-features-fixed
  | nima-six-point-Gram-positive-definite
  | nima-six-point-Douglas-contraction-certified
  | nima-prefix-restriction-compatible-through-rung-six
  | nima-four-independent-six-point-families-certified
  | nima-three-independent-eight-point-towers-certified
  | nima-three-independent-ten-point-towers-certified
  | nima-three-independent-sixteen-point-towers-certified
  | nima-three-independent-twentyfour-point-towers-certified
  | nima-three-independent-fortyeight-point-towers-certified
  | nima-physical-ninety-two-span-awaits-final-interval-certificate

#define nima-current-finite-packet-amplitude-evidence
  : NimaFinitePacketAmplitudeEvidence
  := nima-three-independent-fortyeight-point-towers-certified

#data NimaFinitePacketAmplitudeBoundary
  := nima-one-nested-six-point-family-only
  | nima-no-arbitrary-packet-contraction
  | nima-no-completed-Hilbert-amplitude
  | nima-no-gluing-factorization-yet
  | nima-floating-ninety-two-span-not-certified

#define nima-current-finite-packet-amplitude-boundary
  : NimaFinitePacketAmplitudeBoundary
  := nima-no-arbitrary-packet-contraction
```
