# Marici integer multiplication and sign

The signed multiplication definition makes compatibility with additive
negation computational after case analysis. These paths are proved separately
rather than inferred from unproved distributivity.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-mul-negate-left
  ( x y : MariciInt)
  : marici-int-mul (marici-int-negate x) y
    =_{MariciInt} marici-int-negate (marici-int-mul x y)
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒ refl
            | marici-int-neg b ⇒ refl)
      | marici-int-neg a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒ refl
            | marici-int-neg b ⇒ refl))

#define marici-int-mul-negate-right
  ( x y : MariciInt)
  : marici-int-mul x (marici-int-negate y)
    =_{MariciInt} marici-int-negate (marici-int-mul x y)
  := match x
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒ refl
            | marici-int-neg b ⇒ refl)
      | marici-int-neg a ⇒
          match y
            ( marici-int-zero ⇒ refl
            | marici-int-pos b ⇒ refl
            | marici-int-neg b ⇒ refl))

#define marici-int-mul-negate-both
  ( x y : MariciInt)
  : marici-int-mul (marici-int-negate x) (marici-int-negate y)
    =_{MariciInt} marici-int-mul x y
  := concat MariciInt
      (marici-int-mul (marici-int-negate x) (marici-int-negate y))
      (marici-int-negate
        (marici-int-mul x (marici-int-negate y)))
      (marici-int-mul x y)
      (marici-int-mul-negate-left x (marici-int-negate y))
      (concat MariciInt
        (marici-int-negate
          (marici-int-mul x (marici-int-negate y)))
        (marici-int-negate
          (marici-int-negate (marici-int-mul x y)))
        (marici-int-mul x y)
        (ap MariciInt MariciInt
          (marici-int-mul x (marici-int-negate y))
          (marici-int-negate (marici-int-mul x y))
          marici-int-negate
          (marici-int-mul-negate-right x y))
        (marici-int-negate-involutive (marici-int-mul x y)))
```

Multiplication by negative one follows from the unit laws and the sign laws;
it is not a separate constructor computation for an unknown integer.

```rzk
#define marici-int-mul-minus-one-left
  ( x : MariciInt)
  : marici-int-mul marici-int-minus-one x
    =_{MariciInt} marici-int-negate x
  := concat MariciInt
      (marici-int-mul marici-int-minus-one x)
      (marici-int-negate (marici-int-mul marici-int-one x))
      (marici-int-negate x)
      (marici-int-mul-negate-left marici-int-one x)
      (ap MariciInt MariciInt
        (marici-int-mul marici-int-one x) x
        marici-int-negate
        (marici-int-mul-one-left x))

#define marici-int-mul-minus-one-right
  ( x : MariciInt)
  : marici-int-mul x marici-int-minus-one
    =_{MariciInt} marici-int-negate x
  := concat MariciInt
      (marici-int-mul x marici-int-minus-one)
      (marici-int-negate (marici-int-mul x marici-int-one))
      (marici-int-negate x)
      (marici-int-mul-negate-right x marici-int-one)
      (ap MariciInt MariciInt
        (marici-int-mul x marici-int-one) x
        marici-int-negate
        (marici-int-mul-one-right x))
```

## Boundary

These five laws certify sign transport for multiplication. They do not use or
establish multiplication associativity or distributivity.
