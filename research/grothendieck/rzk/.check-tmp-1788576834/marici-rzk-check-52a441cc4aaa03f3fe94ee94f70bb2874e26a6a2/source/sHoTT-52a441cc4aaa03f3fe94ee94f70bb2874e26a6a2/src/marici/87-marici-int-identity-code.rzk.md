# An identity code for canonical integers

Matching signed constructors receive either the singleton code for zero or the
natural identity code for their predecessor magnitudes. Every mixed-constructor
pair receives the empty type.

```rzk
#lang rzk-1
```

```rzk
#define MariciIntIdentityCode
  ( z w : MariciInt)
  : U
  := (match z into (\ _ → MariciInt → U)
      ( marici-int-zero ⇒ \ q → match q
          ( marici-int-zero ⇒ MariciUnit
          | marici-int-pos b ⇒ MariciEmpty
          | marici-int-neg b ⇒ MariciEmpty)
      | marici-int-pos a ⇒ \ q → match q
          ( marici-int-zero ⇒ MariciEmpty
          | marici-int-pos b ⇒ MariciNatIdentityCode a b
          | marici-int-neg b ⇒ MariciEmpty)
      | marici-int-neg a ⇒ \ q → match q
          ( marici-int-zero ⇒ MariciEmpty
          | marici-int-pos b ⇒ MariciEmpty
          | marici-int-neg b ⇒ MariciNatIdentityCode a b))) w

#define marici-int-identity-code-refl
  ( z : MariciInt)
  : MariciIntIdentityCode z z
  := match z
      ( marici-int-zero ⇒ marici-unit
      | marici-int-pos a ⇒ marici-nat-identity-code-refl a
      | marici-int-neg a ⇒ marici-nat-identity-code-refl a)

#define marici-int-identity-encode
  ( z w : MariciInt)
  ( e : z =_{MariciInt} w)
  : MariciIntIdentityCode z w
  := transport MariciInt
      (\ q → MariciIntIdentityCode z q)
      z w e (marici-int-identity-code-refl z)
```

## Boundary

The canonical-integer identity code and path encoding are checked. Structural
decoding, code uniqueness, and the encode--decode transfer remain before
canonical-integer identity-path uniqueness follows.
