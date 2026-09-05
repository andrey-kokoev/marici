# Reduced uniqueness as the canonicality interface

The remaining arithmetic theorem is isolated as uniqueness of the underlying
raw representatives of equivalent reduced fractions. This exact principle
already implies that computed normalization agrees with every reduced
representative equivalent to the input.

```rzk
#lang rzk-1
```

```rzk
#define MariciReducedRepresentativeUniqueness
  : U
  := (left right : MariciReducedRawFraction)
    → marici-raw-fraction-equivalent
        (marici-reduced-raw-fraction-forget left)
        (marici-reduced-raw-fraction-forget right)
    → marici-reduced-raw-fraction-forget left
        =_{MariciRawFraction}
      marici-reduced-raw-fraction-forget right

#define marici-normalization-representative-canonical-if-unique
  ( uniqueness : MariciReducedRepresentativeUniqueness)
  ( source : MariciRawFraction)
  ( normalization : MariciRawFractionNormalization source)
  ( target : MariciReducedRawFraction)
  ( equivalent : marici-raw-fraction-equivalent source
      (marici-reduced-raw-fraction-forget target))
  : marici-normalization-forget-representative source normalization
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := match normalization into
      (\ normalization-prime →
        marici-normalization-forget-representative
          source normalization-prime
          =_{MariciRawFraction}
        marici-reduced-raw-fraction-forget target)
      ( marici-raw-fraction-normalization representative preserves ⇒
          uniqueness representative target
            (marici-raw-fraction-equivalent-trans
              (marici-reduced-raw-fraction-forget representative)
              source
              (marici-reduced-raw-fraction-forget target)
              (marici-raw-fraction-equivalent-sym
                source
                (marici-reduced-raw-fraction-forget representative)
                preserves)
              equivalent))

#define marici-normalized-representative-canonical-if-unique
  ( uniqueness : MariciReducedRepresentativeUniqueness)
  ( source : MariciRawFraction)
  ( target : MariciReducedRawFraction)
  ( equivalent : marici-raw-fraction-equivalent source
      (marici-reduced-raw-fraction-forget target))
  : marici-normalized-raw-representative source
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := marici-normalization-representative-canonical-if-unique
      uniqueness source (marici-normalize-raw-fraction source)
      target equivalent

#define marici-normalization-fixes-reduced-if-unique
  ( uniqueness : MariciReducedRepresentativeUniqueness)
  ( target : MariciReducedRawFraction)
  : marici-normalized-raw-representative
      (marici-reduced-raw-fraction-forget target)
      =_{MariciRawFraction}
    marici-reduced-raw-fraction-forget target
  := marici-normalized-representative-canonical-if-unique
      uniqueness
      (marici-reduced-raw-fraction-forget target)
      target
      (marici-raw-fraction-equivalent-refl
        (marici-reduced-raw-fraction-forget target))
```

## Boundary

No uniqueness assumption is hidden in normalization existence. The missing
proof obligation is exactly `MariciReducedRepresentativeUniqueness`; once it is
constructed, canonical agreement and preservation of reduced inputs follow
without another normalization argument. Proving the principle requires the
general coprime cross-product theorem.
