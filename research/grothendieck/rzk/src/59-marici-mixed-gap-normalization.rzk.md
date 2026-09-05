# Explicit positive mixed-sign gap normalization

An explicit positive predecessor gap normalizes directly to its residual. This
is the source-side path needed to compare multiplication before and after
normalization.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-pos-neg-gap
  ( b r : MariciNat)
  : marici-int-add
      (marici-int-pos (marici-add (marici-succ b) r))
      (marici-int-neg b)
    =_{MariciInt} marici-int-pos r
  := concat MariciInt
      (marici-int-add
        (marici-int-pos (marici-add (marici-succ b) r))
        (marici-int-neg b))
      (marici-int-pos
        (marici-sub (marici-add (marici-succ b) r) (marici-succ b)))
      (marici-int-pos r)
      (ap MariciOrdering MariciInt
        (marici-compare (marici-add (marici-succ b) r) b)
        marici-greater
        (\ ordering → match ordering into (\ _ → MariciInt)
          ( marici-less ⇒ marici-int-neg
              (marici-sub b
                (marici-succ (marici-add (marici-succ b) r)))
          | marici-equal ⇒ marici-int-zero
          | marici-greater ⇒ marici-int-pos
              (marici-sub (marici-add (marici-succ b) r)
                (marici-succ b))))
        (marici-compare-explicit-gap-greater b r))
      (ap MariciNat MariciInt
        (marici-sub (marici-add (marici-succ b) r) (marici-succ b))
        r
        marici-int-pos
        (marici-sub-add-prefix (marici-succ b) r))
```

## Boundary

This theorem normalizes the positive-result source branch. Its reversed
negative-result analogue remains before both strict distributive paths can be
assembled.
