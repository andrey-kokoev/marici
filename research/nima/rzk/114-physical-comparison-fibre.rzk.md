# Structural physical comparison fibre

The fixed-structure deformation problem is the strict fibre of the difference
between coefficient and physical comparison cochains.  This module constructs
that fibre for arbitrary typed cochain groups and maps; it does not instantiate
the missing physical map.

```rzk
#lang rzk-1

#define nima-comparison-pair (Coefficient Physical : U) : U
  := Sigma (_ : Coefficient), Physical

#define nima-comparison-difference
  (Coefficient Physical Comparison : U)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (x : nima-comparison-pair Coefficient Physical)
  : Comparison
  := sub (coefficient-map (first x)) (physical-map (second x))

#define nima-physical-comparison-fibre
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  : U
  := Sigma (x : nima-comparison-pair Coefficient Physical),
       nima-comparison-difference Coefficient Physical Comparison sub
         coefficient-map physical-map x = zero

#define nima-physical-comparison-fibre-point
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (coefficient : Coefficient) (physical : Physical)
  (coherence : sub (coefficient-map coefficient) (physical-map physical) = zero)
  : nima-physical-comparison-fibre Coefficient Physical Comparison zero sub
      coefficient-map physical-map
  := ((coefficient, physical), coherence)

#define nima-physical-comparison-coefficient
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (x : nima-physical-comparison-fibre Coefficient Physical Comparison zero sub
      coefficient-map physical-map)
  : Coefficient
  := first (first x)

#define nima-physical-comparison-physical
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (x : nima-physical-comparison-fibre Coefficient Physical Comparison zero sub
      coefficient-map physical-map)
  : Physical
  := second (first x)

#define nima-physical-comparison-coherence
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (x : nima-physical-comparison-fibre Coefficient Physical Comparison zero sub
      coefficient-map physical-map)
  : sub (coefficient-map (nima-physical-comparison-coefficient
      Coefficient Physical Comparison zero sub coefficient-map physical-map x))
      (physical-map (nima-physical-comparison-physical
      Coefficient Physical Comparison zero sub coefficient-map physical-map x)) = zero
  := second x

#define nima-physical-comparison-zero
  (Coefficient Physical Comparison : U)
  (zeroCoefficient : Coefficient) (zeroPhysical : Physical)
  (zeroComparison : Comparison)
  (sub : Comparison -> Comparison -> Comparison)
  (coefficient-map : Coefficient -> Comparison)
  (physical-map : Physical -> Comparison)
  (zero-coherence :
    sub (coefficient-map zeroCoefficient) (physical-map zeroPhysical)
      = zeroComparison)
  : nima-physical-comparison-fibre Coefficient Physical Comparison zeroComparison sub
      coefficient-map physical-map
  := ((zeroCoefficient, zeroPhysical), zero-coherence)

#data NimaPhysicalComparisonDirections
  := nima-endpoint-Cech-normal-group-operation-directions-required
  | nima-fixed-module-and-action-structures-required
#define nima-physical-comparison-directions : NimaPhysicalComparisonDirections
  := nima-endpoint-Cech-normal-group-operation-directions-required

#data NimaPhysicalComparisonObstructionSemantics
  := nima-H1-controls-existence
  | nima-H0-acts-on-components
  | nima-negative-cohomology-controls-higher-automorphisms
#define nima-physical-comparison-obstruction-semantics
  : NimaPhysicalComparisonObstructionSemantics
  := nima-H1-controls-existence

#data NimaPhysicalComparisonInstantiationStatus
  := nima-generic-fibre-constructed
  | nima-physical-comparison-map-still-required
#define nima-physical-comparison-instantiation-status
  : NimaPhysicalComparisonInstantiationStatus
  := nima-physical-comparison-map-still-required
```
