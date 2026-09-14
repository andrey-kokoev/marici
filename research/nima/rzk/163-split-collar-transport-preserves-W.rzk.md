# Split collar transport preserves W

```rzk
#lang rzk-1
#define nima-collar-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q
#define nima-collar-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)
#define nima-collar-path-inverse
  (A : U) (x y : A) (p : x = y) : y = x
  := idJ (A, x, (\ y' p' -> y' = x), refl, y, p)
#define nima-split-collar-transport-preserves-W
  (Endpoint Physical Contradiction : U)
  (zeroEndpoint : Endpoint) (zeroPhysical : Physical)
  (transport : Endpoint -> Physical)
  (retract : Physical -> Endpoint)
  (split : (x : Endpoint) -> retract (transport x) = x)
  (retractZero : retract zeroPhysical = zeroEndpoint)
  (W : Endpoint)
  (Wnonzero : (W = zeroEndpoint) -> Contradiction)
  : (transport W = zeroPhysical) -> Contradiction
  := \ transportedZero -> Wnonzero
       (nima-collar-path-concat Endpoint W (retract (transport W)) zeroEndpoint
         (nima-collar-path-inverse Endpoint (retract (transport W)) W (split W))
         (nima-collar-path-concat Endpoint
           (retract (transport W)) (retract zeroPhysical) zeroEndpoint
           (nima-collar-path-ap Physical Endpoint retract
             (transport W) zeroPhysical transportedZero)
           retractZero))
#data NimaSplitCollarTransportGate
  := nima-left-inverse-on-endpoint-class-suffices
  | nima-full-Verdier-equivalence-not-needed-for-W-survival
  | nima-construct-physical-retraction-on-W-sector
#define nima-split-collar-transport-gate : NimaSplitCollarTransportGate
  := nima-construct-physical-retraction-on-W-sector
```
