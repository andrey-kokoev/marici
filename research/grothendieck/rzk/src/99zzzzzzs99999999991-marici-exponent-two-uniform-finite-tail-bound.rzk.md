# Uniform finite-tail bound for exponent two

Order transitivity composes the shifted telescoping estimate with the bound from
an outer reciprocal difference to its initial tolerance. The resulting estimate
is uniform in the finite segment length.

```rzk
#lang rzk-1
```

```rzk
#define marici-exponent-two-uniform-finite-tail-bound
  ( cutoff length : MariciNat)
  : MariciRationalAtMost
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
  := marici-rational-at-most-transitive
      (marici-rational-finite-sum length
        (marici-exponent-two-tail-term cutoff))
      (marici-rational-reciprocal-difference
        cutoff (marici-add length cutoff))
      (marici-rational-positive-reciprocal-power cutoff marici-one)
      (marici-exponent-two-finite-tail-at-most-outer-difference
        cutoff length)
      (marici-rational-reciprocal-difference-at-most-initial
        cutoff (marici-add length cutoff))
```

## Boundary

Every finite exponent-two tail beginning immediately beyond `cutoff` is bounded
by `1/(cutoff+1)`, independently of its finite length. To obtain the Cauchy
witness for Dirichlet partial sums, their pairwise rational distance must be
identified with such a finite segment using natural-index decomposition.
