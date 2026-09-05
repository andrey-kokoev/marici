# Zero bound for positive-coordinate extended Euclid

At external predecessor bound zero, the positive second coordinate must be one.
At-most antisymmetry supplies the index path, and transport carries the unit
Bézout certificate to the requested coordinate.

```rzk
#lang rzk-1
```

```rzk
#define marici-positive-bezout-available-zero
  : MariciPositiveBezoutAvailableUpTo marici-zero
  := \ second-predecessor bounded a-value coprime →
      transport MariciNat
        (\ predecessor →
          MariciNatBezoutDifference a-value (marici-succ predecessor))
        marici-zero second-predecessor
        (rev MariciNat second-predecessor marici-zero
          (marici-at-most-antisymmetric
            second-predecessor marici-zero bounded
            (marici-zero-at-most second-predecessor)))
        (marici-natural-bezout-unit-right a-value)
```

## Boundary

The bounded extended-Euclid base is checked. The nonunit endpoint step is
already available separately; the next module must combine inherited lower
cases and that endpoint into the successor-bound constructor, then iterate it.
