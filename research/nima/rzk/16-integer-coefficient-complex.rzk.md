# Concrete integer coefficient complex

This is a concrete free rank-two integer module in every cochain degree,
with d(a,b)=(b,0) and H(a,b)=(0,a). It is an unbounded contractible test
complex, not the 215-generator physical support complex or its ring.
Canonical integer laws are reused, not supplied as new assumptions.

```rzk
#lang rzk-1

#define NimaZ2 : U := Sigma (_ : MariciInt), MariciInt
#define nima-z2-zero : NimaZ2 := (marici-int-zero,marici-int-zero)
#define nima-z2-add (x y : NimaZ2) : NimaZ2
  := (marici-int-add (first x) (first y), marici-int-add (second x) (second y))
#define nima-z2-neg (x : NimaZ2) : NimaZ2
  := (marici-int-negate (first x), marici-int-negate (second x))
#define nima-z2-sub (x y : NimaZ2) : NimaZ2
  := nima-z2-add x (nima-z2-neg y)
#define nima-z2-scale (a : MariciInt) (x : NimaZ2) : NimaZ2
  := (marici-int-mul a (first x), marici-int-mul a (second x))

#define nima-z2-path (x y : NimaZ2) (p : first x = first y) (q : second x = second y) : x = y
  := nima-cochain-ap2 MariciInt MariciInt NimaZ2 (\ a b -> (a,b))
       (first x) (first y) (second x) (second y) p q

#define nima-z2-assoc (x y z : NimaZ2)
  : nima-z2-add (nima-z2-add x y) z = nima-z2-add x (nima-z2-add y z)
  := nima-z2-path (nima-z2-add (nima-z2-add x y) z) (nima-z2-add x (nima-z2-add y z))
       (marici-int-add-assoc (first x) (first y) (first z))
       (marici-int-add-assoc (second x) (second y) (second z))

#define nima-z2-comm (x y : NimaZ2) : nima-z2-add x y = nima-z2-add y x
  := nima-z2-path (nima-z2-add x y) (nima-z2-add y x)
       (marici-int-add-comm (first x) (first y)) (marici-int-add-comm (second x) (second y))

#define nima-z2-right-zero (x : NimaZ2) : nima-z2-add x nima-z2-zero = x
  := nima-z2-path (nima-z2-add x nima-z2-zero) x
       (marici-int-add-zero-right (first x)) (marici-int-add-zero-right (second x))

#define nima-z2-left-zero (x : NimaZ2) : nima-z2-add nima-z2-zero x = x
  := refl

#define nima-z2-inverse (x : NimaZ2) : nima-z2-add x (nima-z2-neg x) = nima-z2-zero
  := nima-z2-path (nima-z2-add x (nima-z2-neg x)) nima-z2-zero
       (marici-int-add-inverse-right (first x)) (marici-int-add-inverse-right (second x))

#define nima-z2-scale-one (x : NimaZ2) : nima-z2-scale marici-int-one x = x
  := nima-z2-path (nima-z2-scale marici-int-one x) x
       (marici-int-mul-one-left (first x)) (marici-int-mul-one-left (second x))

#define nima-z2-scale-assoc (a b : MariciInt) (x : NimaZ2)
  : nima-z2-scale (marici-int-mul a b) x = nima-z2-scale a (nima-z2-scale b x)
  := nima-z2-path (nima-z2-scale (marici-int-mul a b) x) (nima-z2-scale a (nima-z2-scale b x))
       (marici-int-mul-assoc a b (first x)) (marici-int-mul-assoc a b (second x))

#define nima-z2-scale-add (a : MariciInt) (x y : NimaZ2)
  : nima-z2-scale a (nima-z2-add x y) = nima-z2-add (nima-z2-scale a x) (nima-z2-scale a y)
  := nima-z2-path (nima-z2-scale a (nima-z2-add x y)) (nima-z2-add (nima-z2-scale a x) (nima-z2-scale a y))
       (marici-int-mul-add-left-distrib a (first x) (first y))
       (marici-int-mul-add-left-distrib a (second x) (second y))

#define nima-z2-add-scale (a b : MariciInt) (x : NimaZ2)
  : nima-z2-scale (marici-int-add a b) x = nima-z2-add (nima-z2-scale a x) (nima-z2-scale b x)
  := nima-z2-path (nima-z2-scale (marici-int-add a b) x) (nima-z2-add (nima-z2-scale a x) (nima-z2-scale b x))
       (marici-int-mul-add-right-distrib a b (first x))
       (marici-int-mul-add-right-distrib a b (second x))

#define nima-z2-d (x : NimaZ2) : NimaZ2 := (second x,marici-int-zero)
#define nima-z2-H (x : NimaZ2) : NimaZ2 := (marici-int-zero,first x)
#define nima-z2-d-square (x : NimaZ2) : nima-z2-d (nima-z2-d x) = nima-z2-zero := refl
#define nima-z2-H-square (x : NimaZ2) : nima-z2-H (nima-z2-H x) = nima-z2-zero := refl
#define nima-z2-d-add (x y : NimaZ2)
  : nima-z2-d (nima-z2-add x y) = nima-z2-add (nima-z2-d x) (nima-z2-d y) := refl
#define nima-z2-H-add (x y : NimaZ2)
  : nima-z2-H (nima-z2-add x y) = nima-z2-add (nima-z2-H x) (nima-z2-H y) := refl
#define nima-z2-H-sub (x y : NimaZ2)
  : nima-z2-H (nima-z2-sub x y) = nima-z2-sub (nima-z2-H x) (nima-z2-H y) := refl

#define nima-z2-d-linear (a : MariciInt) (x : NimaZ2)
  : nima-z2-d (nima-z2-scale a x) = nima-z2-scale a (nima-z2-d x)
  := nima-z2-path (nima-z2-d (nima-z2-scale a x)) (nima-z2-scale a (nima-z2-d x)) refl
       (nima-frame-rev MariciInt (marici-int-mul a marici-int-zero) marici-int-zero
         (marici-int-mul-zero-right a))

#define nima-z2-H-linear (a : MariciInt) (x : NimaZ2)
  : nima-z2-H (nima-z2-scale a x) = nima-z2-scale a (nima-z2-H x)
  := nima-z2-path (nima-z2-H (nima-z2-scale a x)) (nima-z2-scale a (nima-z2-H x))
       (nima-frame-rev MariciInt (marici-int-mul a marici-int-zero) marici-int-zero
         (marici-int-mul-zero-right a)) refl

#define nima-z2-contraction (x : NimaZ2)
  : nima-z2-add (nima-z2-d (nima-z2-H x)) (nima-z2-H (nima-z2-d x)) = x
  := nima-z2-path (nima-z2-add (nima-z2-d (nima-z2-H x)) (nima-z2-H (nima-z2-d x))) x
       (marici-int-add-zero-right (first x)) refl

#define nima-constant-index-transport
  (A : U) (i j : MariciInt) (p : i = j) (x : A)
  : nima-hom-transport MariciInt (\ _ -> A) i j p x = x
  := idJ (MariciInt, i,
       (\ j' p' -> nima-hom-transport MariciInt (\ _ -> A) i j' p' x = x), refl, j, p)

#define nima-z2-hom-H
  : nima-integer-hom (\ _ -> NimaZ2) (\ _ -> NimaZ2) marici-int-minus-one
  := \ i x -> nima-z2-H x

#define nima-z2-hom-H-boundary (i : MariciInt) (x : NimaZ2)
  : nima-integer-hom-differential (\ _ -> NimaZ2) (\ _ -> NimaZ2)
      (\ _ -> nima-z2-d) (\ _ -> nima-z2-d)
      (\ _ -> nima-z2-add) (\ _ -> nima-z2-sub)
      marici-int-minus-one nima-z2-hom-H i x = x
  := nima-frame-concat NimaZ2
       (nima-integer-hom-differential (\ _ -> NimaZ2) (\ _ -> NimaZ2)
         (\ _ -> nima-z2-d) (\ _ -> nima-z2-d)
         (\ _ -> nima-z2-add) (\ _ -> nima-z2-sub)
         marici-int-minus-one nima-z2-hom-H i x)
       (nima-z2-add (nima-z2-d (nima-z2-H x)) (nima-z2-H (nima-z2-d x))) x
       (nima-cochain-ap2 NimaZ2 NimaZ2 NimaZ2 nima-z2-add
         (nima-hom-transport MariciInt (\ _ -> NimaZ2)
           (nima-z-next (nima-z-shift marici-int-minus-one i))
           (nima-z-shift (nima-z-next marici-int-minus-one) i)
           (nima-z-target-step marici-int-minus-one i) (nima-z2-d (nima-z2-H x)))
         (nima-z2-d (nima-z2-H x))
         (nima-hom-transport MariciInt (\ _ -> NimaZ2)
           (nima-z-shift marici-int-minus-one (nima-z-next i))
           (nima-z-shift (nima-z-next marici-int-minus-one) i)
           (nima-z-source-step marici-int-minus-one i) (nima-z2-H (nima-z2-d x)))
         (nima-z2-H (nima-z2-d x))
         (nima-constant-index-transport NimaZ2
           (nima-z-next (nima-z-shift marici-int-minus-one i))
           (nima-z-shift (nima-z-next marici-int-minus-one) i)
           (nima-z-target-step marici-int-minus-one i) (nima-z2-d (nima-z2-H x)))
         (nima-constant-index-transport NimaZ2
           (nima-z-shift marici-int-minus-one (nima-z-next i))
           (nima-z-shift (nima-z-next marici-int-minus-one) i)
           (nima-z-source-step marici-int-minus-one i) (nima-z2-H (nima-z2-d x))))
       (nima-z2-contraction x)
```

The final theorem applies the actual parity-selected, integer-indexed Hom
differential with its transports. It proves a concrete Hom boundary in every
integer source degree, not just a finite sample. Derived-category localization,
K-projective resolutions and the physical coefficient modules remain separate.
