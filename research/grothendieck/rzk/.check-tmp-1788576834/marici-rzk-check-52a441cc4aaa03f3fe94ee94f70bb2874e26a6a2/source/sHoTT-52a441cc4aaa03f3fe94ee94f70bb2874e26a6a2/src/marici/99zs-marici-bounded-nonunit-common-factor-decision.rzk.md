# Bounded decision for nonunit common factors

The bound ranges over nonunit-predecessor indices: candidate `f` denotes the
actual positive-factor predecessor `succ f`. A negative result refutes every
common-factor certificate whose index lies in the interval.

```rzk
#lang rzk-1
```

```rzk
#data MariciBoundedNonunitCommonFactorDecision
  ( bound : MariciNat)
  ( numerator : MariciInt)
  ( denominator-predecessor : MariciNat)
  := marici-bounded-nonunit-common-factor-found
      ( nonunit-predecessor : MariciNat)
      ( bounded : MariciNatAtMost nonunit-predecessor bound)
      ( certificate : MariciRawComponentsCommonPositiveFactor
        numerator denominator-predecessor
        (marici-succ nonunit-predecessor))
  | marici-bounded-nonunit-common-factor-absent
      ( refutation : (nonunit-predecessor : MariciNat)
        → MariciNatAtMost nonunit-predecessor bound
        → MariciRawComponentsCommonPositiveFactor
            numerator denominator-predecessor
            (marici-succ nonunit-predecessor)
        → MariciEmpty)

#define marici-reindex-common-factor-certificate
  ( a : MariciInt)
  ( d f g : MariciNat)
  ( p : f =_{MariciNat} g)
  ( c : MariciRawComponentsCommonPositiveFactor a d (marici-succ f))
  : MariciRawComponentsCommonPositiveFactor a d (marici-succ g)
  := transport MariciNat
      (\ x → MariciRawComponentsCommonPositiveFactor a d (marici-succ x))
      f g p c
```

```rzk
#define marici-decide-nonunit-common-factor-bounded
  ( bound : MariciNat)
  ( a : MariciInt)
  ( d : MariciNat)
  : MariciBoundedNonunitCommonFactorDecision bound a d
  := match bound
      ( marici-zero ⇒
          match (marici-decide-common-positive-factor
            a d (marici-succ marici-zero))
            ( marici-common-positive-factor-found certificate ⇒
                marici-bounded-nonunit-common-factor-found
                  marici-zero a d marici-zero
                  (marici-nat-at-most-witness
                    marici-zero marici-zero marici-zero refl)
                  certificate
            | marici-common-positive-factor-absent not-factor ⇒
                marici-bounded-nonunit-common-factor-absent
                  marici-zero a d
                  (\ f bounded certificate →
                    not-factor
                      (marici-reindex-common-factor-certificate
                        a d f marici-zero
                        (marici-at-most-zero-equal-zero f bounded)
                        certificate)))
      | marici-succ n previous ⇒
          match (marici-decide-common-positive-factor
            a d (marici-succ (marici-succ n)))
            ( marici-common-positive-factor-found certificate ⇒
                marici-bounded-nonunit-common-factor-found
                  (marici-succ n) a d (marici-succ n)
                  (marici-nat-at-most-witness
                    (marici-succ n) (marici-succ n) marici-zero refl)
                  certificate
            | marici-common-positive-factor-absent not-endpoint ⇒ match previous
                ( marici-bounded-nonunit-common-factor-found f bounded certificate ⇒
                    marici-bounded-nonunit-common-factor-found
                      (marici-succ n) a d f
                      (marici-at-most-lift-successor f n bounded) certificate
                | marici-bounded-nonunit-common-factor-absent prior ⇒
                    marici-bounded-nonunit-common-factor-absent
                      (marici-succ n) a d
                      (\ f bounded certificate →
                        match (marici-at-most-successor-split f n bounded)
                          ( marici-at-most-strictly-below-successor below ⇒
                              prior f below certificate
                          | marici-at-most-equal-successor endpoint ⇒
                              not-endpoint
                                (marici-reindex-common-factor-certificate
                                  a d f (marici-succ n) endpoint certificate))))))
```

## Boundary

Nonunit common-factor existence is now decidable on every finite predecessor
interval with a universal bounded refutation. Applying the denominator-derived
bound and converting absence to reducedness is the next step.
