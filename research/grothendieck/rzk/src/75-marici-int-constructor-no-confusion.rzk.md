# Canonical integer constructor no-confusion

Constructor payload decoders prove injectivity of positive and negative
constructors. Type-valued discriminators separate zero, positive, and negative
constructors.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-pos-payload
  ( z : MariciInt)
  : MariciNat
  := match z
      ( marici-int-zero ⇒ marici-zero
      | marici-int-pos n ⇒ n
      | marici-int-neg n ⇒ marici-zero)

#define marici-int-neg-payload
  ( z : MariciInt)
  : MariciNat
  := match z
      ( marici-int-zero ⇒ marici-zero
      | marici-int-pos n ⇒ marici-zero
      | marici-int-neg n ⇒ n)

#define marici-int-pos-injective
  ( a b : MariciNat)
  ( e : marici-int-pos a =_{MariciInt} marici-int-pos b)
  : a =_{MariciNat} b
  := ap MariciInt MariciNat
      (marici-int-pos a) (marici-int-pos b) marici-int-pos-payload e

#define marici-int-neg-injective
  ( a b : MariciNat)
  ( e : marici-int-neg a =_{MariciInt} marici-int-neg b)
  : a =_{MariciNat} b
  := ap MariciInt MariciNat
      (marici-int-neg a) (marici-int-neg b) marici-int-neg-payload e
```

```rzk
#define marici-int-is-zero-code
  ( z : MariciInt)
  : U
  := match z
      ( marici-int-zero ⇒ MariciUnit
      | marici-int-pos n ⇒ MariciEmpty
      | marici-int-neg n ⇒ MariciEmpty)

#define marici-int-is-pos-code
  ( z : MariciInt)
  : U
  := match z
      ( marici-int-zero ⇒ MariciEmpty
      | marici-int-pos n ⇒ MariciUnit
      | marici-int-neg n ⇒ MariciEmpty)

#define marici-int-zero-not-pos
  ( n : MariciNat)
  ( e : marici-int-zero =_{MariciInt} marici-int-pos n)
  : MariciEmpty
  := transport MariciInt marici-int-is-zero-code
      marici-int-zero (marici-int-pos n) e marici-unit

#define marici-int-zero-not-neg
  ( n : MariciNat)
  ( e : marici-int-zero =_{MariciInt} marici-int-neg n)
  : MariciEmpty
  := transport MariciInt marici-int-is-zero-code
      marici-int-zero (marici-int-neg n) e marici-unit

#define marici-int-pos-not-zero
  ( n : MariciNat)
  ( e : marici-int-pos n =_{MariciInt} marici-int-zero)
  : MariciEmpty
  := marici-int-zero-not-pos n
      (rev MariciInt (marici-int-pos n) marici-int-zero e)

#define marici-int-neg-not-zero
  ( n : MariciNat)
  ( e : marici-int-neg n =_{MariciInt} marici-int-zero)
  : MariciEmpty
  := marici-int-zero-not-neg n
      (rev MariciInt (marici-int-neg n) marici-int-zero e)

#define marici-int-pos-not-neg
  ( a b : MariciNat)
  ( e : marici-int-pos a =_{MariciInt} marici-int-neg b)
  : MariciEmpty
  := transport MariciInt marici-int-is-pos-code
      (marici-int-pos a) (marici-int-neg b) e marici-unit

#define marici-int-neg-not-pos
  ( a b : MariciNat)
  ( e : marici-int-neg a =_{MariciInt} marici-int-pos b)
  : MariciEmpty
  := marici-int-pos-not-neg b a
      (rev MariciInt (marici-int-neg a) (marici-int-pos b) e)
```

## Boundary

This establishes constructor injectivity and pairwise disjointness for canonical
integers. It does not prove uniqueness of identity paths. Combined with natural
positive-factor cancellation, it supplies the case analysis needed for
injectivity of multiplication by a positive canonical integer.
