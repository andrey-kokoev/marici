# Bounded normalization by structural recursion

Structural recursion on an external denominator bound normalizes every fraction
beneath that bound. At the endpoint, the total reduction decision either stops
or invokes the induction hypothesis on the strictly smaller cofactor
denominator.

```rzk
#lang rzk-1
```

```rzk
#define marici-normalize-bounded
  ( bound : MariciNat)
  : MariciBoundedNormalizationFamily bound
  := match bound
      ( marici-zero ⇒ \ a d bounded →
          transport MariciNat
            (\ x → MariciRawFractionNormalization
              (marici-raw-fraction a x))
            marici-zero d
            (rev MariciNat d marici-zero
              (marici-at-most-zero-equal-zero d bounded))
            (marici-unit-denominator-normalization a)
      | marici-succ n normalize-previous ⇒ \ a d bounded →
          match (marici-at-most-successor-split d n bounded)
            ( marici-at-most-strictly-below-successor below ⇒
                normalize-previous a d below
            | marici-at-most-equal-successor endpoint ⇒
                transport MariciNat
                  (\ x → MariciRawFractionNormalization
                    (marici-raw-fraction a x))
                  (marici-succ n) d
                  (rev MariciNat d (marici-succ n) endpoint)
                  (marici-normalization-from-reduction-decision
                    a (marici-succ n)
                    (marici-decide-raw-components-reduction
                      a (marici-succ n))
                    (\ factor → match factor
                      ( marici-raw-components-nonunit-common-positive-factor
                          f certificate ⇒ match certificate
                            ( marici-raw-components-common-positive-factor
                                q r eq-num eq-den ⇒
                                  normalize-previous q r
                                    (marici-strictly-less-successor-gives-at-most
                                      r n
                                      (marici-nonunit-positive-factor-decreases
                                        (marici-succ n) r f eq-den))))))))
```

## Boundary

The bounded normalization family is now constructed for every bound. Applying
it to each fraction at its reflexive denominator bound yields total
normalization; that final specialization remains to be stated. Representative
uniqueness remains separate.
