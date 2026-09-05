# Raw-fraction relation laws

This increment proves the relation properties available without integer-domain
cancellation. Transitivity is deliberately excluded until positive-factor
cancellation is proved.

```rzk
#lang rzk-1
```

```rzk
#define marici-raw-fraction-equivalent-refl
  ( p : MariciRawFraction)
  : marici-raw-fraction-equivalent p p
  := match p
      ( marici-raw-fraction a d ⇒ refl)

#define marici-raw-fraction-equivalent-sym
  ( p q : MariciRawFraction)
  : marici-raw-fraction-equivalent p q
  → marici-raw-fraction-equivalent q p
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                \ h → rev MariciInt
                  (marici-scale-by-positive-denominator a e)
                  (marici-scale-by-positive-denominator b d)
                  h))
```

Raw negation is involutive at constructor level because integer negation is
involutive.

```rzk
#define marici-raw-fraction-negate-involutive
  ( p : MariciRawFraction)
  : marici-raw-fraction-negate (marici-raw-fraction-negate p)
    =_{MariciRawFraction} p
  := match p
      ( marici-raw-fraction a d ⇒
          ap MariciInt MariciRawFraction
            (marici-int-negate (marici-int-negate a)) a
            (\ z → marici-raw-fraction z d)
            (marici-int-negate-involutive a))
```

Negation respects the cross-product relation. Each side is rewritten using the
checked integer multiplication/negation law, the original relation is mapped
through negation, and the target side is rewritten back.

```rzk
#define marici-raw-fraction-equivalent-negate
  ( p q : MariciRawFraction)
  : marici-raw-fraction-equivalent p q
  → marici-raw-fraction-equivalent
      (marici-raw-fraction-negate p)
      (marici-raw-fraction-negate q)
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                \ h → concat MariciInt
                  (marici-int-mul
                    (marici-int-negate a)
                    (marici-int-positive-denominator e))
                  (marici-int-negate
                    (marici-int-mul a
                      (marici-int-positive-denominator e)))
                  (marici-int-mul
                    (marici-int-negate b)
                    (marici-int-positive-denominator d))
                  (marici-int-mul-negate-left a
                    (marici-int-positive-denominator e))
                  (concat MariciInt
                    (marici-int-negate
                      (marici-int-mul a
                        (marici-int-positive-denominator e)))
                    (marici-int-negate
                      (marici-int-mul b
                        (marici-int-positive-denominator d)))
                    (marici-int-mul
                      (marici-int-negate b)
                      (marici-int-positive-denominator d))
                    (ap MariciInt MariciInt
                      (marici-int-mul a
                        (marici-int-positive-denominator e))
                      (marici-int-mul b
                        (marici-int-positive-denominator d))
                      marici-int-negate h)
                    (rev MariciInt
                      (marici-int-mul
                        (marici-int-negate b)
                        (marici-int-positive-denominator d))
                      (marici-int-negate
                        (marici-int-mul b
                          (marici-int-positive-denominator d)))
                      (marici-int-mul-negate-left b
                        (marici-int-positive-denominator d))))))
```

## Boundary

The relation is reflexive and symmetric and is preserved by negation.
Transitivity requires cancellation of the shared positive integer denominator;
it cannot be obtained from multiplication commutativity and associativity
alone. Addition and multiplication congruence additionally require the still
open integer distributivity laws.
