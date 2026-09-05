# Positive natural-factor cancellation

Multiplication by a successor natural is injective. Simultaneous recursion uses
zero--successor disjointness on the mixed constructor cases and additive-prefix
injectivity on the successor--successor case.

```rzk
#lang rzk-1
```

```rzk
#define marici-mul-positive-left-injective
  ( p a b : MariciNat)
  ( e : marici-mul (marici-succ p) a
      =_{MariciNat} marici-mul (marici-succ p) b)
  : a =_{MariciNat} b
  := (match a into
        (\ a-prime →
          (b-prime : MariciNat)
          → (marici-mul (marici-succ p) a-prime
              =_{MariciNat} marici-mul (marici-succ p) b-prime)
          → a-prime =_{MariciNat} b-prime)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒ \ h → refl
          | marici-succ j jh ⇒ \ h →
              marici-empty-elim
                (marici-zero =_{MariciNat} marici-succ j)
                (marici-zero-not-succ
                  (marici-positive-product-predecessor p j)
                  (concat MariciNat
                    marici-zero
                    (marici-mul (marici-succ p) marici-zero)
                    (marici-succ
                      (marici-positive-product-predecessor p j))
                    (rev MariciNat
                      (marici-mul (marici-succ p) marici-zero)
                      marici-zero
                      (marici-mul-zero-right (marici-succ p)))
                    (concat MariciNat
                      (marici-mul (marici-succ p) marici-zero)
                      (marici-mul (marici-succ p) (marici-succ j))
                      (marici-succ
                        (marici-positive-product-predecessor p j))
                      h
                      (rev MariciNat
                        (marici-succ
                          (marici-positive-product-predecessor p j))
                        (marici-mul (marici-succ p) (marici-succ j))
                        (marici-succ-positive-product p j))))))
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒ \ h →
              marici-empty-elim
                ((marici-succ i) =_{MariciNat} marici-zero)
                (marici-succ-not-zero
                  (marici-positive-product-predecessor p i)
                  (concat MariciNat
                    (marici-succ
                      (marici-positive-product-predecessor p i))
                    (marici-mul (marici-succ p) (marici-succ i))
                    marici-zero
                    (marici-succ-positive-product p i)
                    (concat MariciNat
                      (marici-mul (marici-succ p) (marici-succ i))
                      (marici-mul (marici-succ p) marici-zero)
                      marici-zero
                      h
                      (marici-mul-zero-right (marici-succ p)))))
          | marici-succ j jh ⇒ \ h →
              ap MariciNat MariciNat i j marici-succ
                (ih j
                  (marici-add-prefix-injective (marici-succ p)
                  (marici-mul (marici-succ p) i)
                  (marici-mul (marici-succ p) j)
                  (concat MariciNat
                    (marici-add (marici-succ p)
                      (marici-mul (marici-succ p) i))
                    (marici-mul (marici-succ p) (marici-succ i))
                    (marici-add (marici-succ p)
                      (marici-mul (marici-succ p) j))
                    (rev MariciNat
                      (marici-mul (marici-succ p) (marici-succ i))
                      (marici-add (marici-succ p)
                        (marici-mul (marici-succ p) i))
                      (marici-mul-succ-right (marici-succ p) i))
                    (concat MariciNat
                      (marici-mul (marici-succ p) (marici-succ i))
                      (marici-mul (marici-succ p) (marici-succ j))
                      (marici-add (marici-succ p)
                        (marici-mul (marici-succ p) j))
                      h
                      (marici-mul-succ-right (marici-succ p) j)))))))) b e
```

## Boundary

This proves left multiplication cancellation for every positive natural factor.
The right orientation follows from multiplication commutativity. Transport to
canonical integer multiplication remains before raw-fraction transitivity can
use the result.
