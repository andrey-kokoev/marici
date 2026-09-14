# Comparison-fibre amplitude

This module specializes supported-trace evaluation to a filling represented by
a coherent coefficient/physical comparison pair.  The amplitude reads only the
physical coordinate; the chosen coherence witness is computationally erased.

```rzk
#lang rzk-1

#define nima-amplitude-comparison-filling
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  : U
  := Sigma (coefficient : Coefficient),
       Sigma (physical : Physical), difference coefficient physical = zero

#define nima-amplitude-comparison-filling-point
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient) (physical : Physical)
  (coherence : difference coefficient physical = zero)
  : nima-amplitude-comparison-filling Coefficient Physical Comparison
      zero difference
  := (coefficient, (physical, coherence))

#define nima-amplitude-comparison-physical
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (filling : nima-amplitude-comparison-filling Coefficient Physical Comparison
    zero difference)
  : Physical
  := first (second filling)

#define nima-comparison-fibre-supported-amplitude
  (Coefficient Physical Comparison Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (supported-trace : Physical -> Scalars)
  (filling : nima-amplitude-comparison-filling Coefficient Physical Comparison
    zero difference)
  : Scalars
  := supported-trace
       (nima-amplitude-comparison-physical Coefficient Physical Comparison
         zero difference filling)

#define nima-comparison-fibre-amplitude-evaluates
  (Coefficient Physical Comparison Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (supported-trace : Physical -> Scalars)
  (coefficient : Coefficient) (physical : Physical)
  (coherence : difference coefficient physical = zero)
  : nima-comparison-fibre-supported-amplitude
      Coefficient Physical Comparison Scalars zero difference supported-trace
      (nima-amplitude-comparison-filling-point
        Coefficient Physical Comparison zero difference
        coefficient physical coherence)
    = supported-trace physical
  := refl

#define nima-comparison-fibre-amplitude-coherence-independent
  (Coefficient Physical Comparison Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (supported-trace : Physical -> Scalars)
  (coefficient : Coefficient) (physical : Physical)
  (coherence0 coherence1 : difference coefficient physical = zero)
  : nima-comparison-fibre-supported-amplitude
      Coefficient Physical Comparison Scalars zero difference supported-trace
      (coefficient, (physical, coherence0))
    = nima-comparison-fibre-supported-amplitude
      Coefficient Physical Comparison Scalars zero difference supported-trace
      (coefficient, (physical, coherence1))
  := refl

#define nima-comparison-fibre-amplitude-coefficient-independent
  (Coefficient Physical Comparison Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (supported-trace : Physical -> Scalars)
  (coefficient0 coefficient1 : Coefficient) (physical : Physical)
  (coherence0 : difference coefficient0 physical = zero)
  (coherence1 : difference coefficient1 physical = zero)
  : nima-comparison-fibre-supported-amplitude
      Coefficient Physical Comparison Scalars zero difference supported-trace
      (coefficient0, (physical, coherence0))
    = nima-comparison-fibre-supported-amplitude
      Coefficient Physical Comparison Scalars zero difference supported-trace
      (coefficient1, (physical, coherence1))
  := refl

#data NimaComparisonFibreAmplitudeDependency
  := nima-amplitude-depends-on-physical-coordinate
  | nima-amplitude-independent-of-coherence-witness
  | nima-amplitude-independent-of-coefficient-lift-at-fixed-physical-point
#define nima-comparison-fibre-amplitude-dependency
  : NimaComparisonFibreAmplitudeDependency
  := nima-amplitude-depends-on-physical-coordinate

#data NimaComparisonFibreAmplitudeGate
  := nima-coherent-filling-inhabitant-required
  | nima-supported-trace-required
#define nima-comparison-fibre-amplitude-gate : NimaComparisonFibreAmplitudeGate
  := nima-coherent-filling-inhabitant-required
```
