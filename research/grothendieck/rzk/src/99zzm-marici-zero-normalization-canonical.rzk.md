# Every reduced representative of zero is canonical

Cross-product equivalence from canonical zero forces the target numerator to
be zero by the integer right-unit law. Transporting reducedness along that
numerator path reduces to the already proved denominator-one theorem.

```rzk
#lang rzk-1
```

```rzk
#define marici-zero-equivalent-target-numerator-zero
  ( b : MariciInt)
  ( e : MariciNat)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction marici-int-zero marici-zero)
      (marici-raw-fraction b e))
  : b =_{MariciInt} marici-int-zero
  := concat MariciInt
      b
      (marici-int-mul b marici-int-one)
      marici-int-zero
      (rev MariciInt
        (marici-int-mul b marici-int-one) b
        (marici-int-mul-one-right b))
      (rev MariciInt
        marici-int-zero
        (marici-int-mul b marici-int-one)
        equivalent)

#define marici-equivalent-reduced-zero-representative-canonical
  ( b : MariciInt)
  ( e : MariciNat)
  ( reduced : MariciRawComponentsAreReduced b e)
  ( equivalent : marici-raw-fraction-equivalent
      (marici-raw-fraction marici-int-zero marici-zero)
      (marici-raw-fraction b e))
  : marici-raw-fraction b e =_{MariciRawFraction}
      marici-raw-fraction marici-int-zero marici-zero
  := ind-path MariciInt marici-int-zero
      (\ b-prime numerator-path →
        MariciRawComponentsAreReduced b-prime e
        → marici-raw-fraction-equivalent
            (marici-raw-fraction marici-int-zero marici-zero)
            (marici-raw-fraction b-prime e)
        → marici-raw-fraction b-prime e =_{MariciRawFraction}
            marici-raw-fraction marici-int-zero marici-zero)
      (\ reduced-zero equivalent-zero →
        marici-reduced-zero-raw-representative-canonical
          e reduced-zero)
      b
      (rev MariciInt b marici-int-zero
        (marici-zero-equivalent-target-numerator-zero b e equivalent))
      reduced equivalent

#define marici-zero-normalization-is-canonical
  ( normalization : MariciRawFractionNormalization
      (marici-raw-fraction marici-int-zero marici-zero))
  : marici-normalization-forget-representative
      (marici-raw-fraction marici-int-zero marici-zero)
      normalization
      =_{MariciRawFraction}
    marici-raw-fraction marici-int-zero marici-zero
  := match normalization into
      (\ normalization-prime →
        marici-normalization-forget-representative
          (marici-raw-fraction marici-int-zero marici-zero)
          normalization-prime
          =_{MariciRawFraction}
        marici-raw-fraction marici-int-zero marici-zero)
      ( marici-raw-fraction-normalization representative preserves ⇒
        (match representative into
          (\ representative-prime →
            marici-raw-fraction-equivalent
              (marici-raw-fraction marici-int-zero marici-zero)
              (marici-reduced-raw-fraction-forget representative-prime)
            → marici-reduced-raw-fraction-forget representative-prime
                =_{MariciRawFraction}
              marici-raw-fraction marici-int-zero marici-zero)
          ( marici-reduced-raw-fraction b e reduced ⇒ \ preserves-prime →
              marici-equivalent-reduced-zero-representative-canonical
                b e reduced preserves-prime)) preserves)

#define marici-normalized-zero-is-canonical-zero
  : marici-normalized-raw-representative
      (marici-raw-fraction marici-int-zero marici-zero)
      =_{MariciRawFraction}
    marici-raw-fraction marici-int-zero marici-zero
  := marici-zero-normalization-is-canonical
      (marici-normalize-raw-fraction
        (marici-raw-fraction marici-int-zero marici-zero))
```

## Boundary

Normalization of canonical raw zero now returns canonical raw zero at the
underlying-component level without the general Euclid theorem. The proof does
not identify reducedness evidence paths. Nonzero normalization canonicality
still depends on reduced-representative uniqueness.
