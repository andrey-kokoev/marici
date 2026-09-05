# A mixed associativity cancellation family

Adding positive one to a positive magnitude raises that magnitude by one. The
adjacent mixed normalizer then cancels the following opposite term back to
one. On the other parenthesization, the equal opposite pair cancels first.
This gives an unbounded genuinely mixed associativity family.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-assoc-one-positive-negative-self
  ( b : MariciNat)
  : MariciIntAddAssociates
      marici-int-one (marici-int-pos b) (marici-int-neg b)
  := concat MariciInt
      (marici-int-add
        (marici-int-add marici-int-one (marici-int-pos b))
        (marici-int-neg b))
      marici-int-one
      (marici-int-add marici-int-one
        (marici-int-add (marici-int-pos b) (marici-int-neg b)))
      (marici-int-add-adjacent-positive-negative b)
      (ap MariciInt MariciInt
        marici-int-zero
        (marici-int-add (marici-int-pos b) (marici-int-neg b))
        (\ value → marici-int-add marici-int-one value)
        (rev MariciInt
          (marici-int-add (marici-int-pos b) (marici-int-neg b))
          marici-int-zero
          (marici-int-add-pos-neg-self b)))

#define marici-int-add-assoc-minus-one-negative-positive-self
  ( b : MariciNat)
  : MariciIntAddAssociates
      marici-int-minus-one (marici-int-neg b) (marici-int-pos b)
  := marici-int-add-assoc-sign-reversal
      marici-int-one (marici-int-pos b) (marici-int-neg b)
      (marici-int-add-assoc-one-positive-negative-self b)
```

## Boundary

Associativity is checked on an unbounded mixed cancellation family and its
simultaneous sign reversal. The general two-positive/one-negative face still
requires arbitrary-gap rather than adjacent-gap normalization.
