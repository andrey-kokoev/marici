# Removing an arbitrary divisible summand

If a divisor divides a left summand and also divides the whole sum, expose the
left summand's stored cofactor, reindex the sum to an explicit divisor multiple,
and invoke multiple-prefix removal. This is the subtraction-free cancellation
rule needed to turn a Bézout difference certificate into Euclid's lemma.

```rzk
#lang rzk-1
```

```rzk
#define marici-nat-divisibility-removes-divisible-left-summand
  ( divisor left right : MariciNat)
  ( divides-left : MariciNatDivides divisor left)
  ( divides-sum : MariciNatDivides divisor (marici-add left right))
  : MariciNatDivides divisor right
  := match divides-left
      ( marici-nat-divides-witness cofactor left-equation ⇒
        (match divisor into
            (\ divisor-prime →
              (marici-mul cofactor divisor-prime =_{MariciNat} left)
              → MariciNatDivides divisor-prime (marici-add left right)
              → MariciNatDivides divisor-prime right)
            ( marici-zero ⇒ \ zero-equation divides-zero-sum →
                match divides-zero-sum
                ( marici-nat-divides-witness sum-cofactor sum-equation ⇒
                  marici-nat-divides-witness marici-zero right
                    marici-zero
                    (concat MariciNat
                      (marici-mul marici-zero marici-zero)
                      (marici-add left right)
                      right
                      (concat MariciNat
                        (marici-mul marici-zero marici-zero)
                        (marici-mul sum-cofactor marici-zero)
                        (marici-add left right)
                        (concat MariciNat
                          (marici-mul marici-zero marici-zero)
                          marici-zero
                          (marici-mul sum-cofactor marici-zero)
                          refl
                          (rev MariciNat
                            (marici-mul sum-cofactor marici-zero)
                            marici-zero
                            (marici-mul-zero-right sum-cofactor)))
                        sum-equation)
                      (concat MariciNat
                        (marici-add left right)
                        (marici-add marici-zero right)
                        right
                        (ap MariciNat MariciNat left marici-zero
                          (\ value → marici-add value right)
                          (concat MariciNat
                            left
                            (marici-mul cofactor marici-zero)
                            marici-zero
                            (rev MariciNat
                              (marici-mul cofactor marici-zero)
                              left zero-equation)
                            (marici-mul-zero-right cofactor)))
                        refl)))
            | marici-succ divisor-predecessor ih ⇒
                \ positive-left-equation positive-divides-sum →
                  marici-nat-divisibility-removes-multiple-prefix
                    divisor-predecessor cofactor right
                    (marici-nat-divides-reindex-value
                      (marici-succ divisor-predecessor)
                      (marici-add left right)
                      (marici-add
                        (marici-mul cofactor
                          (marici-succ divisor-predecessor)) right)
                      (ap MariciNat MariciNat left
                        (marici-mul cofactor
                          (marici-succ divisor-predecessor))
                        (\ value → marici-add value right)
                        (rev MariciNat
                          (marici-mul cofactor
                            (marici-succ divisor-predecessor))
                          left positive-left-equation))
                      positive-divides-sum))
            ) left-equation divides-sum)

#define marici-nat-divisibility-removes-divisible-right-summand
  ( divisor left right : MariciNat)
  ( divides-right : MariciNatDivides divisor right)
  ( divides-sum : MariciNatDivides divisor (marici-add left right))
  : MariciNatDivides divisor left
  := marici-nat-divisibility-removes-divisible-left-summand
      divisor right left divides-right
      (marici-nat-divides-reindex-value
        divisor (marici-add left right) (marici-add right left)
        (marici-add-comm left right) divides-sum)
```

## Boundary

Divisibility can now be cancelled from either summand without a primitive
subtraction operation. The zero-divisor branch is handled separately rather
than silently assuming positivity. A natural Bézout difference certificate can
therefore imply Euclid by multiplying its equation by the target and removing
the summand already divisible through the product hypothesis.
