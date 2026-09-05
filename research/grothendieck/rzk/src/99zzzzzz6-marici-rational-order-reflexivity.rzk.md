# Rational order reflexivity

Nonnegativity transports along an integer path to zero. Additive inverse then
proves integer-order reflexivity, and the positive-denominator cross-product
definition specializes it to canonical rationals.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-nonnegative-from-zero-path
  ( z : MariciInt)
  ( zero-path : z =_{MariciInt} marici-int-zero)
  : MariciIntIsNonnegative z
  := idJ
      ( MariciInt , marici-int-zero
      , \ q p → MariciIntIsNonnegative q
      , marici-trivial , z
      , rev MariciInt z marici-int-zero zero-path)

#define marici-int-at-most-reflexive
  ( x : MariciInt)
  : MariciIntAtMost x x
  := marici-int-nonnegative-from-zero-path
      (marici-int-add (marici-int-negate x) x)
      (marici-int-add-inverse-left x)

#define marici-rational-at-most-reflexive
  ( q : MariciRational)
  : MariciRationalAtMost q q
  := match q
      ( marici-reduced-raw-fraction numerator denominator-predecessor reduced ⇒
          marici-int-at-most-reflexive
            (marici-scale-by-positive-denominator
              numerator denominator-predecessor))
```

## Boundary

Rational order is now reflexive. Transitivity and arithmetic compatibility are
still required before Cauchy-sequence equivalence or completion can be proved.
