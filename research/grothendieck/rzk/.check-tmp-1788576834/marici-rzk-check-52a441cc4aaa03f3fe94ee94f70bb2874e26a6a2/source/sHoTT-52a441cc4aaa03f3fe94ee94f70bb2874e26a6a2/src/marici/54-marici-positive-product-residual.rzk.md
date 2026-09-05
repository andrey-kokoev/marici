# General scaled residual for positive-product predecessors

A source decomposition into a smaller positive predecessor, one separating
successor, and a residual is preserved by positive scaling. Induction removes
one matching scaled successor block at each step.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-product-residual
  ( p b r : MariciNat)
  : marici-sub
      (marici-positive-product-predecessor p
        (marici-add (marici-succ b) r))
      (marici-succ (marici-positive-product-predecessor p b))
    =_{MariciNat} marici-positive-product-predecessor p r
  := ind-MariciNat
      (\ b-prime →
        marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ b-prime) r))
          (marici-succ
            (marici-positive-product-predecessor p b-prime))
        =_{MariciNat} marici-positive-product-predecessor p r)
      (marici-positive-product-residual-base p r)
      (\ k ih → concat MariciNat
        (marici-sub
          (marici-positive-product-predecessor p
            (marici-add (marici-succ (marici-succ k)) r))
          (marici-succ
            (marici-positive-product-predecessor p (marici-succ k))))
        (marici-sub
          (marici-add (marici-succ p)
            (marici-positive-product-predecessor p
              (marici-add (marici-succ k) r)))
          (marici-add (marici-succ p)
            (marici-succ
              (marici-positive-product-predecessor p k))))
        (marici-positive-product-predecessor p r)
        (concat MariciNat
          (marici-sub
            (marici-positive-product-predecessor p
              (marici-add (marici-succ (marici-succ k)) r))
            (marici-succ
              (marici-positive-product-predecessor p (marici-succ k))))
          (marici-sub
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p
                (marici-add (marici-succ k) r)))
            (marici-succ
              (marici-positive-product-predecessor p (marici-succ k))))
          (marici-sub
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p
                (marici-add (marici-succ k) r)))
            (marici-add (marici-succ p)
              (marici-succ
                (marici-positive-product-predecessor p k))))
          (ap MariciNat MariciNat
            (marici-positive-product-predecessor p
              (marici-add (marici-succ (marici-succ k)) r))
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p
                (marici-add (marici-succ k) r)))
            (\ z → marici-sub z
              (marici-succ
                (marici-positive-product-predecessor p (marici-succ k))))
            (marici-positive-product-successor-right p
              (marici-add (marici-succ k) r)))
          (ap MariciNat MariciNat
            (marici-succ
              (marici-positive-product-predecessor p (marici-succ k)))
            (marici-add (marici-succ p)
              (marici-succ
                (marici-positive-product-predecessor p k)))
            (\ z → marici-sub
              (marici-add (marici-succ p)
                (marici-positive-product-predecessor p
                  (marici-add (marici-succ k) r))) z)
            (concat MariciNat
              (marici-succ
                (marici-positive-product-predecessor p (marici-succ k)))
              (marici-succ
                (marici-add (marici-succ p)
                  (marici-positive-product-predecessor p k)))
              (marici-add (marici-succ p)
                (marici-succ
                  (marici-positive-product-predecessor p k)))
              (ap MariciNat MariciNat
                (marici-positive-product-predecessor p (marici-succ k))
                (marici-add (marici-succ p)
                  (marici-positive-product-predecessor p k))
                marici-succ
                (marici-positive-product-successor-right p k))
              (rev MariciNat
                (marici-add (marici-succ p)
                  (marici-succ
                    (marici-positive-product-predecessor p k)))
                (marici-succ
                  (marici-add (marici-succ p)
                    (marici-positive-product-predecessor p k)))
                (marici-add-succ-right (marici-succ p)
                  (marici-positive-product-predecessor p k))))))
        (concat MariciNat
          (marici-sub
            (marici-add (marici-succ p)
              (marici-positive-product-predecessor p
                (marici-add (marici-succ k) r)))
            (marici-add (marici-succ p)
              (marici-succ
                (marici-positive-product-predecessor p k))))
          (marici-sub
            (marici-positive-product-predecessor p
              (marici-add (marici-succ k) r))
            (marici-succ
              (marici-positive-product-predecessor p k)))
          (marici-positive-product-predecessor p r)
          (marici-sub-common-prefix (marici-succ p)
            (marici-positive-product-predecessor p
              (marici-add (marici-succ k) r))
            (marici-succ
              (marici-positive-product-predecessor p k)))
          ih))
      b
```

## Boundary

The theorem is uniform in the positive factor, smaller predecessor, and
residual. It identifies the exact normalized residual for the strictly greater
comparison branch; the reversed branch follows by exchanging the magnitudes.
