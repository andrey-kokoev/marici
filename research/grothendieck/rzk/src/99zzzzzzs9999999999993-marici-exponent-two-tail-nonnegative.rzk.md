# Finite exponent-two tails are nonnegative

Joint addition monotonicity preserves nonnegativity after transporting the sum
of two rational zeros back to canonical zero. Induction then proves every finite
sum of exponent-two tail terms lies above zero.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-add-nonnegative
  ( p q : MariciRational)
  ( p-nonnegative : MariciRationalAtMost marici-rational-zero p)
  ( q-nonnegative : MariciRationalAtMost marici-rational-zero q)
  : MariciRationalAtMost marici-rational-zero
      (marici-rational-add p q)
  := marici-rational-at-most-transport-left-components
      (marici-rational-add marici-rational-zero marici-rational-zero)
      marici-rational-zero
      (marici-rational-add p q)
      (marici-rational-add-zero-right-components marici-rational-zero)
      (marici-rational-add-at-most
        marici-rational-zero p marici-rational-zero q
        p-nonnegative q-nonnegative)

#define marici-rational-finite-sum-nonnegative
  ( term : MariciNat → MariciRational)
  ( pointwise : (index : MariciNat)
    → MariciRationalAtMost marici-rational-zero (term index))
  ( bound : MariciNat)
  : MariciRationalAtMost marici-rational-zero
      (marici-rational-finite-sum bound term)
  := match bound
      ( marici-zero ⇒
          marici-rational-at-most-reflexive marici-rational-zero
      | marici-succ k induction ⇒
          marici-rational-add-nonnegative
            (marici-rational-finite-sum k term) (term k)
            induction (pointwise k))

#define marici-exponent-two-tail-nonnegative
  ( cutoff length : MariciNat)
  : MariciRationalAtMost marici-rational-zero
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
  := marici-rational-finite-sum-nonnegative
      (marici-exponent-two-tail-term cutoff)
      (\ index →
        marici-rational-zero-at-most-positive-reciprocal-power
          (marici-succ (marici-add index cutoff)) marici-two)
      length
```

## Boundary

Every extracted exponent-two tail is now nonnegative. To turn the ordered
partial-sum difference bound into a distance bound, rational absolute value must
be shown componentwise fixed on a rational supplied with a zero-at-most witness.
