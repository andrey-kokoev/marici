# An identity code for natural numbers

A recursive code assigns a singleton to matching constructors, the predecessor
code to two successors, and the empty type to mixed constructors. Paths encode
by transport; codes decode structurally to paths.

```rzk
#lang rzk-1
```

```rzk
#define MariciNatIdentityCode
  ( n m : MariciNat)
  : U
  := (match n into (\ _ → MariciNat → U)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒ MariciUnit
          | marici-succ j jh ⇒ MariciEmpty)
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒ MariciEmpty
          | marici-succ j jh ⇒ ih j))) m

#define marici-nat-identity-code-refl
  ( n : MariciNat)
  : MariciNatIdentityCode n n
  := match n
      ( marici-zero ⇒ marici-unit
      | marici-succ i ih ⇒ ih)

#define marici-nat-identity-encode
  ( n m : MariciNat)
  ( e : n =_{MariciNat} m)
  : MariciNatIdentityCode n m
  := transport MariciNat
      (\ q → MariciNatIdentityCode n q)
      n m e (marici-nat-identity-code-refl n)
```

```rzk
#define marici-nat-identity-decode
  ( n m : MariciNat)
  : MariciNatIdentityCode n m → n =_{MariciNat} m
  := (match n into
        (\ n-prime → (m-prime : MariciNat)
          → MariciNatIdentityCode n-prime m-prime
          → n-prime =_{MariciNat} m-prime)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒ \ c → refl
          | marici-succ j jh ⇒ \ c →
              marici-empty-elim
                (marici-zero =_{MariciNat} marici-succ j) c)
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒ \ c →
              marici-empty-elim
                ((marici-succ i) =_{MariciNat} marici-zero) c
          | marici-succ j jh ⇒ \ c →
              ap MariciNat MariciNat i j marici-succ (ih j c)))) m
```

## Boundary

Encoding and decoding are defined and checked, but their composites are not yet
proved homotopic to the relevant identities. Consequently this module alone
does not establish decidable equality or uniqueness of natural identity paths.
