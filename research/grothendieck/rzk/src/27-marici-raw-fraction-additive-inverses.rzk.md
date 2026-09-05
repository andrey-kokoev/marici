# Raw-fraction additive inverses through the relation

Adding a raw fraction to its negation squares the stored denominator, so the
result is generally not the chosen zero constructor. Both inverse laws hold
through cross-product equivalence.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-add-negate-right-equivalent
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add p
        (marici-raw-fraction-negate p))
      (marici-raw-zero-at marici-zero)
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciInt
            (marici-int-mul
              (marici-int-add
                (marici-scale-by-positive-denominator a d)
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d))
              marici-int-one)
            (marici-int-add
              (marici-scale-by-positive-denominator a d)
              (marici-int-negate
                (marici-scale-by-positive-denominator a d)))
            marici-int-zero
            (concat MariciInt
              (marici-int-mul
                (marici-int-add
                  (marici-scale-by-positive-denominator a d)
                  (marici-scale-by-positive-denominator
                    (marici-int-negate a) d))
                marici-int-one)
              (marici-int-add
                (marici-scale-by-positive-denominator a d)
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d))
              (marici-int-add
                (marici-scale-by-positive-denominator a d)
                (marici-int-negate
                  (marici-scale-by-positive-denominator a d)))
              (marici-int-mul-one-right
                (marici-int-add
                  (marici-scale-by-positive-denominator a d)
                  (marici-scale-by-positive-denominator
                    (marici-int-negate a) d)))
              (ap MariciInt MariciInt
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d)
                (marici-int-negate
                  (marici-scale-by-positive-denominator a d))
                (\ z → marici-int-add
                  (marici-scale-by-positive-denominator a d) z)
                (marici-int-mul-negate-left a
                  (marici-int-positive-denominator d))))
            (marici-int-add-inverse-right
              (marici-scale-by-positive-denominator a d)))
```

```rzk
#define marici-raw-fraction-add-negate-left-equivalent
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent
      (marici-raw-fraction-add
        (marici-raw-fraction-negate p) p)
      (marici-raw-zero-at marici-zero)
  := match p
      ( marici-raw-fraction a d ⇒
          concat MariciInt
            (marici-int-mul
              (marici-int-add
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d)
                (marici-scale-by-positive-denominator a d))
              marici-int-one)
            (marici-int-add
              (marici-int-negate
                (marici-scale-by-positive-denominator a d))
              (marici-scale-by-positive-denominator a d))
            marici-int-zero
            (concat MariciInt
              (marici-int-mul
                (marici-int-add
                  (marici-scale-by-positive-denominator
                    (marici-int-negate a) d)
                  (marici-scale-by-positive-denominator a d))
                marici-int-one)
              (marici-int-add
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d)
                (marici-scale-by-positive-denominator a d))
              (marici-int-add
                (marici-int-negate
                  (marici-scale-by-positive-denominator a d))
                (marici-scale-by-positive-denominator a d))
              (marici-int-mul-one-right
                (marici-int-add
                  (marici-scale-by-positive-denominator
                    (marici-int-negate a) d)
                  (marici-scale-by-positive-denominator a d)))
              (ap MariciInt MariciInt
                (marici-scale-by-positive-denominator
                  (marici-int-negate a) d)
                (marici-int-negate
                  (marici-scale-by-positive-denominator a d))
                (\ z → marici-int-add z
                  (marici-scale-by-positive-denominator a d))
                (marici-int-mul-negate-left a
                  (marici-int-positive-denominator d))))
            (marici-int-add-inverse-left
              (marici-scale-by-positive-denominator a d)))
```

## Boundary

These are relation-valued inverse laws, not raw constructor equalities. Their
promotion to a rational additive inverse requires the relation quotient or a
canonical normalization interface, including transitivity and addition
congruence.
