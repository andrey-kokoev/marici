# Supported-trace amplitude construction

An amplitude is now constructed by evaluating the physical component of a
filling through a supported trace.  Theorems below transport homotopy
invariance, specialization, and symmetry from the physical trace data.

```rzk
#lang rzk-1

#define nima-amplitude-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q

#define nima-amplitude-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)

#define nima-supported-trace-amplitude
  (Filling Physical Scalars : U)
  (physical-component : Filling -> Physical)
  (supported-trace : Physical -> Scalars)
  : Filling -> Scalars
  := \ filling -> supported-trace (physical-component filling)

#define nima-supported-trace-amplitude-homotopy-invariant
  (Filling Physical Scalars : U)
  (physical-component : Filling -> Physical)
  (supported-trace : Physical -> Scalars)
  (FillingPath : Filling -> Filling -> U)
  (PhysicalPath : Physical -> Physical -> U)
  (physical-preserves-path : (x y : Filling) -> FillingPath x y ->
    PhysicalPath (physical-component x) (physical-component y))
  (trace-preserves-path : (x y : Physical) -> PhysicalPath x y ->
    supported-trace x = supported-trace y)
  (x y : Filling) (p : FillingPath x y)
  : nima-supported-trace-amplitude Filling Physical Scalars
      physical-component supported-trace x
    = nima-supported-trace-amplitude Filling Physical Scalars
      physical-component supported-trace y
  := trace-preserves-path (physical-component x) (physical-component y)
       (physical-preserves-path x y p)

#define nima-supported-trace-amplitude-specializes
  (Filling Physical Scalars SpecializedFilling SpecializedPhysical
    SpecializedScalars : U)
  (physical-component : Filling -> Physical)
  (specialized-physical-component : SpecializedFilling -> SpecializedPhysical)
  (supported-trace : Physical -> Scalars)
  (specialized-supported-trace : SpecializedPhysical -> SpecializedScalars)
  (specialize-filling : Filling -> SpecializedFilling)
  (specialize-physical : Physical -> SpecializedPhysical)
  (specialize-scalar : Scalars -> SpecializedScalars)
  (physical-specialization : (x : Filling) ->
    specialize-physical (physical-component x) =
      specialized-physical-component (specialize-filling x))
  (trace-specialization : (x : Physical) ->
    specialize-scalar (supported-trace x) =
      specialized-supported-trace (specialize-physical x))
  (x : Filling)
  : specialize-scalar
      (nima-supported-trace-amplitude Filling Physical Scalars
        physical-component supported-trace x)
    = nima-supported-trace-amplitude SpecializedFilling SpecializedPhysical
        SpecializedScalars specialized-physical-component
        specialized-supported-trace (specialize-filling x)
  := nima-amplitude-path-concat SpecializedScalars
       (specialize-scalar (supported-trace (physical-component x)))
       (specialized-supported-trace
         (specialize-physical (physical-component x)))
       (specialized-supported-trace
         (specialized-physical-component (specialize-filling x)))
       (trace-specialization (physical-component x))
       (nima-amplitude-path-ap SpecializedPhysical SpecializedScalars
         specialized-supported-trace
         (specialize-physical (physical-component x))
         (specialized-physical-component (specialize-filling x))
         (physical-specialization x))

#define nima-supported-trace-amplitude-covariant
  (Symmetry Filling Physical Scalars : U)
  (physical-component : Filling -> Physical)
  (supported-trace : Physical -> Scalars)
  (act-filling : Symmetry -> Filling -> Filling)
  (act-physical : Symmetry -> Physical -> Physical)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  (physical-equivariant : (g : Symmetry) -> (x : Filling) ->
    physical-component (act-filling g x) =
      act-physical g (physical-component x))
  (trace-equivariant : (g : Symmetry) -> (x : Physical) ->
    supported-trace (act-physical g x) = act-scalar g (supported-trace x))
  (g : Symmetry) (x : Filling)
  : nima-supported-trace-amplitude Filling Physical Scalars
      physical-component supported-trace (act-filling g x)
    = act-scalar g
      (nima-supported-trace-amplitude Filling Physical Scalars
        physical-component supported-trace x)
  := nima-amplitude-path-concat Scalars
       (supported-trace (physical-component (act-filling g x)))
       (supported-trace (act-physical g (physical-component x)))
       (act-scalar g (supported-trace (physical-component x)))
       (nima-amplitude-path-ap Physical Scalars supported-trace
         (physical-component (act-filling g x))
         (act-physical g (physical-component x))
         (physical-equivariant g x))
       (trace-equivariant g (physical-component x))

#data NimaSupportedTraceAmplitudeStatus
  := nima-amplitude-defined-from-physical-component-and-supported-trace
  | nima-concrete-physical-filling-and-trace-still-required
#define nima-supported-trace-amplitude-status : NimaSupportedTraceAmplitudeStatus
  := nima-amplitude-defined-from-physical-component-and-supported-trace
```
