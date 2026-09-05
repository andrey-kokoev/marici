# Reciprocal tolerances are antitone

For unit numerators, raw reciprocal order reverses denominator order. Integer
multiplication by one is removed on both cross products, after which the lifted
positive-denominator bound applies. Raw order descends through normalization,
and component transport restores the exponent-one tolerance presentations.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-reciprocal-tolerance-antitone
  ( smaller larger : MariciNat)
  ( bound : MariciNatAtMost smaller larger)
  : MariciRawFractionAtMost
      (marici-raw-reciprocal-tolerance larger)
      (marici-raw-reciprocal-tolerance smaller)
  := marici-int-at-most-transport-both
      (marici-int-positive-denominator smaller)
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator smaller))
      (marici-int-positive-denominator larger)
      (marici-int-mul marici-int-one
        (marici-int-positive-denominator larger))
      (rev MariciInt
        (marici-int-mul marici-int-one
          (marici-int-positive-denominator smaller))
        (marici-int-positive-denominator smaller)
        (marici-int-mul-one-left
          (marici-int-positive-denominator smaller)))
      (rev MariciInt
        (marici-int-mul marici-int-one
          (marici-int-positive-denominator larger))
        (marici-int-positive-denominator larger)
        (marici-int-mul-one-left
          (marici-int-positive-denominator larger)))
      (marici-positive-denominator-at-most-from-natural-at-most
        smaller larger bound)

#define marici-rational-reciprocal-tolerance-antitone
  ( smaller larger : MariciNat)
  ( bound : MariciNatAtMost smaller larger)
  : MariciRationalAtMost
      (marici-rational-positive-reciprocal-power larger marici-one)
      (marici-rational-positive-reciprocal-power smaller marici-one)
  := marici-rational-at-most-transport-right-components
      (marici-rational-positive-reciprocal-power larger marici-one)
      (marici-rational-from-raw
        (marici-raw-reciprocal-tolerance smaller))
      (marici-rational-positive-reciprocal-power smaller marici-one)
      (rev MariciRawFraction
        (marici-rational-forget
          (marici-rational-positive-reciprocal-power smaller marici-one))
        (marici-rational-forget
          (marici-rational-from-raw
            (marici-raw-reciprocal-tolerance smaller)))
        (marici-rational-reciprocal-tolerance-simplified-components smaller))
      (marici-rational-at-most-transport-left-components
        (marici-rational-from-raw
          (marici-raw-reciprocal-tolerance larger))
        (marici-rational-positive-reciprocal-power larger marici-one)
        (marici-rational-from-raw
          (marici-raw-reciprocal-tolerance smaller))
        (rev MariciRawFraction
          (marici-rational-forget
            (marici-rational-positive-reciprocal-power larger marici-one))
          (marici-rational-forget
            (marici-rational-from-raw
              (marici-raw-reciprocal-tolerance larger)))
          (marici-rational-reciprocal-tolerance-simplified-components larger))
        (marici-raw-at-most-to-rational-at-most
          (marici-raw-reciprocal-tolerance larger)
          (marici-raw-reciprocal-tolerance smaller)
          (marici-raw-reciprocal-tolerance-antitone
            smaller larger bound)))
```

## Boundary

A later reciprocal tolerance is now bounded by every earlier one witnessed by
natural order. This permits an ordered partial-sum tail starting beyond the
requested Cauchy cutoff to inherit the requested tolerance bound.
