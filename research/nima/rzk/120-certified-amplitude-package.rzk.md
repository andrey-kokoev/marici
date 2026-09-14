# Certified amplitude package

A candidate amplitude is bundled with its normalization, homotopy invariance,
symmetry covariance, and gluing factorization.  This is the first Rzk type whose
inhabitants are complete amplitude certificates relative to supplied physical
filling operations.

```rzk
#lang rzk-1

#define nima-certified-amplitude
  (Symmetry Filling Scalars : U)
  (FillingPath : Filling -> Filling -> U)
  (unit-filling : Filling)
  (glue : Filling -> Filling -> Filling)
  (act-filling : Symmetry -> Filling -> Filling)
  (zero one : Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  : U
  := Sigma (Amplitude : Filling -> Scalars),
       Sigma (_ : Amplitude unit-filling = one),
       Sigma (_ : (x y : Filling) -> FillingPath x y ->
         Amplitude x = Amplitude y),
       Sigma (_ : (g : Symmetry) -> (x : Filling) ->
         Amplitude (act-filling g x) = act-scalar g (Amplitude x)),
       (x y : Filling) ->
         Amplitude (glue x y) = multiply (Amplitude x) (Amplitude y)

#define nima-certified-amplitude-package
  (Symmetry Filling Scalars : U)
  (FillingPath : Filling -> Filling -> U)
  (unit-filling : Filling)
  (glue : Filling -> Filling -> Filling)
  (act-filling : Symmetry -> Filling -> Filling)
  (zero one : Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  (Amplitude : Filling -> Scalars)
  (normalization : Amplitude unit-filling = one)
  (homotopy-invariance : (x y : Filling) -> FillingPath x y ->
    Amplitude x = Amplitude y)
  (symmetry-covariance : (g : Symmetry) -> (x : Filling) ->
    Amplitude (act-filling g x) = act-scalar g (Amplitude x))
  (factorization : (x y : Filling) ->
    Amplitude (glue x y) = multiply (Amplitude x) (Amplitude y))
  : nima-certified-amplitude Symmetry Filling Scalars FillingPath
      unit-filling glue act-filling zero one multiply act-scalar
  := (Amplitude,
      (normalization,
       (homotopy-invariance,
        (symmetry-covariance, factorization))))

#define nima-certified-amplitude-map
  (Symmetry Filling Scalars : U)
  (FillingPath : Filling -> Filling -> U)
  (unit-filling : Filling)
  (glue : Filling -> Filling -> Filling)
  (act-filling : Symmetry -> Filling -> Filling)
  (zero one : Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  (package : nima-certified-amplitude Symmetry Filling Scalars FillingPath
    unit-filling glue act-filling zero one multiply act-scalar)
  : Filling -> Scalars
  := first package

#define nima-certified-amplitude-normalization
  (Symmetry Filling Scalars : U)
  (FillingPath : Filling -> Filling -> U)
  (unit-filling : Filling)
  (glue : Filling -> Filling -> Filling)
  (act-filling : Symmetry -> Filling -> Filling)
  (zero one : Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  (package : nima-certified-amplitude Symmetry Filling Scalars FillingPath
    unit-filling glue act-filling zero one multiply act-scalar)
  : nima-certified-amplitude-map Symmetry Filling Scalars FillingPath
      unit-filling glue act-filling zero one multiply act-scalar package
      unit-filling = one
  := first (second package)

#define nima-certified-amplitude-factorization
  (Symmetry Filling Scalars : U)
  (FillingPath : Filling -> Filling -> U)
  (unit-filling : Filling)
  (glue : Filling -> Filling -> Filling)
  (act-filling : Symmetry -> Filling -> Filling)
  (zero one : Scalars)
  (multiply : Scalars -> Scalars -> Scalars)
  (act-scalar : Symmetry -> Scalars -> Scalars)
  (package : nima-certified-amplitude Symmetry Filling Scalars FillingPath
    unit-filling glue act-filling zero one multiply act-scalar)
  (x y : Filling)
  : nima-certified-amplitude-map Symmetry Filling Scalars FillingPath
      unit-filling glue act-filling zero one multiply act-scalar package
      (glue x y)
    = multiply
      (nima-certified-amplitude-map Symmetry Filling Scalars FillingPath
        unit-filling glue act-filling zero one multiply act-scalar package x)
      (nima-certified-amplitude-map Symmetry Filling Scalars FillingPath
        unit-filling glue act-filling zero one multiply act-scalar package y)
  := second (second (second (second package))) x y

#data NimaCertifiedAmplitudeStatus
  := nima-relative-certified-amplitude-type-constructed
  | nima-no-concrete-physical-package-inhabitant-yet
#define nima-certified-amplitude-status : NimaCertifiedAmplitudeStatus
  := nima-relative-certified-amplitude-type-constructed
```
