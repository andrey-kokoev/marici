# Positive canonical-integer factor cancellation

Left multiplication by every positive canonical integer is injective. Equal
sign cases use positive-product predecessor injectivity; mixed constructor
cases are eliminated by canonical-integer no-confusion.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-positive-left-injective
  ( p : MariciNat)
  ( x y : MariciInt)
  ( e : marici-int-mul (marici-int-pos p) x
      =_{MariciInt} marici-int-mul (marici-int-pos p) y)
  : x =_{MariciInt} y
  := (match x into
        (\ x-prime → (y-prime : MariciInt)
          → (marici-int-mul (marici-int-pos p) x-prime
              =_{MariciInt} marici-int-mul (marici-int-pos p) y-prime)
          → x-prime =_{MariciInt} y-prime)
      ( marici-int-zero ⇒ \ q → match q
          ( marici-int-zero ⇒ \ h → refl
          | marici-int-pos b ⇒ \ h →
              marici-empty-elim
                (marici-int-zero =_{MariciInt} marici-int-pos b)
                (marici-int-zero-not-pos
                  (marici-positive-product-predecessor p b) h)
          | marici-int-neg b ⇒ \ h →
              marici-empty-elim
                (marici-int-zero =_{MariciInt} marici-int-neg b)
                (marici-int-zero-not-neg
                  (marici-positive-product-predecessor p b) h))
      | marici-int-pos a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ h →
              marici-empty-elim
                (marici-int-pos a =_{MariciInt} marici-int-zero)
                (marici-int-pos-not-zero
                  (marici-positive-product-predecessor p a) h)
          | marici-int-pos b ⇒ \ h →
              ap MariciNat MariciInt a b marici-int-pos
                (marici-positive-product-predecessor-injective p a b
                  (marici-int-pos-injective
                    (marici-positive-product-predecessor p a)
                    (marici-positive-product-predecessor p b) h))
          | marici-int-neg b ⇒ \ h →
              marici-empty-elim
                (marici-int-pos a =_{MariciInt} marici-int-neg b)
                (marici-int-pos-not-neg
                  (marici-positive-product-predecessor p a)
                  (marici-positive-product-predecessor p b) h))
      | marici-int-neg a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ h →
              marici-empty-elim
                (marici-int-neg a =_{MariciInt} marici-int-zero)
                (marici-int-neg-not-zero
                  (marici-positive-product-predecessor p a) h)
          | marici-int-pos b ⇒ \ h →
              marici-empty-elim
                (marici-int-neg a =_{MariciInt} marici-int-pos b)
                (marici-int-neg-not-pos
                  (marici-positive-product-predecessor p a)
                  (marici-positive-product-predecessor p b) h)
          | marici-int-neg b ⇒ \ h →
              ap MariciNat MariciInt a b marici-int-neg
                (marici-positive-product-predecessor-injective p a b
                  (marici-int-neg-injective
                    (marici-positive-product-predecessor p a)
                    (marici-positive-product-predecessor p b) h))))) y e
```

## Boundary

Positive canonical-integer left multiplication is injective for arbitrary
integer inputs. The right orientation follows through integer multiplication
commutativity; applying it to the raw-fraction transitivity derivation remains.
