# Zero and successor are disjoint

A small discriminator family sends zero to a singleton type and every
successor to an empty type. Identity elimination transports the singleton
point along a hypothetical zero--successor path, producing an empty witness.

```rzk
#lang rzk-1

#data MariciEmpty

#data MariciUnit
  := marici-unit
```

```rzk
#define marici-empty-elim
  ( A : U)
  ( e : MariciEmpty)
  : A
  := ind-MariciEmpty (\ _ → A) e

#define marici-nat-zero-discriminator
  ( n : MariciNat)
  : U
  := match n
      ( marici-zero ⇒ MariciUnit
      | marici-succ k ih ⇒ MariciEmpty)

#define marici-zero-not-succ
  ( n : MariciNat)
  ( e : marici-zero =_{MariciNat} (marici-succ n))
  : MariciEmpty
  := transport MariciNat
      marici-nat-zero-discriminator
      marici-zero (marici-succ n) e marici-unit

#define marici-succ-not-zero
  ( n : MariciNat)
  ( e : (marici-succ n) =_{MariciNat} marici-zero)
  : MariciEmpty
  := marici-zero-not-succ n
      (rev MariciNat (marici-succ n) marici-zero e)
```

## Boundary

These theorems establish constructor disjointness as empty-valued maps. They do
not yet prove decidable equality or uniqueness of identity paths. Together with
module 71 they provide the no-confusion ingredients for positive-factor
cancellation.
