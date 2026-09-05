# Marici natural-to-integer embedding

This increment proves that the constructor-derived embedding preserves zero,
one, addition, and multiplication. It is the first checked arithmetic
interpretation map between independently defined carriers.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-embed-zero
  : marici-int-embed-nat marici-zero
    =_{MariciInt} marici-int-zero
  := refl

#define marici-int-embed-one
  : marici-int-embed-nat marici-one
    =_{MariciInt} marici-int-one
  := refl

#define marici-int-embed-add
  ( n m : MariciNat)
  : marici-int-embed-nat (marici-add n m)
    =_{MariciInt}
      marici-int-add (marici-int-embed-nat n) (marici-int-embed-nat m)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ a ih ⇒
          match m
            ( marici-zero ⇒
                ap MariciNat MariciInt
                  (marici-add a marici-zero) a
                  marici-int-pos
                  (marici-add-zero-right a)
            | marici-succ b bh ⇒
                ap MariciNat MariciInt
                  (marici-add a (marici-succ b))
                  (marici-succ (marici-add a b))
                  marici-int-pos
                  (marici-add-succ-right a b)))
```

For positive inputs, preservation of multiplication reduces to the predecessor
identity. The first step applies multiplication-by-successor; the second swaps
the two additive prefixes.

```rzk
#define marici-positive-embed-product-predecessor
  ( a b : MariciNat)
  : marici-add b (marici-mul a (marici-succ b))
    =_{MariciNat} marici-positive-product-predecessor a b
  := concat MariciNat
      (marici-add b (marici-mul a (marici-succ b)))
      (marici-add b (marici-add a (marici-mul a b)))
      (marici-add a (marici-add b (marici-mul a b)))
      (ap MariciNat MariciNat
        (marici-mul a (marici-succ b))
        (marici-add a (marici-mul a b))
        (\ q → marici-add b q)
        (marici-mul-succ-right a b))
      (marici-add-swap-prefix b a (marici-mul a b))

#define marici-int-embed-mul
  ( n m : MariciNat)
  : marici-int-embed-nat (marici-mul n m)
    =_{MariciInt}
      marici-int-mul (marici-int-embed-nat n) (marici-int-embed-nat m)
  := match n
      ( marici-zero ⇒ refl
      | marici-succ a ih ⇒
          match m
            ( marici-zero ⇒
                ap MariciNat MariciInt
                  (marici-mul a marici-zero) marici-zero
                  marici-int-embed-nat
                  (marici-mul-zero-right a)
            | marici-succ b bh ⇒
                ap MariciNat MariciInt
                  (marici-add b (marici-mul a (marici-succ b)))
                  (marici-positive-product-predecessor a b)
                  marici-int-pos
                  (marici-positive-embed-product-predecessor a b)))
```

## Boundary

The embedding preserves the displayed operations by checked paths. Calling it
a semiring homomorphism still requires a packaged semiring interface and the
sethood of both carriers; this file does not silently assume either.
