# Butterfly packet residue transport

```rzk
#lang rzk-1
#define nima-butterfly-residue-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)

#define nima-butterfly-residue-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q

#define nima-butterfly-packet-residue-transport
  (Connector PhysicalGysin SupportedPacket Scalars : U)
  (kernel-connector : Connector)
  (selected-physical-gysin : PhysicalGysin)
  (pullback-butterfly : Connector -> PhysicalGysin -> SupportedPacket)
  (selected-packet : SupportedPacket)
  (residue : SupportedPacket -> Scalars)
  (calibrated-value : Scalars)
  (butterfly-witness :
    pullback-butterfly kernel-connector selected-physical-gysin
      = selected-packet)
  (packet-residue-law : residue selected-packet = calibrated-value)
  : residue
      (pullback-butterfly kernel-connector selected-physical-gysin)
      = calibrated-value
  := nima-butterfly-residue-concat Scalars
       (residue
         (pullback-butterfly kernel-connector selected-physical-gysin))
       (residue selected-packet)
       calibrated-value
       (nima-butterfly-residue-ap SupportedPacket Scalars residue
         (pullback-butterfly kernel-connector selected-physical-gysin)
         selected-packet butterfly-witness)
       packet-residue-law

#data NimaButterflyResidueReduction
  := nima-residue-formula-follows-formally-from-butterfly-packet-equality
  | nima-local-normal-residue-adds-no-Jacobian
  | nima-only-detector-coordinate-comparison-remains
#define nima-butterfly-residue-reduction : NimaButterflyResidueReduction
  := nima-only-detector-coordinate-comparison-remains
```
