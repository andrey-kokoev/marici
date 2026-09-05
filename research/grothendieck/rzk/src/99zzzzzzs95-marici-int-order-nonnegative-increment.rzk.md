# Adding a nonnegative integer gives an upper bound

The difference between `x` and `x + y` reduces to `y`. Thus a nonnegative
increment produces an integer-order bound, an order lemma required by triangle
and tolerance-sum estimates.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-difference-after-increment
  ( x y : MariciInt)
  : marici-int-add (marici-int-negate x)
      (marici-int-add x y)
    =_{MariciInt}
    y
  := concat MariciInt
      (marici-int-add (marici-int-negate x)
        (marici-int-add x y))
      (marici-int-add
        (marici-int-add (marici-int-negate x) x) y)
      y
      (rev MariciInt
        (marici-int-add
          (marici-int-add (marici-int-negate x) x) y)
        (marici-int-add (marici-int-negate x)
          (marici-int-add x y))
        (marici-int-add-assoc (marici-int-negate x) x y))
      (concat MariciInt
        (marici-int-add
          (marici-int-add (marici-int-negate x) x) y)
        (marici-int-add marici-int-zero y)
        y
        (ap MariciInt MariciInt
          (marici-int-add (marici-int-negate x) x)
          marici-int-zero
          (\ left → marici-int-add left y)
          (marici-int-add-inverse-left x))
        (marici-int-add-zero-left y))

#define marici-int-at-most-add-nonnegative
  ( x y : MariciInt)
  ( y-nonnegative : MariciIntIsNonnegative y)
  : MariciIntAtMost x (marici-int-add x y)
  := marici-int-nonnegative-transport y
      (marici-int-add (marici-int-negate x)
        (marici-int-add x y))
      (rev MariciInt
        (marici-int-add (marici-int-negate x)
          (marici-int-add x y))
        y
        (marici-int-difference-after-increment x y))
      y-nonnegative
```

## Boundary

This proves upper-boundedness under a nonnegative increment. Full translation
invariance and two-sided addition monotonicity remain open.
