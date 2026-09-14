# Totalized physical amplitude interface

The five required coherence directions are retained as separate coordinates.
No direction is silently collapsed into an endpoint Hom group.

```rzk
#lang rzk-1

#define nima-totalized-cochains
  (Endpoint Cech Normal Group Operation : U) : U
  := Sigma (_ : Endpoint),
       Sigma (_ : Cech),
       Sigma (_ : Normal),
       Sigma (_ : Group), Operation

#define nima-totalized-cochain
  (Endpoint Cech Normal Group Operation : U)
  (endpoint : Endpoint) (cech : Cech) (normal : Normal)
  (group : Group) (operation : Operation)
  : nima-totalized-cochains Endpoint Cech Normal Group Operation
  := (endpoint, (cech, (normal, (group, operation))))

#define nima-totalized-endpoint
  (Endpoint Cech Normal Group Operation : U)
  (x : nima-totalized-cochains Endpoint Cech Normal Group Operation)
  : Endpoint
  := first x

#define nima-totalized-cech
  (Endpoint Cech Normal Group Operation : U)
  (x : nima-totalized-cochains Endpoint Cech Normal Group Operation)
  : Cech
  := first (second x)

#define nima-totalized-normal
  (Endpoint Cech Normal Group Operation : U)
  (x : nima-totalized-cochains Endpoint Cech Normal Group Operation)
  : Normal
  := first (second (second x))

#define nima-totalized-group
  (Endpoint Cech Normal Group Operation : U)
  (x : nima-totalized-cochains Endpoint Cech Normal Group Operation)
  : Group
  := first (second (second (second x)))

#define nima-totalized-operation
  (Endpoint Cech Normal Group Operation : U)
  (x : nima-totalized-cochains Endpoint Cech Normal Group Operation)
  : Operation
  := second (second (second (second x)))

#define nima-totalized-comparison-fibre
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  : U
  := Sigma (coefficient : Coefficient),
       Sigma (physical : Physical),
         difference coefficient physical = zero

#define nima-totalized-comparison-point
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (coefficient : Coefficient) (physical : Physical)
  (coherence : difference coefficient physical = zero)
  : nima-totalized-comparison-fibre Coefficient Physical Comparison zero difference
  := (coefficient, (physical, coherence))

#define nima-totalized-comparison-coefficient
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (x : nima-totalized-comparison-fibre Coefficient Physical Comparison zero difference)
  : Coefficient
  := first x

#define nima-totalized-comparison-physical
  (Coefficient Physical Comparison : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (x : nima-totalized-comparison-fibre Coefficient Physical Comparison zero difference)
  : Physical
  := first (second x)

#define nima-amplitude-functional
  (PhysicalFilling Scalars : U) : U
  := PhysicalFilling -> Scalars

#define nima-amplitude-homotopy-invariant
  (PhysicalFilling Scalars : U)
  (Amplitude : nima-amplitude-functional PhysicalFilling Scalars)
  (FillingPath : PhysicalFilling -> PhysicalFilling -> U)
  : U
  := (x y : PhysicalFilling) -> FillingPath x y -> Amplitude x = Amplitude y

#define nima-amplitude-specialization-compatible
  (PhysicalFilling Scalars SpecializedFilling SpecializedScalars : U)
  (Amplitude : nima-amplitude-functional PhysicalFilling Scalars)
  (SpecializedAmplitude :
    nima-amplitude-functional SpecializedFilling SpecializedScalars)
  (specializeFilling : PhysicalFilling -> SpecializedFilling)
  (specializeScalar : Scalars -> SpecializedScalars)
  : U
  := (x : PhysicalFilling) ->
       specializeScalar (Amplitude x) =
       SpecializedAmplitude (specializeFilling x)

#define nima-amplitude-symmetry-covariant
  (Symmetry PhysicalFilling Scalars : U)
  (Amplitude : nima-amplitude-functional PhysicalFilling Scalars)
  (actFilling : Symmetry -> PhysicalFilling -> PhysicalFilling)
  (actScalar : Symmetry -> Scalars -> Scalars)
  : U
  := (g : Symmetry) -> (x : PhysicalFilling) ->
       Amplitude (actFilling g x) = actScalar g (Amplitude x)

#data NimaAmplitudeConstructionGate
  := nima-totalized-five-direction-source-defined
  | nima-physical-filling-inhabitant-required
  | nima-supported-trace-evaluation-required
#define nima-amplitude-construction-gate : NimaAmplitudeConstructionGate
  := nima-physical-filling-inhabitant-required
```
