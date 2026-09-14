# Three supported detector coordinates

The three amplitude coordinates are assembled from explicit primary,
reciprocal, and relation detectors, matching the jointly detecting frame in the
Cubical Agda interface.  A residue law for these detectors yields the supported
factorization and hence the physical amplitude bridge.

```rzk
#lang rzk-1

#define nima-three-supported-detectors
  (Supported : U) : U
  := Sigma (primary : Supported -> MariciInt),
       Sigma (reciprocal : Supported -> MariciInt),
         Supported -> MariciInt

#define nima-supported-primary-detector
  (Supported : U) (detectors : nima-three-supported-detectors Supported)
  : Supported -> MariciInt
  := first detectors

#define nima-supported-reciprocal-detector
  (Supported : U) (detectors : nima-three-supported-detectors Supported)
  : Supported -> MariciInt
  := first (second detectors)

#define nima-supported-relation-detector
  (Supported : U) (detectors : nima-three-supported-detectors Supported)
  : Supported -> MariciInt
  := second (second detectors)

#define nima-three-detector-coordinate-map
  (Supported : U) (detectors : nima-three-supported-detectors Supported)
  : Supported -> nima-amplitude-coordinates
  := \ s ->
       (nima-supported-primary-detector Supported detectors s,
        (nima-supported-reciprocal-detector Supported detectors s,
         nima-supported-relation-detector Supported detectors s))

#define nima-three-detector-residue-law
  (Supported : U) (beta : MariciInt)
  (residue : Supported -> MariciInt)
  (detectors : nima-three-supported-detectors Supported)
  : U
  := (s : Supported) -> residue s
       = nima-calibrated-coordinate-amplitude beta
          (nima-three-detector-coordinate-map Supported detectors s)

#define nima-three-detectors-to-supported-factorization
  (Supported : U) (beta : MariciInt)
  (residue : Supported -> MariciInt)
  (detectors : nima-three-supported-detectors Supported)
  (law : nima-three-detector-residue-law Supported beta residue detectors)
  : nima-supported-residue-coordinate-factorization Supported beta residue
  := (nima-three-detector-coordinate-map Supported detectors, law)

#define nima-three-detectors-to-physical-amplitude-bridge
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (detectors : nima-three-supported-detectors Supported)
  (law : nima-three-detector-residue-law Supported beta residue detectors)
  : nima-physical-coefficient-amplitude-bridge
      Physical Supported beta gysin residue
  := nima-supported-factorization-to-physical-bridge
       Physical Supported beta gysin residue
       (nima-three-detectors-to-supported-factorization
         Supported beta residue detectors law)

#define nima-coordinate-model-three-detectors
  : nima-three-supported-detectors nima-amplitude-coordinates
  := (nima-amplitude-coordinate-a,
      (nima-amplitude-coordinate-b, nima-amplitude-coordinate-c))

#define nima-coordinate-model-three-detector-law
  (beta : MariciInt)
  : nima-three-detector-residue-law nima-amplitude-coordinates beta
      (nima-coefficient-model-residue beta)
      nima-coordinate-model-three-detectors
  := \ x -> refl

#define nima-coordinate-detectors-induce-canonical-bridge
  (beta : MariciInt)
  : nima-three-detectors-to-physical-amplitude-bridge
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
      nima-coordinate-model-three-detectors
      (nima-coordinate-model-three-detector-law beta)
    = nima-coefficient-model-amplitude-bridge beta
  := refl

#data NimaThreeDetectorPhysicalGate
  := nima-primary-reciprocal-relation-functionals-required
  | nima-joint-detection-not-yet-residue-formula
  | nima-detector-residue-law-required
#define nima-three-detector-physical-gate : NimaThreeDetectorPhysicalGate
  := nima-primary-reciprocal-relation-functionals-required
```
