# Marici canonical-integer multiplication

The product of predecessor-coded positive magnitudes `a` and `b` has
predecessor

```text
a + b + a*b,
```

because `(a+1)(b+1) = (a+b+a*b)+1`. This derives signed multiplication without
an integer quotient or opaque normalization function.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-predecessor
  ( a b : MariciNat)
  : MariciNat
  := marici-add a (marici-add b (marici-mul a b))

#define marici-int-mul
  ( x y : MariciInt)
  : MariciInt
  := (match x into (\ _ → MariciInt → MariciInt)
      ( marici-int-zero ⇒ \ q → marici-int-zero
      | marici-int-pos a ⇒
          \ q → match q
            ( marici-int-zero ⇒ marici-int-zero
            | marici-int-pos b ⇒
                marici-int-pos (marici-positive-product-predecessor a b)
            | marici-int-neg b ⇒
                marici-int-neg (marici-positive-product-predecessor a b))
      | marici-int-neg a ⇒
          \ q → match q
            ( marici-int-zero ⇒ marici-int-zero
            | marici-int-pos b ⇒
                marici-int-neg (marici-positive-product-predecessor a b)
            | marici-int-neg b ⇒
                marici-int-pos (marici-positive-product-predecessor a b)))) y
```

Zero on the right and one on the left compute by case analysis. One on the right
uses the previously proved natural-number right-zero law inside each signed
constructor.

```rzk
#define marici-int-mul-zero-left
  ( x : MariciInt)
  : marici-int-mul marici-int-zero x =_{MariciInt} marici-int-zero
  := refl

#define marici-int-mul-zero-right
  ( x : MariciInt)
  : marici-int-mul x marici-int-zero =_{MariciInt} marici-int-zero
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒ refl
      | marici-int-neg a ⇒ refl)

#define marici-int-mul-one-left
  ( x : MariciInt)
  : marici-int-mul marici-int-one x =_{MariciInt} x
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          ap MariciNat MariciInt
            (marici-add a marici-zero) a
            marici-int-pos (marici-add-zero-right a)
      | marici-int-neg a ⇒
          ap MariciNat MariciInt
            (marici-add a marici-zero) a
            marici-int-neg (marici-add-zero-right a))

#define marici-positive-product-one-right
  ( a : MariciNat)
  : marici-positive-product-predecessor a marici-zero
    =_{MariciNat} a
  := concat MariciNat
      (marici-positive-product-predecessor a marici-zero)
      (marici-add a marici-zero)
      a
      (ap MariciNat MariciNat
        (marici-mul a marici-zero) marici-zero
        (\ q → marici-add a q)
        (marici-mul-zero-right a))
      (marici-add-zero-right a)

#define marici-int-mul-one-right
  ( x : MariciInt)
  : marici-int-mul x marici-int-one =_{MariciInt} x
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          ap MariciNat MariciInt
            (marici-positive-product-predecessor a marici-zero) a
            marici-int-pos (marici-positive-product-one-right a)
      | marici-int-neg a ⇒
          ap MariciNat MariciInt
            (marici-positive-product-predecessor a marici-zero) a
            marici-int-neg (marici-positive-product-one-right a))
```

Closed sign tests ensure that normalization does not create an alternative zero
or lose the intended predecessor magnitude.

```rzk
#define marici-int-minus-one-times-minus-one
  : marici-int-mul marici-int-minus-one marici-int-minus-one
    =_{MariciInt} marici-int-one
  := refl

#define marici-int-minus-two-times-two
  : marici-int-mul marici-int-minus-two marici-int-two
    =_{MariciInt} marici-int-neg marici-three
  := refl

#define marici-int-two-times-two
  : marici-int-mul marici-int-two marici-int-two
    =_{MariciInt} marici-int-pos marici-three
  := refl
```

## Boundary

This module constructs signed multiplication and proves its zero/unit laws.
Commutativity, associativity, distributivity over normalized mixed-sign
addition, and compatibility with negation remain theorem obligations.
