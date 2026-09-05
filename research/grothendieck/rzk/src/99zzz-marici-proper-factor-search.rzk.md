# Proper nonunit factor search for positive naturals

For a value at least three, a nonunit factor is proper exactly when its nonunit
index lies below the index representing the whole value. Reusing bounded common
factor search on the value paired with itself decides that proper interval and
retains the exact factorization certificate.

```rzk
#lang rzk-1
```

```rzk
#define MariciProperNonunitFactorDecision
  ( residual : MariciNat)
  : U
  := MariciBoundedNonunitCommonFactorDecision
      residual
      (marici-int-pos (marici-succ (marici-succ residual)))
      (marici-succ (marici-succ residual))

#define marici-decide-proper-nonunit-factor-at-least-three
  ( residual : MariciNat)
  : MariciProperNonunitFactorDecision residual
  := marici-decide-nonunit-common-factor-bounded
      residual
      (marici-int-pos (marici-succ (marici-succ residual)))
      (marici-succ (marici-succ residual))

#define marici-proper-factor-certificate-denominator-equation
  ( residual factor : MariciNat)
  ( bounded : MariciNatAtMost factor residual)
  ( certificate : MariciRawComponentsCommonPositiveFactor
      (marici-int-pos (marici-succ (marici-succ residual)))
      (marici-succ (marici-succ residual))
      (marici-succ factor))
  : MariciPositiveNatRightDivides
      (marici-succ factor)
      (marici-succ (marici-succ residual))
  := match certificate
      ( marici-raw-components-common-positive-factor
          numerator-cofactor denominator-cofactor
          numerator-equation denominator-equation ⇒
            marici-positive-nat-right-divides-witness
              (marici-succ factor)
              (marici-succ (marici-succ residual))
              denominator-cofactor denominator-equation)
```

## Boundary

Proper nonunit factor existence is now decidable for every natural value at
least three, with exact positive factorization on hits and universal bounded
refutation on misses. Turning a hit into two strictly smaller nonunit factors,
and proving the no-hit branch satisfies irreducible Euclid, remain the two
factorization-induction edges.
