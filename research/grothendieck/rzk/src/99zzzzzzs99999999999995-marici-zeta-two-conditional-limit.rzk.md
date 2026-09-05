# Conditional completed value of the exponent-two Dirichlet series

The explicit exponent-two rational Cauchy sequence determines a class in the
conditional real completion. Pairing that class with completed real zero places
it on the real axis of the conditional complex carrier.

```rzk
#lang rzk-1
```

```rzk
#define marici-zeta-two-real
  : MariciReal
  := marici-real-from-cauchy-sequence
      marici-exponent-two-rational-cauchy-sequence

#define marici-zeta-two-complex
  : MariciComplex
  := marici-complex marici-zeta-two-real marici-real-zero

#define marici-zeta-two-complex-real-part
  : marici-complex-real-part marici-zeta-two-complex
    =_{MariciReal}
    marici-zeta-two-real
  := refl

#define marici-zeta-two-complex-imaginary-part
  : marici-complex-imaginary-part marici-zeta-two-complex
    =_{MariciReal}
    marici-real-zero
  := refl
```

## Boundary

This is the conditional completed value of the natural-exponent-two Dirichlet
series, represented by its proved Cauchy partial sums. It depends on the five
explicit set-quotient assumptions defining `MariciReal`. It does not identify
the value with `pi^2/6`, define `zeta(s)` for a complex argument, construct
complex exponentiation, or provide analytic continuation or a functional
equation. The newly authored dependency suffix remains unverified until an
allowed Rzk checker route is available.
