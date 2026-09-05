# Proper-factor hits fit the previous recursion bound

A proper-factor search hit factors the value into two positive factors. The
searched factor index is bounded by the proper interval. The cofactor index is
bounded by the previous recursion stage because removing a structurally
nonunit factor strictly decreases the denominator predecessor.

```rzk
#lang rzk-1
```

```rzk
#data MariciProperFactorRecursionData
  ( residual : MariciNat)
  := marici-proper-factor-recursion-data
      ( factor-predecessor : MariciNat)
      ( cofactor-predecessor : MariciNat)
      ( factor-bounded : MariciNatAtMost factor-predecessor residual)
      ( cofactor-bounded : MariciNatAtMost cofactor-predecessor
          (marici-succ residual))
      ( factorization : marici-mul
          (marici-succ cofactor-predecessor)
          (marici-succ (marici-succ factor-predecessor))
        =_{MariciNat}
        marici-succ (marici-succ (marici-succ residual)))

#define marici-proper-factor-hit-gives-recursion-data
  ( residual factor : MariciNat)
  ( bounded : MariciNatAtMost factor residual)
  ( certificate : MariciRawComponentsCommonPositiveFactor
      (marici-int-pos (marici-succ (marici-succ residual)))
      (marici-succ (marici-succ residual))
      (marici-succ factor))
  : MariciProperFactorRecursionData residual
  := match certificate
      ( marici-raw-components-common-positive-factor
          numerator-cofactor denominator-cofactor
          numerator-equation denominator-equation ⇒
        marici-proper-factor-recursion-data residual
          factor denominator-cofactor bounded
          (marici-strictly-less-successor-gives-at-most
            denominator-cofactor (marici-succ residual)
            (marici-nonunit-positive-factor-decreases
              (marici-succ (marici-succ residual))
              denominator-cofactor factor denominator-equation))
          denominator-equation)
```

## Boundary

Every proper-factor hit now supplies both recursive factor indices within the
previous external bound, plus the exact product equation. This closes the hit
branch's termination bookkeeping. The no-hit irreducible Euclid theorem and
the bounded Euclid recursion remain.
