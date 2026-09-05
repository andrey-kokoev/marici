# Rational absolute value fixes nonnegative rationals

Integer absolute value is judgmentally fixed on zero and positive integers; the
negative case is eliminated by the nonnegativity witness. The numerator path
lifts through raw absolute value and canonical normalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-absolute-nonnegative
  ( z : MariciInt)
  ( witness : MariciIntIsNonnegative z)
  : marici-int-absolute z =_{MariciInt} z
  := match z into
      (\ z-prime → MariciIntIsNonnegative z-prime
        → marici-int-absolute z-prime =_{MariciInt} z-prime)
      ( marici-int-zero ⇒ \ nonnegative → refl
      | marici-int-pos n ⇒ \ nonnegative → refl
      | marici-int-neg n ⇒ \ impossible →
          marici-empty-elim
            (marici-int-absolute (marici-int-neg n)
              =_{MariciInt} marici-int-neg n)
            impossible)
      witness

#define marici-raw-fraction-absolute-nonnegative-numerator
  ( p : MariciRawFraction)
  ( witness : MariciRawFractionNumeratorIsNonnegative p)
  : marici-raw-fraction-absolute p =_{MariciRawFraction} p
  := match p into
      (\ p-prime → MariciRawFractionNumeratorIsNonnegative p-prime
        → marici-raw-fraction-absolute p-prime =_{MariciRawFraction} p-prime)
      ( marici-raw-fraction numerator denominator ⇒ \ nonnegative →
          ap MariciInt MariciRawFraction
            (marici-int-absolute numerator) numerator
            (\ value → marici-raw-fraction value denominator)
            (marici-int-absolute-nonnegative numerator nonnegative))
      witness

#define marici-rational-absolute-nonnegative-components
  ( q : MariciRational)
  ( witness : MariciRationalAtMost marici-rational-zero q)
  : marici-rational-forget (marici-rational-absolute q)
    =_{MariciRawFraction}
    marici-rational-forget q
  := concat MariciRawFraction
      (marici-rational-forget (marici-rational-absolute q))
      (marici-normalized-raw-representative
        (marici-raw-fraction-absolute (marici-rational-forget q)))
      (marici-rational-forget q)
      (marici-rational-from-raw-forget-normalized
        (marici-raw-fraction-absolute (marici-rational-forget q)))
      (concat MariciRawFraction
        (marici-normalized-raw-representative
          (marici-raw-fraction-absolute (marici-rational-forget q)))
        (marici-normalized-raw-representative
          (marici-rational-forget q))
        (marici-rational-forget q)
        (ap MariciRawFraction MariciRawFraction
          (marici-raw-fraction-absolute (marici-rational-forget q))
          (marici-rational-forget q)
          marici-normalized-raw-representative
          (marici-raw-fraction-absolute-nonnegative-numerator
            (marici-rational-forget q)
            (marici-rational-nonnegative-from-zero-at-most q witness)))
        (concat MariciRawFraction
          (marici-normalized-raw-representative (marici-rational-forget q))
          (marici-rational-forget
            (marici-rational-from-raw (marici-rational-forget q)))
          (marici-rational-forget q)
          (rev MariciRawFraction
            (marici-rational-forget
              (marici-rational-from-raw (marici-rational-forget q)))
            (marici-normalized-raw-representative
              (marici-rational-forget q))
            (marici-rational-from-raw-forget-normalized
              (marici-rational-forget q)))
          (marici-rational-normalization-retraction-components q)))
```

## Boundary

Absolute value now fixes every rational supplied with a zero-at-most witness at
canonical components. Applying this to the extracted nonnegative tail converts
the ordered partial-sum subtraction bound into the corresponding distance
bound.
