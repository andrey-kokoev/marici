# Integer values and their negations are bounded by absolute value

Both signed orientations of an integer lie below its nonnegative absolute
value. These two bounds allow an absolute-value triangle proof to choose the
sign of a sum only after the additive monotonicity step.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-at-most-absolute
  ( z : MariciInt)
  : MariciIntAtMost z (marici-int-absolute z)
  := match z
      ( marici-int-zero ⇒ marici-int-at-most-reflexive marici-int-zero
      | marici-int-pos n ⇒ marici-int-at-most-reflexive (marici-int-pos n)
      | marici-int-neg n ⇒ marici-trivial)

#define marici-int-negate-at-most-absolute
  ( z : MariciInt)
  : MariciIntAtMost (marici-int-negate z) (marici-int-absolute z)
  := match z
      ( marici-int-zero ⇒ marici-int-at-most-reflexive marici-int-zero
      | marici-int-pos n ⇒ marici-trivial
      | marici-int-neg n ⇒ marici-int-at-most-reflexive (marici-int-pos n))
```

## Boundary

Each integer and its negation are bounded by its absolute value. The triangle
inequality still requires selecting the corresponding bound for the sign of the
sum and transporting through addition monotonicity.
