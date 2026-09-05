# Raw-fraction zero laws through the relation

Raw multiplication does not preserve the chosen zero constructor because it
retains the input denominator. The correct available statement is therefore
relation-valued annihilation.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-negate-zero-at
  ( d : MariciNat)
  : marici-raw-fraction-negate (marici-raw-zero-at d)
    =_{MariciRawFraction} marici-raw-zero-at d
  := refl
```

Left annihilation reduces constructor-wise: both cross products have zero
numerator.

```rzk
#define marici-raw-fraction-mul-zero-left-equivalent
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-mul (marici-raw-zero-at marici-zero) p)
      (marici-raw-zero-at marici-zero)
  := match p
      ( marici-raw-fraction a d ⇒ refl)
```

Right annihilation uses the checked integer right-zero and right-one laws. Its
raw result keeps the predecessor of the input denominator, but its cross
product with the chosen zero is zero.

```rzk
#define marici-raw-fraction-mul-zero-right-equivalent
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-mul p (marici-raw-zero-at marici-zero))
      (marici-raw-zero-at marici-zero)
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciInt
            (marici-int-mul
              (marici-int-mul a marici-int-zero)
              marici-int-one)
            (marici-int-mul a marici-int-zero)
            marici-int-zero
            (marici-int-mul-one-right
              (marici-int-mul a marici-int-zero))
            (marici-int-mul-zero-right a))
```

## Boundary

Zero annihilation is proved only through cross-product equivalence, exactly
because raw constructor multiplication retains denominators. Promoting these
laws to equality requires a quotient or a canonical normalization with a
proved relation-to-normal-form correspondence.
