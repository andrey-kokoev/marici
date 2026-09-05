# Natural identity-code uniqueness

The singleton code has a unique inhabitant. Simultaneous structural recursion
then proves uniqueness of inhabitants for every natural identity code; mixed
constructor codes are empty and eliminate immediately.

```rzk
#lang rzk-1
```

```rzk
#define marici-unit-unique
  ( x y : MariciUnit)
  : x =_{MariciUnit} y
  := match x
      ( marici-unit ⇒ match y
          ( marici-unit ⇒ refl))

#define marici-nat-identity-code-unique
  ( n m : MariciNat)
  ( x y : MariciNatIdentityCode n m)
  : x =_{MariciNatIdentityCode n m} y
  := (match n into
        (\ n-prime → (m-prime : MariciNat)
          → (x-prime y-prime : MariciNatIdentityCode n-prime m-prime)
          → x-prime =_{MariciNatIdentityCode n-prime m-prime} y-prime)
      ( marici-zero ⇒ \ q → match q
          ( marici-zero ⇒ \ u v → marici-unit-unique u v
          | marici-succ j jh ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u)
      | marici-succ i ih ⇒ \ q → match q
          ( marici-zero ⇒ \ u v →
              marici-empty-elim (u =_{MariciEmpty} v) u
          | marici-succ j jh ⇒ \ u v → ih j u v))) m x y
```

## Boundary

Every natural identity code is a proposition. The path-side arbitrary composite
still needs a parser-compatible identity-elimination formulation before code
uniqueness can be transferred to uniqueness of natural identity paths.
