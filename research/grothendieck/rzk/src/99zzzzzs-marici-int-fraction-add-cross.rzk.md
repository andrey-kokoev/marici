# Integer cross identity for fraction addition

This is the algebraic theorem at the center of raw-fraction addition
congruence. It uses exactly two supplied cross-product equalities.

```rzk
#lang rzk-1
```

```rzk
#define marici-int-fraction-add-cross
  ( a b c g D E F K : MariciInt)
  ( h : marici-int-mul a E =_{MariciInt} marici-int-mul b D)
  ( j : marici-int-mul c K =_{MariciInt} marici-int-mul g F)
  : marici-int-mul
      (marici-int-add (marici-int-mul a F) (marici-int-mul c D))
      (marici-int-mul E K)
    =_{MariciInt}
    marici-int-mul
      (marici-int-add (marici-int-mul b K) (marici-int-mul g E))
      (marici-int-mul D F)
  := concat MariciInt
      (marici-int-mul
        (marici-int-add (marici-int-mul a F) (marici-int-mul c D))
        (marici-int-mul E K))
      (marici-int-add
        (marici-int-mul (marici-int-mul a E) (marici-int-mul F K))
        (marici-int-mul (marici-int-mul c K) (marici-int-mul D E)))
      (marici-int-mul
        (marici-int-add (marici-int-mul b K) (marici-int-mul g E))
        (marici-int-mul D F))
      (marici-int-mixed-cross-sum-normal-form a F c D E K)
      (concat MariciInt
        (marici-int-add
          (marici-int-mul (marici-int-mul a E) (marici-int-mul F K))
          (marici-int-mul (marici-int-mul c K) (marici-int-mul D E)))
        (marici-int-add
          (marici-int-mul (marici-int-mul b D) (marici-int-mul F K))
          (marici-int-mul (marici-int-mul g F) (marici-int-mul D E)))
        (marici-int-mul
          (marici-int-add (marici-int-mul b K) (marici-int-mul g E))
          (marici-int-mul D F))
        (marici-int-add-congruent
          (marici-int-mul (marici-int-mul a E) (marici-int-mul F K))
          (marici-int-mul (marici-int-mul b D) (marici-int-mul F K))
          (marici-int-mul (marici-int-mul c K) (marici-int-mul D E))
          (marici-int-mul (marici-int-mul g F) (marici-int-mul D E))
          (ap MariciInt MariciInt
            (marici-int-mul a E) (marici-int-mul b D)
            (\ z → marici-int-mul z (marici-int-mul F K)) h)
          (ap MariciInt MariciInt
            (marici-int-mul c K) (marici-int-mul g F)
            (\ z → marici-int-mul z (marici-int-mul D E)) j))
        (concat MariciInt
          (marici-int-add
            (marici-int-mul (marici-int-mul b D) (marici-int-mul F K))
            (marici-int-mul (marici-int-mul g F) (marici-int-mul D E)))
          (marici-int-add
            (marici-int-mul (marici-int-mul b D) (marici-int-mul K F))
            (marici-int-mul (marici-int-mul g F) (marici-int-mul E D)))
          (marici-int-mul
            (marici-int-add (marici-int-mul b K) (marici-int-mul g E))
            (marici-int-mul D F))
          (marici-int-sum-product-right-swaps b D F K g F D E)
          (rev MariciInt
            (marici-int-mul
              (marici-int-add (marici-int-mul b K) (marici-int-mul g E))
              (marici-int-mul D F))
            (marici-int-add
              (marici-int-mul (marici-int-mul b D) (marici-int-mul K F))
              (marici-int-mul (marici-int-mul g F) (marici-int-mul E D)))
            (marici-int-mixed-cross-sum-normal-form b K g E D F))))
```

## Boundary

The theorem proves the full integer identity conditional only on the two input
cross paths. The next wrapper specializes the capital factors to embedded
positive denominators and rewrites structural product predecessors.
