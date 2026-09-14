# Fixed-coefficient physical obstruction

For a selected coefficient class, obstruction vanishing is represented
constructively by a physical lift together with the complete comparison
coherence.  This avoids naming an H1 class without an instantiated complex.

```rzk
#lang rzk-1

#define nima-fixed-coefficient-physical-lifts
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  : U
  := Sigma (physical : Physical), difference coefficient physical = zero

#define nima-fixed-coefficient-obstruction-vanishes
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  : U
  := nima-fixed-coefficient-physical-lifts
       Coefficient Physical Comparison zero difference coefficient

#define nima-physical-lift-to-comparison-filling
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (lift : nima-fixed-coefficient-physical-lifts
    Coefficient Physical Comparison zero difference coefficient)
  : Sigma (c : Coefficient),
      Sigma (p : Physical), difference c p = zero
  := (coefficient, lift)

#define nima-comparison-filling-to-fixed-lift
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (physical : Physical)
  (coherence : difference coefficient physical = zero)
  : nima-fixed-coefficient-physical-lifts
      Coefficient Physical Comparison zero difference coefficient
  := (physical, coherence)

#define nima-fixed-lift-physical
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (lift : nima-fixed-coefficient-physical-lifts
    Coefficient Physical Comparison zero difference coefficient)
  : Physical
  := first lift

#define nima-fixed-lift-coherence
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (lift : nima-fixed-coefficient-physical-lifts
    Coefficient Physical Comparison zero difference coefficient)
  : difference coefficient
      (nima-fixed-lift-physical Coefficient Physical Comparison
        zero difference coefficient lift) = zero
  := second lift

#define nima-fixed-lift-supported-amplitude
  (Coefficient Physical Comparison Supported : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (lift : nima-fixed-coefficient-physical-lifts
    Coefficient Physical Comparison zero difference coefficient)
  : MariciInt
  := residue (gysin (first lift))

#define nima-fixed-lift-calibrated-amplitude
  (Coefficient Physical Comparison Supported : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient)
  (beta : MariciInt)
  (gysin : Physical -> Supported)
  (residue : Supported -> MariciInt)
  (bridge : nima-physical-coefficient-amplitude-bridge
    Physical Supported beta gysin residue)
  (lift : nima-fixed-coefficient-physical-lifts
    Coefficient Physical Comparison zero difference coefficient)
  : nima-fixed-lift-supported-amplitude
      Coefficient Physical Comparison Supported zero difference coefficient
      gysin residue lift
    = nima-calibrated-coordinate-amplitude beta
       (first bridge (first lift))
  := second bridge (first lift)

#data NimaFixedCoefficientObstructionGate
  := nima-totalized-difference-map-required
  | nima-physical-lift-and-coherence-required
  | nima-no-H1-vanishing-claimed-before-instantiation
#define nima-fixed-coefficient-obstruction-gate
  : NimaFixedCoefficientObstructionGate
  := nima-totalized-difference-map-required
```
