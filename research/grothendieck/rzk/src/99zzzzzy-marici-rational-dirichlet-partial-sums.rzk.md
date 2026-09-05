# Rational Dirichlet partial sums at natural exponents

Natural exponentiation and structurally positive reciprocal powers now supply
an executable finite Dirichlet sum. The summation index `k` represents the
positive integer `k+1`.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-positive-reciprocal-power
  ( base-predecessor exponent : MariciNat)
  : MariciRational
  := marici-rational-from-raw
      (marici-raw-fraction
        marici-int-one
        (marici-positive-power-predecessor
          base-predecessor exponent))

#define marici-rational-dirichlet-term
  ( exponent index : MariciNat)
  : MariciRational
  := marici-rational-positive-reciprocal-power index exponent

#define marici-zeta-dirichlet-partial-sum
  ( bound exponent : MariciNat)
  : MariciRational
  := marici-rational-finite-sum bound
      (marici-rational-dirichlet-term exponent)

#define marici-zeta-dirichlet-partial-sum-zero
  ( exponent : MariciNat)
  : marici-zeta-dirichlet-partial-sum marici-zero exponent
    =_{MariciRational}
    marici-rational-zero
  := refl

#define marici-zeta-dirichlet-partial-sum-successor
  ( bound exponent : MariciNat)
  : marici-zeta-dirichlet-partial-sum (marici-succ bound) exponent
    =_{MariciRational}
    marici-rational-add
      (marici-zeta-dirichlet-partial-sum bound exponent)
      (marici-rational-dirichlet-term exponent bound)
  := refl
```

## Boundary

This is the finite rational sum of `(k+1)^(-s)` for natural `s`; it is not the
Riemann zeta function. No infinite-series object, convergence proof, complex
exponent, analytic continuation, or functional equation is supplied. The next
semantic gate is a proof that powers of positive naturals remain positive,
justifying the predecessor encoding independently of computation.
