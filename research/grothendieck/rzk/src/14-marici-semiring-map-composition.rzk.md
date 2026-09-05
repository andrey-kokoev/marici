# Composition of Marici arithmetic interpretation maps

This file proves that the operation-preservation interface has identity maps
and is closed under composition. It is an ordinary algebraic precursor to the
simplicial realization; no categorical structure is inferred from similar
notation.

```rzk
#lang rzk-1
```

```rzk
#define marici-id-map
  ( A : U)
  : A → A
  := \ x → x

#define marici-compose-map
  ( A B C : U)
  ( f : A → B)
  ( g : B → C)
  : A → C
  := \ x → g (f x)

#define marici-semiring-map-id-laws
  ( A : U)
  ( zero one : A)
  ( add mul : A → A → A)
  : MariciSemiringMapLaws
      A A zero one add mul zero one add mul (marici-id-map A)
  := marici-make-semiring-map-laws
      A A zero one add mul zero one add mul (marici-id-map A)
      refl refl (\ x y → refl) (\ x y → refl)
```

The composition proof consumes the two law packages. Each composite path first
applies the outer map to the inner preservation path, then applies the outer
preservation law.

```rzk
#define marici-semiring-map-compose-laws
  ( A B C : U)
  ( zero-A one-A : A)
  ( add-A mul-A : A → A → A)
  ( zero-B one-B : B)
  ( add-B mul-B : B → B → B)
  ( zero-C one-C : C)
  ( add-C mul-C : C → C → C)
  ( f : A → B)
  ( g : B → C)
  ( f-laws : MariciSemiringMapLaws
      A B zero-A one-A add-A mul-A zero-B one-B add-B mul-B f)
  ( g-laws : MariciSemiringMapLaws
      B C zero-B one-B add-B mul-B zero-C one-C add-C mul-C g)
  : MariciSemiringMapLaws
      A C zero-A one-A add-A mul-A zero-C one-C add-C mul-C
      (marici-compose-map A B C f g)
  := match f-laws
      ( marici-make-semiring-map-laws f-zero f-one f-add f-mul ⇒
          match g-laws
            ( marici-make-semiring-map-laws g-zero g-one g-add g-mul ⇒
                marici-make-semiring-map-laws
                  A C zero-A one-A add-A mul-A
                  zero-C one-C add-C mul-C
                  (marici-compose-map A B C f g)
                  (concat C
                    (g (f zero-A)) (g zero-B) zero-C
                    (ap B C (f zero-A) zero-B g f-zero)
                    g-zero)
                  (concat C
                    (g (f one-A)) (g one-B) one-C
                    (ap B C (f one-A) one-B g f-one)
                    g-one)
                  (\ x y → concat C
                    (g (f (add-A x y)))
                    (g (add-B (f x) (f y)))
                    (add-C (g (f x)) (g (f y)))
                    (ap B C
                      (f (add-A x y)) (add-B (f x) (f y))
                      g (f-add x y))
                    (g-add (f x) (f y)))
                  (\ x y → concat C
                    (g (f (mul-A x y)))
                    (g (mul-B (f x) (f y)))
                    (mul-C (g (f x)) (g (f y)))
                    (ap B C
                      (f (mul-A x y)) (mul-B (f x) (f y))
                      g (f-mul x y))
                    (g-mul (f x) (f y)))))
```

The existing natural-to-integer map composes with the integer identity map,
providing a concrete acceptance test for the generic constructor.

```rzk
#define marici-nat-int-map-laws-compose-id
  : MariciSemiringMapLaws
      MariciNat MariciInt
      marici-zero marici-one marici-add marici-mul
      marici-int-zero marici-int-one marici-int-add marici-int-mul
      (marici-compose-map MariciNat MariciInt MariciInt
        marici-int-embed-nat (marici-id-map MariciInt))
  := marici-semiring-map-compose-laws
      MariciNat MariciInt MariciInt
      marici-zero marici-one marici-add marici-mul
      marici-int-zero marici-int-one marici-int-add marici-int-mul
      marici-int-zero marici-int-one marici-int-add marici-int-mul
      marici-int-embed-nat (marici-id-map MariciInt)
      marici-nat-int-map-laws
      (marici-semiring-map-id-laws
        MariciInt marici-int-zero marici-int-one
        marici-int-add marici-int-mul)
```

## Boundary

Identity and composition preserve the four declared operations. This does not
construct a Rezk type of semirings or maps: that requires sethood or another
mapping-space truncation argument, plus a typed simplicial realization.
