# Duality of the mixed-sign integer normalizer

Simultaneous predecessor recursion shows that exchanging the two magnitudes
reverses the sign of the canonical mixed sum. Successor pairs erase one common
prefix and invoke the induction hypothesis; either zero endpoint computes
 directly.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-pos-neg-duality
  ( a b : MariciNat)
  : marici-int-negate (marici-int-add-pos-neg a b)
    =_{MariciInt}
    marici-int-add-pos-neg b a
  := (match a into
      (\ a-prime → (b-prime : MariciNat)
        → marici-int-negate
            (marici-int-add-pos-neg a-prime b-prime)
          =_{MariciInt}
          marici-int-add-pos-neg b-prime a-prime)
      ( marici-zero ⇒ \ b-prime → match b-prime
          ( marici-zero ⇒ refl
          | marici-succ j previous ⇒ refl)
      | marici-succ i induction ⇒ \ b-prime → match b-prime
          ( marici-zero ⇒ refl
          | marici-succ j previous ⇒ induction j))) b

#define marici-int-negate-add
  ( x y : MariciInt)
  : marici-int-negate (marici-int-add x y)
    =_{MariciInt}
    marici-int-add (marici-int-negate x) (marici-int-negate y)
  := match x
      ( marici-int-zero ⇒ match y
          ( marici-int-zero ⇒ refl
          | marici-int-pos b ⇒ refl
          | marici-int-neg b ⇒ refl)
      | marici-int-pos a ⇒ match y
          ( marici-int-zero ⇒ refl
          | marici-int-pos b ⇒ refl
          | marici-int-neg b ⇒ marici-int-add-pos-neg-duality a b)
      | marici-int-neg a ⇒ match y
          ( marici-int-zero ⇒ refl
          | marici-int-pos b ⇒ marici-int-add-pos-neg-duality b a
          | marici-int-neg b ⇒ refl))
```

## Boundary

Negation is now a proved additive involutive symmetry on every constructor
face. A mixed associativity theorem for one sign pattern can therefore be
transported to its simultaneous sign reversal; representative mixed patterns
still require their own nested-normalization proofs.
