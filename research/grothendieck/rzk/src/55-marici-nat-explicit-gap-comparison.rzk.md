# Comparison of an explicit successor gap

A natural formed from a smaller magnitude, one separating successor, and an
arbitrary residual compares strictly greater than the smaller magnitude. The
reversed comparison is strictly less.

```rzk
#lang rzk-1
```

```rzk
#define marici-compare-explicit-gap-greater
  ( b r : MariciNat)
  : marici-compare (marici-add (marici-succ b) r) b
    =_{MariciOrdering} marici-greater
  := ind-MariciNat
      (\ b-prime →
        marici-compare (marici-add (marici-succ b-prime) r) b-prime
        =_{MariciOrdering} marici-greater)
      refl
      (\ k ih → ih)
      b

#define marici-compare-explicit-gap-less
  ( b r : MariciNat)
  : marici-compare b (marici-add (marici-succ b) r)
    =_{MariciOrdering} marici-less
  := ind-MariciNat
      (\ b-prime →
        marici-compare b-prime (marici-add (marici-succ b-prime) r)
        =_{MariciOrdering} marici-less)
      refl
      (\ k ih → ih)
      b
```

## Boundary

These theorems classify a supplied decomposition; they do not infer such a
decomposition from an abstract comparison equation. They provide the branch
witnesses needed to combine module 54 with mixed integer normalization.
