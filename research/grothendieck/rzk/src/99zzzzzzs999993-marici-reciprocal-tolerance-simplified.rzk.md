# Reciprocal tolerance has a simplified raw denominator

At exponent one, the computed positive-power predecessor transports to the base
predecessor. Therefore the reciprocal tolerance is equal to normalization of
the raw fraction with numerator one and denominator predecessor `k`.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-reciprocal-tolerance
  ( k : MariciNat)
  : MariciRawFraction
  := marici-raw-fraction marici-int-one k

#define marici-raw-reciprocal-tolerance-input-path
  ( k : MariciNat)
  : marici-raw-fraction
      marici-int-one
      (marici-positive-power-predecessor k marici-one)
    =_{MariciRawFraction}
    marici-raw-reciprocal-tolerance k
  := marici-raw-fraction-denominator-path
      marici-int-one
      (marici-positive-power-predecessor k marici-one) k
      (marici-positive-power-predecessor-one k)

#define marici-rational-reciprocal-tolerance-simplified
  ( k : MariciNat)
  : marici-rational-positive-reciprocal-power k marici-one
    =_{MariciRational}
    marici-rational-from-raw (marici-raw-reciprocal-tolerance k)
  := ap MariciRawFraction MariciRational
      (marici-raw-fraction
        marici-int-one
        (marici-positive-power-predecessor k marici-one))
      (marici-raw-reciprocal-tolerance k)
      marici-rational-from-raw
      (marici-raw-reciprocal-tolerance-input-path k)

#define marici-rational-reciprocal-tolerance-simplified-components
  ( k : MariciNat)
  : marici-rational-forget
      (marici-rational-positive-reciprocal-power k marici-one)
    =_{MariciRawFraction}
    marici-rational-forget
      (marici-rational-from-raw (marici-raw-reciprocal-tolerance k))
  := ap MariciRational MariciRawFraction
      (marici-rational-positive-reciprocal-power k marici-one)
      (marici-rational-from-raw (marici-raw-reciprocal-tolerance k))
      marici-rational-forget
      (marici-rational-reciprocal-tolerance-simplified k)
```

## Boundary

Reciprocal tolerances can now be manipulated using the simple raw fraction
`1/(k+1)`. The remaining combination theorem proves that two copies at the
doubled index are equivalent to one copy at `k`.
