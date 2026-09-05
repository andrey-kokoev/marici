# Decidable equality for natural numbers

The equality decision type separates an exhibited path from a refutation into
the empty type. Simultaneous recursion uses constructor disjointness and
successor injectivity.

```rzk
#lang rzk-1
```

```rzk
#data MariciNatEqualityDecision
  ( n m : MariciNat)
  := marici-nat-equal
      ( path : n =_{MariciNat} m)
  | marici-nat-unequal
      ( refutation : (n =_{MariciNat} m) → MariciEmpty)

#define marici-nat-decide-equality
  ( n m : MariciNat)
  : MariciNatEqualityDecision n m
  := (match n into
        (\ n-prime → (m-prime : MariciNat)
          → MariciNatEqualityDecision n-prime m-prime)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒
              marici-nat-equal marici-zero marici-zero refl
          | marici-succ j jh ⇒
              marici-nat-unequal marici-zero (marici-succ j)
                (marici-zero-not-succ j))
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒
              marici-nat-unequal (marici-succ i) marici-zero
                (marici-succ-not-zero i)
          | marici-succ j jh ⇒
              match (ih j)
                ( marici-nat-equal p ⇒
                    marici-nat-equal (marici-succ i) (marici-succ j)
                      (ap MariciNat MariciNat i j marici-succ p)
                | marici-nat-unequal not-p ⇒
                    marici-nat-unequal (marici-succ i) (marici-succ j)
                      (\ e → not-p (marici-succ-injective i j e)))))) m
```

## Boundary

Natural equality now returns either an identity path or an empty-valued
refutation. This is the first executable decision component needed by bounded
divisor search; integer divisibility and common-factor search remain to be
constructed.
