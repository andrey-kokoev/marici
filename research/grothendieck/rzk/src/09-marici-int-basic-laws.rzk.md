# Marici canonical-integer basic laws

This increment proves multiplicative commutativity and additive cancellation
against the computational negation.

```rzk
#lang rzk-1
```

The predecessor formula for positive products is symmetric because natural
addition and multiplication are commutative.

```rzk
#define marici-positive-product-predecessor-comm
  ( a b : MariciNat)
  : marici-positive-product-predecessor a b
    =_{MariciNat} marici-positive-product-predecessor b a
  := concat MariciNat
      (marici-add a (marici-add b (marici-mul a b)))
      (marici-add b (marici-add a (marici-mul a b)))
      (marici-add b (marici-add a (marici-mul b a)))
      (marici-add-swap-prefix a b (marici-mul a b))
      (ap MariciNat MariciNat
        (marici-mul a b) (marici-mul b a)
        (\ q → marici-add b (marici-add a q))
        (marici-mul-comm a b))

#define marici-int-mul-comm
  ( x y : MariciInt)
  : marici-int-mul x y =_{MariciInt} marici-int-mul y x
  := match x
      ( marici-int-zero ⇒
          rev MariciInt
            (marici-int-mul y marici-int-zero) marici-int-zero
            (marici-int-mul-zero-right y)
      | marici-int-pos a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒
                ap MariciNat MariciInt
                  (marici-positive-product-predecessor a b)
                  (marici-positive-product-predecessor b a)
                  marici-int-pos
                  (marici-positive-product-predecessor-comm a b)
            | marici-int-neg b ⇒
                ap MariciNat MariciInt
                  (marici-positive-product-predecessor a b)
                  (marici-positive-product-predecessor b a)
                  marici-int-neg
                  (marici-positive-product-predecessor-comm a b))
      | marici-int-neg a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒
                ap MariciNat MariciInt
                  (marici-positive-product-predecessor a b)
                  (marici-positive-product-predecessor b a)
                  marici-int-neg
                  (marici-positive-product-predecessor-comm a b)
            | marici-int-neg b ⇒
                ap MariciNat MariciInt
                  (marici-positive-product-predecessor a b)
                  (marici-positive-product-predecessor b a)
                  marici-int-pos
                  (marici-positive-product-predecessor-comm a b)))
```

The comparison theorem `compare a a = equal` transports each mixed-sign
addition to its cancellation branch.

```rzk
#define marici-int-add-pos-neg-self
  ( a : MariciNat)
  : marici-int-add-pos-neg a a =_{MariciInt} marici-int-zero
  := idJ
      ( MariciOrdering , marici-equal
      , \ q p →
          (match q into (\ _ → MariciInt)
            ( marici-less ⇒ marici-int-neg (marici-sub a (marici-succ a))
            | marici-equal ⇒ marici-int-zero
            | marici-greater ⇒ marici-int-pos (marici-sub a (marici-succ a))))
          =_{MariciInt} marici-int-zero
      , refl , marici-compare a a
      , rev MariciOrdering
          (marici-compare a a) marici-equal
          (marici-compare-self a))

#define marici-int-add-neg-pos-self
  ( a : MariciNat)
  : marici-int-add-neg-pos a a =_{MariciInt} marici-int-zero
  := marici-int-add-pos-neg-self a

#define marici-int-add-inverse-right
  ( x : MariciInt)
  : marici-int-add x (marici-int-negate x)
    =_{MariciInt} marici-int-zero
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ marici-int-add-pos-neg-self a
      | marici-int-neg a ⇒ marici-int-add-neg-pos-self a)

#define marici-int-add-inverse-left
  ( x : MariciInt)
  : marici-int-add (marici-int-negate x) x
    =_{MariciInt} marici-int-zero
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ marici-int-add-neg-pos-self a
      | marici-int-neg a ⇒ marici-int-add-pos-neg-self a)
```

Zero laws compute directly from the canonical constructors.

```rzk
#define marici-int-add-zero-left
  ( x : MariciInt)
  : marici-int-add marici-int-zero x =_{MariciInt} x
  := refl

#define marici-int-add-zero-right
  ( x : MariciInt)
  : marici-int-add x marici-int-zero =_{MariciInt} x
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ refl
      | marici-int-neg a ⇒ refl)
```

## Boundary

The canonical integers now have checked additive zero and inverse laws and
commutative multiplication. Addition commutativity/associativity,
multiplicative associativity, distributivity, sethood, and the universal
property remain open.
