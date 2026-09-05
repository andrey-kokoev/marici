# Marici raw positive-denominator fractions

This file opens the rational branch without claiming a quotient or canonical
fraction type. A denominator stores its predecessor, so every represented
denominator is structurally positive.

```rzk
#lang rzk-1

#data MariciRawFraction
  := marici-raw-fraction
      ( numerator : MariciInt)
      ( denominator-predecessor : MariciNat)
```

```rzk
#define marici-int-positive-denominator
  ( d : MariciNat)
  : MariciInt
  := marici-int-embed-nat (marici-succ d)

#define marici-scale-by-positive-denominator
  ( z : MariciInt)
  ( d : MariciNat)
  : MariciInt
  := marici-int-mul z (marici-int-positive-denominator d)
```

Raw negation, addition, and multiplication preserve structural denominator
positivity. Addition uses cross multiplication; denominator multiplication
uses the already derived predecessor formula.

```rzk
#define marici-raw-fraction-negate
  ( p : MariciRawFraction)
  : MariciRawFraction
  := match p
      ( marici-raw-fraction n d ⇒
          marici-raw-fraction (marici-int-negate n) d)

#define marici-raw-fraction-add
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                marici-raw-fraction
                  (marici-int-add
                    (marici-scale-by-positive-denominator a e)
                    (marici-scale-by-positive-denominator b d))
                  (marici-positive-product-predecessor d e)))

#define marici-raw-fraction-mul
  ( p q : MariciRawFraction)
  : MariciRawFraction
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                marici-raw-fraction
                  (marici-int-mul a b)
                  (marici-positive-product-predecessor d e)))
```

The intended fraction relation is recorded as cross-product equality. This is
a relation on raw syntax, not a quotient constructor.

```rzk
#define marici-raw-fraction-equivalent
  ( p q : MariciRawFraction)
  : U
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                marici-scale-by-positive-denominator a e
                =_{MariciInt}
                marici-scale-by-positive-denominator b d))
```

Concrete terms demonstrate that raw arithmetic does not silently normalize:
one half plus one half is represented as four fourths, and the relation—not
definitional equality of raw constructors—connects it to one first.

```rzk
#define marici-raw-one
  : MariciRawFraction
  := marici-raw-fraction marici-int-one marici-zero

#define marici-raw-one-half
  : MariciRawFraction
  := marici-raw-fraction marici-int-one marici-one

#define marici-raw-four-fourths
  : MariciRawFraction
  := marici-raw-fraction
      (marici-int-pos marici-three) marici-three

#define marici-raw-one-half-plus-one-half
  : marici-raw-fraction-add marici-raw-one-half marici-raw-one-half
    =_{MariciRawFraction} marici-raw-four-fourths
  := refl

#define marici-raw-four-fourths-equivalent-one
  : marici-raw-fraction-equivalent
      marici-raw-four-fourths marici-raw-one
  := refl
```

## Boundary

This is only positive-denominator fraction syntax and its intended relation.
It is not `Rat`: transitivity/congruence, normalization, canonical-representative
uniqueness, field laws, sethood, and the quotient or retract universal property
remain open. The four-fourths example is retained to prevent accidental
promotion of raw constructor equality into rational equality.
