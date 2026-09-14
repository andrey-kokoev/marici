# Supported residue detects transported W

```rzk
#lang rzk-1
#define nima-residue-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q
#define nima-residue-path-inverse
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)
#define nima-supported-residue-readout
  (Physical Supported Scalars : U)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  : Physical -> Scalars
  := \ physical -> residue (gysin physical)
#define nima-supported-residue-W-nonvanishing
  (Endpoint Physical Supported Scalars Contradiction : U)
  (transport : Endpoint -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (endpointDetector : Endpoint -> Scalars)
  (zeroScalar : Scalars) (W : Endpoint)
  (comparison : nima-supported-residue-readout Physical Supported Scalars
    gysin residue (transport W) = endpointDetector W)
  (endpointNonzero : (endpointDetector W = zeroScalar) -> Contradiction)
  : (nima-supported-residue-readout Physical Supported Scalars
       gysin residue (transport W) = zeroScalar) -> Contradiction
  := \ physicalZero -> endpointNonzero
       (nima-residue-path-concat Scalars
         (endpointDetector W)
         (nima-supported-residue-readout Physical Supported Scalars
           gysin residue (transport W))
         zeroScalar
         (nima-residue-path-inverse Scalars
           (nima-supported-residue-readout Physical Supported Scalars
             gysin residue (transport W))
           (endpointDetector W) comparison)
         physicalZero)
#data NimaSupportedResidueWGate
  := nima-endpoint-detector-comparison-implies-physical-nonvanishing
  | nima-prove-comparison-on-W-sector
#define nima-supported-residue-W-gate : NimaSupportedResidueWGate
  := nima-prove-comparison-on-W-sector
```
