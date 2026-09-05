# Embedded naturals are nonnegative integers

The constructor-derived natural embedding lands in the nonnegative part of the
canonical integers. Positive denominator integers inherit the same witness.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-embedded-natural-nonnegative
  ( n : MariciNat)
  : MariciIntIsNonnegative (marici-int-embed-nat n)
  := match n
      ( marici-zero ⇒ marici-trivial
      | marici-succ k ih ⇒ marici-trivial)

#define marici-int-positive-denominator-nonnegative
  ( d : MariciNat)
  : MariciIntIsNonnegative
      (marici-int-positive-denominator d)
  := marici-int-embedded-natural-nonnegative (marici-succ d)
```

## Boundary

This proves nonnegativity of embedded naturals and structural denominators.
Closure under addition and multiplication, order transport, and rational
normalization remain separate theorems.
