# Canonical-integer decode--encode composite

Structural induction proves the reflexive computation. Identity elimination
extends it to every canonical-integer path.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-identity-decode-refl
  ( z : MariciInt)
  : marici-int-identity-decode z z
      (marici-int-identity-code-refl z)
    =_{(z =_{MariciInt} z)} refl
  := match z
      ( marici-int-zero ⇒ refl
      | marici-int-pos a ⇒
          ap (a =_{MariciNat} a)
            (marici-int-pos a =_{MariciInt} marici-int-pos a)
            (marici-nat-identity-decode a a
              (marici-nat-identity-code-refl a))
            refl
            (\ q → ap MariciNat MariciInt a a marici-int-pos q)
            (marici-nat-identity-decode-refl a)
      | marici-int-neg a ⇒
          ap (a =_{MariciNat} a)
            (marici-int-neg a =_{MariciInt} marici-int-neg a)
            (marici-nat-identity-decode a a
              (marici-nat-identity-code-refl a))
            refl
            (\ q → ap MariciNat MariciInt a a marici-int-neg q)
            (marici-nat-identity-decode-refl a))

#define marici-int-identity-decode-encode-all
  ( z w : MariciInt)
  ( e : z =_{MariciInt} w)
  : marici-int-identity-decode z w
      (marici-int-identity-encode z w e)
    =_{(z =_{MariciInt} w)} e
  := idJ
      ( MariciInt , z
      , \ q p →
          marici-int-identity-decode z q
            (marici-int-identity-encode z q p)
          =_{(z =_{MariciInt} q)} p
      , marici-int-identity-decode-refl z
      , w , e)
```

## Boundary

The path-side composite is the identity for arbitrary canonical-integer paths.
Combining it with code uniqueness to state integer identity-path uniqueness is
the remaining transfer step.
