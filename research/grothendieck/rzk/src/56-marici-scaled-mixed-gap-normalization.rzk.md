# Positive scaling of an explicit mixed-sign gap

For a positive factor, an explicit positive-over-negative gap normalizes after
scaling to the positive-product predecessor of the source residual.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-scaled-pos-neg-gap
  ( p b r : MariciNat)
  : marici-int-add
      (marici-int-pos
        (marici-positive-product-predecessor p
          (marici-add (marici-succ b) r)))
      (marici-int-neg (marici-positive-product-predecessor p b))
    =_{MariciInt}
    marici-int-pos (marici-positive-product-predecessor p r)
  := concat MariciInt
      (marici-int-add
        (marici-int-pos
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r)))
        (marici-int-neg (marici-positive-product-predecessor p b)))
      (marici-int-pos
        (marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))
          (marici-succ (marici-positive-product-predecessor p b))))
      (marici-int-pos (marici-positive-product-predecessor p r))
      (ap MariciOrdering MariciInt
        (marici-compare
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))
          (marici-positive-product-predecessor p b))
        marici-greater
        (\ ordering → match ordering into (\ _ → MariciInt)
          ( marici-less ⇒ marici-int-neg
              (marici-sub
                (marici-positive-product-predecessor p b)
                (marici-succ
                  (marici-positive-product-predecessor p
                    (marici-add (marici-succ b) r))))
          | marici-equal ⇒ marici-int-zero
          | marici-greater ⇒ marici-int-pos
              (marici-sub
                (marici-positive-product-predecessor p
                  (marici-add (marici-succ b) r))
                (marici-succ
                  (marici-positive-product-predecessor p b)))))
        (concat MariciOrdering
          (marici-compare
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r))
            (marici-positive-product-predecessor p b))
          (marici-compare (marici-add (marici-succ b) r) b)
          marici-greater
          (marici-compare-positive-product-predecessor p
            (marici-add (marici-succ b) r) b)
          (marici-compare-explicit-gap-greater b r)))
      (ap MariciNat MariciInt
        (marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))
          (marici-succ (marici-positive-product-predecessor p b)))
        (marici-positive-product-predecessor p r)
        marici-int-pos
        (marici-positive-product-residual p b r))
```

## Boundary

This theorem assembles comparison preservation and exact residual preservation
for the positive-result branch. The negative-result branch requires the same
construction with exchanged source magnitudes.
