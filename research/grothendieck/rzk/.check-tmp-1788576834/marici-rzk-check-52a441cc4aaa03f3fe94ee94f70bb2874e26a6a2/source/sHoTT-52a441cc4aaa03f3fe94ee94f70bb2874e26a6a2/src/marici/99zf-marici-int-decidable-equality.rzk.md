# Decidable equality for canonical integers

Constructor no-confusion handles mixed signs and zero. Equal-sign nonzero
branches delegate to natural equality and map payload paths through the signed
constructor.

```rzk
#lang rzk-1
```

```rzk
#data MariciIntEqualityDecision
  ( z w : MariciInt)
  := marici-int-equal
      ( path : z =_{MariciInt} w)
  | marici-int-unequal
      ( refutation : (z =_{MariciInt} w) → MariciEmpty)

#define marici-int-decide-equality
  ( z w : MariciInt)
  : MariciIntEqualityDecision z w
  := (match z into
        (\ z-prime → (w-prime : MariciInt)
          → MariciIntEqualityDecision z-prime w-prime)
      ( marici-int-zero ⇒ \ q → match q
          ( marici-int-zero ⇒
              marici-int-equal marici-int-zero marici-int-zero refl
          | marici-int-pos b ⇒
              marici-int-unequal marici-int-zero (marici-int-pos b)
                (marici-int-zero-not-pos b)
          | marici-int-neg b ⇒
              marici-int-unequal marici-int-zero (marici-int-neg b)
                (marici-int-zero-not-neg b))
      | marici-int-pos a ⇒ \ q → match q
          ( marici-int-zero ⇒
              marici-int-unequal (marici-int-pos a) marici-int-zero
                (marici-int-pos-not-zero a)
          | marici-int-pos b ⇒ match (marici-nat-decide-equality a b)
              ( marici-nat-equal p ⇒
                  marici-int-equal (marici-int-pos a) (marici-int-pos b)
                    (ap MariciNat MariciInt a b marici-int-pos p)
              | marici-nat-unequal not-p ⇒
                  marici-int-unequal (marici-int-pos a) (marici-int-pos b)
                    (\ e → not-p (marici-int-pos-injective a b e)))
          | marici-int-neg b ⇒
              marici-int-unequal (marici-int-pos a) (marici-int-neg b)
                (marici-int-pos-not-neg a b))
      | marici-int-neg a ⇒ \ q → match q
          ( marici-int-zero ⇒
              marici-int-unequal (marici-int-neg a) marici-int-zero
                (marici-int-neg-not-zero a)
          | marici-int-pos b ⇒
              marici-int-unequal (marici-int-neg a) (marici-int-pos b)
                (marici-int-neg-not-pos a b)
          | marici-int-neg b ⇒ match (marici-nat-decide-equality a b)
              ( marici-nat-equal p ⇒
                  marici-int-equal (marici-int-neg a) (marici-int-neg b)
                    (ap MariciNat MariciInt a b marici-int-neg p)
              | marici-nat-unequal not-p ⇒
                  marici-int-unequal (marici-int-neg a) (marici-int-neg b)
                    (\ e → not-p (marici-int-neg-injective a b e)))))) w
```

## Boundary

Canonical-integer equality now returns either a path or a refutation. This
supplies the equality test needed when checking candidate numerator cofactors;
bounded cofactor enumeration and total divisibility decisions remain open.
