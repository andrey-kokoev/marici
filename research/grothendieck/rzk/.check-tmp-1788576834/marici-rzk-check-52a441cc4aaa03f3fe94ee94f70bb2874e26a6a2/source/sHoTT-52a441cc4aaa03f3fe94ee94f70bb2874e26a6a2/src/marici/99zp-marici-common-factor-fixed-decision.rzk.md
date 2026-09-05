# Deciding a fixed common positive factor

For one positive factor, integer numerator divisibility and positive denominator
divisibility are decided independently and then intersected. A failed axis
refutes every common-factor certificate at that factor.

```rzk
#lang rzk-1
```

```rzk
#data MariciCommonPositiveFactorDecision
  ( numerator : MariciInt)
  ( denominator-predecessor factor-predecessor : MariciNat)
  := marici-common-positive-factor-found
      ( certificate : MariciRawComponentsCommonPositiveFactor
        numerator denominator-predecessor factor-predecessor)
  | marici-common-positive-factor-absent
      ( refutation : MariciRawComponentsCommonPositiveFactor
        numerator denominator-predecessor factor-predecessor → MariciEmpty)

#define marici-decide-common-positive-factor
  ( a : MariciInt)
  ( d f : MariciNat)
  : MariciCommonPositiveFactorDecision a d f
  := match (marici-decide-int-right-positive-divisibility f a)
      ( marici-int-right-positive-divisible int-witness ⇒
          match (marici-decide-positive-nat-right-divisibility f d)
            ( marici-positive-nat-right-divisible nat-witness ⇒
                match int-witness
                  ( marici-int-right-positive-divides-witness q eq-num ⇒
                      match nat-witness
                        ( marici-positive-nat-right-divides-witness r eq-den ⇒
                            marici-common-positive-factor-found a d f
                              (marici-raw-components-common-positive-factor
                                a d f q r eq-num eq-den)))
            | marici-positive-nat-right-indivisible not-denominator ⇒
                marici-common-positive-factor-absent a d f
                  (\ common → match common
                    ( marici-raw-components-common-positive-factor
                        q r eq-num eq-den ⇒
                          not-denominator
                            (marici-positive-nat-right-divides-witness
                              f d r eq-den))))
      | marici-int-right-positive-indivisible not-numerator ⇒
          marici-common-positive-factor-absent a d f
            (\ common → match common
              ( marici-raw-components-common-positive-factor
                  q r eq-num eq-den ⇒
                    not-numerator
                      (marici-int-right-positive-divides-witness
                        f a q eq-num))))
```

## Boundary

Common-factor existence is now decidable for each supplied positive factor.
Total reduction selection must search the structurally nonunit factor
predecessors allowed by the denominator and accumulate fixed-factor
refutations into reducedness.
