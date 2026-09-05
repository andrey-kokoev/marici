# Canonical rational carrier aliases

The existing reduced normal-form carrier already provides total normalization,
zero, one, negation, addition, and multiplication. The rational names below
expose that checked carrier for the finite-sum lane without duplicating its
implementation.

```rzk
#lang rzk-1
```

```rzk
#define MariciRational
  : U
  := MariciReducedRawFraction

#define marici-rational-from-raw
  ( p : MariciRawFraction)
  : MariciRational
  := marici-normalize-to-reduced p

#define marici-rational-forget
  ( p : MariciRational)
  : MariciRawFraction
  := marici-reduced-raw-fraction-forget p

#define marici-rational-zero
  : MariciRational
  := marici-reduced-normal-form-zero

#define marici-rational-one
  : MariciRational
  := marici-reduced-normal-form-one

#define marici-rational-add
  ( p q : MariciRational)
  : MariciRational
  := marici-reduced-normal-form-add p q

#define marici-rational-mul
  ( p q : MariciRational)
  : MariciRational
  := marici-reduced-normal-form-mul p q
```

## Boundary

This names the executable reduced-component carrier used by subsequent finite
rational sums. Presentation independence follows at the forgotten canonical
component level from the checked normalization and operation-descent theorems.
A quotient universal property and field laws are not asserted here.
