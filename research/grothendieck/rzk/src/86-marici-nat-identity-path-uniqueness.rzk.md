# Natural identity-path uniqueness

Identity elimination extends module 83's reflexive decode--encode computation
to every natural path. Combining this composite with code uniqueness proves
that every natural identity type is a proposition.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-identity-decode-encode-all
  ( n m : MariciNat)
  ( e : n =_{MariciNat} m)
  : marici-nat-identity-decode n m
      (marici-nat-identity-encode n m e)
    =_{(n =_{MariciNat} m)} e
  := idJ
      ( MariciNat , n
      , \ q p →
          marici-nat-identity-decode n q
            (marici-nat-identity-encode n q p)
          =_{(n =_{MariciNat} q)} p
      , marici-nat-identity-decode-refl n
      , m , e)

#define marici-nat-identity-path-unique
  ( n m : MariciNat)
  ( e f : n =_{MariciNat} m)
  : e =_{(n =_{MariciNat} m)} f
  := marici-nat-path-equal-from-composites n m e f
      (marici-nat-identity-decode-encode-all n m e)
      (marici-nat-identity-decode-encode-all n m f)
```

## Boundary

Every natural identity type is proposition-valued. This is identity-path
uniqueness, not a decision procedure returning equality or inequality data.
Canonical integer path uniqueness still requires a corresponding constructor
code or an equivalent transfer argument.
