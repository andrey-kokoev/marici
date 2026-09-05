# Finite Gaussian-rational algebra

Natural powers and finite sums close the Gaussian-rational carrier under the
finite algebraic operations needed for executable complex approximants.

```rzk
#lang rzk-1
```

```rzk
#define marici-gaussian-rational-power
  ( z : MariciGaussianRational)
  ( exponent : MariciNat)
  : MariciGaussianRational
  := match exponent
      ( marici-zero ⇒ marici-gaussian-rational-one
      | marici-succ k ih ⇒ marici-gaussian-rational-mul z ih)

#define marici-gaussian-rational-finite-sum
  ( bound : MariciNat)
  ( term : MariciNat → MariciGaussianRational)
  : MariciGaussianRational
  := match bound
      ( marici-zero ⇒ marici-gaussian-rational-zero
      | marici-succ k ih ⇒ marici-gaussian-rational-add ih (term k))

#define marici-gaussian-rational-power-zero
  ( z : MariciGaussianRational)
  : marici-gaussian-rational-power z marici-zero
    =_{MariciGaussianRational}
    marici-gaussian-rational-one
  := refl

#define marici-gaussian-rational-power-successor
  ( z : MariciGaussianRational)
  ( exponent : MariciNat)
  : marici-gaussian-rational-power z (marici-succ exponent)
    =_{MariciGaussianRational}
    marici-gaussian-rational-mul z
      (marici-gaussian-rational-power z exponent)
  := refl

#define marici-gaussian-rational-finite-sum-zero
  ( term : MariciNat → MariciGaussianRational)
  : marici-gaussian-rational-finite-sum marici-zero term
    =_{MariciGaussianRational}
    marici-gaussian-rational-zero
  := refl

#define marici-gaussian-rational-finite-sum-successor
  ( bound : MariciNat)
  ( term : MariciNat → MariciGaussianRational)
  : marici-gaussian-rational-finite-sum (marici-succ bound) term
    =_{MariciGaussianRational}
    marici-gaussian-rational-add
      (marici-gaussian-rational-finite-sum bound term)
      (term bound)
  := refl
```

## Boundary

All operations here are finite. They provide no topology, completion,
transcendental exponentiation, or convergence theorem.
