# Data underlying addition of rational Cauchy sequences

Pointwise rational addition and the combined tightened modulus are the data
required for Cauchy-sequence addition. No Cauchy witness is asserted here: that
witness additionally requires a translation-invariant distance bound for
rational addition.

```rzk
#lang rzk-1
```

```rzk
#define marici-rational-cauchy-add-values
  ( x y : MariciRationalCauchySequence)
  ( n : MariciNat)
  : MariciRational
  := marici-rational-add
      (marici-rational-cauchy-sequence-values x n)
      (marici-rational-cauchy-sequence-values y n)

#define marici-rational-cauchy-add-modulus
  ( x y : MariciRationalCauchySequence)
  ( k : MariciNat)
  : MariciNat
  := marici-combined-tightened-modulus
      (marici-rational-cauchy-sequence-modulus x)
      (marici-rational-cauchy-sequence-modulus y)
      k
```

## Boundary

These definitions construct only the value map and proposed modulus. To package
them as `MariciRationalCauchySequence`, one must prove that distance between two
pointwise sums is bounded by the sum of the corresponding coordinate distances,
then combine the two tightened reciprocal tolerances.
