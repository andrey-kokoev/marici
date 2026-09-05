# Positive natural-factor right cancellation

Natural multiplication commutativity transports positive-factor injectivity to
the right multiplication orientation.

```rzk
#lang rzk-1
```

```rzk
#define marici-mul-positive-right-injective
  ( p a b : MariciNat)
  ( e : marici-mul a (marici-succ p)
      =_{MariciNat} marici-mul b (marici-succ p))
  : a =_{MariciNat} b
  := marici-mul-positive-left-injective p a b
      (concat MariciNat
        (marici-mul (marici-succ p) a)
        (marici-mul a (marici-succ p))
        (marici-mul (marici-succ p) b)
        (marici-mul-comm (marici-succ p) a)
        (concat MariciNat
          (marici-mul a (marici-succ p))
          (marici-mul b (marici-succ p))
          (marici-mul (marici-succ p) b)
          e
          (marici-mul-comm b (marici-succ p))))
```

## Boundary

Both natural multiplication orientations are injective for every successor
factor. Canonical integer multiplication still needs constructor-level sign and
zero disjointness before raw-fraction cross-product cancellation can use this
result.
