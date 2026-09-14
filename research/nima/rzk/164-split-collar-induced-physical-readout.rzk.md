# Split collar induces a detector-preserving physical readout

```rzk
#lang rzk-1
#define nima-induced-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)
#define nima-split-collar-induced-readout
  (Endpoint Physical Scalars : U)
  (retract : Physical -> Endpoint)
  (endpointDetector : Endpoint -> Scalars)
  : Physical -> Scalars
  := \ physical -> endpointDetector (retract physical)
#define nima-split-collar-induced-readout-preserves
  (Endpoint Physical Scalars : U)
  (transport : Endpoint -> Physical)
  (retract : Physical -> Endpoint)
  (split : (x : Endpoint) -> retract (transport x) = x)
  (endpointDetector : Endpoint -> Scalars)
  (x : Endpoint)
  : nima-split-collar-induced-readout Endpoint Physical Scalars
      retract endpointDetector (transport x)
    = endpointDetector x
  := nima-induced-path-ap Endpoint Scalars endpointDetector
       (retract (transport x)) x (split x)
#define nima-split-collar-induced-W-value
  (Endpoint Physical Scalars : U)
  (transport : Endpoint -> Physical)
  (retract : Physical -> Endpoint)
  (split : (x : Endpoint) -> retract (transport x) = x)
  (endpointDetector : Endpoint -> Scalars)
  (W : Endpoint)
  : nima-split-collar-induced-readout Endpoint Physical Scalars
      retract endpointDetector (transport W)
    = endpointDetector W
  := nima-split-collar-induced-readout-preserves Endpoint Physical Scalars
       transport retract split endpointDetector W
#data NimaInducedPhysicalReadoutScope
  := nima-retraction-composes-endpoint-detector-to-physical-readout
  | nima-W-value-preserved-definitionally-up-to-split-path
  | nima-identification-with-supported-residue-still-required
#define nima-induced-physical-readout-scope : NimaInducedPhysicalReadoutScope
  := nima-identification-with-supported-residue-still-required
```
