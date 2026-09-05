# Decoding canonical-integer identity codes

Canonical-integer codes decode structurally. Equal-sign nonzero codes decode
through the natural decoder and constructor action; mixed codes eliminate from
the empty type.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-identity-decode
  ( z w : MariciInt)
  : MariciIntIdentityCode z w → z =_{MariciInt} w
  := (match z into
        (\ z-prime → (w-prime : MariciInt)
          → MariciIntIdentityCode z-prime w-prime
          → z-prime =_{MariciInt} w-prime)
      ( marici-int-zero ⇒ \ q → match q
          ( marici-int-zero ⇒ \ c → refl
          | marici-int-pos b ⇒ \ c →
              marici-empty-elim
                (marici-int-zero =_{MariciInt} marici-int-pos b) c
          | marici-int-neg b ⇒ \ c →
              marici-empty-elim
                (marici-int-zero =_{MariciInt} marici-int-neg b) c)
      | marici-int-pos a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ c →
              marici-empty-elim
                (marici-int-pos a =_{MariciInt} marici-int-zero) c
          | marici-int-pos b ⇒ \ c →
              ap MariciNat MariciInt a b marici-int-pos
                (marici-nat-identity-decode a b c)
          | marici-int-neg b ⇒ \ c →
              marici-empty-elim
                (marici-int-pos a =_{MariciInt} marici-int-neg b) c)
      | marici-int-neg a ⇒ \ q → match q
          ( marici-int-zero ⇒ \ c →
              marici-empty-elim
                (marici-int-neg a =_{MariciInt} marici-int-zero) c
          | marici-int-pos b ⇒ \ c →
              marici-empty-elim
                (marici-int-neg a =_{MariciInt} marici-int-pos b) c
          | marici-int-neg b ⇒ \ c →
              ap MariciNat MariciInt a b marici-int-neg
                (marici-nat-identity-decode a b c)))) w
```

## Boundary

Canonical-integer codes now decode to paths. Code uniqueness and the two
composite calculations remain before integer identity-path uniqueness follows.
