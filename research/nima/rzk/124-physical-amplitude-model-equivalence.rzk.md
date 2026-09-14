# Physical amplitude model equivalence

A physical supported object may be identified with the coefficient fixture only
through explicit encoding, decoding, inverse laws, and residue compatibility.
Such an equivalence canonically produces the amplitude bridge.

```rzk
#lang rzk-1

#define nima-physical-amplitude-model-equivalence
  (Physical Supported : U)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  : U
  := Sigma (encode : Physical -> nima-amplitude-coordinates),
       Sigma (decode : nima-amplitude-coordinates -> Physical),
       Sigma (_ : (x : Physical) -> decode (encode x) = x),
       Sigma (_ : (c : nima-amplitude-coordinates) -> encode (decode c) = c),
       (x : Physical) -> residue (gysin x)
         = nima-calibrated-coordinate-amplitude beta (encode x)

#define nima-physical-model-encode
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (equivalence : nima-physical-amplitude-model-equivalence
    Physical Supported beta gysin residue)
  : Physical -> nima-amplitude-coordinates
  := first equivalence

#define nima-physical-model-decode
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (equivalence : nima-physical-amplitude-model-equivalence
    Physical Supported beta gysin residue)
  : nima-amplitude-coordinates -> Physical
  := first (second equivalence)

#define nima-physical-model-encode-decode
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (equivalence : nima-physical-amplitude-model-equivalence
    Physical Supported beta gysin residue)
  (c : nima-amplitude-coordinates)
  : nima-physical-model-encode Physical Supported beta gysin residue
      equivalence
      (nima-physical-model-decode Physical Supported beta gysin residue
        equivalence c) = c
  := first (second (second (second equivalence))) c

#define nima-physical-model-equivalence-to-amplitude-bridge
  (Physical Supported : U) (beta : MariciInt)
  (gysin : Physical -> Supported) (residue : Supported -> MariciInt)
  (equivalence : nima-physical-amplitude-model-equivalence
    Physical Supported beta gysin residue)
  : nima-physical-coefficient-amplitude-bridge
      Physical Supported beta gysin residue
  := (first equivalence,
      second (second (second (second equivalence))))

#define nima-coefficient-amplitude-model-self-equivalence
  (beta : MariciInt)
  : nima-physical-amplitude-model-equivalence
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
  := ((\ x -> x),
      ((\ x -> x),
       ((\ x -> refl),
        ((\ x -> refl), (\ x -> refl)))))

#define nima-self-equivalence-bridge-is-canonical
  (beta : MariciInt)
  : nima-physical-model-equivalence-to-amplitude-bridge
      nima-amplitude-coordinates nima-amplitude-coordinates beta
      nima-coefficient-model-gysin (nima-coefficient-model-residue beta)
      (nima-coefficient-amplitude-model-self-equivalence beta)
    = nima-coefficient-model-amplitude-bridge beta
  := refl

#data NimaPhysicalAmplitudeEquivalenceGate
  := nima-encode-decode-inverse-laws-required
  | nima-supported-residue-coordinate-law-required
  | nima-source-equivalence-alone-insufficient
#define nima-physical-amplitude-equivalence-gate
  : NimaPhysicalAmplitudeEquivalenceGate
  := nima-supported-residue-coordinate-law-required
```
