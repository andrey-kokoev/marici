# Mixed distributivity for every integer multiplier

A constructor split on the integer multiplier assembles the zero, positive, and
negative multiplier theorems into the single mixed family required by the
global reduction.

```rzk
#lang rzk-1
```

```rzk
#define marici-all-factor-positive-negative-left-distrib
  : MariciPositiveNegativeLeftDistributivity
  := \ x a b → match x
      ( marici-int-zero ⇒
          marici-zero-factor-mixed-left-distrib a b
      | marici-int-pos p ⇒
          marici-positive-factor-mixed-left-distrib p a b
      | marici-int-neg p ⇒
          marici-negative-factor-mixed-left-distrib p a b)
```

## Boundary

The sole mixed family required by module 43 now holds for every integer
multiplier and arbitrary predecessor magnitudes. Applying module 43's reduction
to obtain both unrestricted distributive orientations remains as a separate
assembly step.
