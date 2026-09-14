# Supported residue coordinate factorization

Full equivalence with the three-coordinate model is unnecessary.  It suffices
that the supported residue factors through three amplitude coordinates.  This
weaker and more realistic datum already constructs the physical amplitude
bridge.

```rzk
#lang rzk-1

#define nima-supported-residue-coordinate-factorization
  (Supported : U) (beta : MariciInt)
  (residue : Supported -> MariciInt)
  : U
  := Sigma (coordinates : Supported -> nima-amplitude-coordinates),
       (s : Supported) -> residue s
         = nima-calibrated-coordinate-amplitude beta (coordinates s)

#define nima-supported-residue-coordinates
  (Supported : U) (beta : MariciInt)
  (residue : Supported -> MariciInt)
  (factorization : nima-supported-residue-coordinate-factorization
    Supported beta residue)
  : Supported -> nima-amplitude-coordinates
  := first factorization

#define nima-supported-factorization-to-physical-bridge
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (factorization : nima-supported-residue-coordinate-factorization
    Supported beta residue)
  : nima-physical-coefficient-amplitude-bridge
      Physical Supported beta gysin residue
  := ((\ x -> first factorization (gysin x)),
      (\ x -> second factorization (gysin x)))

#define nima-supported-factorization-bridge-calibration
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (factorization : nima-supported-residue-coordinate-factorization
    Supported beta residue)
  (x : Physical)
  : residue (gysin x)
    = nima-calibrated-coordinate-amplitude beta
       (nima-supported-residue-coordinates Supported beta residue
         factorization (gysin x))
  := second factorization (gysin x)

#define nima-coefficient-supported-residue-factorization
  (beta : MariciInt)
  : nima-supported-residue-coordinate-factorization
      nima-amplitude-coordinates beta (nima-coefficient-model-residue beta)
  := ((\ x -> x), (\ x -> refl))

#define nima-coefficient-supported-factorization-induces-canonical-bridge
  (beta : MariciInt)
  : nima-supported-factorization-to-physical-bridge
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
      (nima-coefficient-supported-residue-factorization beta)
    = nima-coefficient-model-amplitude-bridge beta
  := refl

#data NimaSupportedFactorizationStrength
  := nima-residue-factorization-sufficient
  | nima-full-physical-coordinate-equivalence-not-required
#define nima-supported-factorization-strength : NimaSupportedFactorizationStrength
  := nima-residue-factorization-sufficient

#data NimaSupportedFactorizationGate
  := nima-three-supported-coordinate-functionals-required
  | nima-pointwise-residue-formula-required
#define nima-supported-factorization-gate : NimaSupportedFactorizationGate
  := nima-three-supported-coordinate-functionals-required
```
