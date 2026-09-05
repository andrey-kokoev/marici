# Marici natural comparison and truncated subtraction

This increment supplies computational comparison and subtraction needed by the
canonical signed-integer representation.

```rzk
#lang rzk-1

#data MariciOrdering
  := marici-less
  | marici-equal
  | marici-greater
```

Comparison recursively removes one successor from both inputs.

```rzk
#define marici-compare
  ( n m : MariciNat)
  : MariciOrdering
  := (match n into (\ _ → MariciNat → MariciOrdering)
      ( marici-zero ⇒
          \ q → match q
            ( marici-zero ⇒ marici-equal
            | marici-succ j jh ⇒ marici-less)
      | marici-succ k ih ⇒
          \ q → match q
            ( marici-zero ⇒ marici-greater
            | marici-succ j jh ⇒ ih j))) m

#define marici-compare-self
  ( n : MariciNat)
  : marici-compare n n =_{MariciOrdering} marici-equal
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)

#define marici-compare-zero-succ
  ( n : MariciNat)
  : marici-compare marici-zero (marici-succ n)
    =_{MariciOrdering} marici-less
  := refl

#define marici-compare-succ-zero
  ( n : MariciNat)
  : marici-compare (marici-succ n) marici-zero
    =_{MariciOrdering} marici-greater
  := refl
```

Truncated subtraction returns zero when the subtrahend exceeds the minuend.
Like comparison, it is defined by simultaneous structural reduction rather than
by an assumed order operation.

```rzk
#define marici-sub
  ( n m : MariciNat)
  : MariciNat
  := (match n into (\ _ → MariciNat → MariciNat)
      ( marici-zero ⇒ \ q → marici-zero
      | marici-succ k ih ⇒
          \ q → match q
            ( marici-zero ⇒ marici-succ k
            | marici-succ j jh ⇒ ih j))) m

#define marici-sub-zero-right
  ( n : MariciNat)
  : marici-sub n marici-zero =_{MariciNat} n
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ refl)

#define marici-sub-zero-left
  ( n : MariciNat)
  : marici-sub marici-zero n =_{MariciNat} marici-zero
  := refl

#define marici-sub-self
  ( n : MariciNat)
  : marici-sub n n =_{MariciNat} marici-zero
  := match n
      ( marici-zero ⇒ refl
      | marici-succ k ih ⇒ ih)

#define marici-three : MariciNat := marici-succ marici-two

#define marici-four-minus-two
  : marici-sub marici-four marici-two =_{MariciNat} marici-two
  := refl

#define marici-two-minus-four
  : marici-sub marici-two marici-four =_{MariciNat} marici-zero
  := refl
```

## Boundary

This module provides executable trichotomy data and truncated subtraction, not
yet a proposition-valued order relation or proofs of comparison completeness,
antisymmetry, transitivity, and subtraction/addition interaction. Canonical
integer operations may inspect `MariciOrdering`, but their ring proofs require
those remaining lemmas.
