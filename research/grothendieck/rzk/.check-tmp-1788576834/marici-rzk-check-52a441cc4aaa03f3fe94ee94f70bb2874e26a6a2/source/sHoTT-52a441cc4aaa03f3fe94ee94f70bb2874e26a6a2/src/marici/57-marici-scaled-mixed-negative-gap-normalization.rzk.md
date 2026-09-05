# Positive scaling of an explicit negative mixed-sign gap

For a positive factor, an explicit negative-over-positive gap normalizes after
scaling to the negative constructor carrying the scaled source residual.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-add-scaled-pos-neg-negative-gap
  ( p b r : MariciNat)
  : marici-int-add
      (marici-int-pos (marici-positive-product-predecessor p b))
      (marici-int-neg
        (marici-positive-product-predecessor p
          (marici-add (marici-succ b) r)))
    =_{MariciInt}
    marici-int-neg (marici-positive-product-predecessor p r)
  := concat MariciInt
      (marici-int-add
        (marici-int-pos (marici-positive-product-predecessor p b))
        (marici-int-neg
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))))
      (marici-int-neg
        (marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))
          (marici-succ (marici-positive-product-predecessor p b))))
      (marici-int-neg (marici-positive-product-predecessor p r))
      (ap MariciOrdering MariciInt
        (marici-compare
          (marici-positive-product-predecessor p b)
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r)))
        marici-less
        (\ ordering → match ordering into (\ _ → MariciInt)
          ( marici-less ⇒ marici-int-neg
              (marici-sub
                (marici-positive-product-predecessor p
                  (marici-add (marici-succ b) r))
                (marici-succ
                  (marici-positive-product-predecessor p b)))
          | marici-equal ⇒ marici-int-zero
          | marici-greater ⇒ marici-int-pos
              (marici-sub
                (marici-positive-product-predecessor p b)
                (marici-succ
                  (marici-positive-product-predecessor p
                    (marici-add (marici-succ b) r))))))
        (concat MariciOrdering
          (marici-compare
            (marici-positive-product-predecessor p b)
            (marici-positive-product-predecessor p
              (marici-add (marici-succ b) r)))
          (marici-compare b (marici-add (marici-succ b) r))
          marici-less
          (marici-compare-positive-product-predecessor p b
            (marici-add (marici-succ b) r))
          (marici-compare-explicit-gap-less b r)))
      (ap MariciNat MariciInt
        (marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b) r))
          (marici-succ (marici-positive-product-predecessor p b)))
        (marici-positive-product-predecessor p r)
        marici-int-neg
        (marici-positive-product-residual p b r))
```

## Boundary

Both strict mixed-sign branches now normalize compatibly with positive scaling.
The equal-magnitude branch and multiplication-side paths remain for the full
positive-factor distributive family.
