# Normalization respects raw-fraction equivalence

Every normalization witness preserves its source equivalence. Combining that
fact with closed canonicality proves that equivalent raw presentations compute
the same normalized numerator and denominator predecessor.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalized-raw-representative-preserves-equivalence
  ( source : MariciRawFraction)
  : marici-raw-fraction-equivalent source
      (marici-normalized-raw-representative source)
  := match (marici-normalize-raw-fraction source) into
      (\ normalization →
        marici-raw-fraction-equivalent source
          (marici-normalization-forget-representative
            source normalization))
      ( marici-raw-fraction-normalization representative preserves ⇒
          preserves)

#define marici-forget-normalize-to-reduced
  ( source : MariciRawFraction)
  : marici-reduced-raw-fraction-forget
      (marici-normalize-to-reduced source)
      =_{MariciRawFraction}
    marici-normalized-raw-representative source
  := match (marici-normalize-raw-fraction source) into
      (\ normalization →
        marici-reduced-raw-fraction-forget
          (marici-normalization-representative source normalization)
          =_{MariciRawFraction}
        marici-normalization-forget-representative
          source normalization)
      ( marici-raw-fraction-normalization representative preserves ⇒
          refl)

#define marici-normalized-raw-representatives-respect-equivalence
  ( source target : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent source target)
  : marici-normalized-raw-representative source
      =_{MariciRawFraction}
    marici-normalized-raw-representative target
  := concat MariciRawFraction
      (marici-normalized-raw-representative source)
      (marici-reduced-raw-fraction-forget
        (marici-normalize-to-reduced target))
      (marici-normalized-raw-representative target)
      (marici-normalized-representative-canonical
        source
        (marici-normalize-to-reduced target)
        (transport MariciRawFraction
          (\ representative →
            marici-raw-fraction-equivalent source representative)
          (marici-normalized-raw-representative target)
          (marici-reduced-raw-fraction-forget
            (marici-normalize-to-reduced target))
          (rev MariciRawFraction
            (marici-reduced-raw-fraction-forget
              (marici-normalize-to-reduced target))
            (marici-normalized-raw-representative target)
            (marici-forget-normalize-to-reduced target))
          (marici-raw-fraction-equivalent-trans
            source target
            (marici-normalized-raw-representative target)
            equivalent
            (marici-normalized-raw-representative-preserves-equivalence
              target))))
      (marici-forget-normalize-to-reduced target)
```

## Boundary

Raw-fraction normalization now descends extensionally through the declared
fraction-equivalence relation: presentation changes cannot alter the computed
canonical components. This proves the missing presentation-independence gate
for normalize-after-raw operations once their raw constructors are shown to
preserve equivalence in each argument. It does not supply the outstanding
mixed-sign integer addition associativity needed for full additive laws.
