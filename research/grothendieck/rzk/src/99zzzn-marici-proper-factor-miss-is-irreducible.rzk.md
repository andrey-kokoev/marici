# A proper-factor search miss yields irreducibility

An exact proper natural factorization lifts to the signed-numerator
factorization used by bounded common-factor search. Therefore the search's
universal miss refutes every proper nonunit natural factorization.

```rzk
#lang rzk-1
```

```rzk
#define marici-natural-proper-factorization-to-common-certificate
  ( residual factor-predecessor cofactor-predecessor : MariciNat)
  ( factorization : marici-mul (marici-succ cofactor-predecessor)
      (marici-succ (marici-succ factor-predecessor))
    =_{MariciNat}
    marici-succ (marici-succ (marici-succ residual)))
  : MariciRawComponentsCommonPositiveFactor
      (marici-int-pos (marici-succ (marici-succ residual)))
      (marici-succ (marici-succ residual))
      (marici-succ factor-predecessor)
  := match (marici-magnitude-factorization-lifts-to-int
      (marici-int-pos (marici-succ (marici-succ residual)))
      cofactor-predecessor (marici-succ factor-predecessor)
      factorization)
      ( marici-int-right-positive-divides-witness
          numerator-cofactor numerator-equation ⇒
        marici-raw-components-common-positive-factor
          (marici-int-pos (marici-succ (marici-succ residual)))
          (marici-succ (marici-succ residual))
          (marici-succ factor-predecessor)
          numerator-cofactor cofactor-predecessor
          numerator-equation factorization)

#define marici-proper-factor-search-refutation-is-irreducible
  ( residual : MariciNat)
  ( refutation : (factor-predecessor : MariciNat)
    → MariciNatAtMost factor-predecessor residual
    → MariciRawComponentsCommonPositiveFactor
        (marici-int-pos (marici-succ (marici-succ residual)))
        (marici-succ (marici-succ residual))
        (marici-succ factor-predecessor)
    → MariciEmpty)
  : MariciNatNoProperNonunitFactor residual
  := \ factor-predecessor cofactor-predecessor bounded factorization →
      refutation factor-predecessor bounded
        (marici-natural-proper-factorization-to-common-certificate
          residual factor-predecessor cofactor-predecessor factorization)

#define marici-proper-factor-decision-miss-is-irreducible
  ( residual : MariciNat)
  ( decision : MariciProperNonunitFactorDecision residual)
  : U
  := match decision
      ( marici-bounded-nonunit-common-factor-found
          factor-predecessor bounded certificate ⇒ MariciUnit
      | marici-bounded-nonunit-common-factor-absent refutation ⇒
          MariciNatNoProperNonunitFactor residual)

#define marici-proper-factor-decision-miss-evidence
  ( residual : MariciNat)
  ( refutation : (factor-predecessor : MariciNat)
    → MariciNatAtMost factor-predecessor residual
    → MariciRawComponentsCommonPositiveFactor
        (marici-int-pos (marici-succ (marici-succ residual)))
        (marici-succ (marici-succ residual))
        (marici-succ factor-predecessor)
    → MariciEmpty)
  : MariciNatNoProperNonunitFactor residual
  := marici-proper-factor-search-refutation-is-irreducible
      residual refutation
```

## Boundary

The no-hit branch of executable proper-factor search now carries the exact
irreducibility predicate consumed by divisor rigidity. No source or
factorization assumption is inserted. The remaining Euclid work is the
additive division induction that promotes this natural-number irreducibility
to the prime-divisor property.
