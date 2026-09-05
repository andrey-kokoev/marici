# Rational order transports along component equality

Factoring rational order through raw canonical components permits endpoint
transport without equality of reducedness proofs.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-at-most-transport-left
  ( p p-prime q : MariciRawFraction)
  ( path : p =_{MariciRawFraction} p-prime)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRawFractionAtMost p-prime q
  := idJ
      ( MariciRawFraction , p
      , \ u equality → MariciRawFractionAtMost u q
      , witness , p-prime , path)

#define marici-raw-fraction-at-most-transport-right
  ( p q q-prime : MariciRawFraction)
  ( path : q =_{MariciRawFraction} q-prime)
  ( witness : MariciRawFractionAtMost p q)
  : MariciRawFractionAtMost p q-prime
  := idJ
      ( MariciRawFraction , q
      , \ u equality → MariciRawFractionAtMost p u
      , witness , q-prime , path)

#define marici-rational-at-most-transport-left-components
  ( p p-prime q : MariciRational)
  ( path : marici-rational-forget p
      =_{MariciRawFraction} marici-rational-forget p-prime)
  ( witness : MariciRationalAtMost p q)
  : MariciRationalAtMost p-prime q
  := marici-raw-fraction-at-most-transport-left
      (marici-rational-forget p)
      (marici-rational-forget p-prime)
      (marici-rational-forget q) path witness

#define marici-rational-at-most-transport-right-components
  ( p q q-prime : MariciRational)
  ( path : marici-rational-forget q
      =_{MariciRawFraction} marici-rational-forget q-prime)
  ( witness : MariciRationalAtMost p q)
  : MariciRationalAtMost p q-prime
  := marici-raw-fraction-at-most-transport-right
      (marici-rational-forget p)
      (marici-rational-forget q)
      (marici-rational-forget q-prime) path witness
```

## Boundary

These are endpoint transports for the component-level order relation. They add
no inequality and make no quotient claim.
