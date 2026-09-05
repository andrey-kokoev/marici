# Nonunit factor removal decreases the denominator

If a positive denominator factors through a factor of magnitude at least two,
its positive cofactor predecessor is strictly smaller. The additive gap is the
predecessor of the product of the remaining positive factor and cofactor.

```rzk
#lang rzk-1
```

```rzk
#define marici-nonunit-positive-factor-decreases
  ( d r f : MariciNat)
  ( e : marici-mul
      (marici-succ r) (marici-succ (marici-succ f))
    =_{MariciNat} marici-succ d)
  : MariciNatStrictlyLess r d
  := marici-nat-strictly-less-witness r d
      (marici-positive-product-predecessor f r)
      (concat MariciNat
        (marici-add
          (marici-succ (marici-positive-product-predecessor f r)) r)
        (marici-add
          (marici-mul (marici-succ f) (marici-succ r)) r)
        d
        (ap MariciNat MariciNat
          (marici-succ (marici-positive-product-predecessor f r))
          (marici-mul (marici-succ f) (marici-succ r))
          (\ x → marici-add x r)
          (marici-succ-positive-product f r))
        (concat MariciNat
          (marici-add
            (marici-mul (marici-succ f) (marici-succ r)) r)
          (marici-add r
            (marici-mul (marici-succ f) (marici-succ r)))
          d
          (marici-add-comm
            (marici-mul (marici-succ f) (marici-succ r)) r)
          (marici-succ-injective
            (marici-add r
              (marici-mul (marici-succ f) (marici-succ r)))
            d
            (concat MariciNat
              (marici-mul
                (marici-succ (marici-succ f)) (marici-succ r))
              (marici-mul
                (marici-succ r) (marici-succ (marici-succ f)))
              (marici-succ d)
              (rev MariciNat
                (marici-mul
                  (marici-succ r) (marici-succ (marici-succ f)))
                (marici-mul
                  (marici-succ (marici-succ f)) (marici-succ r))
                (marici-mul-comm
                  (marici-succ r) (marici-succ (marici-succ f))))
              e))))

#define marici-nonunit-common-factor-with-decrease
  ( a : MariciInt)
  ( d : MariciNat)
  ( c : MariciRawComponentsNonunitCommonPositiveFactor a d)
  : MariciRawComponentsDecreasingReduction a d
  := match c
      ( marici-raw-components-nonunit-common-positive-factor f cert ⇒
          match cert
            ( marici-raw-components-common-positive-factor q r en ed ⇒
                marici-raw-components-decreasing-reduction
                  a d f q r en ed
                  (marici-nonunit-positive-factor-decreases d r f ed)))
```

## Boundary

Every nonunit common-factor witness now supplies the denominator decrease needed
for recursion. A well-founded eliminator and a total reduction decision remain
before universal normalization can be constructed.
