# Rational order relation

Integer nonnegativity is read from canonical sign constructors. Integer order is
nonnegativity of a difference; rational order compares cross-products because
all denominators are structurally positive.

```rzk
#lang rzk-1
```

```rzk
#data MariciTruth
  := marici-trivial

#define MariciIntIsNonnegative
  ( z : MariciInt)
  : U
  := match z
      ( marici-int-zero ⇒ MariciTruth
      | marici-int-pos n ⇒ MariciTruth
      | marici-int-neg n ⇒ MariciEmpty)

#define MariciIntAtMost
  ( x y : MariciInt)
  : U
  := MariciIntIsNonnegative
      (marici-int-add (marici-int-negate x) y)

#define MariciRawFractionAtMost
  ( p q : MariciRawFraction)
  : U
  := match p
      ( marici-raw-fraction a d ⇒
          match q
            ( marici-raw-fraction b e ⇒
                MariciIntAtMost
                  (marici-scale-by-positive-denominator a e)
                  (marici-scale-by-positive-denominator b d)))

#define MariciRationalAtMost
  ( p q : MariciRational)
  : U
  := MariciRawFractionAtMost
      (marici-rational-forget p)
      (marici-rational-forget q)

#define marici-int-zero-nonnegative
  : MariciIntIsNonnegative marici-int-zero
  := marici-trivial
```

## Boundary

This defines order on canonical rational components and proves only the zero
witness. Reflexivity, transitivity, compatibility with arithmetic, and
presentation transport remain separate theorems. Those laws are required
before this relation supports a metric completion.
