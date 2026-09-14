# Normalized physical amplitude witness

```rzk
#lang rzk-1
#define nima-normalized-amplitude-path-ap
  (A B : U) (f : A -> B) (x y : A) (p : x = y) : f x = f y
  := idJ (A, x, (\ y' p' -> f x = f y'), refl, y, p)

#define nima-normalized-amplitude-path-concat
  (A : U) (x y z : A) (p : x = y) (q : y = z) : x = z
  := idJ (A, x, (\ y' p' -> (z' : A) -> (q' : y' = z') -> x = z'),
       (\ z' q' -> q'), y, p) z q

#define nima-normalized-physical-amplitude-witness
  (Physical Supported Scalars : U)
  (selected-physical : Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add negative-product : Scalars -> Scalars -> Scalars)
  : U
  := Sigma
       (image-law : gysin selected-physical = add s (add W v)),
       residue (gysin selected-physical)
         = negative-product beta (scalar-add one (scalar-add one one))

#define nima-normalized-amplitude-witness-from-packet-law
  (Physical Supported Scalars : U)
  (selected-physical : Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add negative-product : Scalars -> Scalars -> Scalars)
  (image-law : gysin selected-physical = add s (add W v))
  (packet-law : residue (add s (add W v))
    = negative-product beta (scalar-add one (scalar-add one one)))
  : nima-normalized-physical-amplitude-witness
      Physical Supported Scalars selected-physical gysin residue
      s W v add beta one scalar-add negative-product
  := (image-law,
      nima-normalized-amplitude-path-concat Scalars
        (residue (gysin selected-physical))
        (residue (add s (add W v)))
        (negative-product beta (scalar-add one (scalar-add one one)))
        (nima-normalized-amplitude-path-ap Supported Scalars residue
          (gysin selected-physical) (add s (add W v)) image-law)
        packet-law)

#define nima-normalized-amplitude-value
  (Physical Supported Scalars : U)
  (selected-physical : Physical)
  (gysin : Physical -> Supported)
  (residue : Supported -> Scalars)
  (s W v : Supported)
  (add : Supported -> Supported -> Supported)
  (beta one : Scalars)
  (scalar-add negative-product : Scalars -> Scalars -> Scalars)
  (witness : nima-normalized-physical-amplitude-witness
    Physical Supported Scalars selected-physical gysin residue
    s W v add beta one scalar-add negative-product)
  : residue (gysin selected-physical)
      = negative-product beta (scalar-add one (scalar-add one one))
  := second witness

#data NimaNormalizedAmplitudeScope
  := nima-selected-six-point-positive-sheet-primitive
  | nima-detector-coordinates-one-one-one
  | nima-residue-minus-beta-times-one-plus-one-plus-one
  | nima-symbolic-independent-a-b-c-family-not-claimed
#define nima-normalized-amplitude-scope : NimaNormalizedAmplitudeScope
  := nima-residue-minus-beta-times-one-plus-one-plus-one
```
