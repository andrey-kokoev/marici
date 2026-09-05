# Fraction equivalence preserves numerator nonnegativity

Positive denominators let numerator sign pass through cross-product equality.
This is the normalization-sign theorem needed to prove positivity of rational
tolerances and absolute values.

```rzk
#lang rzk-1
```

```rzk
#define MariciRawFractionNumeratorIsNonnegative
  ( p : MariciRawFraction)
  : U
  := match p
      ( marici-raw-fraction numerator denominator-predecessor ⇒
          MariciIntIsNonnegative numerator)

#define marici-raw-fraction-equivalence-preserves-nonnegative-numerator
  ( p q : MariciRawFraction)
  ( equivalent : marici-raw-fraction-equivalent p q)
  ( source-nonnegative : MariciRawFractionNumeratorIsNonnegative p)
  : MariciRawFractionNumeratorIsNonnegative q
  := (match p into
      (\ p-prime → marici-raw-fraction-equivalent p-prime q
        → MariciRawFractionNumeratorIsNonnegative p-prime
        → MariciRawFractionNumeratorIsNonnegative q)
      ( marici-raw-fraction a d ⇒ \ equivalent-prime a-nonnegative →
          (match q into
            (\ q-prime → marici-raw-fraction-equivalent
                (marici-raw-fraction a d) q-prime
              → MariciRawFractionNumeratorIsNonnegative q-prime)
            ( marici-raw-fraction b e ⇒ \ cross-path →
                marici-int-nonnegative-positive-product-reflects-left b d
                  (marici-int-nonnegative-transport
                    (marici-int-mul a
                      (marici-int-positive-denominator e))
                    (marici-int-mul b
                      (marici-int-positive-denominator d))
                    cross-path
                    (marici-int-nonnegative-mul a
                      (marici-int-positive-denominator e)
                      a-nonnegative
                      (marici-int-positive-denominator-nonnegative e)))))
          equivalent-prime)) equivalent source-nonnegative
```

## Boundary

This proves sign preservation along raw fraction equivalence. It does not claim
that arbitrary normalization preserves order between two distinct fractions;
it supplies numerator nonnegativity for normalized representatives of
nonnegative sources.
