# The conditional zeta-two class has the Dirichlet approximants

The Cauchy representative used for the conditional completed value unfolds to
the previously defined exponent-two Dirichlet partial sums. Their rational-to-
complex images therefore coincide with the existing complex finite
approximants.

```rzk
#lang rzk-1
```

```rzk
#define marici-zeta-two-cauchy-value-is-dirichlet-partial-sum
  ( bound : MariciNat)
  : marici-rational-cauchy-sequence-values
      marici-exponent-two-rational-cauchy-sequence bound
    =_{MariciRational}
    marici-zeta-dirichlet-partial-sum bound marici-two
  := refl

#define marici-zeta-two-cauchy-value-complex-approximant
  ( bound : MariciNat)
  : marici-rational-to-complex
      (marici-rational-cauchy-sequence-values
        marici-exponent-two-rational-cauchy-sequence bound)
    =_{MariciComplex}
    marici-zeta-complex-partial-sum bound marici-two
  := ap MariciRational MariciComplex
      (marici-rational-cauchy-sequence-values
        marici-exponent-two-rational-cauchy-sequence bound)
      (marici-zeta-dirichlet-partial-sum bound marici-two)
      marici-rational-to-complex
      (marici-zeta-two-cauchy-value-is-dirichlet-partial-sum bound)

#define marici-zeta-two-real-is-cauchy-class
  : marici-zeta-two-real
    =_{MariciReal}
    marici-real-from-cauchy-sequence
      marici-exponent-two-rational-cauchy-sequence
  := refl
```

## Boundary

The conditional completed value at exponent two is now explicitly tied to the
existing rational and complex Dirichlet approximants. This remains conditional
on the set-quotient assumptions and unverified pending an allowed Rzk checker.
It supplies no complex-variable `zeta(s)`, exponentiation, analytic
continuation, functional equation, or evaluation as `pi^2/6`.
