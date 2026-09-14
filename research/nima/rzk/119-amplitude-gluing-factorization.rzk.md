# Amplitude gluing and factorization

This module isolates the multiplicative theorem needed after supported-residue
evaluation: gluing two independent physical fillings factors their amplitude.
The hypotheses expose exactly where geometric gluing, Gysin multiplicativity,
and residue multiplicativity enter.

```rzk
#lang rzk-1

#define nima-amplitude-glued-fillings (Left Right : U) : U
  := Sigma (_ : Left), Right

#define nima-amplitude-product
  (Left Right Physical Supported Scalars : U)
  (glue : Left -> Right -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (x : nima-amplitude-glued-fillings Left Right)
  : Scalars
  := residue (gysin (glue (first x) (second x)))

#define nima-amplitude-factorized-product
  (Left Right LeftSupported RightSupported Scalars : U)
  (left-gysin : Left -> LeftSupported)
  (right-gysin : Right -> RightSupported)
  (left-residue : LeftSupported -> Scalars)
  (right-residue : RightSupported -> Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (x : nima-amplitude-glued-fillings Left Right)
  : Scalars
  := multiply (left-residue (left-gysin (first x)))
       (right-residue (right-gysin (second x)))

#define nima-amplitude-gluing-factorization
  (Left Right Physical Supported LeftSupported RightSupported Scalars : U)
  (glue : Left -> Right -> Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (left-gysin : Left -> LeftSupported)
  (right-gysin : Right -> RightSupported)
  (left-residue : LeftSupported -> Scalars)
  (right-residue : RightSupported -> Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (factorization : (left : Left) -> (right : Right) ->
    residue (gysin (glue left right)) =
      multiply (left-residue (left-gysin left))
        (right-residue (right-gysin right)))
  (x : nima-amplitude-glued-fillings Left Right)
  : nima-amplitude-product Left Right Physical Supported Scalars
      glue gysin residue x
    = nima-amplitude-factorized-product Left Right LeftSupported
      RightSupported Scalars left-gysin right-gysin left-residue
      right-residue multiply x
  := factorization (first x) (second x)

#define nima-amplitude-unit-normalization
  (Filling Scalars : U)
  (Amplitude : Filling -> Scalars)
  (unit-filling : Filling)
  (one : Scalars)
  : U
  := Amplitude unit-filling = one

#define nima-amplitude-disjoint-factorization-law
  (Filling Scalars : U)
  (Amplitude : Filling -> Scalars)
  (glue : Filling -> Filling -> Filling)
  (multiply : Scalars -> Scalars -> Scalars)
  : U
  := (x y : Filling) ->
       Amplitude (glue x y) = multiply (Amplitude x) (Amplitude y)

#define nima-amplitude-associative-gluing-coherence
  (Filling Scalars : U)
  (Amplitude : Filling -> Scalars)
  (glue : Filling -> Filling -> Filling)
  (multiply : Scalars -> Scalars -> Scalars)
  : U
  := (x y z : Filling) ->
       Amplitude (glue (glue x y) z) =
       multiply (Amplitude x) (multiply (Amplitude y) (Amplitude z))

#define nima-amplitude-reflection-factorization-compatibility
  (Reflection Filling Scalars : U)
  (Amplitude : Filling -> Scalars)
  (glue : Filling -> Filling -> Filling)
  (multiply : Scalars -> Scalars -> Scalars)
  (reflect-filling : Reflection -> Filling -> Filling)
  (reflect-scalar : Reflection -> Scalars -> Scalars)
  : U
  := (r : Reflection) -> (x y : Filling) ->
       Amplitude (reflect-filling r (glue x y)) =
       reflect-scalar r (multiply (Amplitude x) (Amplitude y))

#data NimaAmplitudeFactorizationGate
  := nima-physical-gluing-map-required
  | nima-supported-Gysin-gluing-required
  | nima-oriented-residue-multiplicativity-required
#define nima-amplitude-factorization-gate : NimaAmplitudeFactorizationGate
  := nima-physical-gluing-map-required
```
