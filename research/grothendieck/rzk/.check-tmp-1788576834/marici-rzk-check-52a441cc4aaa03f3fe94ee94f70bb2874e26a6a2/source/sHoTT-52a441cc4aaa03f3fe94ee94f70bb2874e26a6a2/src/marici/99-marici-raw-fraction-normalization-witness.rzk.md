# Raw-fraction normalization witnesses

A normalization witness packages a reduced representative together with a
proof that its underlying raw fraction is equivalent to the source. This keeps
existence separate from uniqueness and from any future quotient construction.

```rzk
#lang rzk-1
```

```rzk
#data MariciRawFractionNormalization
  ( source : MariciRawFraction)
  := marici-raw-fraction-normalization
      ( representative : MariciReducedRawFraction)
      ( preserves-value : marici-raw-fraction-equivalent source
          (marici-reduced-raw-fraction-forget representative))

#define marici-reduced-fraction-normalizes-itself
  ( p : MariciReducedRawFraction)
  : MariciRawFractionNormalization
      (marici-reduced-raw-fraction-forget p)
  := marici-raw-fraction-normalization
      (marici-reduced-raw-fraction-forget p) p
      (marici-raw-fraction-equivalent-refl
        (marici-reduced-raw-fraction-forget p))

#define marici-normalization-forget-representative
  ( p : MariciRawFraction)
  ( n : MariciRawFractionNormalization p)
  : MariciRawFraction
  := match n
      ( marici-raw-fraction-normalization representative preserves ⇒
          marici-reduced-raw-fraction-forget representative)
```

## Boundary

The normalization target now requires both a reduced representative and its
value-preservation proof. Reduced fractions normalize themselves. Producing
this witness for every raw fraction still requires constructive factor
selection and termination; uniqueness remains a separate theorem.
