# Supported residue amplitude channel

The physical trace is factored through a supported local-cohomology class and
an oriented residue.  This excludes the ordinary polynomial-return channel,
which is known to specialize to zero.

```rzk
#lang rzk-1

#define nima-supported-residue-trace
  (Physical SupportedClass Scalars : U)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  : Physical -> Scalars
  := \ physical -> residue (gysin physical)

#define nima-supported-residue-amplitude
  (Filling Physical SupportedClass Scalars : U)
  (physical-component : Filling -> Physical)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  : Filling -> Scalars
  := \ filling -> residue (gysin (physical-component filling))

#define nima-supported-residue-amplitude-factorizes
  (Filling Physical SupportedClass Scalars : U)
  (physical-component : Filling -> Physical)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  (filling : Filling)
  : nima-supported-residue-amplitude Filling Physical SupportedClass Scalars
      physical-component gysin residue filling
    = nima-supported-residue-trace Physical SupportedClass Scalars
      gysin residue (physical-component filling)
  := refl

#define nima-supported-residue-amplitude-on-comparison
  (Coefficient Physical Comparison SupportedClass Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  (filling : Sigma (coefficient : Coefficient),
    Sigma (physical : Physical), difference coefficient physical = zero)
  : Scalars
  := residue (gysin (first (second filling)))

#define nima-supported-residue-comparison-evaluates
  (Coefficient Physical Comparison SupportedClass Scalars : U)
  (zero : Comparison)
  (difference : Coefficient -> Physical -> Comparison)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  (coefficient : Coefficient) (physical : Physical)
  (coherence : difference coefficient physical = zero)
  : nima-supported-residue-amplitude-on-comparison
      Coefficient Physical Comparison SupportedClass Scalars
      zero difference gysin residue
      (coefficient, (physical, coherence))
    = residue (gysin physical)
  := refl

#define nima-supported-residue-reflection-covariant
  (Reflection Physical SupportedClass Scalars : U)
  (gysin : Physical -> SupportedClass)
  (residue : SupportedClass -> Scalars)
  (reflect-physical : Reflection -> Physical -> Physical)
  (reflect-supported : Reflection -> SupportedClass -> SupportedClass)
  (reflect-scalar : Reflection -> Scalars -> Scalars)
  (gysin-reflection : (r : Reflection) -> (x : Physical) ->
    gysin (reflect-physical r x) = reflect-supported r (gysin x))
  (oriented-residue : (r : Reflection) -> (x : Physical) ->
    residue (gysin (reflect-physical r x)) =
      reflect-scalar r (residue (gysin x)))
  (r : Reflection) (x : Physical)
  : nima-supported-residue-trace Physical SupportedClass Scalars
      gysin residue (reflect-physical r x)
    = reflect-scalar r
      (nima-supported-residue-trace Physical SupportedClass Scalars
        gysin residue x)
  := oriented-residue r x

#data NimaAmplitudeResidueChannelChoice
  := nima-ordinary-polynomial-return-specializes-zero
  | nima-shifted-supported-Gysin-residue-retains-primitive
#define nima-amplitude-residue-channel-choice : NimaAmplitudeResidueChannelChoice
  := nima-shifted-supported-Gysin-residue-retains-primitive

#data NimaAmplitudeOrientationRequirement
  := nima-ordered-conormal-determinant-required
  | nima-sheet-exchange-orientation-odd
#define nima-amplitude-orientation-requirement : NimaAmplitudeOrientationRequirement
  := nima-ordered-conormal-determinant-required

#data NimaSupportedResidueInstantiationGate
  := nima-physical-Gysin-map-required
  | nima-oriented-residue-map-required
#define nima-supported-residue-instantiation-gate
  : NimaSupportedResidueInstantiationGate
  := nima-physical-Gysin-map-required
```
