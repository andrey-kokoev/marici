# Marici integer multiplication associativity

The predecessor formula is related to ordinary positive natural
multiplication, used to derive its associativity rather than expanding a large
polynomial normalization by hand.

```rzk
#lang rzk-1
```

```rzk
#define marici-pred
  ( n : MariciNat)
  : MariciNat
  := match n
      ( marici-zero ⇒ marici-zero
      | marici-succ k ih ⇒ k)

#define marici-succ-positive-product
  ( a b : MariciNat)
  : marici-succ (marici-positive-product-predecessor a b)
    =_{MariciNat} marici-mul (marici-succ a) (marici-succ b)
  := ap MariciNat MariciNat
      (marici-positive-product-predecessor a b)
      (marici-add b (marici-mul a (marici-succ b)))
      marici-succ
      (rev MariciNat
        (marici-add b (marici-mul a (marici-succ b)))
        (marici-positive-product-predecessor a b)
        (marici-positive-embed-product-predecessor a b))
```

The successor-level chain factors through natural multiplication
associativity. Applying predecessor recovers equality of the encoded positive
magnitudes.

```rzk
#define marici-positive-product-predecessor-assoc
  ( a b c : MariciNat)
  : marici-positive-product-predecessor
      (marici-positive-product-predecessor a b) c
    =_{MariciNat}
      marici-positive-product-predecessor
        a (marici-positive-product-predecessor b c)
  := ap MariciNat MariciNat
      (marici-succ
        (marici-positive-product-predecessor
          (marici-positive-product-predecessor a b) c))
      (marici-succ
        (marici-positive-product-predecessor
          a (marici-positive-product-predecessor b c)))
      marici-pred
      (concat MariciNat
        (marici-succ
          (marici-positive-product-predecessor
            (marici-positive-product-predecessor a b) c))
        (marici-mul
          (marici-succ (marici-positive-product-predecessor a b))
          (marici-succ c))
        (marici-succ
          (marici-positive-product-predecessor
            a (marici-positive-product-predecessor b c)))
        (marici-succ-positive-product
          (marici-positive-product-predecessor a b) c)
        (concat MariciNat
          (marici-mul
            (marici-succ (marici-positive-product-predecessor a b))
            (marici-succ c))
          (marici-mul
            (marici-mul (marici-succ a) (marici-succ b))
            (marici-succ c))
          (marici-succ
            (marici-positive-product-predecessor
              a (marici-positive-product-predecessor b c)))
          (ap MariciNat MariciNat
            (marici-succ (marici-positive-product-predecessor a b))
            (marici-mul (marici-succ a) (marici-succ b))
            (\ q → marici-mul q (marici-succ c))
            (marici-succ-positive-product a b))
          (concat MariciNat
            (marici-mul
              (marici-mul (marici-succ a) (marici-succ b))
              (marici-succ c))
            (marici-mul
              (marici-succ a)
              (marici-mul (marici-succ b) (marici-succ c)))
            (marici-succ
              (marici-positive-product-predecessor
                a (marici-positive-product-predecessor b c)))
            (marici-mul-assoc
              (marici-succ a) (marici-succ b) (marici-succ c))
            (concat MariciNat
              (marici-mul
                (marici-succ a)
                (marici-mul (marici-succ b) (marici-succ c)))
              (marici-mul
                (marici-succ a)
                (marici-succ (marici-positive-product-predecessor b c)))
              (marici-succ
                (marici-positive-product-predecessor
                  a (marici-positive-product-predecessor b c)))
              (ap MariciNat MariciNat
                (marici-mul (marici-succ b) (marici-succ c))
                (marici-succ (marici-positive-product-predecessor b c))
                (\ q → marici-mul (marici-succ a) q)
                (rev MariciNat
                  (marici-succ (marici-positive-product-predecessor b c))
                  (marici-mul (marici-succ b) (marici-succ c))
                  (marici-succ-positive-product b c)))
              (rev MariciNat
                (marici-succ
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c)))
                (marici-mul
                  (marici-succ a)
                  (marici-succ (marici-positive-product-predecessor b c)))
                (marici-succ-positive-product
                  a (marici-positive-product-predecessor b c)))))))
```

Signed associativity is then constructor-wise, with the same predecessor path
mapped through the sign selected by each branch.

```rzk
#define marici-int-mul-assoc
  ( x y z : MariciInt)
  : marici-int-mul (marici-int-mul x y) z
    =_{MariciInt} marici-int-mul x (marici-int-mul y z)
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ match y
          ( marici-int-zero ⇒ refl
          | marici-int-pos b ⇒ match z
              ( marici-int-zero ⇒ refl
              | marici-int-pos c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-pos
                  (marici-positive-product-predecessor-assoc a b c)
              | marici-int-neg c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-neg
                  (marici-positive-product-predecessor-assoc a b c))
          | marici-int-neg b ⇒ match z
              ( marici-int-zero ⇒ refl
              | marici-int-pos c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-neg
                  (marici-positive-product-predecessor-assoc a b c)
              | marici-int-neg c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-pos
                  (marici-positive-product-predecessor-assoc a b c)))
      | marici-int-neg a ⇒ match y
          ( marici-int-zero ⇒ refl
          | marici-int-pos b ⇒ match z
              ( marici-int-zero ⇒ refl
              | marici-int-pos c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-neg
                  (marici-positive-product-predecessor-assoc a b c)
              | marici-int-neg c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-pos
                  (marici-positive-product-predecessor-assoc a b c))
          | marici-int-neg b ⇒ match z
              ( marici-int-zero ⇒ refl
              | marici-int-pos c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-pos
                  (marici-positive-product-predecessor-assoc a b c)
              | marici-int-neg c ⇒ ap MariciNat MariciInt
                  (marici-positive-product-predecessor
                    (marici-positive-product-predecessor a b) c)
                  (marici-positive-product-predecessor
                    a (marici-positive-product-predecessor b c))
                  marici-int-neg
                  (marici-positive-product-predecessor-assoc a b c))))
```

## Boundary

Integer multiplication is now associative. Distributivity still depends on the
mixed-sign addition normalizer and remains open.
